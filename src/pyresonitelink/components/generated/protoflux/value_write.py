"""Generated component: ValueWrite.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueWriteBase(GeneratedComponent):
    """Base class for ValueWrite<T> variants."""

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
class ValueWriteBool(ValueWriteBase):
    """ValueWrite<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool>


@dataclass
class ValueWriteByte(ValueWriteBase):
    """ValueWrite<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte>


@dataclass
class ValueWriteUshort(ValueWriteBase):
    """ValueWrite<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort>


@dataclass
class ValueWriteUint(ValueWriteBase):
    """ValueWrite<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint>


@dataclass
class ValueWriteUlong(ValueWriteBase):
    """ValueWrite<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong>


@dataclass
class ValueWriteSbyte(ValueWriteBase):
    """ValueWrite<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte>


@dataclass
class ValueWriteShort(ValueWriteBase):
    """ValueWrite<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short>


@dataclass
class ValueWriteInt(ValueWriteBase):
    """ValueWrite<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int>


@dataclass
class ValueWriteLong(ValueWriteBase):
    """ValueWrite<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long>


@dataclass
class ValueWriteFloat(ValueWriteBase):
    """ValueWrite<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float>


@dataclass
class ValueWriteDouble(ValueWriteBase):
    """ValueWrite<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double>


@dataclass
class ValueWriteDecimal(ValueWriteBase):
    """ValueWrite<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,decimal>


@dataclass
class ValueWriteChar(ValueWriteBase):
    """ValueWrite<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,char>


@dataclass
class ValueWriteString(ValueWriteBase):
    """ValueWrite<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,string>


@dataclass
class ValueWriteUri(ValueWriteBase):
    """ValueWrite<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,Uri>


@dataclass
class ValueWriteBool2(ValueWriteBase):
    """ValueWrite<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool2>


@dataclass
class ValueWriteByte2(ValueWriteBase):
    """ValueWrite<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte2>


@dataclass
class ValueWriteUshort2(ValueWriteBase):
    """ValueWrite<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort2>


@dataclass
class ValueWriteUint2(ValueWriteBase):
    """ValueWrite<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint2>


@dataclass
class ValueWriteUlong2(ValueWriteBase):
    """ValueWrite<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong2>


@dataclass
class ValueWriteSbyte2(ValueWriteBase):
    """ValueWrite<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte2>


@dataclass
class ValueWriteShort2(ValueWriteBase):
    """ValueWrite<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short2>


@dataclass
class ValueWriteInt2(ValueWriteBase):
    """ValueWrite<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int2>


@dataclass
class ValueWriteLong2(ValueWriteBase):
    """ValueWrite<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long2>


@dataclass
class ValueWriteFloat2(ValueWriteBase):
    """ValueWrite<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2>


@dataclass
class ValueWriteDouble2(ValueWriteBase):
    """ValueWrite<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2>


@dataclass
class ValueWriteBool3(ValueWriteBase):
    """ValueWrite<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool3>


@dataclass
class ValueWriteByte3(ValueWriteBase):
    """ValueWrite<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte3>


@dataclass
class ValueWriteUshort3(ValueWriteBase):
    """ValueWrite<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort3>


@dataclass
class ValueWriteUint3(ValueWriteBase):
    """ValueWrite<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint3>


@dataclass
class ValueWriteUlong3(ValueWriteBase):
    """ValueWrite<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong3>


@dataclass
class ValueWriteSbyte3(ValueWriteBase):
    """ValueWrite<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte3>


@dataclass
class ValueWriteShort3(ValueWriteBase):
    """ValueWrite<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short3>


@dataclass
class ValueWriteInt3(ValueWriteBase):
    """ValueWrite<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int3>


@dataclass
class ValueWriteLong3(ValueWriteBase):
    """ValueWrite<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long3>


@dataclass
class ValueWriteFloat3(ValueWriteBase):
    """ValueWrite<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3>


@dataclass
class ValueWriteDouble3(ValueWriteBase):
    """ValueWrite<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3>


@dataclass
class ValueWriteBool4(ValueWriteBase):
    """ValueWrite<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,bool4>


@dataclass
class ValueWriteByte4(ValueWriteBase):
    """ValueWrite<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,byte4>


@dataclass
class ValueWriteUshort4(ValueWriteBase):
    """ValueWrite<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ushort4>


@dataclass
class ValueWriteUint4(ValueWriteBase):
    """ValueWrite<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,uint4>


@dataclass
class ValueWriteUlong4(ValueWriteBase):
    """ValueWrite<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,ulong4>


@dataclass
class ValueWriteSbyte4(ValueWriteBase):
    """ValueWrite<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,sbyte4>


@dataclass
class ValueWriteShort4(ValueWriteBase):
    """ValueWrite<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,short4>


@dataclass
class ValueWriteInt4(ValueWriteBase):
    """ValueWrite<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,int4>


@dataclass
class ValueWriteLong4(ValueWriteBase):
    """ValueWrite<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,long4>


@dataclass
class ValueWriteFloat4(ValueWriteBase):
    """ValueWrite<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4>


@dataclass
class ValueWriteDouble4(ValueWriteBase):
    """ValueWrite<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4>


@dataclass
class ValueWriteFloat_2x2(ValueWriteBase):
    """ValueWrite<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float2x2>


@dataclass
class ValueWriteDouble_2x2(ValueWriteBase):
    """ValueWrite<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double2x2>


@dataclass
class ValueWriteFloat_3x3(ValueWriteBase):
    """ValueWrite<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float3x3>


@dataclass
class ValueWriteDouble_3x3(ValueWriteBase):
    """ValueWrite<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double3x3>


@dataclass
class ValueWriteFloat_4x4(ValueWriteBase):
    """ValueWrite<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,float4x4>


