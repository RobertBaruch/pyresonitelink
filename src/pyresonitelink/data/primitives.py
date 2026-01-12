"""Primitive types for ResoniteLink data model.

This module contains vector, quaternion, matrix, and color types that mirror
the C# structs used in ResoniteLink.
"""

# pylint: disable=invalid-name

from dataclasses import dataclass

import numpy as np


# =============================================================================
# Color Types
# =============================================================================


@dataclass
class color:
    """RGBA color with float components."""

    r: np.float32 = np.float32(0)
    g: np.float32 = np.float32(0)
    b: np.float32 = np.float32(0)
    a: np.float32 = np.float32(1)


@dataclass
class colorX:
    """RGBA color with float components and color profile."""

    r: np.float32 = np.float32(0)
    g: np.float32 = np.float32(0)
    b: np.float32 = np.float32(0)
    a: np.float32 = np.float32(1)
    profile: str = ""


@dataclass
class color32:
    """RGBA color with byte components (0-255)."""

    r: np.uint8 = np.uint8(0)
    g: np.uint8 = np.uint8(0)
    b: np.uint8 = np.uint8(0)
    a: np.uint8 = np.uint8(255)


# =============================================================================
# 2D Vector Types
# =============================================================================


@dataclass
class float2:
    """2D vector with float components."""

    x: np.float32 = np.float32(0.0)
    y: np.float32 = np.float32(0.0)


@dataclass
class double2:
    """2D vector with double components."""

    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)


@dataclass
class byte2:
    """2D vector with byte components."""

    x: np.uint8 = np.uint8(0)
    y: np.uint8 = np.uint8(0)


@dataclass
class ushort2:
    """2D vector with unsigned short components."""

    x: np.uint16 = np.uint16(0)
    y: np.uint16 = np.uint16(0)


@dataclass
class uint2:
    """2D vector with unsigned int components."""

    x: np.uint32 = np.uint32(0)
    y: np.uint32 = np.uint32(0)


@dataclass
class ulong2:
    """2D vector with unsigned long components."""

    x: np.uint64 = np.uint64(0)
    y: np.uint64 = np.uint64(0)


@dataclass
class sbyte2:
    """2D vector with signed byte components."""

    x: np.int8 = np.int8(0)
    y: np.int8 = np.int8(0)


@dataclass
class short2:
    """2D vector with short components."""

    x: np.int16 = np.int16(0)
    y: np.int16 = np.int16(0)


@dataclass
class int2:
    """2D vector with int components."""

    x: np.int32 = np.int32(0)
    y: np.int32 = np.int32(0)


@dataclass
class long2:
    """2D vector with long components."""

    x: np.int64 = np.int64(0)
    y: np.int64 = np.int64(0)


@dataclass
class bool2:
    """2D vector with bool components."""

    x: bool = False
    y: bool = False


# =============================================================================
# 3D Vector Types
# =============================================================================


@dataclass
class float3:
    """3D vector with float components."""

    x: np.float32 = np.float32(0.0)
    y: np.float32 = np.float32(0.0)
    z: np.float32 = np.float32(0.0)


@dataclass
class double3:
    """3D vector with double components."""

    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)
    z: np.float64 = np.float64(0.0)


@dataclass
class byte3:
    """3D vector with byte components."""

    x: np.uint8 = np.uint8(0)
    y: np.uint8 = np.uint8(0)
    z: np.uint8 = np.uint8(0)


@dataclass
class ushort3:
    """3D vector with unsigned short components."""

    x: np.uint16 = np.uint16(0)
    y: np.uint16 = np.uint16(0)
    z: np.uint16 = np.uint16(0)


@dataclass
class uint3:
    """3D vector with unsigned int components."""

    x: np.uint32 = np.uint32(0)
    y: np.uint32 = np.uint32(0)
    z: np.uint32 = np.uint32(0)


