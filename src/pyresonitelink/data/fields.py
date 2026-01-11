"""Field types for ResoniteLink data model.

This module contains Field and Array classes for all primitive types, mirroring
the auto-generated C# classes from the PrimitiveContainers.tt template.

Note: The C# BoxedValue and ValueType properties are marked [JsonIgnore] and
are not included in these dataclasses.
"""

from dataclasses import dataclass, field

import numpy as np

from .members import Member
from .primitives import (
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
# Standalone Primitive Fields
# =============================================================================


@dataclass
class FieldByte(Member):
    """Field containing a byte value."""

    value: np.uint8 = np.uint8(0)


@dataclass
class ArrayByte(Member):
    """Array of byte values."""

    values: list[np.uint8] = field(default_factory=list[np.uint8])


@dataclass
class FieldNullableByte(Member):
    """Field containing an optional byte value."""

    value: np.uint8 | None = None


@dataclass
class FieldUshort(Member):
    """Field containing an unsigned short value."""

    value: int = 0


@dataclass
class ArrayUshort(Member):
    """Array of unsigned short values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableUshort(Member):
    """Field containing an optional unsigned short value."""

    value: int | None = None


@dataclass
class FieldUint(Member):
    """Field containing an unsigned int value."""

    value: int = 0


@dataclass
class ArrayUint(Member):
    """Array of unsigned int values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableUint(Member):
    """Field containing an optional unsigned int value."""

    value: int | None = None


@dataclass
class FieldUlong(Member):
    """Field containing an unsigned long value."""

    value: int = 0


@dataclass
class ArrayUlong(Member):
    """Array of unsigned long values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableUlong(Member):
    """Field containing an optional unsigned long value."""

    value: int | None = None


@dataclass
class FieldSbyte(Member):
    """Field containing a signed byte value."""

    value: int = 0


@dataclass
class ArraySbyte(Member):
    """Array of signed byte values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableSbyte(Member):
    """Field containing an optional signed byte value."""

    value: int | None = None


@dataclass
class FieldShort(Member):
    """Field containing a short value."""

    value: int = 0


@dataclass
class ArrayShort(Member):
    """Array of short values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableShort(Member):
    """Field containing an optional short value."""

    value: int | None = None


@dataclass
class FieldInt(Member):
    """Field containing an int value."""

    value: int = 0


@dataclass
class ArrayInt(Member):
    """Array of int values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableInt(Member):
    """Field containing an optional int value."""

    value: int | None = None


@dataclass
class FieldLong(Member):
    """Field containing a long value."""

    value: int = 0


@dataclass
class ArrayLong(Member):
    """Array of long values."""

    values: list[int] = field(default_factory=list[int])


@dataclass
class FieldNullableLong(Member):
    """Field containing an optional long value."""

    value: int | None = None


@dataclass
class FieldFloat(Member):
    """Field containing a float value."""

    value: float = 0.0


@dataclass
class ArrayFloat(Member):
    """Array of float values."""

    values: list[float] = field(default_factory=list[float])


@dataclass
class FieldNullableFloat(Member):
    """Field containing an optional float value."""

    value: float | None = None


@dataclass
class FieldDouble(Member):
    """Field containing a double value."""

    value: float = 0.0


@dataclass
class ArrayDouble(Member):
    """Array of double values."""

    values: list[float] = field(default_factory=list[float])


@dataclass
class FieldNullableDouble(Member):
    """Field containing an optional double value."""

    value: float | None = None


@dataclass
class FieldDecimal(Member):
    """Field containing a decimal value."""

    value: float = 0.0


@dataclass
class ArrayDecimal(Member):
    """Array of decimal values."""

    values: list[float] = field(default_factory=list[float])


@dataclass
class FieldNullableDecimal(Member):
    """Field containing an optional decimal value."""

    value: float | None = None


@dataclass
class FieldBool(Member):
    """Field containing a boolean value."""

    value: bool = False


@dataclass
class ArrayBool(Member):
    """Array of boolean values."""

    values: list[bool] = field(default_factory=list[bool])


@dataclass
class FieldNullableBool(Member):
    """Field containing an optional boolean value."""

    value: bool | None = None


@dataclass
class FieldChar(Member):
    """Field containing a character value."""

    value: str = ""


@dataclass
class ArrayChar(Member):
    """Array of character values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldNullableChar(Member):
    """Field containing an optional character value."""

    value: str | None = None


@dataclass
class FieldString(Member):
    """Field containing a string value."""

    value: str | None = None


@dataclass
class ArrayString(Member):
    """Array of string values."""

    values: list[str] = field(default_factory=list[str])


@dataclass
class FieldUri(Member):
    """Field containing a URI value."""

    value: str | None = None


@dataclass
class ArrayUri(Member):
    """Array of URI values."""

    values: list[str] = field(default_factory=list[str])


# =============================================================================
# Color Fields
# =============================================================================


@dataclass
class FieldColor(Member):
    """Field containing a color value."""

    value: color | None = None


@dataclass
class ArrayColor(Member):
    """Array of color values."""

    values: list[color] = field(default_factory=list[color])


@dataclass
class FieldNullableColor(Member):
    """Field containing an optional color value."""

    value: color | None = None


@dataclass
class FieldColorX(Member):
    """Field containing a colorX value."""

    value: colorX | None = None


@dataclass
class ArrayColorX(Member):
    """Array of colorX values."""

    values: list[colorX] = field(default_factory=list[colorX])


@dataclass
class FieldNullableColorX(Member):
    """Field containing an optional colorX value."""

    value: colorX | None = None


@dataclass
class FieldColor32(Member):
    """Field containing a color32 value."""

    value: color32 | None = None


@dataclass
class ArrayColor32(Member):
    """Array of color32 values."""

    values: list[color32] = field(default_factory=list[color32])


@dataclass
class FieldNullableColor32(Member):
    """Field containing an optional color32 value."""

    value: color32 | None = None


# =============================================================================
# 2D Vector Fields
# =============================================================================


@dataclass
class FieldFloat2(Member):
    """Field containing a float2 value."""

    value: float2 | None = None


@dataclass
class ArrayFloat2(Member):
    """Array of float2 values."""

    values: list[float2] = field(default_factory=list[float2])


@dataclass
class FieldNullableFloat2(Member):
    """Field containing an optional float2 value."""

    value: float2 | None = None


@dataclass
class FieldDouble2(Member):
    """Field containing a double2 value."""

    value: double2 | None = None


@dataclass
class ArrayDouble2(Member):
    """Array of double2 values."""

    values: list[double2] = field(default_factory=list[double2])


@dataclass
class FieldNullableDouble2(Member):
    """Field containing an optional double2 value."""

    value: double2 | None = None


@dataclass
class FieldByte2(Member):
    """Field containing a byte2 value."""

    value: byte2 | None = None


@dataclass
class ArrayByte2(Member):
    """Array of byte2 values."""

    values: list[byte2] = field(default_factory=list[byte2])


@dataclass
class FieldNullableByte2(Member):
    """Field containing an optional byte2 value."""

    value: byte2 | None = None


@dataclass
class FieldUshort2(Member):
    """Field containing a ushort2 value."""

    value: ushort2 | None = None


@dataclass
class ArrayUshort2(Member):
    """Array of ushort2 values."""

    values: list[ushort2] = field(default_factory=list[ushort2])


@dataclass
class FieldNullableUshort2(Member):
    """Field containing an optional ushort2 value."""

    value: ushort2 | None = None


@dataclass
class FieldUint2(Member):
    """Field containing a uint2 value."""

    value: uint2 | None = None


@dataclass
class ArrayUint2(Member):
    """Array of uint2 values."""

    values: list[uint2] = field(default_factory=list[uint2])


@dataclass
class FieldNullableUint2(Member):
    """Field containing an optional uint2 value."""

    value: uint2 | None = None


@dataclass
class FieldUlong2(Member):
    """Field containing a ulong2 value."""

    value: ulong2 | None = None


@dataclass
class ArrayUlong2(Member):
    """Array of ulong2 values."""

    values: list[ulong2] = field(default_factory=list[ulong2])


@dataclass
class FieldNullableUlong2(Member):
    """Field containing an optional ulong2 value."""

    value: ulong2 | None = None


@dataclass
class FieldSbyte2(Member):
    """Field containing a sbyte2 value."""

    value: sbyte2 | None = None


@dataclass
class ArraySbyte2(Member):
    """Array of sbyte2 values."""

    values: list[sbyte2] = field(default_factory=list[sbyte2])


@dataclass
class FieldNullableSbyte2(Member):
    """Field containing an optional sbyte2 value."""

    value: sbyte2 | None = None


@dataclass
class FieldShort2(Member):
    """Field containing a short2 value."""

    value: short2 | None = None


@dataclass
class ArrayShort2(Member):
    """Array of short2 values."""

    values: list[short2] = field(default_factory=list[short2])


@dataclass
class FieldNullableShort2(Member):
    """Field containing an optional short2 value."""

    value: short2 | None = None


@dataclass
class FieldInt2(Member):
    """Field containing an int2 value."""

    value: int2 | None = None


@dataclass
class ArrayInt2(Member):
    """Array of int2 values."""

    values: list[int2] = field(default_factory=list[int2])


@dataclass
class FieldNullableInt2(Member):
    """Field containing an optional int2 value."""

    value: int2 | None = None


@dataclass
class FieldLong2(Member):
    """Field containing a long2 value."""

    value: long2 | None = None


@dataclass
class ArrayLong2(Member):
    """Array of long2 values."""

    values: list[long2] = field(default_factory=list[long2])


@dataclass
class FieldNullableLong2(Member):
    """Field containing an optional long2 value."""

    value: long2 | None = None


@dataclass
class FieldBool2(Member):
    """Field containing a bool2 value."""

    value: bool2 | None = None


@dataclass
class ArrayBool2(Member):
    """Array of bool2 values."""

    values: list[bool2] = field(default_factory=list[bool2])


@dataclass
class FieldNullableBool2(Member):
    """Field containing an optional bool2 value."""

    value: bool2 | None = None


# =============================================================================
# 3D Vector Fields
# =============================================================================


@dataclass
class FieldFloat3(Member):
    """Field containing a float3 value."""

    value: float3 | None = None


@dataclass
class ArrayFloat3(Member):
    """Array of float3 values."""

    values: list[float3] = field(default_factory=list[float3])


@dataclass
class FieldNullableFloat3(Member):
    """Field containing an optional float3 value."""

    value: float3 | None = None


@dataclass
class FieldDouble3(Member):
    """Field containing a double3 value."""

    value: double3 | None = None


@dataclass
class ArrayDouble3(Member):
    """Array of double3 values."""

    values: list[double3] = field(default_factory=list[double3])


@dataclass
class FieldNullableDouble3(Member):
    """Field containing an optional double3 value."""

    value: double3 | None = None


@dataclass
class FieldByte3(Member):
    """Field containing a byte3 value."""

    value: byte3 | None = None


@dataclass
class ArrayByte3(Member):
    """Array of byte3 values."""

    values: list[byte3] = field(default_factory=list[byte3])


@dataclass
class FieldNullableByte3(Member):
    """Field containing an optional byte3 value."""

    value: byte3 | None = None


@dataclass
class FieldUshort3(Member):
    """Field containing a ushort3 value."""

    value: ushort3 | None = None


@dataclass
class ArrayUshort3(Member):
    """Array of ushort3 values."""

    values: list[ushort3] = field(default_factory=list[ushort3])


@dataclass
class FieldNullableUshort3(Member):
    """Field containing an optional ushort3 value."""

    value: ushort3 | None = None


@dataclass
class FieldUint3(Member):
    """Field containing a uint3 value."""

    value: uint3 | None = None


@dataclass
class ArrayUint3(Member):
    """Array of uint3 values."""

    values: list[uint3] = field(default_factory=list[uint3])


@dataclass
class FieldNullableUint3(Member):
    """Field containing an optional uint3 value."""

    value: uint3 | None = None


@dataclass
class FieldUlong3(Member):
    """Field containing a ulong3 value."""

    value: ulong3 | None = None


@dataclass
class ArrayUlong3(Member):
    """Array of ulong3 values."""

    values: list[ulong3] = field(default_factory=list[ulong3])


@dataclass
class FieldNullableUlong3(Member):
    """Field containing an optional ulong3 value."""

    value: ulong3 | None = None


@dataclass
class FieldSbyte3(Member):
    """Field containing a sbyte3 value."""

    value: sbyte3 | None = None


@dataclass
class ArraySbyte3(Member):
    """Array of sbyte3 values."""

    values: list[sbyte3] = field(default_factory=list[sbyte3])


@dataclass
class FieldNullableSbyte3(Member):
    """Field containing an optional sbyte3 value."""

    value: sbyte3 | None = None


@dataclass
class FieldShort3(Member):
    """Field containing a short3 value."""

    value: short3 | None = None


@dataclass
class ArrayShort3(Member):
    """Array of short3 values."""

    values: list[short3] = field(default_factory=list[short3])


@dataclass
class FieldNullableShort3(Member):
    """Field containing an optional short3 value."""

    value: short3 | None = None


@dataclass
class FieldInt3(Member):
    """Field containing an int3 value."""

    value: int3 | None = None


@dataclass
class ArrayInt3(Member):
    """Array of int3 values."""

    values: list[int3] = field(default_factory=list[int3])


@dataclass
class FieldNullableInt3(Member):
    """Field containing an optional int3 value."""

    value: int3 | None = None


@dataclass
class FieldLong3(Member):
    """Field containing a long3 value."""

    value: long3 | None = None


@dataclass
class ArrayLong3(Member):
    """Array of long3 values."""

    values: list[long3] = field(default_factory=list[long3])


@dataclass
class FieldNullableLong3(Member):
    """Field containing an optional long3 value."""

    value: long3 | None = None


@dataclass
class FieldBool3(Member):
    """Field containing a bool3 value."""

    value: bool3 | None = None


@dataclass
class ArrayBool3(Member):
    """Array of bool3 values."""

    values: list[bool3] = field(default_factory=list[bool3])


@dataclass
class FieldNullableBool3(Member):
    """Field containing an optional bool3 value."""

    value: bool3 | None = None


# =============================================================================
# 4D Vector Fields
# =============================================================================


@dataclass
class FieldFloat4(Member):
    """Field containing a float4 value."""

    value: float4 | None = None


@dataclass
class ArrayFloat4(Member):
    """Array of float4 values."""

    values: list[float4] = field(default_factory=list[float4])


@dataclass
class FieldNullableFloat4(Member):
    """Field containing an optional float4 value."""

    value: float4 | None = None


@dataclass
class FieldDouble4(Member):
    """Field containing a double4 value."""

    value: double4 | None = None


@dataclass
class ArrayDouble4(Member):
    """Array of double4 values."""

    values: list[double4] = field(default_factory=list[double4])


@dataclass
class FieldNullableDouble4(Member):
    """Field containing an optional double4 value."""

    value: double4 | None = None


@dataclass
class FieldByte4(Member):
    """Field containing a byte4 value."""

    value: byte4 | None = None


@dataclass
class ArrayByte4(Member):
    """Array of byte4 values."""

    values: list[byte4] = field(default_factory=list[byte4])


@dataclass
class FieldNullableByte4(Member):
    """Field containing an optional byte4 value."""

    value: byte4 | None = None


@dataclass
class FieldUshort4(Member):
    """Field containing a ushort4 value."""

    value: ushort4 | None = None


@dataclass
class ArrayUshort4(Member):
    """Array of ushort4 values."""

    values: list[ushort4] = field(default_factory=list[ushort4])


@dataclass
class FieldNullableUshort4(Member):
    """Field containing an optional ushort4 value."""

    value: ushort4 | None = None


@dataclass
class FieldUint4(Member):
    """Field containing a uint4 value."""

    value: uint4 | None = None


@dataclass
class ArrayUint4(Member):
    """Array of uint4 values."""

    values: list[uint4] = field(default_factory=list[uint4])


@dataclass
class FieldNullableUint4(Member):
    """Field containing an optional uint4 value."""

    value: uint4 | None = None


@dataclass
class FieldUlong4(Member):
    """Field containing a ulong4 value."""

    value: ulong4 | None = None


@dataclass
class ArrayUlong4(Member):
    """Array of ulong4 values."""

    values: list[ulong4] = field(default_factory=list[ulong4])


@dataclass
class FieldNullableUlong4(Member):
    """Field containing an optional ulong4 value."""

    value: ulong4 | None = None


@dataclass
class FieldSbyte4(Member):
    """Field containing a sbyte4 value."""

    value: sbyte4 | None = None


@dataclass
class ArraySbyte4(Member):
    """Array of sbyte4 values."""

    values: list[sbyte4] = field(default_factory=list[sbyte4])


@dataclass
class FieldNullableSbyte4(Member):
    """Field containing an optional sbyte4 value."""

    value: sbyte4 | None = None


@dataclass
class FieldShort4(Member):
    """Field containing a short4 value."""

    value: short4 | None = None


@dataclass
class ArrayShort4(Member):
    """Array of short4 values."""

    values: list[short4] = field(default_factory=list[short4])


@dataclass
class FieldNullableShort4(Member):
    """Field containing an optional short4 value."""

    value: short4 | None = None


@dataclass
class FieldInt4(Member):
    """Field containing an int4 value."""

    value: int4 | None = None


@dataclass
class ArrayInt4(Member):
    """Array of int4 values."""

    values: list[int4] = field(default_factory=list[int4])


@dataclass
class FieldNullableInt4(Member):
    """Field containing an optional int4 value."""

    value: int4 | None = None


@dataclass
class FieldLong4(Member):
    """Field containing a long4 value."""

    value: long4 | None = None


@dataclass
class ArrayLong4(Member):
    """Array of long4 values."""

    values: list[long4] = field(default_factory=list[long4])


@dataclass
class FieldNullableLong4(Member):
    """Field containing an optional long4 value."""

    value: long4 | None = None


@dataclass
class FieldBool4(Member):
    """Field containing a bool4 value."""

    value: bool4 | None = None


@dataclass
class ArrayBool4(Member):
    """Array of bool4 values."""

    values: list[bool4] = field(default_factory=list[bool4])


@dataclass
class FieldNullableBool4(Member):
    """Field containing an optional bool4 value."""

    value: bool4 | None = None


# =============================================================================
# Quaternion Fields
# =============================================================================


@dataclass
class FieldFloatQ(Member):
    """Field containing a floatQ (quaternion) value."""

    value: floatQ | None = None


@dataclass
class ArrayFloatQ(Member):
    """Array of floatQ values."""

    values: list[floatQ] = field(default_factory=list[floatQ])


@dataclass
class FieldNullableFloatQ(Member):
    """Field containing an optional floatQ value."""

    value: floatQ | None = None


@dataclass
class FieldDoubleQ(Member):
    """Field containing a doubleQ (quaternion) value."""

    value: doubleQ | None = None


@dataclass
class ArrayDoubleQ(Member):
    """Array of doubleQ values."""

    values: list[doubleQ] = field(default_factory=list[doubleQ])


@dataclass
class FieldNullableDoubleQ(Member):
    """Field containing an optional doubleQ value."""

    value: doubleQ | None = None


# =============================================================================
# Matrix Fields
# =============================================================================


@dataclass
class FieldFloat2x2(Member):
    """Field containing a float2x2 matrix value."""

    value: float2x2 | None = None


@dataclass
class ArrayFloat2x2(Member):
    """Array of float2x2 values."""

    values: list[float2x2] = field(default_factory=list[float2x2])


@dataclass
class FieldNullableFloat2x2(Member):
    """Field containing an optional float2x2 value."""

    value: float2x2 | None = None


@dataclass
class FieldDouble2x2(Member):
    """Field containing a double2x2 matrix value."""

    value: double2x2 | None = None


@dataclass
class ArrayDouble2x2(Member):
    """Array of double2x2 values."""

    values: list[double2x2] = field(default_factory=list[double2x2])


@dataclass
class FieldNullableDouble2x2(Member):
    """Field containing an optional double2x2 value."""

    value: double2x2 | None = None


@dataclass
class FieldFloat3x3(Member):
    """Field containing a float3x3 matrix value."""

    value: float3x3 | None = None


@dataclass
class ArrayFloat3x3(Member):
    """Array of float3x3 values."""

    values: list[float3x3] = field(default_factory=list[float3x3])


@dataclass
class FieldNullableFloat3x3(Member):
    """Field containing an optional float3x3 value."""

    value: float3x3 | None = None


@dataclass
class FieldDouble3x3(Member):
    """Field containing a double3x3 matrix value."""

    value: double3x3 | None = None


@dataclass
class ArrayDouble3x3(Member):
    """Array of double3x3 values."""

    values: list[double3x3] = field(default_factory=list[double3x3])


@dataclass
class FieldNullableDouble3x3(Member):
    """Field containing an optional double3x3 value."""

    value: double3x3 | None = None


@dataclass
class FieldFloat4x4(Member):
    """Field containing a float4x4 matrix value."""

    value: float4x4 | None = None


@dataclass
class ArrayFloat4x4(Member):
    """Array of float4x4 values."""

    values: list[float4x4] = field(default_factory=list[float4x4])


@dataclass
class FieldNullableFloat4x4(Member):
    """Field containing an optional float4x4 value."""

    value: float4x4 | None = None


@dataclass
class FieldDouble4x4(Member):
    """Field containing a double4x4 matrix value."""

    value: double4x4 | None = None


@dataclass
class ArrayDouble4x4(Member):
    """Array of double4x4 values."""

    values: list[double4x4] = field(default_factory=list[double4x4])


@dataclass
class FieldNullableDouble4x4(Member):
    """Field containing an optional double4x4 value."""

    value: double4x4 | None = None
