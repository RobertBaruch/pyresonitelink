"""Classes representing ValueField<type> components."""

from __future__ import annotations  # For forward references

from dataclasses import dataclass
from typing import Any, cast

import numpy as np

from pyresonitelink.components import base
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.responses import ComponentData
from pyresonitelink.data.primitives import (
    bool2,
    bool3,
    bool4,
    byte2,
    byte3,
    byte4,
    color,
    colorX,
    double2,
    double2x2,
    double3,
    double3x3,
    double4,
    double4x4,
    doubleQ,
    float2,
    float2x2,
    float3,
    float3x3,
    float4,
    float4x4,
    floatQ,
    int2,
    int3,
    int4,
    long2,
    long3,
    long4,
    sbyte2,
    sbyte3,
    sbyte4,
    short2,
    short3,
    short4,
    uint2,
    uint3,
    uint4,
    ulong2,
    ulong3,
    ulong4,
    ushort2,
    ushort3,
    ushort4,
)


@dataclass
class ValueFieldComponent(base.Component):
    """Base class for ValueField<> components."""

    value: Any = None

    @staticmethod
    def unmarshal(data: ComponentData) -> ValueFieldComponent:
        assert data.data is not None
        assert data.data.componentType is not None
        if not data.data.componentType.startswith("[FrooxEngine]FrooxEngine.ValueField<"):
            raise ValueError(f"Invalid component type: {data.data.componentType}")

        # Lazy import to avoid circular imports
        from pyresonitelink.components import NAME_TO_CLASS

        full_type_name = data.data.componentType
        if full_type_name not in NAME_TO_CLASS:
            raise NotImplementedError(f"Unsupported ValueField type: {full_type_name}")

        component_class = cast(
            type["ValueFieldComponent"], NAME_TO_CLASS[full_type_name]
        )

        # Extract common fields from members
        assert data.data.id is not None
        members = data.data.members

        # Get persistent field (FieldBool)
        persistent_member = members.get("persistent")
        persistent: bool = False
        if isinstance(persistent_member, FieldBool):
            persistent = persistent_member.value

        # Get UpdateOrder field (FieldInt)
        update_order_member = members.get("UpdateOrder")
        update_order: np.int32 = np.int32(0)
        if isinstance(update_order_member, FieldInt):
            update_order = update_order_member.value

        # Get Enabled field (FieldBool)
        enabled_member = members.get("Enabled")
        enabled: bool = False
        if isinstance(enabled_member, FieldBool):
            enabled = enabled_member.value

        # Get Value field (type varies based on component type)
        value_member = members.get("Value")
        value: Any = None
        if value_member is not None and hasattr(value_member, "value"):
            value = getattr(value_member, "value")

        return component_class(
            id=data.data.id,
            persistent=persistent,
            update_order=update_order,
            enabled=enabled,
            value=value,
        )


# =============================================================================
# Standalone Primitive Value Fields
# =============================================================================

@dataclass
class DateTime(ValueFieldComponent):
    """ValueField<DateTime> component."""

    value: str = "0001-01-01T00:00:00"


@dataclass
class TimeSpan(ValueFieldComponent):
    """ValueField<TimeSpan> component."""

    value: str = "00:00:00"


@dataclass
class Bool(ValueFieldComponent):
    """ValueField<bool> component."""

    value: bool = False


@dataclass
class Byte(ValueFieldComponent):
    """ValueField<byte> component."""

    value: np.uint8 = np.uint8(0)


@dataclass
class UShort(ValueFieldComponent):
    """ValueField<ushort> component."""

    value: np.uint16 = np.uint16(0)


@dataclass
class UInt(ValueFieldComponent):
    """ValueField<uint> component."""

    value: np.uint32 = np.uint32(0)


@dataclass
class ULong(ValueFieldComponent):
    """ValueField<ulong> component."""

    value: np.uint64 = np.uint64(0)


@dataclass
class SByte(ValueFieldComponent):
    """ValueField<sbyte> component."""

    value: np.int8 = np.int8(0)


@dataclass
class Short(ValueFieldComponent):
    """ValueField<short> component."""

    value: np.int16 = np.int16(0)


@dataclass
class Int(ValueFieldComponent):
    """ValueField<int> component."""

    value: np.int32 = np.int32(0)


@dataclass
class Long(ValueFieldComponent):
    """ValueField<long> component."""

    value: np.int64 = np.int64(0)


@dataclass
class Float(ValueFieldComponent):
    """ValueField<float> component."""

    value: np.float32 = np.float32(0.0)


@dataclass
class Double(ValueFieldComponent):
    """ValueField<double> component."""

    value: np.float64 = np.float64(0.0)


@dataclass
class Decimal(ValueFieldComponent):
    """ValueField<decimal> component."""

    value: float = 0.0


@dataclass
class Char(ValueFieldComponent):
    """ValueField<char> component."""

    value: str = ""


@dataclass
class String(ValueFieldComponent):
    """ValueField<string> component."""

    value: str | None = None


@dataclass
class Uri(ValueFieldComponent):
    """ValueField<Uri> component."""

    value: str | None = None


# =============================================================================
# Color Value Fields
# =============================================================================


@dataclass
class Color(ValueFieldComponent):
    """ValueField<color> component."""

    value: color | None = None


@dataclass
class ColorX(ValueFieldComponent):
    """ValueField<colorX> component."""

    value: colorX | None = None


# =============================================================================
# 2D Vector Value Fields
# =============================================================================


@dataclass
class Float2(ValueFieldComponent):
    """ValueField<float2> component."""

    value: float2 | None = None