@dataclass
class ulong3:
    """3D vector with unsigned long components."""

    x: np.uint64 = np.uint64(0)
    y: np.uint64 = np.uint64(0)
    z: np.uint64 = np.uint64(0)


@dataclass
class sbyte3:
    """3D vector with signed byte components."""

    x: np.int8 = np.int8(0)
    y: np.int8 = np.int8(0)
    z: np.int8 = np.int8(0)


@dataclass
class short3:
    """3D vector with short components."""

    x: np.int16 = np.int16(0)
    y: np.int16 = np.int16(0)
    z: np.int16 = np.int16(0)


@dataclass
class int3:
    """3D vector with int components."""

    x: np.int32 = np.int32(0)
    y: np.int32 = np.int32(0)
    z: np.int32 = np.int32(0)


@dataclass
class long3:
    """3D vector with long components."""

    x: np.int64 = np.int64(0)
    y: np.int64 = np.int64(0)
    z: np.int64 = np.int64(0)


@dataclass
class bool3:
    """3D vector with bool components."""

    x: bool = False
    y: bool = False
    z: bool = False


# =============================================================================
# 4D Vector Types
# =============================================================================


@dataclass
class float4:
    """4D vector with float components."""

    x: np.float32 = np.float32(0.0)
    y: np.float32 = np.float32(0.0)
    z: np.float32 = np.float32(0.0)
    w: np.float32 = np.float32(0.0)


@dataclass
class double4:
    """4D vector with double components."""

    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)
    z: np.float64 = np.float64(0.0)
    w: np.float64 = np.float64(0.0)


@dataclass
class byte4:
    """4D vector with byte components."""

    x: np.uint8 = np.uint8(0)
    y: np.uint8 = np.uint8(0)
    z: np.uint8 = np.uint8(0)
    w: np.uint8 = np.uint8(0)


@dataclass
class ushort4:
    """4D vector with unsigned short components."""

    x: np.uint16 = np.uint16(0)
    y: np.uint16 = np.uint16(0)
    z: np.uint16 = np.uint16(0)
    w: np.uint16 = np.uint16(0)


@dataclass
class uint4:
    """4D vector with unsigned int components."""

    x: np.uint32 = np.uint32(0)
    y: np.uint32 = np.uint32(0)
    z: np.uint32 = np.uint32(0)
    w: np.uint32 = np.uint32(0)


@dataclass
class ulong4:
    """4D vector with unsigned long components."""

    x: np.uint64 = np.uint64(0)
    y: np.uint64 = np.uint64(0)
    z: np.uint64 = np.uint64(0)
    w: np.uint64 = np.uint64(0)


@dataclass
class sbyte4:
    """4D vector with signed byte components."""

    x: np.int8 = np.int8(0)
    y: np.int8 = np.int8(0)
    z: np.int8 = np.int8(0)
    w: np.int8 = np.int8(0)


@dataclass
class short4:
    """4D vector with short components."""

    x: np.int16 = np.int16(0)
    y: np.int16 = np.int16(0)
    z: np.int16 = np.int16(0)
    w: np.int16 = np.int16(0)


@dataclass
class int4:
    """4D vector with int components."""

    x: np.int32 = np.int32(0)
    y: np.int32 = np.int32(0)
    z: np.int32 = np.int32(0)
    w: np.int32 = np.int32(0)


@dataclass
class long4:
    """4D vector with long components."""

    x: np.int64 = np.int64(0)
    y: np.int64 = np.int64(0)
    z: np.int64 = np.int64(0)
    w: np.int64 = np.int64(0)


@dataclass
class bool4:
    """4D vector with bool components."""

    x: bool = False
    y: bool = False
    z: bool = False
    w: bool = False


# =============================================================================
# Quaternion Types
# =============================================================================


@dataclass
class floatQ:
    """Quaternion with float components."""

    x: np.float32 = np.float32(0.0)
    y: np.float32 = np.float32(0.0)
    z: np.float32 = np.float32(0.0)
    w: np.float32 = np.float32(1.0)


