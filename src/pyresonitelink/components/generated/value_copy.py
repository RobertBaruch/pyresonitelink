"""Generated component: ValueCopy.

Auto-generated from FrooxEngine.ValueCopy_1.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueCopyBase(GeneratedComponent):
    """Base class for ValueCopy<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.ValueCopy_1.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class ValueCopyBool(ValueCopyBase):
    """ValueCopy<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<bool>
    target: Reference | None = None  # -> FrooxEngine.IField<bool>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyByte(ValueCopyBase):
    """ValueCopy<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<byte>
    target: Reference | None = None  # -> FrooxEngine.IField<byte>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUshort(ValueCopyBase):
    """ValueCopy<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ushort>
    target: Reference | None = None  # -> FrooxEngine.IField<ushort>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUint(ValueCopyBase):
    """ValueCopy<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<uint>
    target: Reference | None = None  # -> FrooxEngine.IField<uint>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUlong(ValueCopyBase):
    """ValueCopy<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ulong>
    target: Reference | None = None  # -> FrooxEngine.IField<ulong>
    write_back: FieldBool | None = None


@dataclass
class ValueCopySbyte(ValueCopyBase):
    """ValueCopy<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<sbyte>
    target: Reference | None = None  # -> FrooxEngine.IField<sbyte>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyShort(ValueCopyBase):
    """ValueCopy<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<short>
    target: Reference | None = None  # -> FrooxEngine.IField<short>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyInt(ValueCopyBase):
    """ValueCopy<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<int>
    target: Reference | None = None  # -> FrooxEngine.IField<int>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyLong(ValueCopyBase):
    """ValueCopy<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<long>
    target: Reference | None = None  # -> FrooxEngine.IField<long>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat(ValueCopyBase):
    """ValueCopy<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float>
    target: Reference | None = None  # -> FrooxEngine.IField<float>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble(ValueCopyBase):
    """ValueCopy<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double>
    target: Reference | None = None  # -> FrooxEngine.IField<double>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDecimal(ValueCopyBase):
    """ValueCopy<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<decimal>
    target: Reference | None = None  # -> FrooxEngine.IField<decimal>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyChar(ValueCopyBase):
    """ValueCopy<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<char>
    target: Reference | None = None  # -> FrooxEngine.IField<char>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyString(ValueCopyBase):
    """ValueCopy<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<string>
    target: Reference | None = None  # -> FrooxEngine.IField<string>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUri(ValueCopyBase):
    """ValueCopy<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<Uri>
    target: Reference | None = None  # -> FrooxEngine.IField<Uri>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyBool2(ValueCopyBase):
    """ValueCopy<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<bool2>
    target: Reference | None = None  # -> FrooxEngine.IField<bool2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyByte2(ValueCopyBase):
    """ValueCopy<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<byte2>
    target: Reference | None = None  # -> FrooxEngine.IField<byte2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUshort2(ValueCopyBase):
    """ValueCopy<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ushort2>
    target: Reference | None = None  # -> FrooxEngine.IField<ushort2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUint2(ValueCopyBase):
    """ValueCopy<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<uint2>
    target: Reference | None = None  # -> FrooxEngine.IField<uint2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUlong2(ValueCopyBase):
    """ValueCopy<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ulong2>
    target: Reference | None = None  # -> FrooxEngine.IField<ulong2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopySbyte2(ValueCopyBase):
    """ValueCopy<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<sbyte2>
    target: Reference | None = None  # -> FrooxEngine.IField<sbyte2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyShort2(ValueCopyBase):
    """ValueCopy<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<short2>
    target: Reference | None = None  # -> FrooxEngine.IField<short2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyInt2(ValueCopyBase):
    """ValueCopy<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<int2>
    target: Reference | None = None  # -> FrooxEngine.IField<int2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyLong2(ValueCopyBase):
    """ValueCopy<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<long2>
    target: Reference | None = None  # -> FrooxEngine.IField<long2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat2(ValueCopyBase):
    """ValueCopy<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float2>
    target: Reference | None = None  # -> FrooxEngine.IField<float2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble2(ValueCopyBase):
    """ValueCopy<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double2>
    target: Reference | None = None  # -> FrooxEngine.IField<double2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyBool3(ValueCopyBase):
    """ValueCopy<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<bool3>
    target: Reference | None = None  # -> FrooxEngine.IField<bool3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyByte3(ValueCopyBase):
    """ValueCopy<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<byte3>
    target: Reference | None = None  # -> FrooxEngine.IField<byte3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUshort3(ValueCopyBase):
    """ValueCopy<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ushort3>
    target: Reference | None = None  # -> FrooxEngine.IField<ushort3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUint3(ValueCopyBase):
    """ValueCopy<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<uint3>
    target: Reference | None = None  # -> FrooxEngine.IField<uint3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUlong3(ValueCopyBase):
    """ValueCopy<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ulong3>
    target: Reference | None = None  # -> FrooxEngine.IField<ulong3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopySbyte3(ValueCopyBase):
    """ValueCopy<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<sbyte3>
    target: Reference | None = None  # -> FrooxEngine.IField<sbyte3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyShort3(ValueCopyBase):
    """ValueCopy<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<short3>
    target: Reference | None = None  # -> FrooxEngine.IField<short3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyInt3(ValueCopyBase):
    """ValueCopy<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<int3>
    target: Reference | None = None  # -> FrooxEngine.IField<int3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyLong3(ValueCopyBase):
    """ValueCopy<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<long3>
    target: Reference | None = None  # -> FrooxEngine.IField<long3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat3(ValueCopyBase):
    """ValueCopy<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float3>
    target: Reference | None = None  # -> FrooxEngine.IField<float3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble3(ValueCopyBase):
    """ValueCopy<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double3>
    target: Reference | None = None  # -> FrooxEngine.IField<double3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyBool4(ValueCopyBase):
    """ValueCopy<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<bool4>
    target: Reference | None = None  # -> FrooxEngine.IField<bool4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyByte4(ValueCopyBase):
    """ValueCopy<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<byte4>
    target: Reference | None = None  # -> FrooxEngine.IField<byte4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUshort4(ValueCopyBase):
    """ValueCopy<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ushort4>
    target: Reference | None = None  # -> FrooxEngine.IField<ushort4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUint4(ValueCopyBase):
    """ValueCopy<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<uint4>
    target: Reference | None = None  # -> FrooxEngine.IField<uint4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyUlong4(ValueCopyBase):
    """ValueCopy<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<ulong4>
    target: Reference | None = None  # -> FrooxEngine.IField<ulong4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopySbyte4(ValueCopyBase):
    """ValueCopy<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<sbyte4>
    target: Reference | None = None  # -> FrooxEngine.IField<sbyte4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyShort4(ValueCopyBase):
    """ValueCopy<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<short4>
    target: Reference | None = None  # -> FrooxEngine.IField<short4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyInt4(ValueCopyBase):
    """ValueCopy<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<int4>
    target: Reference | None = None  # -> FrooxEngine.IField<int4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyLong4(ValueCopyBase):
    """ValueCopy<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<long4>
    target: Reference | None = None  # -> FrooxEngine.IField<long4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat4(ValueCopyBase):
    """ValueCopy<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float4>
    target: Reference | None = None  # -> FrooxEngine.IField<float4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble4(ValueCopyBase):
    """ValueCopy<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double4>
    target: Reference | None = None  # -> FrooxEngine.IField<double4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat_2x2(ValueCopyBase):
    """ValueCopy<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float2x2>
    target: Reference | None = None  # -> FrooxEngine.IField<float2x2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble_2x2(ValueCopyBase):
    """ValueCopy<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double2x2>
    target: Reference | None = None  # -> FrooxEngine.IField<double2x2>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat_3x3(ValueCopyBase):
    """ValueCopy<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float3x3>
    target: Reference | None = None  # -> FrooxEngine.IField<float3x3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble_3x3(ValueCopyBase):
    """ValueCopy<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double3x3>
    target: Reference | None = None  # -> FrooxEngine.IField<double3x3>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloat_4x4(ValueCopyBase):
    """ValueCopy<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<float4x4>
    target: Reference | None = None  # -> FrooxEngine.IField<float4x4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDouble_4x4(ValueCopyBase):
    """ValueCopy<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<double4x4>
    target: Reference | None = None  # -> FrooxEngine.IField<double4x4>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyFloatQ(ValueCopyBase):
    """ValueCopy<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<floatQ>
    target: Reference | None = None  # -> FrooxEngine.IField<floatQ>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDoubleQ(ValueCopyBase):
    """ValueCopy<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<doubleQ>
    target: Reference | None = None  # -> FrooxEngine.IField<doubleQ>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyDateTime(ValueCopyBase):
    """ValueCopy<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.DateTime>
    target: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.DateTime>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyTimeSpan(ValueCopyBase):
    """ValueCopy<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.TimeSpan>
    target: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.TimeSpan>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyColor(ValueCopyBase):
    """ValueCopy<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<color>
    target: Reference | None = None  # -> FrooxEngine.IField<color>
    write_back: FieldBool | None = None


@dataclass
class ValueCopyColorX(ValueCopyBase):
    """ValueCopy<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.ValueCopy<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "source": "Source",
        "target": "Target",
        "write_back": "WriteBack",
    }

    source: Reference | None = None  # -> FrooxEngine.IField<colorX>
    target: Reference | None = None  # -> FrooxEngine.IField<colorX>
    write_back: FieldBool | None = None


