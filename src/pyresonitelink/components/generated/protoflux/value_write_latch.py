"""Generated component: ValueWriteLatch.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueWriteLatchBase(GeneratedComponent):
    """Base class for ValueWriteLatch<T> variants."""

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
class ValueWriteLatchBool(ValueWriteLatchBase):
    """ValueWriteLatch<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>


@dataclass
class ValueWriteLatchByte(ValueWriteLatchBase):
    """ValueWriteLatch<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>


@dataclass
class ValueWriteLatchUshort(ValueWriteLatchBase):
    """ValueWriteLatch<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>


@dataclass
class ValueWriteLatchUint(ValueWriteLatchBase):
    """ValueWriteLatch<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>


@dataclass
class ValueWriteLatchUlong(ValueWriteLatchBase):
    """ValueWriteLatch<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>


@dataclass
class ValueWriteLatchSbyte(ValueWriteLatchBase):
    """ValueWriteLatch<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>


@dataclass
class ValueWriteLatchShort(ValueWriteLatchBase):
    """ValueWriteLatch<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>


@dataclass
class ValueWriteLatchInt(ValueWriteLatchBase):
    """ValueWriteLatch<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>


@dataclass
class ValueWriteLatchLong(ValueWriteLatchBase):
    """ValueWriteLatch<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>


@dataclass
class ValueWriteLatchFloat(ValueWriteLatchBase):
    """ValueWriteLatch<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>


@dataclass
class ValueWriteLatchDouble(ValueWriteLatchBase):
    """ValueWriteLatch<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>


@dataclass
class ValueWriteLatchDecimal(ValueWriteLatchBase):
    """ValueWriteLatch<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>


@dataclass
class ValueWriteLatchChar(ValueWriteLatchBase):
    """ValueWriteLatch<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>


@dataclass
class ValueWriteLatchString(ValueWriteLatchBase):
    """ValueWriteLatch<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>


@dataclass
class ValueWriteLatchUri(ValueWriteLatchBase):
    """ValueWriteLatch<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>


@dataclass
class ValueWriteLatchBool2(ValueWriteLatchBase):
    """ValueWriteLatch<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>


@dataclass
class ValueWriteLatchByte2(ValueWriteLatchBase):
    """ValueWriteLatch<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>


@dataclass
class ValueWriteLatchUshort2(ValueWriteLatchBase):
    """ValueWriteLatch<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>


@dataclass
class ValueWriteLatchUint2(ValueWriteLatchBase):
    """ValueWriteLatch<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>


@dataclass
class ValueWriteLatchUlong2(ValueWriteLatchBase):
    """ValueWriteLatch<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>


@dataclass
class ValueWriteLatchSbyte2(ValueWriteLatchBase):
    """ValueWriteLatch<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>


@dataclass
class ValueWriteLatchShort2(ValueWriteLatchBase):
    """ValueWriteLatch<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>


@dataclass
class ValueWriteLatchInt2(ValueWriteLatchBase):
    """ValueWriteLatch<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>


@dataclass
class ValueWriteLatchLong2(ValueWriteLatchBase):
    """ValueWriteLatch<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>


@dataclass
class ValueWriteLatchFloat2(ValueWriteLatchBase):
    """ValueWriteLatch<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>


@dataclass
class ValueWriteLatchDouble2(ValueWriteLatchBase):
    """ValueWriteLatch<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>


@dataclass
class ValueWriteLatchBool3(ValueWriteLatchBase):
    """ValueWriteLatch<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>


@dataclass
class ValueWriteLatchByte3(ValueWriteLatchBase):
    """ValueWriteLatch<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>


@dataclass
class ValueWriteLatchUshort3(ValueWriteLatchBase):
    """ValueWriteLatch<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>


@dataclass
class ValueWriteLatchUint3(ValueWriteLatchBase):
    """ValueWriteLatch<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>


@dataclass
class ValueWriteLatchUlong3(ValueWriteLatchBase):
    """ValueWriteLatch<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>


@dataclass
class ValueWriteLatchSbyte3(ValueWriteLatchBase):
    """ValueWriteLatch<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>


@dataclass
class ValueWriteLatchShort3(ValueWriteLatchBase):
    """ValueWriteLatch<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>


@dataclass
class ValueWriteLatchInt3(ValueWriteLatchBase):
    """ValueWriteLatch<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>


@dataclass
class ValueWriteLatchLong3(ValueWriteLatchBase):
    """ValueWriteLatch<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>


