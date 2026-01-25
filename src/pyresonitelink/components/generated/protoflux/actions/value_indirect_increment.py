"""Generated component: ValueIndirectIncrement.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueIndirectIncrementBase(GeneratedComponent):
    """Base class for ValueIndirectIncrement<T> variants."""

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
class ValueIndirectIncrementBool(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>>


@dataclass
class ValueIndirectIncrementByte(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>>


@dataclass
class ValueIndirectIncrementUshort(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>>


@dataclass
class ValueIndirectIncrementUint(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>>


@dataclass
class ValueIndirectIncrementUlong(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>>


@dataclass
class ValueIndirectIncrementSbyte(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>>


@dataclass
class ValueIndirectIncrementShort(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>>


@dataclass
class ValueIndirectIncrementInt(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>>


@dataclass
class ValueIndirectIncrementLong(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>>


@dataclass
class ValueIndirectIncrementFloat(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>>


@dataclass
class ValueIndirectIncrementDouble(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>>


@dataclass
class ValueIndirectIncrementDecimal(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>>


@dataclass
class ValueIndirectIncrementChar(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>>


@dataclass
class ValueIndirectIncrementString(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>>


@dataclass
class ValueIndirectIncrementUri(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>>


@dataclass
class ValueIndirectIncrementBool2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>>


@dataclass
class ValueIndirectIncrementByte2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>>


@dataclass
class ValueIndirectIncrementUshort2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>>


@dataclass
class ValueIndirectIncrementUint2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>>


@dataclass
class ValueIndirectIncrementUlong2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>>


@dataclass
class ValueIndirectIncrementSbyte2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>>


@dataclass
class ValueIndirectIncrementShort2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>>


@dataclass
class ValueIndirectIncrementInt2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>>


@dataclass
class ValueIndirectIncrementLong2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>>


@dataclass
class ValueIndirectIncrementFloat2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>>


@dataclass
class ValueIndirectIncrementDouble2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>>


@dataclass
class ValueIndirectIncrementBool3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>>


@dataclass
class ValueIndirectIncrementByte3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>>


@dataclass
class ValueIndirectIncrementUshort3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>>


@dataclass
class ValueIndirectIncrementUint3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>>


@dataclass
class ValueIndirectIncrementUlong3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>>


@dataclass
class ValueIndirectIncrementSbyte3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>>


@dataclass
class ValueIndirectIncrementShort3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>>


@dataclass
class ValueIndirectIncrementInt3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>>


@dataclass
class ValueIndirectIncrementLong3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>>


@dataclass
class ValueIndirectIncrementFloat3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>>


@dataclass
class ValueIndirectIncrementDouble3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>>


@dataclass
class ValueIndirectIncrementBool4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>>


@dataclass
class ValueIndirectIncrementByte4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>>


@dataclass
class ValueIndirectIncrementUshort4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>>


@dataclass
class ValueIndirectIncrementUint4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>>


@dataclass
class ValueIndirectIncrementUlong4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>>


@dataclass
class ValueIndirectIncrementSbyte4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>>


@dataclass
class ValueIndirectIncrementShort4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>>


@dataclass
class ValueIndirectIncrementInt4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>>


@dataclass
class ValueIndirectIncrementLong4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>>


@dataclass
class ValueIndirectIncrementFloat4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>>


@dataclass
class ValueIndirectIncrementDouble4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>>


@dataclass
class ValueIndirectIncrementFloat_2x2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>>


@dataclass
class ValueIndirectIncrementDouble_2x2(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>>


@dataclass
class ValueIndirectIncrementFloat_3x3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>>


@dataclass
class ValueIndirectIncrementDouble_3x3(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>>


@dataclass
class ValueIndirectIncrementFloat_4x4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>>


@dataclass
class ValueIndirectIncrementDouble_4x4(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>>


@dataclass
class ValueIndirectIncrementFloatQ(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>>


@dataclass
class ValueIndirectIncrementDoubleQ(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>>


@dataclass
class ValueIndirectIncrementDateTime(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>>


@dataclass
class ValueIndirectIncrementTimeSpan(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>>


@dataclass
class ValueIndirectIncrementColor(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>>


@dataclass
class ValueIndirectIncrementColorX(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>>


@dataclass
class ValueIndirectIncrementShadowCastMode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>>


@dataclass
class ValueIndirectIncrementLightType(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>>


@dataclass
class ValueIndirectIncrementSessionAccessLevel(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>


@dataclass
class ValueIndirectIncrementKey(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>>


@dataclass
class ValueIndirectIncrementHttpStatusCode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>>


@dataclass
class ValueIndirectIncrementHeadOutputDevice(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>


@dataclass
class ValueIndirectIncrementReflectionProbeClear(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>


@dataclass
class ValueIndirectIncrementReflectionProbeType(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>


@dataclass
class ValueIndirectIncrementReflectionProbeTimeSlicingMode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>


@dataclass
class ValueIndirectIncrementCameraClearMode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>>


@dataclass
class ValueIndirectIncrementCameraPositioningMode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.CameraPositioningMode>>


@dataclass
class ValueIndirectIncrementCameraProjection(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>>


@dataclass
class ValueIndirectIncrementZWrite(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZWrite>>


@dataclass
class ValueIndirectIncrementZTest(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZTest>>


@dataclass
class ValueIndirectIncrementBlend(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Blend>>


@dataclass
class ValueIndirectIncrementBlendMode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.BlendMode>>


@dataclass
class ValueIndirectIncrementCulling(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Culling>>


@dataclass
class ValueIndirectIncrementBodyNode(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>>


@dataclass
class ValueIndirectIncrementChirality(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>>


@dataclass
class ValueIndirectIncrementDummyEnum(ValueIndirectIncrementBase):
    """ValueIndirectIncrement<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.ValueIndirectIncrement<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>>


