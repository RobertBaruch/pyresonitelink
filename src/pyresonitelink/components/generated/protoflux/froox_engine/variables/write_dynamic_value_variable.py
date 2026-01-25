"""Generated component: WriteDynamicValueVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WriteDynamicValueVariableBase(GeneratedComponent):
    """Base class for WriteDynamicValueVariable<T> variants."""

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
class WriteDynamicValueVariableBool(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class WriteDynamicValueVariableByte(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class WriteDynamicValueVariableUshort(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class WriteDynamicValueVariableUint(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class WriteDynamicValueVariableUlong(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class WriteDynamicValueVariableSbyte(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class WriteDynamicValueVariableShort(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class WriteDynamicValueVariableInt(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class WriteDynamicValueVariableLong(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class WriteDynamicValueVariableFloat(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class WriteDynamicValueVariableDouble(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class WriteDynamicValueVariableDecimal(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class WriteDynamicValueVariableChar(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class WriteDynamicValueVariableString(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class WriteDynamicValueVariableUri(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class WriteDynamicValueVariableBool2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class WriteDynamicValueVariableByte2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class WriteDynamicValueVariableUshort2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class WriteDynamicValueVariableUint2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class WriteDynamicValueVariableUlong2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class WriteDynamicValueVariableSbyte2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class WriteDynamicValueVariableShort2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class WriteDynamicValueVariableInt2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class WriteDynamicValueVariableLong2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class WriteDynamicValueVariableFloat2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class WriteDynamicValueVariableDouble2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class WriteDynamicValueVariableBool3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class WriteDynamicValueVariableByte3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class WriteDynamicValueVariableUshort3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class WriteDynamicValueVariableUint3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class WriteDynamicValueVariableUlong3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class WriteDynamicValueVariableSbyte3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class WriteDynamicValueVariableShort3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class WriteDynamicValueVariableInt3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class WriteDynamicValueVariableLong3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class WriteDynamicValueVariableFloat3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class WriteDynamicValueVariableDouble3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class WriteDynamicValueVariableBool4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class WriteDynamicValueVariableByte4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class WriteDynamicValueVariableUshort4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class WriteDynamicValueVariableUint4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class WriteDynamicValueVariableUlong4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class WriteDynamicValueVariableSbyte4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class WriteDynamicValueVariableShort4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class WriteDynamicValueVariableInt4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class WriteDynamicValueVariableLong4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class WriteDynamicValueVariableFloat4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class WriteDynamicValueVariableDouble4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class WriteDynamicValueVariableFloat_2x2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class WriteDynamicValueVariableDouble_2x2(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class WriteDynamicValueVariableFloat_3x3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class WriteDynamicValueVariableDouble_3x3(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class WriteDynamicValueVariableFloat_4x4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class WriteDynamicValueVariableDouble_4x4(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class WriteDynamicValueVariableFloatQ(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class WriteDynamicValueVariableDoubleQ(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class WriteDynamicValueVariableDateTime(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class WriteDynamicValueVariableTimeSpan(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class WriteDynamicValueVariableColor(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class WriteDynamicValueVariableColorX(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class WriteDynamicValueVariableShadowCastMode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class WriteDynamicValueVariableLightType(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class WriteDynamicValueVariableSessionAccessLevel(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class WriteDynamicValueVariableKey(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class WriteDynamicValueVariableHttpStatusCode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class WriteDynamicValueVariableHeadOutputDevice(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class WriteDynamicValueVariableReflectionProbeClear(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class WriteDynamicValueVariableReflectionProbeType(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class WriteDynamicValueVariableReflectionProbeTimeSlicingMode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class WriteDynamicValueVariableCameraClearMode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class WriteDynamicValueVariableCameraPositioningMode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class WriteDynamicValueVariableCameraProjection(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class WriteDynamicValueVariableZWrite(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class WriteDynamicValueVariableZTest(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class WriteDynamicValueVariableBlend(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class WriteDynamicValueVariableBlendMode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class WriteDynamicValueVariableCulling(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class WriteDynamicValueVariableBodyNode(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class WriteDynamicValueVariableChirality(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class WriteDynamicValueVariableDummyEnum(WriteDynamicValueVariableBase):
    """WriteDynamicValueVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteDynamicValueVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_success": "OnSuccess",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_success: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any WriteDynamicValueVariable variant