@dataclass
class Double2(ValueFieldComponent):
    """ValueField<double2> component."""

    value: double2 | None = None


@dataclass
class Byte2(ValueFieldComponent):
    """ValueField<byte2> component."""

    value: byte2 | None = None


@dataclass
class UShort2(ValueFieldComponent):
    """ValueField<ushort2> component."""

    value: ushort2 | None = None


@dataclass
class UInt2(ValueFieldComponent):
    """ValueField<uint2> component."""

    value: uint2 | None = None


@dataclass
class ULong2(ValueFieldComponent):
    """ValueField<ulong2> component."""

    value: ulong2 | None = None


@dataclass
class SByte2(ValueFieldComponent):
    """ValueField<sbyte2> component."""

    value: sbyte2 | None = None


@dataclass
class Short2(ValueFieldComponent):
    """ValueField<short2> component."""

    value: short2 | None = None


@dataclass
class Int2(ValueFieldComponent):
    """ValueField<int2> component."""

    value: int2 | None = None


@dataclass
class Long2(ValueFieldComponent):
    """ValueField<long2> component."""

    value: long2 | None = None


@dataclass
class Bool2(ValueFieldComponent):
    """ValueField<bool2> component."""

    value: bool2 | None = None


# =============================================================================
# 3D Vector Value Fields
# =============================================================================


@dataclass
class Float3(ValueFieldComponent):
    """ValueField<float3> component."""

    value: float3 | None = None


@dataclass
class Double3(ValueFieldComponent):
    """ValueField<double3> component."""

    value: double3 | None = None


@dataclass
class Byte3(ValueFieldComponent):
    """ValueField<byte3> component."""

    value: byte3 | None = None


@dataclass
class UShort3(ValueFieldComponent):
    """ValueField<ushort3> component."""

    value: ushort3 | None = None


@dataclass
class UInt3(ValueFieldComponent):
    """ValueField<uint3> component."""

    value: uint3 | None = None


@dataclass
class ULong3(ValueFieldComponent):
    """ValueField<ulong3> component."""

    value: ulong3 | None = None


@dataclass
class SByte3(ValueFieldComponent):
    """ValueField<sbyte3> component."""

    value: sbyte3 | None = None


@dataclass
class Short3(ValueFieldComponent):
    """ValueField<short3> component."""

    value: short3 | None = None


@dataclass
class Int3(ValueFieldComponent):
    """ValueField<int3> component."""

    value: int3 | None = None


@dataclass
class Long3(ValueFieldComponent):
    """ValueField<long3> component."""

    value: long3 | None = None


@dataclass
class Bool3(ValueFieldComponent):
    """ValueField<bool3> component."""

    value: bool3 | None = None


# =============================================================================
# 4D Vector Value Fields
# =============================================================================


@dataclass
class Float4(ValueFieldComponent):
    """ValueField<float4> component."""

    value: float4 | None = None


@dataclass
class Double4(ValueFieldComponent):
    """ValueField<double4> component."""

    value: double4 | None = None


@dataclass
class Byte4(ValueFieldComponent):
    """ValueField<byte4> component."""

    value: byte4 | None = None


@dataclass
class UShort4(ValueFieldComponent):
    """ValueField<ushort4> component."""

    value: ushort4 | None = None


@dataclass
class UInt4(ValueFieldComponent):
    """ValueField<uint4> component."""

    value: uint4 | None = None


@dataclass
class ULong4(ValueFieldComponent):
    """ValueField<ulong4> component."""

    value: ulong4 | None = None


@dataclass
class SByte4(ValueFieldComponent):
    """ValueField<sbyte4> component."""

    value: sbyte4 | None = None


@dataclass
class Short4(ValueFieldComponent):
    """ValueField<short4> component."""

    value: short4 | None = None


@dataclass
class Int4(ValueFieldComponent):
    """ValueField<int4> component."""

    value: int4 | None = None


@dataclass
class Long4(ValueFieldComponent):
    """ValueField<long4> component."""

    value: long4 | None = None


@dataclass
class Bool4(ValueFieldComponent):
    """ValueField<bool4> component."""

    value: bool4 | None = None


# =============================================================================
# Quaternion Value Fields
# =============================================================================


@dataclass
class FloatQ(ValueFieldComponent):
    """ValueField<floatQ> component."""

    value: floatQ | None = None


@dataclass
class DoubleQ(ValueFieldComponent):
    """ValueField<doubleQ> component."""

    value: doubleQ | None = None


# =============================================================================
# 2x2 Matrix Value Fields
# =============================================================================


@dataclass
class Float2x2(ValueFieldComponent):
    """ValueField<float2x2> component."""

    value: float2x2 | None = None


@dataclass
class Double2x2(ValueFieldComponent):
    """ValueField<double2x2> component."""

    value: double2x2 | None = None


# =============================================================================
# 3x3 Matrix Value Fields
# =============================================================================


@dataclass
class Float3x3(ValueFieldComponent):
    """ValueField<float3x3> component."""

    value: float3x3 | None = None


@dataclass
class Double3x3(ValueFieldComponent):
    """ValueField<double3x3> component."""

    value: double3x3 | None = None


# =============================================================================
# 4x4 Matrix Value Fields
# =============================================================================


@dataclass
class Float4x4(ValueFieldComponent):
    """ValueField<float4x4> component."""

    value: float4x4 | None = None


@dataclass
class Double4x4(ValueFieldComponent):
    """ValueField<double4x4> component."""

    value: double4x4 | None = None