@dataclass
class ValueWriteLatchFloat3(ValueWriteLatchBase):
    """ValueWriteLatch<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>


@dataclass
class ValueWriteLatchDouble3(ValueWriteLatchBase):
    """ValueWriteLatch<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>


@dataclass
class ValueWriteLatchBool4(ValueWriteLatchBase):
    """ValueWriteLatch<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>


@dataclass
class ValueWriteLatchByte4(ValueWriteLatchBase):
    """ValueWriteLatch<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>


@dataclass
class ValueWriteLatchUshort4(ValueWriteLatchBase):
    """ValueWriteLatch<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>


@dataclass
class ValueWriteLatchUint4(ValueWriteLatchBase):
    """ValueWriteLatch<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>


@dataclass
class ValueWriteLatchUlong4(ValueWriteLatchBase):
    """ValueWriteLatch<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>


@dataclass
class ValueWriteLatchSbyte4(ValueWriteLatchBase):
    """ValueWriteLatch<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>


@dataclass
class ValueWriteLatchShort4(ValueWriteLatchBase):
    """ValueWriteLatch<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>


@dataclass
class ValueWriteLatchInt4(ValueWriteLatchBase):
    """ValueWriteLatch<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>


@dataclass
class ValueWriteLatchLong4(ValueWriteLatchBase):
    """ValueWriteLatch<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>


@dataclass
class ValueWriteLatchFloat4(ValueWriteLatchBase):
    """ValueWriteLatch<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>


@dataclass
class ValueWriteLatchDouble4(ValueWriteLatchBase):
    """ValueWriteLatch<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>


@dataclass
class ValueWriteLatchFloat_2x2(ValueWriteLatchBase):
    """ValueWriteLatch<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>


@dataclass
class ValueWriteLatchDouble_2x2(ValueWriteLatchBase):
    """ValueWriteLatch<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>


@dataclass
class ValueWriteLatchFloat_3x3(ValueWriteLatchBase):
    """ValueWriteLatch<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>


@dataclass
class ValueWriteLatchDouble_3x3(ValueWriteLatchBase):
    """ValueWriteLatch<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>


@dataclass
class ValueWriteLatchFloat_4x4(ValueWriteLatchBase):
    """ValueWriteLatch<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>


@dataclass
class ValueWriteLatchDouble_4x4(ValueWriteLatchBase):
    """ValueWriteLatch<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>


@dataclass
class ValueWriteLatchFloatQ(ValueWriteLatchBase):
    """ValueWriteLatch<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>


@dataclass
class ValueWriteLatchDoubleQ(ValueWriteLatchBase):
    """ValueWriteLatch<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>


@dataclass
class ValueWriteLatchDateTime(ValueWriteLatchBase):
    """ValueWriteLatch<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueWriteLatchTimeSpan(ValueWriteLatchBase):
    """ValueWriteLatch<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueWriteLatchColor(ValueWriteLatchBase):
    """ValueWriteLatch<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>


@dataclass
class ValueWriteLatchColorX(ValueWriteLatchBase):
    """ValueWriteLatch<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>


@dataclass
class ValueWriteLatchShadowCastMode(ValueWriteLatchBase):
    """ValueWriteLatch<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueWriteLatchLightType(ValueWriteLatchBase):
    """ValueWriteLatch<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueWriteLatchSessionAccessLevel(ValueWriteLatchBase):
    """ValueWriteLatch<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueWriteLatchKey(ValueWriteLatchBase):
    """ValueWriteLatch<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueWriteLatchHttpStatusCode(ValueWriteLatchBase):
    """ValueWriteLatch<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueWriteLatchHeadOutputDevice(ValueWriteLatchBase):
    """ValueWriteLatch<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueWriteLatchReflectionProbeClear(ValueWriteLatchBase):
    """ValueWriteLatch<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueWriteLatchReflectionProbeType(ValueWriteLatchBase):
    """ValueWriteLatch<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueWriteLatchReflectionProbeTimeSlicingMode(ValueWriteLatchBase):
    """ValueWriteLatch<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueWriteLatchCameraClearMode(ValueWriteLatchBase):
    """ValueWriteLatch<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueWriteLatchCameraPositioningMode(ValueWriteLatchBase):
    """ValueWriteLatch<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.CameraPositioningMode>


@dataclass
class ValueWriteLatchCameraProjection(ValueWriteLatchBase):
    """ValueWriteLatch<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueWriteLatchZWrite(ValueWriteLatchBase):
    """ValueWriteLatch<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZWrite>


