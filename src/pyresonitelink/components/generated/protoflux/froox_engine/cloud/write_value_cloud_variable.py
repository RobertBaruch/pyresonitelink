"""Generated component: WriteValueCloudVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WriteValueCloudVariableBase(GeneratedComponent):
    """Base class for WriteValueCloudVariable<T> variants."""

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
class WriteValueCloudVariableBool(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableByte(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUshort(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUint(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUlong(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableSbyte(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableShort(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableInt(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableLong(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDecimal(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableChar(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableString(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUri(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBool2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableByte2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUshort2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUint2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUlong2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableSbyte2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableShort2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableInt2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableLong2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBool3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableByte3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUshort3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUint3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUlong3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableSbyte3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableShort3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableInt3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableLong3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBool4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableByte4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUshort4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUint4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableUlong4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableSbyte4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableShort4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableInt4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableLong4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat_2x2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble_2x2(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat_3x3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble_3x3(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloat_4x4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDouble_4x4(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableFloatQ(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDoubleQ(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDateTime(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableTimeSpan(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableColor(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableColorX(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableShadowCastMode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableLightType(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableSessionAccessLevel(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableKey(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableHttpStatusCode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableHeadOutputDevice(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableReflectionProbeClear(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableReflectionProbeType(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableReflectionProbeTimeSlicingMode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableCameraClearMode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableCameraPositioningMode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableCameraProjection(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableZWrite(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableZTest(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBlend(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBlendMode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableCulling(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableBodyNode(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableChirality(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class WriteValueCloudVariableDummyEnum(WriteValueCloudVariableBase):
    """WriteValueCloudVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Cloud.WriteValueCloudVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_done": "OnDone",
        "on_fail": "OnFail",
        "on_request": "OnRequest",
        "path": "Path",
        "value": "Value",
        "variable_owner_id": "VariableOwnerId",
    }

    on_done: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_request: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    variable_owner_id: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


# Type alias for any WriteValueCloudVariable variant
WriteValueCloudVariable = (
    WriteValueCloudVariableBool |
    WriteValueCloudVariableByte |
    WriteValueCloudVariableUshort |
    WriteValueCloudVariableUint |
    WriteValueCloudVariableUlong |
    WriteValueCloudVariableSbyte |
    WriteValueCloudVariableShort |
    WriteValueCloudVariableInt |
    WriteValueCloudVariableLong |
    WriteValueCloudVariableFloat |
    WriteValueCloudVariableDouble |
    WriteValueCloudVariableDecimal |
    WriteValueCloudVariableChar |
    WriteValueCloudVariableString |
    WriteValueCloudVariableUri |
    WriteValueCloudVariableBool2 |
    WriteValueCloudVariableByte2 |
    WriteValueCloudVariableUshort2 |
    WriteValueCloudVariableUint2 |
    WriteValueCloudVariableUlong2 |
    WriteValueCloudVariableSbyte2 |
    WriteValueCloudVariableShort2 |
    WriteValueCloudVariableInt2 |
    WriteValueCloudVariableLong2 |
    WriteValueCloudVariableFloat2 |
    WriteValueCloudVariableDouble2 |
    WriteValueCloudVariableBool3 |
    WriteValueCloudVariableByte3 |
    WriteValueCloudVariableUshort3 |
    WriteValueCloudVariableUint3 |
    WriteValueCloudVariableUlong3 |
    WriteValueCloudVariableSbyte3 |
    WriteValueCloudVariableShort3 |
    WriteValueCloudVariableInt3 |
    WriteValueCloudVariableLong3 |
    WriteValueCloudVariableFloat3 |
    WriteValueCloudVariableDouble3 |
    WriteValueCloudVariableBool4 |
    WriteValueCloudVariableByte4 |
    WriteValueCloudVariableUshort4 |
    WriteValueCloudVariableUint4 |
    WriteValueCloudVariableUlong4 |
    WriteValueCloudVariableSbyte4 |
    WriteValueCloudVariableShort4 |
    WriteValueCloudVariableInt4 |
    WriteValueCloudVariableLong4 |
    WriteValueCloudVariableFloat4 |
    WriteValueCloudVariableDouble4 |
    WriteValueCloudVariableFloat_2x2 |
    WriteValueCloudVariableDouble_2x2 |
    WriteValueCloudVariableFloat_3x3 |
    WriteValueCloudVariableDouble_3x3 |
    WriteValueCloudVariableFloat_4x4 |
    WriteValueCloudVariableDouble_4x4 |
    WriteValueCloudVariableFloatQ |
    WriteValueCloudVariableDoubleQ |
    WriteValueCloudVariableDateTime |
    WriteValueCloudVariableTimeSpan |
    WriteValueCloudVariableColor |
    WriteValueCloudVariableColorX |
    WriteValueCloudVariableShadowCastMode |
    WriteValueCloudVariableLightType |
    WriteValueCloudVariableSessionAccessLevel |
    WriteValueCloudVariableKey |
    WriteValueCloudVariableHttpStatusCode |
    WriteValueCloudVariableHeadOutputDevice |
    WriteValueCloudVariableReflectionProbeClear |
    WriteValueCloudVariableReflectionProbeType |
    WriteValueCloudVariableReflectionProbeTimeSlicingMode |
    WriteValueCloudVariableCameraClearMode |
    WriteValueCloudVariableCameraPositioningMode |
    WriteValueCloudVariableCameraProjection |
    WriteValueCloudVariableZWrite |
    WriteValueCloudVariableZTest |
    WriteValueCloudVariableBlend |
    WriteValueCloudVariableBlendMode |
    WriteValueCloudVariableCulling |
    WriteValueCloudVariableBodyNode |
    WriteValueCloudVariableChirality |
    WriteValueCloudVariableDummyEnum
)