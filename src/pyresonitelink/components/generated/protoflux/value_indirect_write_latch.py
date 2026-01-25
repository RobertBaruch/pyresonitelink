"""Generated component: ValueIndirectWriteLatch.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueIndirectWriteLatchBase(GeneratedComponent):
    """Base class for ValueIndirectWriteLatch<T> variants."""

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
class ValueIndirectWriteLatchBool(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<bool>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>>


@dataclass
class ValueIndirectWriteLatchByte(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<byte>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>>


@dataclass
class ValueIndirectWriteLatchUshort(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ushort>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>>


@dataclass
class ValueIndirectWriteLatchUint(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<uint>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>>


@dataclass
class ValueIndirectWriteLatchUlong(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ulong>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>>


@dataclass
class ValueIndirectWriteLatchSbyte(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<sbyte>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>>


@dataclass
class ValueIndirectWriteLatchShort(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<short>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>>


@dataclass
class ValueIndirectWriteLatchInt(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<int>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>>


@dataclass
class ValueIndirectWriteLatchLong(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<long>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>>


@dataclass
class ValueIndirectWriteLatchFloat(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>>


@dataclass
class ValueIndirectWriteLatchDouble(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>>


@dataclass
class ValueIndirectWriteLatchDecimal(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<decimal>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>>


@dataclass
class ValueIndirectWriteLatchChar(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<char>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>>


@dataclass
class ValueIndirectWriteLatchString(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<string>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>>


@dataclass
class ValueIndirectWriteLatchUri(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<Uri>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>>


@dataclass
class ValueIndirectWriteLatchBool2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<bool2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>>


@dataclass
class ValueIndirectWriteLatchByte2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<byte2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>>


@dataclass
class ValueIndirectWriteLatchUshort2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ushort2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>>


@dataclass
class ValueIndirectWriteLatchUint2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<uint2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>>


@dataclass
class ValueIndirectWriteLatchUlong2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ulong2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>>


@dataclass
class ValueIndirectWriteLatchSbyte2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<sbyte2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>>


@dataclass
class ValueIndirectWriteLatchShort2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<short2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>>


@dataclass
class ValueIndirectWriteLatchInt2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<int2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>>


@dataclass
class ValueIndirectWriteLatchLong2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<long2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>>


@dataclass
class ValueIndirectWriteLatchFloat2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>>


@dataclass
class ValueIndirectWriteLatchDouble2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>>


@dataclass
class ValueIndirectWriteLatchBool3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<bool3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>>


@dataclass
class ValueIndirectWriteLatchByte3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<byte3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>>


@dataclass
class ValueIndirectWriteLatchUshort3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ushort3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>>


@dataclass
class ValueIndirectWriteLatchUint3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<uint3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>>


@dataclass
class ValueIndirectWriteLatchUlong3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ulong3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>>


@dataclass
class ValueIndirectWriteLatchSbyte3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<sbyte3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>>


@dataclass
class ValueIndirectWriteLatchShort3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<short3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>>


@dataclass
class ValueIndirectWriteLatchInt3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<int3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>>


@dataclass
class ValueIndirectWriteLatchLong3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<long3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>>


@dataclass
class ValueIndirectWriteLatchFloat3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>>


@dataclass
class ValueIndirectWriteLatchDouble3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>>


@dataclass
class ValueIndirectWriteLatchBool4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<bool4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>>


@dataclass
class ValueIndirectWriteLatchByte4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<byte4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>>


@dataclass
class ValueIndirectWriteLatchUshort4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ushort4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>>


@dataclass
class ValueIndirectWriteLatchUint4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<uint4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>>


@dataclass
class ValueIndirectWriteLatchUlong4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<ulong4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>>


@dataclass
class ValueIndirectWriteLatchSbyte4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<sbyte4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>>


@dataclass
class ValueIndirectWriteLatchShort4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<short4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>>


@dataclass
class ValueIndirectWriteLatchInt4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<int4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>>


@dataclass
class ValueIndirectWriteLatchLong4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<long4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>>


@dataclass
class ValueIndirectWriteLatchFloat4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>>


@dataclass
class ValueIndirectWriteLatchDouble4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>>


@dataclass
class ValueIndirectWriteLatchFloat_2x2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float2x2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>>


@dataclass
class ValueIndirectWriteLatchDouble_2x2(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double2x2>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>>


@dataclass
class ValueIndirectWriteLatchFloat_3x3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float3x3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>>


@dataclass
class ValueIndirectWriteLatchDouble_3x3(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double3x3>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>>


@dataclass
class ValueIndirectWriteLatchFloat_4x4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<float4x4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>>


@dataclass
class ValueIndirectWriteLatchDouble_4x4(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<double4x4>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>>


@dataclass
class ValueIndirectWriteLatchFloatQ(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<floatQ>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>>


@dataclass
class ValueIndirectWriteLatchDoubleQ(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<doubleQ>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>>


@dataclass
class ValueIndirectWriteLatchDateTime(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[System.Private.CoreLib]System.DateTime>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>>


@dataclass
class ValueIndirectWriteLatchTimeSpan(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[System.Private.CoreLib]System.TimeSpan>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>>


@dataclass
class ValueIndirectWriteLatchColor(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<color>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>>


@dataclass
class ValueIndirectWriteLatchColorX(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<colorX>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>>


@dataclass
class ValueIndirectWriteLatchShadowCastMode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>>


@dataclass
class ValueIndirectWriteLatchLightType(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.LightType>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>>


@dataclass
class ValueIndirectWriteLatchSessionAccessLevel(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>


@dataclass
class ValueIndirectWriteLatchKey(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.Key>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>>


@dataclass
class ValueIndirectWriteLatchHttpStatusCode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[System.Net.Primitives]System.Net.HttpStatusCode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>>


@dataclass
class ValueIndirectWriteLatchHeadOutputDevice(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>


@dataclass
class ValueIndirectWriteLatchReflectionProbeClear(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>


@dataclass
class ValueIndirectWriteLatchReflectionProbeType(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>


@dataclass
class ValueIndirectWriteLatchReflectionProbeTimeSlicingMode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>


@dataclass
class ValueIndirectWriteLatchCameraClearMode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>>


@dataclass
class ValueIndirectWriteLatchCameraPositioningMode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.CameraPositioningMode>>


@dataclass
class ValueIndirectWriteLatchCameraProjection(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.CameraProjection>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>>


@dataclass
class ValueIndirectWriteLatchZWrite(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.ZWrite>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZWrite>>


@dataclass
class ValueIndirectWriteLatchZTest(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.ZTest>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZTest>>


@dataclass
class ValueIndirectWriteLatchBlend(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.Blend>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Blend>>


@dataclass
class ValueIndirectWriteLatchBlendMode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.BlendMode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.BlendMode>>


@dataclass
class ValueIndirectWriteLatchCulling(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[FrooxEngine]FrooxEngine.Culling>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Culling>>


@dataclass
class ValueIndirectWriteLatchBodyNode(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.BodyNode>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>>


@dataclass
class ValueIndirectWriteLatchChirality(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<[Renderite.Shared]Renderite.Shared.Chirality>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>>


@dataclass
class ValueIndirectWriteLatchDummyEnum(ValueIndirectWriteLatchBase):
    """ValueIndirectWriteLatch<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWriteLatch<DummyEnum>"

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
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>>


