"""Generated component: TextEditorEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TextEditorEvents(GeneratedComponent):
    """TextEditorEvents component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.TextEditorEvents
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.TextEditorEvents"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "editing_changed": "EditingChanged",
        "editing_finished": "EditingFinished",
        "editing_started": "EditingStarted",
        "editor": "Editor",
        "enabled": "Enabled",
        "persistent": "persistent",
        "submit_pressed": "SubmitPressed",
        "update_order": "UpdateOrder",
    }

    editing_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    editing_finished: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    editing_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    editor: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.TextEditor>
    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    submit_pressed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    update_order: FieldInt | None = None