@dataclass
class ValueWriteLatchZTest(ValueWriteLatchBase):
    """ValueWriteLatch<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZTest>


@dataclass
class ValueWriteLatchBlend(ValueWriteLatchBase):
    """ValueWriteLatch<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Blend>


@dataclass
class ValueWriteLatchBlendMode(ValueWriteLatchBase):
    """ValueWriteLatch<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.BlendMode>


@dataclass
class ValueWriteLatchCulling(ValueWriteLatchBase):
    """ValueWriteLatch<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Culling>


@dataclass
class ValueWriteLatchBodyNode(ValueWriteLatchBase):
    """ValueWriteLatch<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueWriteLatchChirality(ValueWriteLatchBase):
    """ValueWriteLatch<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueWriteLatchDummyEnum(ValueWriteLatchBase):
    """ValueWriteLatch<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWriteLatch<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_reset": "OnReset",
        "on_set": "OnSet",
        "reset_value": "ResetValue",
        "set_value": "SetValue",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_reset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_set: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    reset_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    set_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>


# Type alias for any ValueWriteLatch variant
ValueWriteLatch = (
    ValueWriteLatchBool |
    ValueWriteLatchByte |
    ValueWriteLatchUshort |
    ValueWriteLatchUint |
    ValueWriteLatchUlong |
    ValueWriteLatchSbyte |
    ValueWriteLatchShort |
    ValueWriteLatchInt |
    ValueWriteLatchLong |
    ValueWriteLatchFloat |
    ValueWriteLatchDouble |
    ValueWriteLatchDecimal |
    ValueWriteLatchChar |
    ValueWriteLatchString |
    ValueWriteLatchUri |
    ValueWriteLatchBool2 |
    ValueWriteLatchByte2 |
    ValueWriteLatchUshort2 |
    ValueWriteLatchUint2 |
    ValueWriteLatchUlong2 |
    ValueWriteLatchSbyte2 |
    ValueWriteLatchShort2 |
    ValueWriteLatchInt2 |
    ValueWriteLatchLong2 |
    ValueWriteLatchFloat2 |
    ValueWriteLatchDouble2 |
    ValueWriteLatchBool3 |
    ValueWriteLatchByte3 |
    ValueWriteLatchUshort3 |
    ValueWriteLatchUint3 |
    ValueWriteLatchUlong3 |
    ValueWriteLatchSbyte3 |
    ValueWriteLatchShort3 |
    ValueWriteLatchInt3 |
    ValueWriteLatchLong3 |
    ValueWriteLatchFloat3 |
    ValueWriteLatchDouble3 |
    ValueWriteLatchBool4 |
    ValueWriteLatchByte4 |
    ValueWriteLatchUshort4 |
    ValueWriteLatchUint4 |
    ValueWriteLatchUlong4 |
    ValueWriteLatchSbyte4 |
    ValueWriteLatchShort4 |
    ValueWriteLatchInt4 |
    ValueWriteLatchLong4 |
    ValueWriteLatchFloat4 |
    ValueWriteLatchDouble4 |
    ValueWriteLatchFloat_2x2 |
    ValueWriteLatchDouble_2x2 |
    ValueWriteLatchFloat_3x3 |
    ValueWriteLatchDouble_3x3 |
    ValueWriteLatchFloat_4x4 |
    ValueWriteLatchDouble_4x4 |
    ValueWriteLatchFloatQ |
    ValueWriteLatchDoubleQ |
    ValueWriteLatchDateTime |
    ValueWriteLatchTimeSpan |
    ValueWriteLatchColor |
    ValueWriteLatchColorX |
    ValueWriteLatchShadowCastMode |
    ValueWriteLatchLightType |
    ValueWriteLatchSessionAccessLevel |
    ValueWriteLatchKey |
    ValueWriteLatchHttpStatusCode |
    ValueWriteLatchHeadOutputDevice |
    ValueWriteLatchReflectionProbeClear |
    ValueWriteLatchReflectionProbeType |
    ValueWriteLatchReflectionProbeTimeSlicingMode |
    ValueWriteLatchCameraClearMode |
    ValueWriteLatchCameraPositioningMode |
    ValueWriteLatchCameraProjection |
    ValueWriteLatchZWrite |
    ValueWriteLatchZTest |
    ValueWriteLatchBlend |
    ValueWriteLatchBlendMode |
    ValueWriteLatchCulling |
    ValueWriteLatchBodyNode |
    ValueWriteLatchChirality |
    ValueWriteLatchDummyEnum
)