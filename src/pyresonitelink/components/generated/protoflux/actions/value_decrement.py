"""Generated component: ValueDecrement.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueDecrementBase(GeneratedComponent):
    """Base class for ValueDecrement<T> variants."""

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
class ValueDecrementBool(ValueDecrementBase):
    """ValueDecrement<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>


@dataclass
class ValueDecrementByte(ValueDecrementBase):
    """ValueDecrement<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>


@dataclass
class ValueDecrementUshort(ValueDecrementBase):
    """ValueDecrement<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>


@dataclass
class ValueDecrementUint(ValueDecrementBase):
    """ValueDecrement<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>


@dataclass
class ValueDecrementUlong(ValueDecrementBase):
    """ValueDecrement<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>


@dataclass
class ValueDecrementSbyte(ValueDecrementBase):
    """ValueDecrement<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>


@dataclass
class ValueDecrementShort(ValueDecrementBase):
    """ValueDecrement<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>


@dataclass
class ValueDecrementInt(ValueDecrementBase):
    """ValueDecrement<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>


@dataclass
class ValueDecrementLong(ValueDecrementBase):
    """ValueDecrement<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>


@dataclass
class ValueDecrementFloat(ValueDecrementBase):
    """ValueDecrement<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>


@dataclass
class ValueDecrementDouble(ValueDecrementBase):
    """ValueDecrement<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>


@dataclass
class ValueDecrementDecimal(ValueDecrementBase):
    """ValueDecrement<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>


@dataclass
class ValueDecrementChar(ValueDecrementBase):
    """ValueDecrement<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>


@dataclass
class ValueDecrementString(ValueDecrementBase):
    """ValueDecrement<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>


@dataclass
class ValueDecrementUri(ValueDecrementBase):
    """ValueDecrement<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>


@dataclass
class ValueDecrementBool2(ValueDecrementBase):
    """ValueDecrement<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>


@dataclass
class ValueDecrementByte2(ValueDecrementBase):
    """ValueDecrement<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>


@dataclass
class ValueDecrementUshort2(ValueDecrementBase):
    """ValueDecrement<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>


@dataclass
class ValueDecrementUint2(ValueDecrementBase):
    """ValueDecrement<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>


@dataclass
class ValueDecrementUlong2(ValueDecrementBase):
    """ValueDecrement<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>


@dataclass
class ValueDecrementSbyte2(ValueDecrementBase):
    """ValueDecrement<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>


@dataclass
class ValueDecrementShort2(ValueDecrementBase):
    """ValueDecrement<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>


@dataclass
class ValueDecrementInt2(ValueDecrementBase):
    """ValueDecrement<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>


@dataclass
class ValueDecrementLong2(ValueDecrementBase):
    """ValueDecrement<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>


@dataclass
class ValueDecrementFloat2(ValueDecrementBase):
    """ValueDecrement<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>


@dataclass
class ValueDecrementDouble2(ValueDecrementBase):
    """ValueDecrement<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>


@dataclass
class ValueDecrementBool3(ValueDecrementBase):
    """ValueDecrement<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>


@dataclass
class ValueDecrementByte3(ValueDecrementBase):
    """ValueDecrement<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>


@dataclass
class ValueDecrementUshort3(ValueDecrementBase):
    """ValueDecrement<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>


@dataclass
class ValueDecrementUint3(ValueDecrementBase):
    """ValueDecrement<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>


@dataclass
class ValueDecrementUlong3(ValueDecrementBase):
    """ValueDecrement<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>


@dataclass
class ValueDecrementSbyte3(ValueDecrementBase):
    """ValueDecrement<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>


@dataclass
class ValueDecrementShort3(ValueDecrementBase):
    """ValueDecrement<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>


@dataclass
class ValueDecrementInt3(ValueDecrementBase):
    """ValueDecrement<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>


@dataclass
class ValueDecrementLong3(ValueDecrementBase):
    """ValueDecrement<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>