@dataclass
class doubleQ:
    """Quaternion with double components."""

    x: np.float64 = np.float64(0.0)
    y: np.float64 = np.float64(0.0)
    z: np.float64 = np.float64(0.0)
    w: np.float64 = np.float64(1.0)


# =============================================================================
# 2x2 Matrix Types
# =============================================================================


@dataclass
class float2x2:
    """2x2 matrix with float components."""

    m00: np.float32 = np.float32(0.0)
    m01: np.float32 = np.float32(0.0)
    m10: np.float32 = np.float32(0.0)
    m11: np.float32 = np.float32(0.0)


@dataclass
class double2x2:
    """2x2 matrix with double components."""

    m00: np.float64 = np.float64(0.0)
    m01: np.float64 = np.float64(0.0)
    m10: np.float64 = np.float64(0.0)
    m11: np.float64 = np.float64(0.0)


# =============================================================================
# 3x3 Matrix Types
# =============================================================================


@dataclass
class float3x3:
    """3x3 matrix with float components."""

    m00: np.float32 = np.float32(0.0)
    m01: np.float32 = np.float32(0.0)
    m02: np.float32 = np.float32(0.0)
    m10: np.float32 = np.float32(0.0)
    m11: np.float32 = np.float32(0.0)
    m12: np.float32 = np.float32(0.0)
    m20: np.float32 = np.float32(0.0)
    m21: np.float32 = np.float32(0.0)
    m22: np.float32 = np.float32(0.0)


@dataclass
class double3x3:
    """3x3 matrix with double components."""

    m00: np.float64 = np.float64(0.0)
    m01: np.float64 = np.float64(0.0)
    m02: np.float64 = np.float64(0.0)
    m10: np.float64 = np.float64(0.0)
    m11: np.float64 = np.float64(0.0)
    m12: np.float64 = np.float64(0.0)
    m20: np.float64 = np.float64(0.0)
    m21: np.float64 = np.float64(0.0)
    m22: np.float64 = np.float64(0.0)


# =============================================================================
# 4x4 Matrix Types
# =============================================================================


@dataclass
class float4x4:
    """4x4 matrix with float components."""

    m00: np.float32 = np.float32(0.0)
    m01: np.float32 = np.float32(0.0)
    m02: np.float32 = np.float32(0.0)
    m03: np.float32 = np.float32(0.0)
    m10: np.float32 = np.float32(0.0)
    m11: np.float32 = np.float32(0.0)
    m12: np.float32 = np.float32(0.0)
    m13: np.float32 = np.float32(0.0)
    m20: np.float32 = np.float32(0.0)
    m21: np.float32 = np.float32(0.0)
    m22: np.float32 = np.float32(0.0)
    m23: np.float32 = np.float32(0.0)
    m30: np.float32 = np.float32(0.0)
    m31: np.float32 = np.float32(0.0)
    m32: np.float32 = np.float32(0.0)
    m33: np.float32 = np.float32(0.0)


@dataclass
class double4x4:
    """4x4 matrix with double components."""

    m00: np.float64 = np.float64(0.0)
    m01: np.float64 = np.float64(0.0)
    m02: np.float64 = np.float64(0.0)
    m03: np.float64 = np.float64(0.0)
    m10: np.float64 = np.float64(0.0)
    m11: np.float64 = np.float64(0.0)
    m12: np.float64 = np.float64(0.0)
    m13: np.float64 = np.float64(0.0)
    m20: np.float64 = np.float64(0.0)
    m21: np.float64 = np.float64(0.0)
    m22: np.float64 = np.float64(0.0)
    m23: np.float64 = np.float64(0.0)
    m30: np.float64 = np.float64(0.0)
    m31: np.float64 = np.float64(0.0)
    m32: np.float64 = np.float64(0.0)
    m33: np.float64 = np.float64(0.0)