# Type alias for any ValueCopy variant
ValueCopy = (
    ValueCopyBool |
    ValueCopyByte |
    ValueCopyUshort |
    ValueCopyUint |
    ValueCopyUlong |
    ValueCopySbyte |
    ValueCopyShort |
    ValueCopyInt |
    ValueCopyLong |
    ValueCopyFloat |
    ValueCopyDouble |
    ValueCopyDecimal |
    ValueCopyChar |
    ValueCopyString |
    ValueCopyUri |
    ValueCopyBool2 |
    ValueCopyByte2 |
    ValueCopyUshort2 |
    ValueCopyUint2 |
    ValueCopyUlong2 |
    ValueCopySbyte2 |
    ValueCopyShort2 |
    ValueCopyInt2 |
    ValueCopyLong2 |
    ValueCopyFloat2 |
    ValueCopyDouble2 |
    ValueCopyBool3 |
    ValueCopyByte3 |
    ValueCopyUshort3 |
    ValueCopyUint3 |
    ValueCopyUlong3 |
    ValueCopySbyte3 |
    ValueCopyShort3 |
    ValueCopyInt3 |
    ValueCopyLong3 |
    ValueCopyFloat3 |
    ValueCopyDouble3 |
    ValueCopyBool4 |
    ValueCopyByte4 |
    ValueCopyUshort4 |
    ValueCopyUint4 |
    ValueCopyUlong4 |
    ValueCopySbyte4 |
    ValueCopyShort4 |
    ValueCopyInt4 |
    ValueCopyLong4 |
    ValueCopyFloat4 |
    ValueCopyDouble4 |
    ValueCopyFloat_2x2 |
    ValueCopyDouble_2x2 |
    ValueCopyFloat_3x3 |
    ValueCopyDouble_3x3 |
    ValueCopyFloat_4x4 |
    ValueCopyDouble_4x4 |
    ValueCopyFloatQ |
    ValueCopyDoubleQ |
    ValueCopyDateTime |
    ValueCopyTimeSpan |
    ValueCopyColor |
    ValueCopyColorX
)