# Type alias for any ValueIndirectWriteLatch variant
ValueIndirectWriteLatch = (
    ValueIndirectWriteLatchBool |
    ValueIndirectWriteLatchByte |
    ValueIndirectWriteLatchUshort |
    ValueIndirectWriteLatchUint |
    ValueIndirectWriteLatchUlong |
    ValueIndirectWriteLatchSbyte |
    ValueIndirectWriteLatchShort |
    ValueIndirectWriteLatchInt |
    ValueIndirectWriteLatchLong |
    ValueIndirectWriteLatchFloat |
    ValueIndirectWriteLatchDouble |
    ValueIndirectWriteLatchDecimal |
    ValueIndirectWriteLatchChar |
    ValueIndirectWriteLatchString |
    ValueIndirectWriteLatchUri |
    ValueIndirectWriteLatchBool2 |
    ValueIndirectWriteLatchByte2 |
    ValueIndirectWriteLatchUshort2 |
    ValueIndirectWriteLatchUint2 |
    ValueIndirectWriteLatchUlong2 |
    ValueIndirectWriteLatchSbyte2 |
    ValueIndirectWriteLatchShort2 |
    ValueIndirectWriteLatchInt2 |
    ValueIndirectWriteLatchLong2 |
    ValueIndirectWriteLatchFloat2 |
    ValueIndirectWriteLatchDouble2 |
    ValueIndirectWriteLatchBool3 |
    ValueIndirectWriteLatchByte3 |
    ValueIndirectWriteLatchUshort3 |
    ValueIndirectWriteLatchUint3 |
    ValueIndirectWriteLatchUlong3 |
    ValueIndirectWriteLatchSbyte3 |
    ValueIndirectWriteLatchShort3 |
    ValueIndirectWriteLatchInt3 |
    ValueIndirectWriteLatchLong3 |
    ValueIndirectWriteLatchFloat3 |
    ValueIndirectWriteLatchDouble3 |
    ValueIndirectWriteLatchBool4 |
    ValueIndirectWriteLatchByte4 |
    ValueIndirectWriteLatchUshort4 |
    ValueIndirectWriteLatchUint4 |
    ValueIndirectWriteLatchUlong4 |
    ValueIndirectWriteLatchSbyte4 |
    ValueIndirectWriteLatchShort4 |
    ValueIndirectWriteLatchInt4 |
    ValueIndirectWriteLatchLong4 |
    ValueIndirectWriteLatchFloat4 |
    ValueIndirectWriteLatchDouble4 |
    ValueIndirectWriteLatchFloat_2x2 |
    ValueIndirectWriteLatchDouble_2x2 |
    ValueIndirectWriteLatchFloat_3x3 |
    ValueIndirectWriteLatchDouble_3x3 |
    ValueIndirectWriteLatchFloat_4x4 |
    ValueIndirectWriteLatchDouble_4x4 |
    ValueIndirectWriteLatchFloatQ |
    ValueIndirectWriteLatchDoubleQ |
    ValueIndirectWriteLatchDateTime |
    ValueIndirectWriteLatchTimeSpan |
    ValueIndirectWriteLatchColor |
    ValueIndirectWriteLatchColorX |
    ValueIndirectWriteLatchShadowCastMode |
    ValueIndirectWriteLatchLightType |
    ValueIndirectWriteLatchSessionAccessLevel |
    ValueIndirectWriteLatchKey |
    ValueIndirectWriteLatchHttpStatusCode |
    ValueIndirectWriteLatchHeadOutputDevice |
    ValueIndirectWriteLatchReflectionProbeClear |
    ValueIndirectWriteLatchReflectionProbeType |
    ValueIndirectWriteLatchReflectionProbeTimeSlicingMode |
    ValueIndirectWriteLatchCameraClearMode |
    ValueIndirectWriteLatchCameraPositioningMode |
    ValueIndirectWriteLatchCameraProjection |
    ValueIndirectWriteLatchZWrite |
    ValueIndirectWriteLatchZTest |
    ValueIndirectWriteLatchBlend |
    ValueIndirectWriteLatchBlendMode |
    ValueIndirectWriteLatchCulling |
    ValueIndirectWriteLatchBodyNode |
    ValueIndirectWriteLatchChirality |
    ValueIndirectWriteLatchDummyEnum
)