@dataclass
class ValueWriteDouble_4x4(ValueWriteBase):
    """ValueWrite<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,double4x4>


@dataclass
class ValueWriteFloatQ(ValueWriteBase):
    """ValueWrite<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,floatQ>


@dataclass
class ValueWriteDoubleQ(ValueWriteBase):
    """ValueWrite<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,doubleQ>


@dataclass
class ValueWriteDateTime(ValueWriteBase):
    """ValueWrite<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueWriteTimeSpan(ValueWriteBase):
    """ValueWrite<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueWriteColor(ValueWriteBase):
    """ValueWrite<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,color>


@dataclass
class ValueWriteColorX(ValueWriteBase):
    """ValueWrite<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,colorX>


@dataclass
class ValueWriteShadowCastMode(ValueWriteBase):
    """ValueWrite<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueWriteLightType(ValueWriteBase):
    """ValueWrite<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueWriteSessionAccessLevel(ValueWriteBase):
    """ValueWrite<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueWriteKey(ValueWriteBase):
    """ValueWrite<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueWriteHttpStatusCode(ValueWriteBase):
    """ValueWrite<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueWriteHeadOutputDevice(ValueWriteBase):
    """ValueWrite<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueWriteReflectionProbeClear(ValueWriteBase):
    """ValueWrite<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueWriteReflectionProbeType(ValueWriteBase):
    """ValueWrite<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueWriteReflectionProbeTimeSlicingMode(ValueWriteBase):
    """ValueWrite<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueWriteCameraClearMode(ValueWriteBase):
    """ValueWrite<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueWriteCameraPositioningMode(ValueWriteBase):
    """ValueWrite<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.CameraPositioningMode>


@dataclass
class ValueWriteCameraProjection(ValueWriteBase):
    """ValueWrite<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueWriteZWrite(ValueWriteBase):
    """ValueWrite<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZWrite>


@dataclass
class ValueWriteZTest(ValueWriteBase):
    """ValueWrite<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.ZTest>


@dataclass
class ValueWriteBlend(ValueWriteBase):
    """ValueWrite<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Blend>


@dataclass
class ValueWriteBlendMode(ValueWriteBase):
    """ValueWrite<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.BlendMode>


@dataclass
class ValueWriteCulling(ValueWriteBase):
    """ValueWrite<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[FrooxEngine]FrooxEngine.Culling>


@dataclass
class ValueWriteBodyNode(ValueWriteBase):
    """ValueWrite<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueWriteChirality(ValueWriteBase):
    """ValueWrite<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueWriteDummyEnum(ValueWriteBase):
    """ValueWrite<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueWrite<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_fail": "OnFail",
        "on_written": "OnWritten",
        "value": "Value",
        "variable": "Variable",
    }

    on_fail: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    variable: Reference | None = None  # -> [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IVariable<[ProtoFlux.Core]ProtoFlux.Runtimes.Execution.ExecutionContext,DummyEnum>


# Type alias for any ValueWrite variant
ValueWrite = (
    ValueWriteBool |
    ValueWriteByte |
    ValueWriteUshort |
    ValueWriteUint |
    ValueWriteUlong |
    ValueWriteSbyte |
    ValueWriteShort |
    ValueWriteInt |
    ValueWriteLong |
    ValueWriteFloat |
    ValueWriteDouble |
    ValueWriteDecimal |
    ValueWriteChar |
    ValueWriteString |
    ValueWriteUri |
    ValueWriteBool2 |
    ValueWriteByte2 |
    ValueWriteUshort2 |
    ValueWriteUint2 |
    ValueWriteUlong2 |
    ValueWriteSbyte2 |
    ValueWriteShort2 |
    ValueWriteInt2 |
    ValueWriteLong2 |
    ValueWriteFloat2 |
    ValueWriteDouble2 |
    ValueWriteBool3 |
    ValueWriteByte3 |
    ValueWriteUshort3 |
    ValueWriteUint3 |
    ValueWriteUlong3 |
    ValueWriteSbyte3 |
    ValueWriteShort3 |
    ValueWriteInt3 |
    ValueWriteLong3 |
    ValueWriteFloat3 |
    ValueWriteDouble3 |
    ValueWriteBool4 |
    ValueWriteByte4 |
    ValueWriteUshort4 |
    ValueWriteUint4 |
    ValueWriteUlong4 |
    ValueWriteSbyte4 |
    ValueWriteShort4 |
    ValueWriteInt4 |
    ValueWriteLong4 |
    ValueWriteFloat4 |
    ValueWriteDouble4 |
    ValueWriteFloat_2x2 |
    ValueWriteDouble_2x2 |
    ValueWriteFloat_3x3 |
    ValueWriteDouble_3x3 |
    ValueWriteFloat_4x4 |
    ValueWriteDouble_4x4 |
    ValueWriteFloatQ |
    ValueWriteDoubleQ |
    ValueWriteDateTime |
    ValueWriteTimeSpan |
    ValueWriteColor |
    ValueWriteColorX |
    ValueWriteShadowCastMode |
    ValueWriteLightType |
    ValueWriteSessionAccessLevel |
    ValueWriteKey |
    ValueWriteHttpStatusCode |
    ValueWriteHeadOutputDevice |
    ValueWriteReflectionProbeClear |
    ValueWriteReflectionProbeType |
    ValueWriteReflectionProbeTimeSlicingMode |
    ValueWriteCameraClearMode |
    ValueWriteCameraPositioningMode |
    ValueWriteCameraProjection |
    ValueWriteZWrite |
    ValueWriteZTest |
    ValueWriteBlend |
    ValueWriteBlendMode |
    ValueWriteCulling |
    ValueWriteBodyNode |
    ValueWriteChirality |
    ValueWriteDummyEnum
)