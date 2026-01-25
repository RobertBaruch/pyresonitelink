"""Generated component: NullableToObjectCast.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class NullableToObjectCastBase(GeneratedComponent):
    """Base class for NullableToObjectCast<T> variants."""

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
class NullableToObjectCastBool(NullableToObjectCastBase):
    """NullableToObjectCast<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool>>


@dataclass
class NullableToObjectCastByte(NullableToObjectCastBase):
    """NullableToObjectCast<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte>>


@dataclass
class NullableToObjectCastUshort(NullableToObjectCastBase):
    """NullableToObjectCast<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort>>


@dataclass
class NullableToObjectCastUint(NullableToObjectCastBase):
    """NullableToObjectCast<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint>>


@dataclass
class NullableToObjectCastUlong(NullableToObjectCastBase):
    """NullableToObjectCast<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong>>


@dataclass
class NullableToObjectCastSbyte(NullableToObjectCastBase):
    """NullableToObjectCast<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte>>


@dataclass
class NullableToObjectCastShort(NullableToObjectCastBase):
    """NullableToObjectCast<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short>>


@dataclass
class NullableToObjectCastInt(NullableToObjectCastBase):
    """NullableToObjectCast<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int>>


@dataclass
class NullableToObjectCastLong(NullableToObjectCastBase):
    """NullableToObjectCast<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long>>


@dataclass
class NullableToObjectCastFloat(NullableToObjectCastBase):
    """NullableToObjectCast<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float>>


@dataclass
class NullableToObjectCastDouble(NullableToObjectCastBase):
    """NullableToObjectCast<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double>>


@dataclass
class NullableToObjectCastDecimal(NullableToObjectCastBase):
    """NullableToObjectCast<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<decimal>>


@dataclass
class NullableToObjectCastChar(NullableToObjectCastBase):
    """NullableToObjectCast<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<char>>


@dataclass
class NullableToObjectCastString(NullableToObjectCastBase):
    """NullableToObjectCast<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<string>>


@dataclass
class NullableToObjectCastUri(NullableToObjectCastBase):
    """NullableToObjectCast<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<Uri>>


@dataclass
class NullableToObjectCastBool2(NullableToObjectCastBase):
    """NullableToObjectCast<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool2>>


@dataclass
class NullableToObjectCastByte2(NullableToObjectCastBase):
    """NullableToObjectCast<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte2>>


@dataclass
class NullableToObjectCastUshort2(NullableToObjectCastBase):
    """NullableToObjectCast<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort2>>


@dataclass
class NullableToObjectCastUint2(NullableToObjectCastBase):
    """NullableToObjectCast<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint2>>


@dataclass
class NullableToObjectCastUlong2(NullableToObjectCastBase):
    """NullableToObjectCast<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong2>>


@dataclass
class NullableToObjectCastSbyte2(NullableToObjectCastBase):
    """NullableToObjectCast<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte2>>


@dataclass
class NullableToObjectCastShort2(NullableToObjectCastBase):
    """NullableToObjectCast<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short2>>


@dataclass
class NullableToObjectCastInt2(NullableToObjectCastBase):
    """NullableToObjectCast<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int2>>


@dataclass
class NullableToObjectCastLong2(NullableToObjectCastBase):
    """NullableToObjectCast<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long2>>


@dataclass
class NullableToObjectCastFloat2(NullableToObjectCastBase):
    """NullableToObjectCast<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float2>>


@dataclass
class NullableToObjectCastDouble2(NullableToObjectCastBase):
    """NullableToObjectCast<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double2>>


@dataclass
class NullableToObjectCastBool3(NullableToObjectCastBase):
    """NullableToObjectCast<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool3>>


@dataclass
class NullableToObjectCastByte3(NullableToObjectCastBase):
    """NullableToObjectCast<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte3>>


@dataclass
class NullableToObjectCastUshort3(NullableToObjectCastBase):
    """NullableToObjectCast<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort3>>


@dataclass
class NullableToObjectCastUint3(NullableToObjectCastBase):
    """NullableToObjectCast<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint3>>


@dataclass
class NullableToObjectCastUlong3(NullableToObjectCastBase):
    """NullableToObjectCast<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong3>>


@dataclass
class NullableToObjectCastSbyte3(NullableToObjectCastBase):
    """NullableToObjectCast<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte3>>


@dataclass
class NullableToObjectCastShort3(NullableToObjectCastBase):
    """NullableToObjectCast<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short3>>


@dataclass
class NullableToObjectCastInt3(NullableToObjectCastBase):
    """NullableToObjectCast<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int3>>


@dataclass
class NullableToObjectCastLong3(NullableToObjectCastBase):
    """NullableToObjectCast<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long3>>


