"""Generated component: ValueFilterInvalid.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueFilterInvalidBase(GeneratedComponent):
    """Base class for ValueFilterInvalid<T> variants."""

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
class ValueFilterInvalidBool(ValueFilterInvalidBase):
    """ValueFilterInvalid<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueFilterInvalidByte(ValueFilterInvalidBase):
    """ValueFilterInvalid<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueFilterInvalidUshort(ValueFilterInvalidBase):
    """ValueFilterInvalid<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueFilterInvalidUint(ValueFilterInvalidBase):
    """ValueFilterInvalid<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueFilterInvalidUlong(ValueFilterInvalidBase):
    """ValueFilterInvalid<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueFilterInvalidSbyte(ValueFilterInvalidBase):
    """ValueFilterInvalid<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueFilterInvalidShort(ValueFilterInvalidBase):
    """ValueFilterInvalid<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueFilterInvalidInt(ValueFilterInvalidBase):
    """ValueFilterInvalid<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueFilterInvalidLong(ValueFilterInvalidBase):
    """ValueFilterInvalid<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueFilterInvalidFloat(ValueFilterInvalidBase):
    """ValueFilterInvalid<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueFilterInvalidDouble(ValueFilterInvalidBase):
    """ValueFilterInvalid<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueFilterInvalidDecimal(ValueFilterInvalidBase):
    """ValueFilterInvalid<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueFilterInvalidChar(ValueFilterInvalidBase):
    """ValueFilterInvalid<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueFilterInvalidString(ValueFilterInvalidBase):
    """ValueFilterInvalid<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueFilterInvalidUri(ValueFilterInvalidBase):
    """ValueFilterInvalid<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueFilterInvalidBool2(ValueFilterInvalidBase):
    """ValueFilterInvalid<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueFilterInvalidByte2(ValueFilterInvalidBase):
    """ValueFilterInvalid<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueFilterInvalidUshort2(ValueFilterInvalidBase):
    """ValueFilterInvalid<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueFilterInvalidUint2(ValueFilterInvalidBase):
    """ValueFilterInvalid<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueFilterInvalidUlong2(ValueFilterInvalidBase):
    """ValueFilterInvalid<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueFilterInvalidSbyte2(ValueFilterInvalidBase):
    """ValueFilterInvalid<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueFilterInvalidShort2(ValueFilterInvalidBase):
    """ValueFilterInvalid<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueFilterInvalidInt2(ValueFilterInvalidBase):
    """ValueFilterInvalid<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueFilterInvalidLong2(ValueFilterInvalidBase):
    """ValueFilterInvalid<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueFilterInvalidFloat2(ValueFilterInvalidBase):
    """ValueFilterInvalid<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueFilterInvalidDouble2(ValueFilterInvalidBase):
    """ValueFilterInvalid<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueFilterInvalidBool3(ValueFilterInvalidBase):
    """ValueFilterInvalid<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueFilterInvalidByte3(ValueFilterInvalidBase):
    """ValueFilterInvalid<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueFilterInvalidUshort3(ValueFilterInvalidBase):
    """ValueFilterInvalid<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueFilterInvalidUint3(ValueFilterInvalidBase):
    """ValueFilterInvalid<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueFilterInvalidUlong3(ValueFilterInvalidBase):
    """ValueFilterInvalid<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueFilterInvalidSbyte3(ValueFilterInvalidBase):
    """ValueFilterInvalid<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueFilterInvalidShort3(ValueFilterInvalidBase):
    """ValueFilterInvalid<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueFilterInvalidInt3(ValueFilterInvalidBase):
    """ValueFilterInvalid<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueFilterInvalidLong3(ValueFilterInvalidBase):
    """ValueFilterInvalid<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueFilterInvalidFloat3(ValueFilterInvalidBase):
    """ValueFilterInvalid<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueFilterInvalidDouble3(ValueFilterInvalidBase):
    """ValueFilterInvalid<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueFilterInvalidBool4(ValueFilterInvalidBase):
    """ValueFilterInvalid<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueFilterInvalidByte4(ValueFilterInvalidBase):
    """ValueFilterInvalid<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueFilterInvalidUshort4(ValueFilterInvalidBase):
    """ValueFilterInvalid<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueFilterInvalidUint4(ValueFilterInvalidBase):
    """ValueFilterInvalid<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueFilterInvalidUlong4(ValueFilterInvalidBase):
    """ValueFilterInvalid<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueFilterInvalidSbyte4(ValueFilterInvalidBase):
    """ValueFilterInvalid<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueFilterInvalidShort4(ValueFilterInvalidBase):
    """ValueFilterInvalid<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueFilterInvalidInt4(ValueFilterInvalidBase):
    """ValueFilterInvalid<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueFilterInvalidLong4(ValueFilterInvalidBase):
    """ValueFilterInvalid<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueFilterInvalidFloat4(ValueFilterInvalidBase):
    """ValueFilterInvalid<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueFilterInvalidDouble4(ValueFilterInvalidBase):
    """ValueFilterInvalid<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueFilterInvalidFloat_2x2(ValueFilterInvalidBase):
    """ValueFilterInvalid<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueFilterInvalidDouble_2x2(ValueFilterInvalidBase):
    """ValueFilterInvalid<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueFilterInvalidFloat_3x3(ValueFilterInvalidBase):
    """ValueFilterInvalid<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueFilterInvalidDouble_3x3(ValueFilterInvalidBase):
    """ValueFilterInvalid<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueFilterInvalidFloat_4x4(ValueFilterInvalidBase):
    """ValueFilterInvalid<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueFilterInvalidDouble_4x4(ValueFilterInvalidBase):
    """ValueFilterInvalid<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueFilterInvalidFloatQ(ValueFilterInvalidBase):
    """ValueFilterInvalid<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueFilterInvalidDoubleQ(ValueFilterInvalidBase):
    """ValueFilterInvalid<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueFilterInvalidDateTime(ValueFilterInvalidBase):
    """ValueFilterInvalid<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueFilterInvalidTimeSpan(ValueFilterInvalidBase):
    """ValueFilterInvalid<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueFilterInvalidColor(ValueFilterInvalidBase):
    """ValueFilterInvalid<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueFilterInvalidColorX(ValueFilterInvalidBase):
    """ValueFilterInvalid<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueFilterInvalidShadowCastMode(ValueFilterInvalidBase):
    """ValueFilterInvalid<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueFilterInvalidLightType(ValueFilterInvalidBase):
    """ValueFilterInvalid<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueFilterInvalidSessionAccessLevel(ValueFilterInvalidBase):
    """ValueFilterInvalid<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueFilterInvalidKey(ValueFilterInvalidBase):
    """ValueFilterInvalid<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueFilterInvalidHttpStatusCode(ValueFilterInvalidBase):
    """ValueFilterInvalid<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueFilterInvalidHeadOutputDevice(ValueFilterInvalidBase):
    """ValueFilterInvalid<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueFilterInvalidReflectionProbeClear(ValueFilterInvalidBase):
    """ValueFilterInvalid<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueFilterInvalidReflectionProbeType(ValueFilterInvalidBase):
    """ValueFilterInvalid<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueFilterInvalidReflectionProbeTimeSlicingMode(ValueFilterInvalidBase):
    """ValueFilterInvalid<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueFilterInvalidCameraClearMode(ValueFilterInvalidBase):
    """ValueFilterInvalid<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueFilterInvalidCameraPositioningMode(ValueFilterInvalidBase):
    """ValueFilterInvalid<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueFilterInvalidCameraProjection(ValueFilterInvalidBase):
    """ValueFilterInvalid<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueFilterInvalidZWrite(ValueFilterInvalidBase):
    """ValueFilterInvalid<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueFilterInvalidZTest(ValueFilterInvalidBase):
    """ValueFilterInvalid<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueFilterInvalidBlend(ValueFilterInvalidBase):
    """ValueFilterInvalid<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueFilterInvalidBlendMode(ValueFilterInvalidBase):
    """ValueFilterInvalid<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueFilterInvalidCulling(ValueFilterInvalidBase):
    """ValueFilterInvalid<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueFilterInvalidBodyNode(ValueFilterInvalidBase):
    """ValueFilterInvalid<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueFilterInvalidChirality(ValueFilterInvalidBase):
    """ValueFilterInvalid<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueFilterInvalidDummyEnum(ValueFilterInvalidBase):
    """ValueFilterInvalid<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueFilterInvalid<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fallback": "Fallback",
        "value": "Value",
    }

    fallback: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueFilterInvalid variant
ValueFilterInvalid = (
    ValueFilterInvalidBool |
    ValueFilterInvalidByte |
    ValueFilterInvalidUshort |
    ValueFilterInvalidUint |
    ValueFilterInvalidUlong |
    ValueFilterInvalidSbyte |
    ValueFilterInvalidShort |
    ValueFilterInvalidInt |
    ValueFilterInvalidLong |
    ValueFilterInvalidFloat |
    ValueFilterInvalidDouble |
    ValueFilterInvalidDecimal |
    ValueFilterInvalidChar |
    ValueFilterInvalidString |
    ValueFilterInvalidUri |
    ValueFilterInvalidBool2 |
    ValueFilterInvalidByte2 |
    ValueFilterInvalidUshort2 |
    ValueFilterInvalidUint2 |
    ValueFilterInvalidUlong2 |
    ValueFilterInvalidSbyte2 |
    ValueFilterInvalidShort2 |
    ValueFilterInvalidInt2 |
    ValueFilterInvalidLong2 |
    ValueFilterInvalidFloat2 |
    ValueFilterInvalidDouble2 |
    ValueFilterInvalidBool3 |
    ValueFilterInvalidByte3 |
    ValueFilterInvalidUshort3 |
    ValueFilterInvalidUint3 |
    ValueFilterInvalidUlong3 |
    ValueFilterInvalidSbyte3 |
    ValueFilterInvalidShort3 |
    ValueFilterInvalidInt3 |
    ValueFilterInvalidLong3 |
    ValueFilterInvalidFloat3 |
    ValueFilterInvalidDouble3 |
    ValueFilterInvalidBool4 |
    ValueFilterInvalidByte4 |
    ValueFilterInvalidUshort4 |
    ValueFilterInvalidUint4 |
    ValueFilterInvalidUlong4 |
    ValueFilterInvalidSbyte4 |
    ValueFilterInvalidShort4 |
    ValueFilterInvalidInt4 |
    ValueFilterInvalidLong4 |
    ValueFilterInvalidFloat4 |
    ValueFilterInvalidDouble4 |
    ValueFilterInvalidFloat_2x2 |
    ValueFilterInvalidDouble_2x2 |
    ValueFilterInvalidFloat_3x3 |
    ValueFilterInvalidDouble_3x3 |
    ValueFilterInvalidFloat_4x4 |
    ValueFilterInvalidDouble_4x4 |
    ValueFilterInvalidFloatQ |
    ValueFilterInvalidDoubleQ |
    ValueFilterInvalidDateTime |
    ValueFilterInvalidTimeSpan |
    ValueFilterInvalidColor |
    ValueFilterInvalidColorX |
    ValueFilterInvalidShadowCastMode |
    ValueFilterInvalidLightType |
    ValueFilterInvalidSessionAccessLevel |
    ValueFilterInvalidKey |
    ValueFilterInvalidHttpStatusCode |
    ValueFilterInvalidHeadOutputDevice |
    ValueFilterInvalidReflectionProbeClear |
    ValueFilterInvalidReflectionProbeType |
    ValueFilterInvalidReflectionProbeTimeSlicingMode |
    ValueFilterInvalidCameraClearMode |
    ValueFilterInvalidCameraPositioningMode |
    ValueFilterInvalidCameraProjection |
    ValueFilterInvalidZWrite |
    ValueFilterInvalidZTest |
    ValueFilterInvalidBlend |
    ValueFilterInvalidBlendMode |
    ValueFilterInvalidCulling |
    ValueFilterInvalidBodyNode |
    ValueFilterInvalidChirality |
    ValueFilterInvalidDummyEnum
)