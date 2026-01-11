"""TUI app for displaying Resonite slot hierarchy as an interactive tree."""

import sys

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header, Tree
from textual.widgets.tree import TreeNode

from pyresonitelink import client
from pyresonitelink.data import messages, responses
from pyresonitelink.data.workers import Slot


class SlotTreeApp(App):
    """A Textual app to display and navigate the Resonite slot hierarchy."""

    TITLE = "Resonite Slot Tree"
    CSS = """
    Tree {
        scrollbar-gutter: stable;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("c", "collapse_all", "Collapse All"),
        Binding("up", "cursor_up", "Up", show=False),
        Binding("down", "cursor_down", "Down", show=False),
        Binding("enter", "toggle_node", "Expand/Collapse", show=False),
        Binding("space", "toggle_node", "Expand/Collapse"),
    ]

    def __init__(self, port: int, host: str = "localhost"):
        super().__init__()
        self.port = port
        self.host = host
        self.resolink: client.Client | None = None
        self.root_slot: Slot | None = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Tree("Connecting...")
        yield Footer()

    async def on_mount(self) -> None:
        """Connect to Resonite and fetch the root slot on app mount."""
        tree = self.query_one(Tree)
        tree.show_root = True

        try:
            self.resolink = client.Client()
            await self.resolink.connect(self.port, self.host)

            # Fetch root slot with full depth (-1 means all children)
            response = await self.resolink.request(
                messages.GetSlot(slotId="Root", depth=-1, includeComponentData=False)
            )

            if response.success and isinstance(response, responses.SlotData) and response.data:
                self.root_slot = response.data
                self._build_tree(tree, response.data)
            else:
                error_msg = getattr(response, "errorInfo", None) or "Unknown error"
                tree.root.set_label(f"Error: {error_msg}")

        except Exception as e:
            tree.root.set_label(f"Connection failed: {e}")

    def _build_tree(self, tree: Tree, root_slot: Slot) -> None:
        """Build the tree widget from slot data."""
        tree.root.set_label(self._get_slot_name(root_slot))
        tree.root.data = root_slot

        # Add children recursively
        self._add_children(tree.root, root_slot)

        # Collapse the root initially
        tree.root.collapse()

    def _get_slot_name(self, slot: Slot) -> str:
        """Get the display name for a slot."""
        if slot.name and slot.name.value:
            return slot.name.value
        return "(unnamed)"

    def _add_children(self, node: TreeNode, slot: Slot) -> None:
        """Recursively add child slots to a tree node."""
        if not slot.children:
            return
        for child in slot.children:
            child_name = self._get_slot_name(child)
            child_node = node.add(child_name, data=child)
            self._add_children(child_node, child)
            child_node.collapse()

    def action_collapse_all(self) -> None:
        """Collapse all nodes in the tree."""
        tree = self.query_one(Tree)

        def collapse_recursive(node: TreeNode) -> None:
            node.collapse()
            for child in node.children:
                collapse_recursive(child)

        collapse_recursive(tree.root)

    def action_toggle_node(self) -> None:
        """Toggle expansion of the currently selected node."""
        tree = self.query_one(Tree)
        if tree.cursor_node:
            tree.cursor_node.toggle()

    async def on_unmount(self) -> None:
        """Close the connection when the app exits."""
        if self.resolink:
            await self.resolink.close()


def main(port: int, host: str = "localhost") -> None:
    """Run the slot tree TUI app."""
    app = SlotTreeApp(port, host)
    app.run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tree.py <port> [host]")
        sys.exit(1)

    port_arg = int(sys.argv[1])
    host_arg = sys.argv[2] if len(sys.argv) > 2 else "localhost"
    main(port_arg, host_arg)