@dataclass
class NullableToObjectCastFloat3(NullableToObjectCastBase):
    """NullableToObjectCast<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float3>>


@dataclass
class NullableToObjectCastDouble3(NullableToObjectCastBase):
    """NullableToObjectCast<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double3>>


@dataclass
class NullableToObjectCastBool4(NullableToObjectCastBase):
    """NullableToObjectCast<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool4>>


@dataclass
class NullableToObjectCastByte4(NullableToObjectCastBase):
    """NullableToObjectCast<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte4>>


@dataclass
class NullableToObjectCastUshort4(NullableToObjectCastBase):
    """NullableToObjectCast<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort4>>


@dataclass
class NullableToObjectCastUint4(NullableToObjectCastBase):
    """NullableToObjectCast<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint4>>


@dataclass
class NullableToObjectCastUlong4(NullableToObjectCastBase):
    """NullableToObjectCast<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong4>>


@dataclass
class NullableToObjectCastSbyte4(NullableToObjectCastBase):
    """NullableToObjectCast<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte4>>


@dataclass
class NullableToObjectCastShort4(NullableToObjectCastBase):
    """NullableToObjectCast<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short4>>


@dataclass
class NullableToObjectCastInt4(NullableToObjectCastBase):
    """NullableToObjectCast<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int4>>


@dataclass
class NullableToObjectCastLong4(NullableToObjectCastBase):
    """NullableToObjectCast<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long4>>


@dataclass
class NullableToObjectCastFloat4(NullableToObjectCastBase):
    """NullableToObjectCast<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float4>>


@dataclass
class NullableToObjectCastDouble4(NullableToObjectCastBase):
    """NullableToObjectCast<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double4>>


@dataclass
class NullableToObjectCastFloat_2x2(NullableToObjectCastBase):
    """NullableToObjectCast<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float2x2>>


@dataclass
class NullableToObjectCastDouble_2x2(NullableToObjectCastBase):
    """NullableToObjectCast<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double2x2>>


@dataclass
class NullableToObjectCastFloat_3x3(NullableToObjectCastBase):
    """NullableToObjectCast<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float3x3>>


@dataclass
class NullableToObjectCastDouble_3x3(NullableToObjectCastBase):
    """NullableToObjectCast<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double3x3>>


@dataclass
class NullableToObjectCastFloat_4x4(NullableToObjectCastBase):
    """NullableToObjectCast<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float4x4>>


@dataclass
class NullableToObjectCastDouble_4x4(NullableToObjectCastBase):
    """NullableToObjectCast<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double4x4>>


@dataclass
class NullableToObjectCastFloatQ(NullableToObjectCastBase):
    """NullableToObjectCast<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<floatQ>>


@dataclass
class NullableToObjectCastDoubleQ(NullableToObjectCastBase):
    """NullableToObjectCast<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<doubleQ>>


@dataclass
class NullableToObjectCastDateTime(NullableToObjectCastBase):
    """NullableToObjectCast<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Private.CoreLib]System.DateTime>>


@dataclass
class NullableToObjectCastTimeSpan(NullableToObjectCastBase):
    """NullableToObjectCast<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Private.CoreLib]System.TimeSpan>>


@dataclass
class NullableToObjectCastColor(NullableToObjectCastBase):
    """NullableToObjectCast<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<color>>


@dataclass
class NullableToObjectCastColorX(NullableToObjectCastBase):
    """NullableToObjectCast<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<colorX>>


@dataclass
class NullableToObjectCastShadowCastMode(NullableToObjectCastBase):
    """NullableToObjectCast<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>>


@dataclass
class NullableToObjectCastLightType(NullableToObjectCastBase):
    """NullableToObjectCast<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.LightType>>


@dataclass
class NullableToObjectCastSessionAccessLevel(NullableToObjectCastBase):
    """NullableToObjectCast<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>


@dataclass
class NullableToObjectCastKey(NullableToObjectCastBase):
    """NullableToObjectCast<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.Key>>


@dataclass
class NullableToObjectCastHttpStatusCode(NullableToObjectCastBase):
    """NullableToObjectCast<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Net.Primitives]System.Net.HttpStatusCode>>


@dataclass
class NullableToObjectCastHeadOutputDevice(NullableToObjectCastBase):
    """NullableToObjectCast<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>


@dataclass
class NullableToObjectCastReflectionProbeClear(NullableToObjectCastBase):
    """NullableToObjectCast<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>


@dataclass
class NullableToObjectCastReflectionProbeType(NullableToObjectCastBase):
    """NullableToObjectCast<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>


@dataclass
class NullableToObjectCastReflectionProbeTimeSlicingMode(NullableToObjectCastBase):
    """NullableToObjectCast<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>


@dataclass
class NullableToObjectCastCameraClearMode(NullableToObjectCastBase):
    """NullableToObjectCast<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.CameraClearMode>>


@dataclass
class NullableToObjectCastCameraPositioningMode(NullableToObjectCastBase):
    """NullableToObjectCast<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.CameraPositioningMode>>


