"""CLI tool for dumping Resonite slot hierarchy to a JSON file."""

import argparse
import asyncio
import json

from pyresonitelink import client
from pyresonitelink.data import messages
from pyresonitelink.data import workers


async def dump_slot_data(
    port: int, host: str, output_file: str, depth: int, include_components: bool
) -> None:
    """Connect to Resonite and dump the root slot data to a JSON file."""
    uri = f"ws://{host}:{port}"

    print(f"Connecting to {uri}...")
    resolink = client.Client()
    await resolink.connect(port, host)
    print(
        f"Connected. Requesting slot data (depth {depth}, include components:"
        f" {include_components})..."
    )

    json_response = await resolink.request_json(
        messages.GetSlot(
            slotId=workers.Slot.ROOT_SLOT_ID,
            depth=depth,
            includeComponentData=include_components,
        )
    )

    # Check for success
    if not json_response.get("success", False):
        error_info = json_response.get("errorInfo", "Unknown error")
        print(f"Error: {error_info}")
        return

    # Write to file with pretty formatting
    print(f"Writing to {output_file}...")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(json_response, f, indent=2, ensure_ascii=False)

    print(f"Done. Slot data written to {output_file}")


def main() -> None:
    """Run the dump tree CLI tool."""
    parser = argparse.ArgumentParser(
        description="Dump Resonite slot hierarchy to a JSON file"
    )
    parser.add_argument(
        "port", type=int, help="Port number for ResoniteLink connection"
    )
    parser.add_argument("output", type=str, help="Output JSON file path")
    parser.add_argument(
        "--host", default="localhost", help="Host address (default: localhost)"
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=-1,
        help="Depth of slot hierarchy to fetch (-1 for unlimited, default: -1)",
    )
    parser.add_argument(
        "--include-components",
        action="store_true",
        help="Include component data in the output (default: False)",
    )

    args = parser.parse_args()

    asyncio.run(
        dump_slot_data(
            args.port, args.host, args.output, args.depth, args.include_components
        )
    )


if __name__ == "__main__":
    main()
