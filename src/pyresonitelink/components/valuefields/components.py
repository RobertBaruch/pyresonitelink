"""Classes representing ValueField<type> components."""

import numpy as np

from .. import base
from ...data.primitives import (
    bool2,
    bool3,
    bool4,
    byte2,
    byte3,
    byte4,
    color,
    color32,
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


# =============================================================================
# Standalone Primitive Value Fields
# =============================================================================


class Bool(base.Component):
    """ValueField<bool> component."""

    value: bool


class Byte(base.Component):
    """ValueField<byte> component."""

    value: np.uint8


class UShort(base.Component):
    """ValueField<ushort> component."""

    value: np.uint16


class UInt(base.Component):
    """ValueField<uint> component."""

    value: np.uint32


class ULong(base.Component):
    """ValueField<ulong> component."""

    value: np.uint64


class SByte(base.Component):
    """ValueField<sbyte> component."""

    value: np.int8


class Short(base.Component):
    """ValueField<short> component."""

    value: np.int16


class Int(base.Component):
    """ValueField<int> component."""

    value: np.int32


class Long(base.Component):
    """ValueField<long> component."""

    value: np.int64


class Float(base.Component):
    """ValueField<float> component."""

    value: np.float32


class Double(base.Component):
    """ValueField<double> component."""

    value: np.float64


class Decimal(base.Component):
    """ValueField<decimal> component."""

    value: float


class Char(base.Component):
    """ValueField<char> component."""

    value: str


class String(base.Component):
    """ValueField<string> component."""

    value: str | None


class Uri(base.Component):
    """ValueField<Uri> component."""

    value: str | None


# =============================================================================
# Color Value Fields
# =============================================================================


class Color(base.Component):
    """ValueField<color> component."""

    value: color | None


class ColorX(base.Component):
    """ValueField<colorX> component."""

    value: colorX | None


class Color32(base.Component):
    """ValueField<color32> component."""

    value: color32 | None


# =============================================================================
# 2D Vector Value Fields
# =============================================================================


class Float2(base.Component):
    """ValueField<float2> component."""

    value: float2 | None


class Double2(base.Component):
    """ValueField<double2> component."""

    value: double2 | None


class Byte2(base.Component):
    """ValueField<byte2> component."""

    value: byte2 | None


class UShort2(base.Component):
    """ValueField<ushort2> component."""

    value: ushort2 | None


class UInt2(base.Component):
    """ValueField<uint2> component."""

    value: uint2 | None


class ULong2(base.Component):
    """ValueField<ulong2> component."""

    value: ulong2 | None


class SByte2(base.Component):
    """ValueField<sbyte2> component."""

    value: sbyte2 | None


class Short2(base.Component):
    """ValueField<short2> component."""

    value: short2 | None


class Int2(base.Component):
    """ValueField<int2> component."""

    value: int2 | None


class Long2(base.Component):
    """ValueField<long2> component."""

    value: long2 | None


class Bool2(base.Component):
    """ValueField<bool2> component."""

    value: bool2 | None


# =============================================================================
# 3D Vector Value Fields
# =============================================================================


class Float3(base.Component):
    """ValueField<float3> component."""

    value: float3 | None


class Double3(base.Component):
    """ValueField<double3> component."""

    value: double3 | None


class Byte3(base.Component):
    """ValueField<byte3> component."""

    value: byte3 | None


class UShort3(base.Component):
    """ValueField<ushort3> component."""

    value: ushort3 | None


class UInt3(base.Component):
    """ValueField<uint3> component."""

    value: uint3 | None


class ULong3(base.Component):
    """ValueField<ulong3> component."""

    value: ulong3 | None


class SByte3(base.Component):
    """ValueField<sbyte3> component."""

    value: sbyte3 | None


class Short3(base.Component):
    """ValueField<short3> component."""

    value: short3 | None


class Int3(base.Component):
    """ValueField<int3> component."""

    value: int3 | None


class Long3(base.Component):
    """ValueField<long3> component."""

    value: long3 | None


class Bool3(base.Component):
    """ValueField<bool3> component."""

    value: bool3 | None


# =============================================================================
# 4D Vector Value Fields
# =============================================================================


class Float4(base.Component):
    """ValueField<float4> component."""

    value: float4 | None


class Double4(base.Component):
    """ValueField<double4> component."""

    value: double4 | None


class Byte4(base.Component):
    """ValueField<byte4> component."""

    value: byte4 | None


class UShort4(base.Component):
    """ValueField<ushort4> component."""

    value: ushort4 | None


class UInt4(base.Component):
    """ValueField<uint4> component."""

    value: uint4 | None


class ULong4(base.Component):
    """ValueField<ulong4> component."""

    value: ulong4 | None


class SByte4(base.Component):
    """ValueField<sbyte4> component."""

    value: sbyte4 | None


class Short4(base.Component):
    """ValueField<short4> component."""

    value: short4 | None


class Int4(base.Component):
    """ValueField<int4> component."""

    value: int4 | None


class Long4(base.Component):
    """ValueField<long4> component."""

    value: long4 | None


class Bool4(base.Component):
    """ValueField<bool4> component."""

    value: bool4 | None


# =============================================================================
# Quaternion Value Fields
# =============================================================================


class FloatQ(base.Component):
    """ValueField<floatQ> component."""

    value: floatQ | None


class DoubleQ(base.Component):
    """ValueField<doubleQ> component."""

    value: doubleQ | None


# =============================================================================
# 2x2 Matrix Value Fields
# =============================================================================


class Float2x2(base.Component):
    """ValueField<float2x2> component."""

    value: float2x2 | None


class Double2x2(base.Component):
    """ValueField<double2x2> component."""

    value: double2x2 | None


# =============================================================================
# 3x3 Matrix Value Fields
# =============================================================================


class Float3x3(base.Component):
    """ValueField<float3x3> component."""

    value: float3x3 | None


class Double3x3(base.Component):
    """ValueField<double3x3> component."""

    value: double3x3 | None


# =============================================================================
# 4x4 Matrix Value Fields
# =============================================================================


class Float4x4(base.Component):
    """ValueField<float4x4> component."""

    value: float4x4 | None


class Double4x4(base.Component):
    """ValueField<double4x4> component."""

    value: double4x4 | None