@dataclass
class ValueDecrementFloat3(ValueDecrementBase):
    """ValueDecrement<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>


@dataclass
class ValueDecrementDouble3(ValueDecrementBase):
    """ValueDecrement<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>


@dataclass
class ValueDecrementBool4(ValueDecrementBase):
    """ValueDecrement<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>


@dataclass
class ValueDecrementByte4(ValueDecrementBase):
    """ValueDecrement<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>


@dataclass
class ValueDecrementUshort4(ValueDecrementBase):
    """ValueDecrement<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>


@dataclass
class ValueDecrementUint4(ValueDecrementBase):
    """ValueDecrement<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>


@dataclass
class ValueDecrementUlong4(ValueDecrementBase):
    """ValueDecrement<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>


@dataclass
class ValueDecrementSbyte4(ValueDecrementBase):
    """ValueDecrement<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>


@dataclass
class ValueDecrementShort4(ValueDecrementBase):
    """ValueDecrement<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>


@dataclass
class ValueDecrementInt4(ValueDecrementBase):
    """ValueDecrement<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>


@dataclass
class ValueDecrementLong4(ValueDecrementBase):
    """ValueDecrement<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>


@dataclass
class ValueDecrementFloat4(ValueDecrementBase):
    """ValueDecrement<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>


@dataclass
class ValueDecrementDouble4(ValueDecrementBase):
    """ValueDecrement<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>


@dataclass
class ValueDecrementFloat_2x2(ValueDecrementBase):
    """ValueDecrement<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>


@dataclass
class ValueDecrementDouble_2x2(ValueDecrementBase):
    """ValueDecrement<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>


@dataclass
class ValueDecrementFloat_3x3(ValueDecrementBase):
    """ValueDecrement<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>


@dataclass
class ValueDecrementDouble_3x3(ValueDecrementBase):
    """ValueDecrement<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>


@dataclass
class ValueDecrementFloat_4x4(ValueDecrementBase):
    """ValueDecrement<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>


@dataclass
class ValueDecrementDouble_4x4(ValueDecrementBase):
    """ValueDecrement<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>


@dataclass
class ValueDecrementFloatQ(ValueDecrementBase):
    """ValueDecrement<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>


@dataclass
class ValueDecrementDoubleQ(ValueDecrementBase):
    """ValueDecrement<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>


@dataclass
class ValueDecrementDateTime(ValueDecrementBase):
    """ValueDecrement<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueDecrementTimeSpan(ValueDecrementBase):
    """ValueDecrement<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueDecrementColor(ValueDecrementBase):
    """ValueDecrement<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>


@dataclass
class ValueDecrementColorX(ValueDecrementBase):
    """ValueDecrement<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>


@dataclass
class ValueDecrementShadowCastMode(ValueDecrementBase):
    """ValueDecrement<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueDecrementLightType(ValueDecrementBase):
    """ValueDecrement<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueDecrementSessionAccessLevel(ValueDecrementBase):
    """ValueDecrement<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueDecrementKey(ValueDecrementBase):
    """ValueDecrement<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueDecrementHttpStatusCode(ValueDecrementBase):
    """ValueDecrement<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueDecrementHeadOutputDevice(ValueDecrementBase):
    """ValueDecrement<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueDecrementReflectionProbeClear(ValueDecrementBase):
    """ValueDecrement<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueDecrementReflectionProbeType(ValueDecrementBase):
    """ValueDecrement<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueDecrementReflectionProbeTimeSlicingMode(ValueDecrementBase):
    """ValueDecrement<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueDecrementCameraClearMode(ValueDecrementBase):
    """ValueDecrement<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueDecrementCameraPositioningMode(ValueDecrementBase):
    """ValueDecrement<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.CameraPositioningMode>


@dataclass
class ValueDecrementCameraProjection(ValueDecrementBase):
    """ValueDecrement<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueDecrementZWrite(ValueDecrementBase):
    """ValueDecrement<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZWrite>


