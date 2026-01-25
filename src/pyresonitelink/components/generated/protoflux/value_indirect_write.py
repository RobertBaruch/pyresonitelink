"""Generated component: ValueIndirectWrite.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueIndirectWriteBase(GeneratedComponent):
    """Base class for ValueIndirectWrite<T> variants."""

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
class ValueIndirectWriteBool(ValueIndirectWriteBase):
    """ValueIndirectWrite<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>>


@dataclass
class ValueIndirectWriteByte(ValueIndirectWriteBase):
    """ValueIndirectWrite<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>>


@dataclass
class ValueIndirectWriteUshort(ValueIndirectWriteBase):
    """ValueIndirectWrite<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>>


@dataclass
class ValueIndirectWriteUint(ValueIndirectWriteBase):
    """ValueIndirectWrite<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>>


@dataclass
class ValueIndirectWriteUlong(ValueIndirectWriteBase):
    """ValueIndirectWrite<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>>


@dataclass
class ValueIndirectWriteSbyte(ValueIndirectWriteBase):
    """ValueIndirectWrite<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>>


@dataclass
class ValueIndirectWriteShort(ValueIndirectWriteBase):
    """ValueIndirectWrite<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>>


@dataclass
class ValueIndirectWriteInt(ValueIndirectWriteBase):
    """ValueIndirectWrite<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>>


@dataclass
class ValueIndirectWriteLong(ValueIndirectWriteBase):
    """ValueIndirectWrite<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>>


@dataclass
class ValueIndirectWriteFloat(ValueIndirectWriteBase):
    """ValueIndirectWrite<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>>


@dataclass
class ValueIndirectWriteDouble(ValueIndirectWriteBase):
    """ValueIndirectWrite<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>>


@dataclass
class ValueIndirectWriteDecimal(ValueIndirectWriteBase):
    """ValueIndirectWrite<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>>


@dataclass
class ValueIndirectWriteChar(ValueIndirectWriteBase):
    """ValueIndirectWrite<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>>


@dataclass
class ValueIndirectWriteString(ValueIndirectWriteBase):
    """ValueIndirectWrite<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>>


@dataclass
class ValueIndirectWriteUri(ValueIndirectWriteBase):
    """ValueIndirectWrite<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>>


@dataclass
class ValueIndirectWriteBool2(ValueIndirectWriteBase):
    """ValueIndirectWrite<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>>


@dataclass
class ValueIndirectWriteByte2(ValueIndirectWriteBase):
    """ValueIndirectWrite<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>>


@dataclass
class ValueIndirectWriteUshort2(ValueIndirectWriteBase):
    """ValueIndirectWrite<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>>


@dataclass
class ValueIndirectWriteUint2(ValueIndirectWriteBase):
    """ValueIndirectWrite<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>>


@dataclass
class ValueIndirectWriteUlong2(ValueIndirectWriteBase):
    """ValueIndirectWrite<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>>


@dataclass
class ValueIndirectWriteSbyte2(ValueIndirectWriteBase):
    """ValueIndirectWrite<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>>


@dataclass
class ValueIndirectWriteShort2(ValueIndirectWriteBase):
    """ValueIndirectWrite<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>>


@dataclass
class ValueIndirectWriteInt2(ValueIndirectWriteBase):
    """ValueIndirectWrite<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>>


@dataclass
class ValueIndirectWriteLong2(ValueIndirectWriteBase):
    """ValueIndirectWrite<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>>


@dataclass
class ValueIndirectWriteFloat2(ValueIndirectWriteBase):
    """ValueIndirectWrite<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>>


@dataclass
class ValueIndirectWriteDouble2(ValueIndirectWriteBase):
    """ValueIndirectWrite<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>>


@dataclass
class ValueIndirectWriteBool3(ValueIndirectWriteBase):
    """ValueIndirectWrite<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>>


@dataclass
class ValueIndirectWriteByte3(ValueIndirectWriteBase):
    """ValueIndirectWrite<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>>


@dataclass
class ValueIndirectWriteUshort3(ValueIndirectWriteBase):
    """ValueIndirectWrite<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>>


@dataclass
class ValueIndirectWriteUint3(ValueIndirectWriteBase):
    """ValueIndirectWrite<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>>


@dataclass
class ValueIndirectWriteUlong3(ValueIndirectWriteBase):
    """ValueIndirectWrite<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>>


@dataclass
class ValueIndirectWriteSbyte3(ValueIndirectWriteBase):
    """ValueIndirectWrite<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>>


@dataclass
class ValueIndirectWriteShort3(ValueIndirectWriteBase):
    """ValueIndirectWrite<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>>


@dataclass
class ValueIndirectWriteInt3(ValueIndirectWriteBase):
    """ValueIndirectWrite<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>>


@dataclass
class ValueIndirectWriteLong3(ValueIndirectWriteBase):
    """ValueIndirectWrite<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>>


