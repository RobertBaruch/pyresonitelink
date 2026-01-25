"""Generated component: ValuePlusMinus.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValuePlusMinusBase(GeneratedComponent):
    """Base class for ValuePlusMinus<T> variants."""

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
class ValuePlusMinusBool(ValuePlusMinusBase):
    """ValuePlusMinus<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValuePlusMinusByte(ValuePlusMinusBase):
    """ValuePlusMinus<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValuePlusMinusUshort(ValuePlusMinusBase):
    """ValuePlusMinus<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValuePlusMinusUint(ValuePlusMinusBase):
    """ValuePlusMinus<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValuePlusMinusUlong(ValuePlusMinusBase):
    """ValuePlusMinus<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValuePlusMinusSbyte(ValuePlusMinusBase):
    """ValuePlusMinus<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValuePlusMinusShort(ValuePlusMinusBase):
    """ValuePlusMinus<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValuePlusMinusInt(ValuePlusMinusBase):
    """ValuePlusMinus<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValuePlusMinusLong(ValuePlusMinusBase):
    """ValuePlusMinus<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValuePlusMinusFloat(ValuePlusMinusBase):
    """ValuePlusMinus<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValuePlusMinusDouble(ValuePlusMinusBase):
    """ValuePlusMinus<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValuePlusMinusDecimal(ValuePlusMinusBase):
    """ValuePlusMinus<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValuePlusMinusChar(ValuePlusMinusBase):
    """ValuePlusMinus<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValuePlusMinusString(ValuePlusMinusBase):
    """ValuePlusMinus<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValuePlusMinusUri(ValuePlusMinusBase):
    """ValuePlusMinus<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValuePlusMinusBool2(ValuePlusMinusBase):
    """ValuePlusMinus<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValuePlusMinusByte2(ValuePlusMinusBase):
    """ValuePlusMinus<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValuePlusMinusUshort2(ValuePlusMinusBase):
    """ValuePlusMinus<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValuePlusMinusUint2(ValuePlusMinusBase):
    """ValuePlusMinus<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValuePlusMinusUlong2(ValuePlusMinusBase):
    """ValuePlusMinus<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValuePlusMinusSbyte2(ValuePlusMinusBase):
    """ValuePlusMinus<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValuePlusMinusShort2(ValuePlusMinusBase):
    """ValuePlusMinus<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValuePlusMinusInt2(ValuePlusMinusBase):
    """ValuePlusMinus<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValuePlusMinusLong2(ValuePlusMinusBase):
    """ValuePlusMinus<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValuePlusMinusFloat2(ValuePlusMinusBase):
    """ValuePlusMinus<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValuePlusMinusDouble2(ValuePlusMinusBase):
    """ValuePlusMinus<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValuePlusMinusBool3(ValuePlusMinusBase):
    """ValuePlusMinus<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValuePlusMinusByte3(ValuePlusMinusBase):
    """ValuePlusMinus<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValuePlusMinusUshort3(ValuePlusMinusBase):
    """ValuePlusMinus<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValuePlusMinusUint3(ValuePlusMinusBase):
    """ValuePlusMinus<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValuePlusMinusUlong3(ValuePlusMinusBase):
    """ValuePlusMinus<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValuePlusMinusSbyte3(ValuePlusMinusBase):
    """ValuePlusMinus<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValuePlusMinusShort3(ValuePlusMinusBase):
    """ValuePlusMinus<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValuePlusMinusInt3(ValuePlusMinusBase):
    """ValuePlusMinus<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValuePlusMinusLong3(ValuePlusMinusBase):
    """ValuePlusMinus<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValuePlusMinusFloat3(ValuePlusMinusBase):
    """ValuePlusMinus<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValuePlusMinusDouble3(ValuePlusMinusBase):
    """ValuePlusMinus<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValuePlusMinusBool4(ValuePlusMinusBase):
    """ValuePlusMinus<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValuePlusMinusByte4(ValuePlusMinusBase):
    """ValuePlusMinus<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValuePlusMinusUshort4(ValuePlusMinusBase):
    """ValuePlusMinus<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValuePlusMinusUint4(ValuePlusMinusBase):
    """ValuePlusMinus<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValuePlusMinusUlong4(ValuePlusMinusBase):
    """ValuePlusMinus<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValuePlusMinusSbyte4(ValuePlusMinusBase):
    """ValuePlusMinus<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValuePlusMinusShort4(ValuePlusMinusBase):
    """ValuePlusMinus<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValuePlusMinusInt4(ValuePlusMinusBase):
    """ValuePlusMinus<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValuePlusMinusLong4(ValuePlusMinusBase):
    """ValuePlusMinus<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValuePlusMinusFloat4(ValuePlusMinusBase):
    """ValuePlusMinus<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValuePlusMinusDouble4(ValuePlusMinusBase):
    """ValuePlusMinus<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValuePlusMinusFloat_2x2(ValuePlusMinusBase):
    """ValuePlusMinus<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValuePlusMinusDouble_2x2(ValuePlusMinusBase):
    """ValuePlusMinus<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValuePlusMinusFloat_3x3(ValuePlusMinusBase):
    """ValuePlusMinus<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValuePlusMinusDouble_3x3(ValuePlusMinusBase):
    """ValuePlusMinus<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValuePlusMinusFloat_4x4(ValuePlusMinusBase):
    """ValuePlusMinus<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValuePlusMinusDouble_4x4(ValuePlusMinusBase):
    """ValuePlusMinus<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValuePlusMinusFloatQ(ValuePlusMinusBase):
    """ValuePlusMinus<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValuePlusMinusDoubleQ(ValuePlusMinusBase):
    """ValuePlusMinus<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValuePlusMinusDateTime(ValuePlusMinusBase):
    """ValuePlusMinus<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValuePlusMinusTimeSpan(ValuePlusMinusBase):
    """ValuePlusMinus<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValuePlusMinusColor(ValuePlusMinusBase):
    """ValuePlusMinus<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValuePlusMinusColorX(ValuePlusMinusBase):
    """ValuePlusMinus<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValuePlusMinusShadowCastMode(ValuePlusMinusBase):
    """ValuePlusMinus<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValuePlusMinusLightType(ValuePlusMinusBase):
    """ValuePlusMinus<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValuePlusMinusSessionAccessLevel(ValuePlusMinusBase):
    """ValuePlusMinus<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValuePlusMinusKey(ValuePlusMinusBase):
    """ValuePlusMinus<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValuePlusMinusHttpStatusCode(ValuePlusMinusBase):
    """ValuePlusMinus<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValuePlusMinusHeadOutputDevice(ValuePlusMinusBase):
    """ValuePlusMinus<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValuePlusMinusReflectionProbeClear(ValuePlusMinusBase):
    """ValuePlusMinus<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValuePlusMinusReflectionProbeType(ValuePlusMinusBase):
    """ValuePlusMinus<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValuePlusMinusReflectionProbeTimeSlicingMode(ValuePlusMinusBase):
    """ValuePlusMinus<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValuePlusMinusCameraClearMode(ValuePlusMinusBase):
    """ValuePlusMinus<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValuePlusMinusCameraPositioningMode(ValuePlusMinusBase):
    """ValuePlusMinus<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValuePlusMinusCameraProjection(ValuePlusMinusBase):
    """ValuePlusMinus<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValuePlusMinusZWrite(ValuePlusMinusBase):
    """ValuePlusMinus<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValuePlusMinusZTest(ValuePlusMinusBase):
    """ValuePlusMinus<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValuePlusMinusBlend(ValuePlusMinusBase):
    """ValuePlusMinus<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValuePlusMinusBlendMode(ValuePlusMinusBase):
    """ValuePlusMinus<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValuePlusMinusCulling(ValuePlusMinusBase):
    """ValuePlusMinus<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValuePlusMinusBodyNode(ValuePlusMinusBase):
    """ValuePlusMinus<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValuePlusMinusChirality(ValuePlusMinusBase):
    """ValuePlusMinus<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValuePlusMinusDummyEnum(ValuePlusMinusBase):
    """ValuePlusMinus<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "offset": "Offset",
        "value": "Value",
    }

    offset: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValuePlusMinus variant
ValuePlusMinus = (
    ValuePlusMinusBool |
    ValuePlusMinusByte |
    ValuePlusMinusUshort |
    ValuePlusMinusUint |
    ValuePlusMinusUlong |
    ValuePlusMinusSbyte |
    ValuePlusMinusShort |
    ValuePlusMinusInt |
    ValuePlusMinusLong |
    ValuePlusMinusFloat |
    ValuePlusMinusDouble |
    ValuePlusMinusDecimal |
    ValuePlusMinusChar |
    ValuePlusMinusString |
    ValuePlusMinusUri |
    ValuePlusMinusBool2 |
    ValuePlusMinusByte2 |
    ValuePlusMinusUshort2 |
    ValuePlusMinusUint2 |
    ValuePlusMinusUlong2 |
    ValuePlusMinusSbyte2 |
    ValuePlusMinusShort2 |
    ValuePlusMinusInt2 |
    ValuePlusMinusLong2 |
    ValuePlusMinusFloat2 |
    ValuePlusMinusDouble2 |
    ValuePlusMinusBool3 |
    ValuePlusMinusByte3 |
    ValuePlusMinusUshort3 |
    ValuePlusMinusUint3 |
    ValuePlusMinusUlong3 |
    ValuePlusMinusSbyte3 |
    ValuePlusMinusShort3 |
    ValuePlusMinusInt3 |
    ValuePlusMinusLong3 |
    ValuePlusMinusFloat3 |
    ValuePlusMinusDouble3 |
    ValuePlusMinusBool4 |
    ValuePlusMinusByte4 |
    ValuePlusMinusUshort4 |
    ValuePlusMinusUint4 |
    ValuePlusMinusUlong4 |
    ValuePlusMinusSbyte4 |
    ValuePlusMinusShort4 |
    ValuePlusMinusInt4 |
    ValuePlusMinusLong4 |
    ValuePlusMinusFloat4 |
    ValuePlusMinusDouble4 |
    ValuePlusMinusFloat_2x2 |
    ValuePlusMinusDouble_2x2 |
    ValuePlusMinusFloat_3x3 |
    ValuePlusMinusDouble_3x3 |
    ValuePlusMinusFloat_4x4 |
    ValuePlusMinusDouble_4x4 |
    ValuePlusMinusFloatQ |
    ValuePlusMinusDoubleQ |
    ValuePlusMinusDateTime |
    ValuePlusMinusTimeSpan |
    ValuePlusMinusColor |
    ValuePlusMinusColorX |
    ValuePlusMinusShadowCastMode |
    ValuePlusMinusLightType |
    ValuePlusMinusSessionAccessLevel |
    ValuePlusMinusKey |
    ValuePlusMinusHttpStatusCode |
    ValuePlusMinusHeadOutputDevice |
    ValuePlusMinusReflectionProbeClear |
    ValuePlusMinusReflectionProbeType |
    ValuePlusMinusReflectionProbeTimeSlicingMode |
    ValuePlusMinusCameraClearMode |
    ValuePlusMinusCameraPositioningMode |
    ValuePlusMinusCameraProjection |
    ValuePlusMinusZWrite |
    ValuePlusMinusZTest |
    ValuePlusMinusBlend |
    ValuePlusMinusBlendMode |
    ValuePlusMinusCulling |
    ValuePlusMinusBodyNode |
    ValuePlusMinusChirality |
    ValuePlusMinusDummyEnum
)