@dataclass
class ValueDecrementZTest(ValueDecrementBase):
    """ValueDecrement<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZTest>


@dataclass
class ValueDecrementBlend(ValueDecrementBase):
    """ValueDecrement<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Blend>


@dataclass
class ValueDecrementBlendMode(ValueDecrementBase):
    """ValueDecrement<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.BlendMode>


@dataclass
class ValueDecrementCulling(ValueDecrementBase):
    """ValueDecrement<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Culling>


@dataclass
class ValueDecrementBodyNode(ValueDecrementBase):
    """ValueDecrement<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueDecrementChirality(ValueDecrementBase):
    """ValueDecrement<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueDecrementDummyEnum(ValueDecrementBase):
    """ValueDecrement<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueDecrement<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>


# Type alias for any ValueDecrement variant
ValueDecrement = (
    ValueDecrementBool |
    ValueDecrementByte |
    ValueDecrementUshort |
    ValueDecrementUint |
    ValueDecrementUlong |
    ValueDecrementSbyte |
    ValueDecrementShort |
    ValueDecrementInt |
    ValueDecrementLong |
    ValueDecrementFloat |
    ValueDecrementDouble |
    ValueDecrementDecimal |
    ValueDecrementChar |
    ValueDecrementString |
    ValueDecrementUri |
    ValueDecrementBool2 |
    ValueDecrementByte2 |
    ValueDecrementUshort2 |
    ValueDecrementUint2 |
    ValueDecrementUlong2 |
    ValueDecrementSbyte2 |
    ValueDecrementShort2 |
    ValueDecrementInt2 |
    ValueDecrementLong2 |
    ValueDecrementFloat2 |
    ValueDecrementDouble2 |
    ValueDecrementBool3 |
    ValueDecrementByte3 |
    ValueDecrementUshort3 |
    ValueDecrementUint3 |
    ValueDecrementUlong3 |
    ValueDecrementSbyte3 |
    ValueDecrementShort3 |
    ValueDecrementInt3 |
    ValueDecrementLong3 |
    ValueDecrementFloat3 |
    ValueDecrementDouble3 |
    ValueDecrementBool4 |
    ValueDecrementByte4 |
    ValueDecrementUshort4 |
    ValueDecrementUint4 |
    ValueDecrementUlong4 |
    ValueDecrementSbyte4 |
    ValueDecrementShort4 |
    ValueDecrementInt4 |
    ValueDecrementLong4 |
    ValueDecrementFloat4 |
    ValueDecrementDouble4 |
    ValueDecrementFloat_2x2 |
    ValueDecrementDouble_2x2 |
    ValueDecrementFloat_3x3 |
    ValueDecrementDouble_3x3 |
    ValueDecrementFloat_4x4 |
    ValueDecrementDouble_4x4 |
    ValueDecrementFloatQ |
    ValueDecrementDoubleQ |
    ValueDecrementDateTime |
    ValueDecrementTimeSpan |
    ValueDecrementColor |
    ValueDecrementColorX |
    ValueDecrementShadowCastMode |
    ValueDecrementLightType |
    ValueDecrementSessionAccessLevel |
    ValueDecrementKey |
    ValueDecrementHttpStatusCode |
    ValueDecrementHeadOutputDevice |
    ValueDecrementReflectionProbeClear |
    ValueDecrementReflectionProbeType |
    ValueDecrementReflectionProbeTimeSlicingMode |
    ValueDecrementCameraClearMode |
    ValueDecrementCameraPositioningMode |
    ValueDecrementCameraProjection |
    ValueDecrementZWrite |
    ValueDecrementZTest |
    ValueDecrementBlend |
    ValueDecrementBlendMode |
    ValueDecrementCulling |
    ValueDecrementBodyNode |
    ValueDecrementChirality |
    ValueDecrementDummyEnum
)