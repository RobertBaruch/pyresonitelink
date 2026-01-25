"""Generated component: ReadValueCloudVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ReadValueCloudVariableBase(GeneratedComponent):
    """Base class for ReadValueCloudVariable<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "protoflux.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class ReadValueCloudVariableBool(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableByte(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUshort(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUint(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUlong(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableSbyte(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableShort(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableInt(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableLong(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDecimal(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableChar(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableString(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUri(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBool2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableByte2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUshort2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUint2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUlong2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableSbyte2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableShort2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableInt2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableLong2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBool3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableByte3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUshort3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUint3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUlong3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableSbyte3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableShort3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableInt3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableLong3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBool4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableByte4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUshort4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUint4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableUlong4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableSbyte4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableShort4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableInt4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableLong4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat_2x2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble_2x2(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat_3x3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble_3x3(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloat_4x4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDouble_4x4(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableFloatQ(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDoubleQ(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDateTime(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableTimeSpan(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableColor(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableColorX(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableShadowCastMode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableLightType(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableSessionAccessLevel(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableKey(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableHttpStatusCode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableHeadOutputDevice(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableReflectionProbeClear(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableReflectionProbeType(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableReflectionProbeTimeSlicingMode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableCameraClearMode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableCameraPositioningMode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableCameraProjection(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableZWrite(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableZTest(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBlend(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBlendMode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableCulling(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableBodyNode(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableChirality(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ReadValueCloudVariableDummyEnum(ReadValueCloudVariableBase):
    """ReadValueCloudVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.ReadValueCloudVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


# Type alias for any ReadValueCloudVariable variant
ReadValueCloudVariable = (
    ReadValueCloudVariableBool |
    ReadValueCloudVariableByte |
    ReadValueCloudVariableUshort |
    ReadValueCloudVariableUint |
    ReadValueCloudVariableUlong |
    ReadValueCloudVariableSbyte |
    ReadValueCloudVariableShort |
    ReadValueCloudVariableInt |
    ReadValueCloudVariableLong |
    ReadValueCloudVariableFloat |
    ReadValueCloudVariableDouble |
    ReadValueCloudVariableDecimal |
    ReadValueCloudVariableChar |
    ReadValueCloudVariableString |
    ReadValueCloudVariableUri |
    ReadValueCloudVariableBool2 |
    ReadValueCloudVariableByte2 |
    ReadValueCloudVariableUshort2 |
    ReadValueCloudVariableUint2 |
    ReadValueCloudVariableUlong2 |
    ReadValueCloudVariableSbyte2 |
    ReadValueCloudVariableShort2 |
    ReadValueCloudVariableInt2 |
    ReadValueCloudVariableLong2 |
    ReadValueCloudVariableFloat2 |
    ReadValueCloudVariableDouble2 |
    ReadValueCloudVariableBool3 |
    ReadValueCloudVariableByte3 |
    ReadValueCloudVariableUshort3 |
    ReadValueCloudVariableUint3 |
    ReadValueCloudVariableUlong3 |
    ReadValueCloudVariableSbyte3 |
    ReadValueCloudVariableShort3 |
    ReadValueCloudVariableInt3 |
    ReadValueCloudVariableLong3 |
    ReadValueCloudVariableFloat3 |
    ReadValueCloudVariableDouble3 |
    ReadValueCloudVariableBool4 |
    ReadValueCloudVariableByte4 |
    ReadValueCloudVariableUshort4 |
    ReadValueCloudVariableUint4 |
    ReadValueCloudVariableUlong4 |
    ReadValueCloudVariableSbyte4 |
    ReadValueCloudVariableShort4 |
    ReadValueCloudVariableInt4 |
    ReadValueCloudVariableLong4 |
    ReadValueCloudVariableFloat4 |
    ReadValueCloudVariableDouble4 |
    ReadValueCloudVariableFloat_2x2 |
    ReadValueCloudVariableDouble_2x2 |
    ReadValueCloudVariableFloat_3x3 |
    ReadValueCloudVariableDouble_3x3 |
    ReadValueCloudVariableFloat_4x4 |
    ReadValueCloudVariableDouble_4x4 |
    ReadValueCloudVariableFloatQ |
    ReadValueCloudVariableDoubleQ |
    ReadValueCloudVariableDateTime |
    ReadValueCloudVariableTimeSpan |
    ReadValueCloudVariableColor |
    ReadValueCloudVariableColorX |
    ReadValueCloudVariableShadowCastMode |
    ReadValueCloudVariableLightType |
    ReadValueCloudVariableSessionAccessLevel |
    ReadValueCloudVariableKey |
    ReadValueCloudVariableHttpStatusCode |
    ReadValueCloudVariableHeadOutputDevice |
    ReadValueCloudVariableReflectionProbeClear |
    ReadValueCloudVariableReflectionProbeType |
    ReadValueCloudVariableReflectionProbeTimeSlicingMode |
    ReadValueCloudVariableCameraClearMode |
    ReadValueCloudVariableCameraPositioningMode |
    ReadValueCloudVariableCameraProjection |
    ReadValueCloudVariableZWrite |
    ReadValueCloudVariableZTest |
    ReadValueCloudVariableBlend |
    ReadValueCloudVariableBlendMode |
    ReadValueCloudVariableCulling |
    ReadValueCloudVariableBodyNode |
    ReadValueCloudVariableChirality |
    ReadValueCloudVariableDummyEnum
)