WriteDynamicValueVariable = (
    WriteDynamicValueVariableBool |
    WriteDynamicValueVariableByte |
    WriteDynamicValueVariableUshort |
    WriteDynamicValueVariableUint |
    WriteDynamicValueVariableUlong |
    WriteDynamicValueVariableSbyte |
    WriteDynamicValueVariableShort |
    WriteDynamicValueVariableInt |
    WriteDynamicValueVariableLong |
    WriteDynamicValueVariableFloat |
    WriteDynamicValueVariableDouble |
    WriteDynamicValueVariableDecimal |
    WriteDynamicValueVariableChar |
    WriteDynamicValueVariableString |
    WriteDynamicValueVariableUri |
    WriteDynamicValueVariableBool2 |
    WriteDynamicValueVariableByte2 |
    WriteDynamicValueVariableUshort2 |
    WriteDynamicValueVariableUint2 |
    WriteDynamicValueVariableUlong2 |
    WriteDynamicValueVariableSbyte2 |
    WriteDynamicValueVariableShort2 |
    WriteDynamicValueVariableInt2 |
    WriteDynamicValueVariableLong2 |
    WriteDynamicValueVariableFloat2 |
    WriteDynamicValueVariableDouble2 |
    WriteDynamicValueVariableBool3 |
    WriteDynamicValueVariableByte3 |
    WriteDynamicValueVariableUshort3 |
    WriteDynamicValueVariableUint3 |
    WriteDynamicValueVariableUlong3 |
    WriteDynamicValueVariableSbyte3 |
    WriteDynamicValueVariableShort3 |
    WriteDynamicValueVariableInt3 |
    WriteDynamicValueVariableLong3 |
    WriteDynamicValueVariableFloat3 |
    WriteDynamicValueVariableDouble3 |
    WriteDynamicValueVariableBool4 |
    WriteDynamicValueVariableByte4 |
    WriteDynamicValueVariableUshort4 |
    WriteDynamicValueVariableUint4 |
    WriteDynamicValueVariableUlong4 |
    WriteDynamicValueVariableSbyte4 |
    WriteDynamicValueVariableShort4 |
    WriteDynamicValueVariableInt4 |
    WriteDynamicValueVariableLong4 |
    WriteDynamicValueVariableFloat4 |
    WriteDynamicValueVariableDouble4 |
    WriteDynamicValueVariableFloat_2x2 |
    WriteDynamicValueVariableDouble_2x2 |
    WriteDynamicValueVariableFloat_3x3 |
    WriteDynamicValueVariableDouble_3x3 |
    WriteDynamicValueVariableFloat_4x4 |
    WriteDynamicValueVariableDouble_4x4 |
    WriteDynamicValueVariableFloatQ |
    WriteDynamicValueVariableDoubleQ |
    WriteDynamicValueVariableDateTime |
    WriteDynamicValueVariableTimeSpan |
    WriteDynamicValueVariableColor |
    WriteDynamicValueVariableColorX |
    WriteDynamicValueVariableShadowCastMode |
    WriteDynamicValueVariableLightType |
    WriteDynamicValueVariableSessionAccessLevel |
    WriteDynamicValueVariableKey |
    WriteDynamicValueVariableHttpStatusCode |
    WriteDynamicValueVariableHeadOutputDevice |
    WriteDynamicValueVariableReflectionProbeClear |
    WriteDynamicValueVariableReflectionProbeType |
    WriteDynamicValueVariableReflectionProbeTimeSlicingMode |
    WriteDynamicValueVariableCameraClearMode |
    WriteDynamicValueVariableCameraPositioningMode |
    WriteDynamicValueVariableCameraProjection |
    WriteDynamicValueVariableZWrite |
    WriteDynamicValueVariableZTest |
    WriteDynamicValueVariableBlend |
    WriteDynamicValueVariableBlendMode |
    WriteDynamicValueVariableCulling |
    WriteDynamicValueVariableBodyNode |
    WriteDynamicValueVariableChirality |
    WriteDynamicValueVariableDummyEnum
)