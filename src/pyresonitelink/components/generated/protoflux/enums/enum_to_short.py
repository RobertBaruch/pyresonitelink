"""Generated component: EnumToShort.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class EnumToShortBase(GeneratedComponent):
    """Base class for EnumToShort<T> variants."""

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
class EnumToShortBool(EnumToShortBase):
    """EnumToShort<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class EnumToShortByte(EnumToShortBase):
    """EnumToShort<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class EnumToShortUshort(EnumToShortBase):
    """EnumToShort<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class EnumToShortUint(EnumToShortBase):
    """EnumToShort<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class EnumToShortUlong(EnumToShortBase):
    """EnumToShort<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class EnumToShortSbyte(EnumToShortBase):
    """EnumToShort<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class EnumToShortShort(EnumToShortBase):
    """EnumToShort<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class EnumToShortInt(EnumToShortBase):
    """EnumToShort<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class EnumToShortLong(EnumToShortBase):
    """EnumToShort<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class EnumToShortFloat(EnumToShortBase):
    """EnumToShort<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class EnumToShortDouble(EnumToShortBase):
    """EnumToShort<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class EnumToShortDecimal(EnumToShortBase):
    """EnumToShort<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class EnumToShortChar(EnumToShortBase):
    """EnumToShort<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class EnumToShortString(EnumToShortBase):
    """EnumToShort<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class EnumToShortUri(EnumToShortBase):
    """EnumToShort<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class EnumToShortBool2(EnumToShortBase):
    """EnumToShort<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class EnumToShortByte2(EnumToShortBase):
    """EnumToShort<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class EnumToShortUshort2(EnumToShortBase):
    """EnumToShort<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class EnumToShortUint2(EnumToShortBase):
    """EnumToShort<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class EnumToShortUlong2(EnumToShortBase):
    """EnumToShort<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class EnumToShortSbyte2(EnumToShortBase):
    """EnumToShort<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class EnumToShortShort2(EnumToShortBase):
    """EnumToShort<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class EnumToShortInt2(EnumToShortBase):
    """EnumToShort<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class EnumToShortLong2(EnumToShortBase):
    """EnumToShort<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class EnumToShortFloat2(EnumToShortBase):
    """EnumToShort<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class EnumToShortDouble2(EnumToShortBase):
    """EnumToShort<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class EnumToShortBool3(EnumToShortBase):
    """EnumToShort<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class EnumToShortByte3(EnumToShortBase):
    """EnumToShort<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class EnumToShortUshort3(EnumToShortBase):
    """EnumToShort<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class EnumToShortUint3(EnumToShortBase):
    """EnumToShort<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class EnumToShortUlong3(EnumToShortBase):
    """EnumToShort<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class EnumToShortSbyte3(EnumToShortBase):
    """EnumToShort<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class EnumToShortShort3(EnumToShortBase):
    """EnumToShort<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class EnumToShortInt3(EnumToShortBase):
    """EnumToShort<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class EnumToShortLong3(EnumToShortBase):
    """EnumToShort<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class EnumToShortFloat3(EnumToShortBase):
    """EnumToShort<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class EnumToShortDouble3(EnumToShortBase):
    """EnumToShort<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class EnumToShortBool4(EnumToShortBase):
    """EnumToShort<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class EnumToShortByte4(EnumToShortBase):
    """EnumToShort<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class EnumToShortUshort4(EnumToShortBase):
    """EnumToShort<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class EnumToShortUint4(EnumToShortBase):
    """EnumToShort<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class EnumToShortUlong4(EnumToShortBase):
    """EnumToShort<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class EnumToShortSbyte4(EnumToShortBase):
    """EnumToShort<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class EnumToShortShort4(EnumToShortBase):
    """EnumToShort<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class EnumToShortInt4(EnumToShortBase):
    """EnumToShort<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class EnumToShortLong4(EnumToShortBase):
    """EnumToShort<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class EnumToShortFloat4(EnumToShortBase):
    """EnumToShort<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class EnumToShortDouble4(EnumToShortBase):
    """EnumToShort<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class EnumToShortFloat_2x2(EnumToShortBase):
    """EnumToShort<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class EnumToShortDouble_2x2(EnumToShortBase):
    """EnumToShort<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class EnumToShortFloat_3x3(EnumToShortBase):
    """EnumToShort<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class EnumToShortDouble_3x3(EnumToShortBase):
    """EnumToShort<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class EnumToShortFloat_4x4(EnumToShortBase):
    """EnumToShort<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class EnumToShortDouble_4x4(EnumToShortBase):
    """EnumToShort<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class EnumToShortFloatQ(EnumToShortBase):
    """EnumToShort<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class EnumToShortDoubleQ(EnumToShortBase):
    """EnumToShort<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class EnumToShortDateTime(EnumToShortBase):
    """EnumToShort<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class EnumToShortTimeSpan(EnumToShortBase):
    """EnumToShort<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class EnumToShortColor(EnumToShortBase):
    """EnumToShort<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class EnumToShortColorX(EnumToShortBase):
    """EnumToShort<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class EnumToShortShadowCastMode(EnumToShortBase):
    """EnumToShort<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class EnumToShortLightType(EnumToShortBase):
    """EnumToShort<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class EnumToShortSessionAccessLevel(EnumToShortBase):
    """EnumToShort<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class EnumToShortKey(EnumToShortBase):
    """EnumToShort<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class EnumToShortHttpStatusCode(EnumToShortBase):
    """EnumToShort<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class EnumToShortHeadOutputDevice(EnumToShortBase):
    """EnumToShort<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class EnumToShortReflectionProbeClear(EnumToShortBase):
    """EnumToShort<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class EnumToShortReflectionProbeType(EnumToShortBase):
    """EnumToShort<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class EnumToShortReflectionProbeTimeSlicingMode(EnumToShortBase):
    """EnumToShort<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class EnumToShortCameraClearMode(EnumToShortBase):
    """EnumToShort<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class EnumToShortCameraPositioningMode(EnumToShortBase):
    """EnumToShort<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class EnumToShortCameraProjection(EnumToShortBase):
    """EnumToShort<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class EnumToShortZWrite(EnumToShortBase):
    """EnumToShort<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class EnumToShortZTest(EnumToShortBase):
    """EnumToShort<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class EnumToShortBlend(EnumToShortBase):
    """EnumToShort<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class EnumToShortBlendMode(EnumToShortBase):
    """EnumToShort<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class EnumToShortCulling(EnumToShortBase):
    """EnumToShort<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class EnumToShortBodyNode(EnumToShortBase):
    """EnumToShort<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class EnumToShortChirality(EnumToShortBase):
    """EnumToShort<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class EnumToShortDummyEnum(EnumToShortBase):
    """EnumToShort<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.EnumToShort<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any EnumToShort variant
EnumToShort = (
    EnumToShortBool |
    EnumToShortByte |
    EnumToShortUshort |
    EnumToShortUint |
    EnumToShortUlong |
    EnumToShortSbyte |
    EnumToShortShort |
    EnumToShortInt |
    EnumToShortLong |
    EnumToShortFloat |
    EnumToShortDouble |
    EnumToShortDecimal |
    EnumToShortChar |
    EnumToShortString |
    EnumToShortUri |
    EnumToShortBool2 |
    EnumToShortByte2 |
    EnumToShortUshort2 |
    EnumToShortUint2 |
    EnumToShortUlong2 |
    EnumToShortSbyte2 |
    EnumToShortShort2 |
    EnumToShortInt2 |
    EnumToShortLong2 |
    EnumToShortFloat2 |
    EnumToShortDouble2 |
    EnumToShortBool3 |
    EnumToShortByte3 |
    EnumToShortUshort3 |
    EnumToShortUint3 |
    EnumToShortUlong3 |
    EnumToShortSbyte3 |
    EnumToShortShort3 |
    EnumToShortInt3 |
    EnumToShortLong3 |
    EnumToShortFloat3 |
    EnumToShortDouble3 |
    EnumToShortBool4 |
    EnumToShortByte4 |
    EnumToShortUshort4 |
    EnumToShortUint4 |
    EnumToShortUlong4 |
    EnumToShortSbyte4 |
    EnumToShortShort4 |
    EnumToShortInt4 |
    EnumToShortLong4 |
    EnumToShortFloat4 |
    EnumToShortDouble4 |
    EnumToShortFloat_2x2 |
    EnumToShortDouble_2x2 |
    EnumToShortFloat_3x3 |
    EnumToShortDouble_3x3 |
    EnumToShortFloat_4x4 |
    EnumToShortDouble_4x4 |
    EnumToShortFloatQ |
    EnumToShortDoubleQ |
    EnumToShortDateTime |
    EnumToShortTimeSpan |
    EnumToShortColor |
    EnumToShortColorX |
    EnumToShortShadowCastMode |
    EnumToShortLightType |
    EnumToShortSessionAccessLevel |
    EnumToShortKey |
    EnumToShortHttpStatusCode |
    EnumToShortHeadOutputDevice |
    EnumToShortReflectionProbeClear |
    EnumToShortReflectionProbeType |
    EnumToShortReflectionProbeTimeSlicingMode |
    EnumToShortCameraClearMode |
    EnumToShortCameraPositioningMode |
    EnumToShortCameraProjection |
    EnumToShortZWrite |
    EnumToShortZTest |
    EnumToShortBlend |
    EnumToShortBlendMode |
    EnumToShortCulling |
    EnumToShortBodyNode |
    EnumToShortChirality |
    EnumToShortDummyEnum
)