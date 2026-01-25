"""Generated component: WriteTextToFile.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WriteTextToFile(GeneratedComponent):
    """WriteTextToFile component.

    ResoniteLink schema for FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Experimental.WriteTextToFile
    """

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Experimental.WriteTextToFile"
    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "append": "Append",
        "enabled": "Enabled",
        "file_path": "FilePath",
        "new_line": "NewLine",
        "on_write_fail": "OnWriteFail",
        "on_write_finished": "OnWriteFinished",
        "on_write_started": "OnWriteStarted",
        "persistent": "persistent",
        "string": "String",
        "update_order": "UpdateOrder",
    }

    append: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    enabled: FieldBool | None = None
    file_path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    new_line: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_write_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_write_finished: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_write_started: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    persistent: FieldBool | None = None
    string: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    update_order: FieldInt | None = None