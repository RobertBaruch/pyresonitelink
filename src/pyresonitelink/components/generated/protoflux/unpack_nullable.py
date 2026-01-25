"""Generated component: UnpackNullable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UnpackNullableBase(GeneratedComponent):
    """Base class for UnpackNullable<T> variants."""

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
class UnpackNullableBool(UnpackNullableBase):
    """UnpackNullable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool>>


@dataclass
class UnpackNullableByte(UnpackNullableBase):
    """UnpackNullable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte>>


@dataclass
class UnpackNullableUshort(UnpackNullableBase):
    """UnpackNullable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort>>


@dataclass
class UnpackNullableUint(UnpackNullableBase):
    """UnpackNullable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint>>


@dataclass
class UnpackNullableUlong(UnpackNullableBase):
    """UnpackNullable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong>>


@dataclass
class UnpackNullableSbyte(UnpackNullableBase):
    """UnpackNullable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte>>


@dataclass
class UnpackNullableShort(UnpackNullableBase):
    """UnpackNullable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short>>


@dataclass
class UnpackNullableInt(UnpackNullableBase):
    """UnpackNullable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int>>


@dataclass
class UnpackNullableLong(UnpackNullableBase):
    """UnpackNullable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long>>


@dataclass
class UnpackNullableFloat(UnpackNullableBase):
    """UnpackNullable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float>>


@dataclass
class UnpackNullableDouble(UnpackNullableBase):
    """UnpackNullable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double>>


@dataclass
class UnpackNullableDecimal(UnpackNullableBase):
    """UnpackNullable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<decimal>>


@dataclass
class UnpackNullableChar(UnpackNullableBase):
    """UnpackNullable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<char>>


@dataclass
class UnpackNullableString(UnpackNullableBase):
    """UnpackNullable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<string>>


@dataclass
class UnpackNullableUri(UnpackNullableBase):
    """UnpackNullable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<Uri>>


@dataclass
class UnpackNullableBool2(UnpackNullableBase):
    """UnpackNullable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool2>>


@dataclass
class UnpackNullableByte2(UnpackNullableBase):
    """UnpackNullable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte2>>


@dataclass
class UnpackNullableUshort2(UnpackNullableBase):
    """UnpackNullable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort2>>


@dataclass
class UnpackNullableUint2(UnpackNullableBase):
    """UnpackNullable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint2>>


@dataclass
class UnpackNullableUlong2(UnpackNullableBase):
    """UnpackNullable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong2>>


@dataclass
class UnpackNullableSbyte2(UnpackNullableBase):
    """UnpackNullable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte2>>


@dataclass
class UnpackNullableShort2(UnpackNullableBase):
    """UnpackNullable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short2>>


@dataclass
class UnpackNullableInt2(UnpackNullableBase):
    """UnpackNullable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int2>>


@dataclass
class UnpackNullableLong2(UnpackNullableBase):
    """UnpackNullable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long2>>


@dataclass
class UnpackNullableFloat2(UnpackNullableBase):
    """UnpackNullable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float2>>


@dataclass
class UnpackNullableDouble2(UnpackNullableBase):
    """UnpackNullable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double2>>


@dataclass
class UnpackNullableBool3(UnpackNullableBase):
    """UnpackNullable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool3>>


@dataclass
class UnpackNullableByte3(UnpackNullableBase):
    """UnpackNullable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte3>>


@dataclass
class UnpackNullableUshort3(UnpackNullableBase):
    """UnpackNullable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort3>>


@dataclass
class UnpackNullableUint3(UnpackNullableBase):
    """UnpackNullable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint3>>


@dataclass
class UnpackNullableUlong3(UnpackNullableBase):
    """UnpackNullable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong3>>


@dataclass
class UnpackNullableSbyte3(UnpackNullableBase):
    """UnpackNullable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte3>>


@dataclass
class UnpackNullableShort3(UnpackNullableBase):
    """UnpackNullable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short3>>


@dataclass
class UnpackNullableInt3(UnpackNullableBase):
    """UnpackNullable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int3>>


@dataclass
class UnpackNullableLong3(UnpackNullableBase):
    """UnpackNullable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long3>>


@dataclass
class UnpackNullableFloat3(UnpackNullableBase):
    """UnpackNullable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float3>>


@dataclass
class UnpackNullableDouble3(UnpackNullableBase):
    """UnpackNullable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double3>>