@dataclass
class ValueIndirectWriteFloat3(ValueIndirectWriteBase):
    """ValueIndirectWrite<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>>


@dataclass
class ValueIndirectWriteDouble3(ValueIndirectWriteBase):
    """ValueIndirectWrite<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>>


@dataclass
class ValueIndirectWriteBool4(ValueIndirectWriteBase):
    """ValueIndirectWrite<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>>


@dataclass
class ValueIndirectWriteByte4(ValueIndirectWriteBase):
    """ValueIndirectWrite<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>>


@dataclass
class ValueIndirectWriteUshort4(ValueIndirectWriteBase):
    """ValueIndirectWrite<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>>


@dataclass
class ValueIndirectWriteUint4(ValueIndirectWriteBase):
    """ValueIndirectWrite<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>>


@dataclass
class ValueIndirectWriteUlong4(ValueIndirectWriteBase):
    """ValueIndirectWrite<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>>


@dataclass
class ValueIndirectWriteSbyte4(ValueIndirectWriteBase):
    """ValueIndirectWrite<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>>


@dataclass
class ValueIndirectWriteShort4(ValueIndirectWriteBase):
    """ValueIndirectWrite<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>>


@dataclass
class ValueIndirectWriteInt4(ValueIndirectWriteBase):
    """ValueIndirectWrite<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>>


@dataclass
class ValueIndirectWriteLong4(ValueIndirectWriteBase):
    """ValueIndirectWrite<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>>


@dataclass
class ValueIndirectWriteFloat4(ValueIndirectWriteBase):
    """ValueIndirectWrite<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>>


@dataclass
class ValueIndirectWriteDouble4(ValueIndirectWriteBase):
    """ValueIndirectWrite<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>>


@dataclass
class ValueIndirectWriteFloat_2x2(ValueIndirectWriteBase):
    """ValueIndirectWrite<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>>


@dataclass
class ValueIndirectWriteDouble_2x2(ValueIndirectWriteBase):
    """ValueIndirectWrite<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>>


@dataclass
class ValueIndirectWriteFloat_3x3(ValueIndirectWriteBase):
    """ValueIndirectWrite<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>>


@dataclass
class ValueIndirectWriteDouble_3x3(ValueIndirectWriteBase):
    """ValueIndirectWrite<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>>


@dataclass
class ValueIndirectWriteFloat_4x4(ValueIndirectWriteBase):
    """ValueIndirectWrite<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>>


@dataclass
class ValueIndirectWriteDouble_4x4(ValueIndirectWriteBase):
    """ValueIndirectWrite<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>>


@dataclass
class ValueIndirectWriteFloatQ(ValueIndirectWriteBase):
    """ValueIndirectWrite<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>>


@dataclass
class ValueIndirectWriteDoubleQ(ValueIndirectWriteBase):
    """ValueIndirectWrite<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>>


@dataclass
class ValueIndirectWriteDateTime(ValueIndirectWriteBase):
    """ValueIndirectWrite<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>>


@dataclass
class ValueIndirectWriteTimeSpan(ValueIndirectWriteBase):
    """ValueIndirectWrite<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>>


@dataclass
class ValueIndirectWriteColor(ValueIndirectWriteBase):
    """ValueIndirectWrite<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>>


@dataclass
class ValueIndirectWriteColorX(ValueIndirectWriteBase):
    """ValueIndirectWrite<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>>


@dataclass
class ValueIndirectWriteShadowCastMode(ValueIndirectWriteBase):
    """ValueIndirectWrite<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>>


@dataclass
class ValueIndirectWriteLightType(ValueIndirectWriteBase):
    """ValueIndirectWrite<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>>


@dataclass
class ValueIndirectWriteSessionAccessLevel(ValueIndirectWriteBase):
    """ValueIndirectWrite<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>


@dataclass
class ValueIndirectWriteKey(ValueIndirectWriteBase):
    """ValueIndirectWrite<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>>


@dataclass
class ValueIndirectWriteHttpStatusCode(ValueIndirectWriteBase):
    """ValueIndirectWrite<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>>


@dataclass
class ValueIndirectWriteHeadOutputDevice(ValueIndirectWriteBase):
    """ValueIndirectWrite<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>


@dataclass
class ValueIndirectWriteReflectionProbeClear(ValueIndirectWriteBase):
    """ValueIndirectWrite<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>


@dataclass
class ValueIndirectWriteReflectionProbeType(ValueIndirectWriteBase):
    """ValueIndirectWrite<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>


@dataclass
class ValueIndirectWriteReflectionProbeTimeSlicingMode(ValueIndirectWriteBase):
    """ValueIndirectWrite<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>


@dataclass
class ValueIndirectWriteCameraClearMode(ValueIndirectWriteBase):
    """ValueIndirectWrite<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>>


@dataclass
class ValueIndirectWriteCameraPositioningMode(ValueIndirectWriteBase):
    """ValueIndirectWrite<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.CameraPositioningMode>>