# Type alias for any ValueIndirectIncrement variant
ValueIndirectIncrement = (
    ValueIndirectIncrementBool |
    ValueIndirectIncrementByte |
    ValueIndirectIncrementUshort |
    ValueIndirectIncrementUint |
    ValueIndirectIncrementUlong |
    ValueIndirectIncrementSbyte |
    ValueIndirectIncrementShort |
    ValueIndirectIncrementInt |
    ValueIndirectIncrementLong |
    ValueIndirectIncrementFloat |
    ValueIndirectIncrementDouble |
    ValueIndirectIncrementDecimal |
    ValueIndirectIncrementChar |
    ValueIndirectIncrementString |
    ValueIndirectIncrementUri |
    ValueIndirectIncrementBool2 |
    ValueIndirectIncrementByte2 |
    ValueIndirectIncrementUshort2 |
    ValueIndirectIncrementUint2 |
    ValueIndirectIncrementUlong2 |
    ValueIndirectIncrementSbyte2 |
    ValueIndirectIncrementShort2 |
    ValueIndirectIncrementInt2 |
    ValueIndirectIncrementLong2 |
    ValueIndirectIncrementFloat2 |
    ValueIndirectIncrementDouble2 |
    ValueIndirectIncrementBool3 |
    ValueIndirectIncrementByte3 |
    ValueIndirectIncrementUshort3 |
    ValueIndirectIncrementUint3 |
    ValueIndirectIncrementUlong3 |
    ValueIndirectIncrementSbyte3 |
    ValueIndirectIncrementShort3 |
    ValueIndirectIncrementInt3 |
    ValueIndirectIncrementLong3 |
    ValueIndirectIncrementFloat3 |
    ValueIndirectIncrementDouble3 |
    ValueIndirectIncrementBool4 |
    ValueIndirectIncrementByte4 |
    ValueIndirectIncrementUshort4 |
    ValueIndirectIncrementUint4 |
    ValueIndirectIncrementUlong4 |
    ValueIndirectIncrementSbyte4 |
    ValueIndirectIncrementShort4 |
    ValueIndirectIncrementInt4 |
    ValueIndirectIncrementLong4 |
    ValueIndirectIncrementFloat4 |
    ValueIndirectIncrementDouble4 |
    ValueIndirectIncrementFloat_2x2 |
    ValueIndirectIncrementDouble_2x2 |
    ValueIndirectIncrementFloat_3x3 |
    ValueIndirectIncrementDouble_3x3 |
    ValueIndirectIncrementFloat_4x4 |
    ValueIndirectIncrementDouble_4x4 |
    ValueIndirectIncrementFloatQ |
    ValueIndirectIncrementDoubleQ |
    ValueIndirectIncrementDateTime |
    ValueIndirectIncrementTimeSpan |
    ValueIndirectIncrementColor |
    ValueIndirectIncrementColorX |
    ValueIndirectIncrementShadowCastMode |
    ValueIndirectIncrementLightType |
    ValueIndirectIncrementSessionAccessLevel |
    ValueIndirectIncrementKey |
    ValueIndirectIncrementHttpStatusCode |
    ValueIndirectIncrementHeadOutputDevice |
    ValueIndirectIncrementReflectionProbeClear |
    ValueIndirectIncrementReflectionProbeType |
    ValueIndirectIncrementReflectionProbeTimeSlicingMode |
    ValueIndirectIncrementCameraClearMode |
    ValueIndirectIncrementCameraPositioningMode |
    ValueIndirectIncrementCameraProjection |
    ValueIndirectIncrementZWrite |
    ValueIndirectIncrementZTest |
    ValueIndirectIncrementBlend |
    ValueIndirectIncrementBlendMode |
    ValueIndirectIncrementCulling |
    ValueIndirectIncrementBodyNode |
    ValueIndirectIncrementChirality |
    ValueIndirectIncrementDummyEnum
)