@dataclass
class UnpackNullableBool4(UnpackNullableBase):
    """UnpackNullable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<bool4>>


@dataclass
class UnpackNullableByte4(UnpackNullableBase):
    """UnpackNullable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<byte4>>


@dataclass
class UnpackNullableUshort4(UnpackNullableBase):
    """UnpackNullable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ushort4>>


@dataclass
class UnpackNullableUint4(UnpackNullableBase):
    """UnpackNullable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<uint4>>


@dataclass
class UnpackNullableUlong4(UnpackNullableBase):
    """UnpackNullable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<ulong4>>


@dataclass
class UnpackNullableSbyte4(UnpackNullableBase):
    """UnpackNullable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<sbyte4>>


@dataclass
class UnpackNullableShort4(UnpackNullableBase):
    """UnpackNullable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<short4>>


@dataclass
class UnpackNullableInt4(UnpackNullableBase):
    """UnpackNullable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<int4>>


@dataclass
class UnpackNullableLong4(UnpackNullableBase):
    """UnpackNullable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<long4>>


@dataclass
class UnpackNullableFloat4(UnpackNullableBase):
    """UnpackNullable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float4>>


@dataclass
class UnpackNullableDouble4(UnpackNullableBase):
    """UnpackNullable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double4>>


@dataclass
class UnpackNullableFloat_2x2(UnpackNullableBase):
    """UnpackNullable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float2x2>>


@dataclass
class UnpackNullableDouble_2x2(UnpackNullableBase):
    """UnpackNullable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double2x2>>


@dataclass
class UnpackNullableFloat_3x3(UnpackNullableBase):
    """UnpackNullable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float3x3>>


@dataclass
class UnpackNullableDouble_3x3(UnpackNullableBase):
    """UnpackNullable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double3x3>>


@dataclass
class UnpackNullableFloat_4x4(UnpackNullableBase):
    """UnpackNullable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<float4x4>>


@dataclass
class UnpackNullableDouble_4x4(UnpackNullableBase):
    """UnpackNullable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<double4x4>>


@dataclass
class UnpackNullableFloatQ(UnpackNullableBase):
    """UnpackNullable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<floatQ>>


@dataclass
class UnpackNullableDoubleQ(UnpackNullableBase):
    """UnpackNullable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<doubleQ>>


@dataclass
class UnpackNullableDateTime(UnpackNullableBase):
    """UnpackNullable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Private.CoreLib]System.DateTime>>


@dataclass
class UnpackNullableTimeSpan(UnpackNullableBase):
    """UnpackNullable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Private.CoreLib]System.TimeSpan>>


@dataclass
class UnpackNullableColor(UnpackNullableBase):
    """UnpackNullable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<color>>


@dataclass
class UnpackNullableColorX(UnpackNullableBase):
    """UnpackNullable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<colorX>>


@dataclass
class UnpackNullableShadowCastMode(UnpackNullableBase):
    """UnpackNullable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>>


@dataclass
class UnpackNullableLightType(UnpackNullableBase):
    """UnpackNullable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.LightType>>


@dataclass
class UnpackNullableSessionAccessLevel(UnpackNullableBase):
    """UnpackNullable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>>


@dataclass
class UnpackNullableKey(UnpackNullableBase):
    """UnpackNullable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.Key>>


@dataclass
class UnpackNullableHttpStatusCode(UnpackNullableBase):
    """UnpackNullable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[System.Net.Primitives]System.Net.HttpStatusCode>>


@dataclass
class UnpackNullableHeadOutputDevice(UnpackNullableBase):
    """UnpackNullable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>>


@dataclass
class UnpackNullableReflectionProbeClear(UnpackNullableBase):
    """UnpackNullable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>>


@dataclass
class UnpackNullableReflectionProbeType(UnpackNullableBase):
    """UnpackNullable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>>


@dataclass
class UnpackNullableReflectionProbeTimeSlicingMode(UnpackNullableBase):
    """UnpackNullable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>>


@dataclass
class UnpackNullableCameraClearMode(UnpackNullableBase):
    """UnpackNullable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.CameraClearMode>>


@dataclass
class UnpackNullableCameraPositioningMode(UnpackNullableBase):
    """UnpackNullable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.CameraPositioningMode>>