@dataclass
class ValueIndirectWriteCameraProjection(ValueIndirectWriteBase):
    """ValueIndirectWrite<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>>


@dataclass
class ValueIndirectWriteZWrite(ValueIndirectWriteBase):
    """ValueIndirectWrite<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZWrite>>


@dataclass
class ValueIndirectWriteZTest(ValueIndirectWriteBase):
    """ValueIndirectWrite<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.ZTest>>


@dataclass
class ValueIndirectWriteBlend(ValueIndirectWriteBase):
    """ValueIndirectWrite<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Blend>>


@dataclass
class ValueIndirectWriteBlendMode(ValueIndirectWriteBase):
    """ValueIndirectWrite<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.BlendMode>>


@dataclass
class ValueIndirectWriteCulling(ValueIndirectWriteBase):
    """ValueIndirectWrite<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,FrooxEngine.Culling>>


@dataclass
class ValueIndirectWriteBodyNode(ValueIndirectWriteBase):
    """ValueIndirectWrite<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>>


@dataclass
class ValueIndirectWriteChirality(ValueIndirectWriteBase):
    """ValueIndirectWrite<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>>


@dataclass
class ValueIndirectWriteDummyEnum(ValueIndirectWriteBase):
    """ValueIndirectWrite<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueIndirectWrite<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    variable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>>


# Type alias for any ValueIndirectWrite variant
ValueIndirectWrite = (
    ValueIndirectWriteBool |
    ValueIndirectWriteByte |
    ValueIndirectWriteUshort |
    ValueIndirectWriteUint |
    ValueIndirectWriteUlong |
    ValueIndirectWriteSbyte |
    ValueIndirectWriteShort |
    ValueIndirectWriteInt |
    ValueIndirectWriteLong |
    ValueIndirectWriteFloat |
    ValueIndirectWriteDouble |
    ValueIndirectWriteDecimal |
    ValueIndirectWriteChar |
    ValueIndirectWriteString |
    ValueIndirectWriteUri |
    ValueIndirectWriteBool2 |
    ValueIndirectWriteByte2 |
    ValueIndirectWriteUshort2 |
    ValueIndirectWriteUint2 |
    ValueIndirectWriteUlong2 |
    ValueIndirectWriteSbyte2 |
    ValueIndirectWriteShort2 |
    ValueIndirectWriteInt2 |
    ValueIndirectWriteLong2 |
    ValueIndirectWriteFloat2 |
    ValueIndirectWriteDouble2 |
    ValueIndirectWriteBool3 |
    ValueIndirectWriteByte3 |
    ValueIndirectWriteUshort3 |
    ValueIndirectWriteUint3 |
    ValueIndirectWriteUlong3 |
    ValueIndirectWriteSbyte3 |
    ValueIndirectWriteShort3 |
    ValueIndirectWriteInt3 |
    ValueIndirectWriteLong3 |
    ValueIndirectWriteFloat3 |
    ValueIndirectWriteDouble3 |
    ValueIndirectWriteBool4 |
    ValueIndirectWriteByte4 |
    ValueIndirectWriteUshort4 |
    ValueIndirectWriteUint4 |
    ValueIndirectWriteUlong4 |
    ValueIndirectWriteSbyte4 |
    ValueIndirectWriteShort4 |
    ValueIndirectWriteInt4 |
    ValueIndirectWriteLong4 |
    ValueIndirectWriteFloat4 |
    ValueIndirectWriteDouble4 |
    ValueIndirectWriteFloat_2x2 |
    ValueIndirectWriteDouble_2x2 |
    ValueIndirectWriteFloat_3x3 |
    ValueIndirectWriteDouble_3x3 |
    ValueIndirectWriteFloat_4x4 |
    ValueIndirectWriteDouble_4x4 |
    ValueIndirectWriteFloatQ |
    ValueIndirectWriteDoubleQ |
    ValueIndirectWriteDateTime |
    ValueIndirectWriteTimeSpan |
    ValueIndirectWriteColor |
    ValueIndirectWriteColorX |
    ValueIndirectWriteShadowCastMode |
    ValueIndirectWriteLightType |
    ValueIndirectWriteSessionAccessLevel |
    ValueIndirectWriteKey |
    ValueIndirectWriteHttpStatusCode |
    ValueIndirectWriteHeadOutputDevice |
    ValueIndirectWriteReflectionProbeClear |
    ValueIndirectWriteReflectionProbeType |
    ValueIndirectWriteReflectionProbeTimeSlicingMode |
    ValueIndirectWriteCameraClearMode |
    ValueIndirectWriteCameraPositioningMode |
    ValueIndirectWriteCameraProjection |
    ValueIndirectWriteZWrite |
    ValueIndirectWriteZTest |
    ValueIndirectWriteBlend |
    ValueIndirectWriteBlendMode |
    ValueIndirectWriteCulling |
    ValueIndirectWriteBodyNode |
    ValueIndirectWriteChirality |
    ValueIndirectWriteDummyEnum
)