@dataclass
class NullableToObjectCastCameraProjection(NullableToObjectCastBase):
    """NullableToObjectCast<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.CameraProjection>>


@dataclass
class NullableToObjectCastZWrite(NullableToObjectCastBase):
    """NullableToObjectCast<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.ZWrite>>


@dataclass
class NullableToObjectCastZTest(NullableToObjectCastBase):
    """NullableToObjectCast<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.ZTest>>


@dataclass
class NullableToObjectCastBlend(NullableToObjectCastBase):
    """NullableToObjectCast<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.Blend>>


@dataclass
class NullableToObjectCastBlendMode(NullableToObjectCastBase):
    """NullableToObjectCast<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.BlendMode>>


@dataclass
class NullableToObjectCastCulling(NullableToObjectCastBase):
    """NullableToObjectCast<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.Culling>>


@dataclass
class NullableToObjectCastBodyNode(NullableToObjectCastBase):
    """NullableToObjectCast<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.BodyNode>>


@dataclass
class NullableToObjectCastChirality(NullableToObjectCastBase):
    """NullableToObjectCast<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.Chirality>>


@dataclass
class NullableToObjectCastDummyEnum(NullableToObjectCastBase):
    """NullableToObjectCast<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.NullableToObjectCast<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<DummyEnum>>


# Type alias for any NullableToObjectCast variant
NullableToObjectCast = (
    NullableToObjectCastBool |
    NullableToObjectCastByte |
    NullableToObjectCastUshort |
    NullableToObjectCastUint |
    NullableToObjectCastUlong |
    NullableToObjectCastSbyte |
    NullableToObjectCastShort |
    NullableToObjectCastInt |
    NullableToObjectCastLong |
    NullableToObjectCastFloat |
    NullableToObjectCastDouble |
    NullableToObjectCastDecimal |
    NullableToObjectCastChar |
    NullableToObjectCastString |
    NullableToObjectCastUri |
    NullableToObjectCastBool2 |
    NullableToObjectCastByte2 |
    NullableToObjectCastUshort2 |
    NullableToObjectCastUint2 |
    NullableToObjectCastUlong2 |
    NullableToObjectCastSbyte2 |
    NullableToObjectCastShort2 |
    NullableToObjectCastInt2 |
    NullableToObjectCastLong2 |
    NullableToObjectCastFloat2 |
    NullableToObjectCastDouble2 |
    NullableToObjectCastBool3 |
    NullableToObjectCastByte3 |
    NullableToObjectCastUshort3 |
    NullableToObjectCastUint3 |
    NullableToObjectCastUlong3 |
    NullableToObjectCastSbyte3 |
    NullableToObjectCastShort3 |
    NullableToObjectCastInt3 |
    NullableToObjectCastLong3 |
    NullableToObjectCastFloat3 |
    NullableToObjectCastDouble3 |
    NullableToObjectCastBool4 |
    NullableToObjectCastByte4 |
    NullableToObjectCastUshort4 |
    NullableToObjectCastUint4 |
    NullableToObjectCastUlong4 |
    NullableToObjectCastSbyte4 |
    NullableToObjectCastShort4 |
    NullableToObjectCastInt4 |
    NullableToObjectCastLong4 |
    NullableToObjectCastFloat4 |
    NullableToObjectCastDouble4 |
    NullableToObjectCastFloat_2x2 |
    NullableToObjectCastDouble_2x2 |
    NullableToObjectCastFloat_3x3 |
    NullableToObjectCastDouble_3x3 |
    NullableToObjectCastFloat_4x4 |
    NullableToObjectCastDouble_4x4 |
    NullableToObjectCastFloatQ |
    NullableToObjectCastDoubleQ |
    NullableToObjectCastDateTime |
    NullableToObjectCastTimeSpan |
    NullableToObjectCastColor |
    NullableToObjectCastColorX |
    NullableToObjectCastShadowCastMode |
    NullableToObjectCastLightType |
    NullableToObjectCastSessionAccessLevel |
    NullableToObjectCastKey |
    NullableToObjectCastHttpStatusCode |
    NullableToObjectCastHeadOutputDevice |
    NullableToObjectCastReflectionProbeClear |
    NullableToObjectCastReflectionProbeType |
    NullableToObjectCastReflectionProbeTimeSlicingMode |
    NullableToObjectCastCameraClearMode |
    NullableToObjectCastCameraPositioningMode |
    NullableToObjectCastCameraProjection |
    NullableToObjectCastZWrite |
    NullableToObjectCastZTest |
    NullableToObjectCastBlend |
    NullableToObjectCastBlendMode |
    NullableToObjectCastCulling |
    NullableToObjectCastBodyNode |
    NullableToObjectCastChirality |
    NullableToObjectCastDummyEnum
)