@dataclass
class UnpackNullableCameraProjection(UnpackNullableBase):
    """UnpackNullable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.CameraProjection>>


@dataclass
class UnpackNullableZWrite(UnpackNullableBase):
    """UnpackNullable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.ZWrite>>


@dataclass
class UnpackNullableZTest(UnpackNullableBase):
    """UnpackNullable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.ZTest>>


@dataclass
class UnpackNullableBlend(UnpackNullableBase):
    """UnpackNullable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.Blend>>


@dataclass
class UnpackNullableBlendMode(UnpackNullableBase):
    """UnpackNullable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.BlendMode>>


@dataclass
class UnpackNullableCulling(UnpackNullableBase):
    """UnpackNullable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<FrooxEngine.Culling>>


@dataclass
class UnpackNullableBodyNode(UnpackNullableBase):
    """UnpackNullable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.BodyNode>>


@dataclass
class UnpackNullableChirality(UnpackNullableBase):
    """UnpackNullable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<[Renderite.Shared]Renderite.Shared.Chirality>>


@dataclass
class UnpackNullableDummyEnum(UnpackNullableBase):
    """UnpackNullable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.UnpackNullable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "nullable": "Nullable",
    }

    nullable: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<[System.Private.CoreLib]System.Nullable<DummyEnum>>


# Type alias for any UnpackNullable variant
UnpackNullable = (
    UnpackNullableBool |
    UnpackNullableByte |
    UnpackNullableUshort |
    UnpackNullableUint |
    UnpackNullableUlong |
    UnpackNullableSbyte |
    UnpackNullableShort |
    UnpackNullableInt |
    UnpackNullableLong |
    UnpackNullableFloat |
    UnpackNullableDouble |
    UnpackNullableDecimal |
    UnpackNullableChar |
    UnpackNullableString |
    UnpackNullableUri |
    UnpackNullableBool2 |
    UnpackNullableByte2 |
    UnpackNullableUshort2 |
    UnpackNullableUint2 |
    UnpackNullableUlong2 |
    UnpackNullableSbyte2 |
    UnpackNullableShort2 |
    UnpackNullableInt2 |
    UnpackNullableLong2 |
    UnpackNullableFloat2 |
    UnpackNullableDouble2 |
    UnpackNullableBool3 |
    UnpackNullableByte3 |
    UnpackNullableUshort3 |
    UnpackNullableUint3 |
    UnpackNullableUlong3 |
    UnpackNullableSbyte3 |
    UnpackNullableShort3 |
    UnpackNullableInt3 |
    UnpackNullableLong3 |
    UnpackNullableFloat3 |
    UnpackNullableDouble3 |
    UnpackNullableBool4 |
    UnpackNullableByte4 |
    UnpackNullableUshort4 |
    UnpackNullableUint4 |
    UnpackNullableUlong4 |
    UnpackNullableSbyte4 |
    UnpackNullableShort4 |
    UnpackNullableInt4 |
    UnpackNullableLong4 |
    UnpackNullableFloat4 |
    UnpackNullableDouble4 |
    UnpackNullableFloat_2x2 |
    UnpackNullableDouble_2x2 |
    UnpackNullableFloat_3x3 |
    UnpackNullableDouble_3x3 |
    UnpackNullableFloat_4x4 |
    UnpackNullableDouble_4x4 |
    UnpackNullableFloatQ |
    UnpackNullableDoubleQ |
    UnpackNullableDateTime |
    UnpackNullableTimeSpan |
    UnpackNullableColor |
    UnpackNullableColorX |
    UnpackNullableShadowCastMode |
    UnpackNullableLightType |
    UnpackNullableSessionAccessLevel |
    UnpackNullableKey |
    UnpackNullableHttpStatusCode |
    UnpackNullableHeadOutputDevice |
    UnpackNullableReflectionProbeClear |
    UnpackNullableReflectionProbeType |
    UnpackNullableReflectionProbeTimeSlicingMode |
    UnpackNullableCameraClearMode |
    UnpackNullableCameraPositioningMode |
    UnpackNullableCameraProjection |
    UnpackNullableZWrite |
    UnpackNullableZTest |
    UnpackNullableBlend |
    UnpackNullableBlendMode |
    UnpackNullableCulling |
    UnpackNullableBodyNode |
    UnpackNullableChirality |
    UnpackNullableDummyEnum
)