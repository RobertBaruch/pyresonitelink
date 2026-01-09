"""Primitive types for ResoniteLink data model.

This module contains vector, quaternion, matrix, and color types that mirror
the C# structs used in ResoniteLink.
"""

from dataclasses import dataclass


# =============================================================================
# Color Types
# =============================================================================


@dataclass
class color:
    """RGBA color with float components."""

    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0


@dataclass
class colorX:
    """RGBA color with float components and color profile."""

    r: float = 0.0
    g: float = 0.0
    b: float = 0.0
    a: float = 1.0
    profile: str = ""


@dataclass
class color32:
    """RGBA color with byte components (0-255)."""

    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255


# =============================================================================
# 2D Vector Types
# =============================================================================


@dataclass
class float2:
    """2D vector with float components."""

    x: float = 0.0
    y: float = 0.0


@dataclass
class double2:
    """2D vector with double components."""

    x: float = 0.0
    y: float = 0.0


@dataclass
class byte2:
    """2D vector with byte components."""

    x: int = 0
    y: int = 0


@dataclass
class ushort2:
    """2D vector with unsigned short components."""

    x: int = 0
    y: int = 0


@dataclass
class uint2:
    """2D vector with unsigned int components."""

    x: int = 0
    y: int = 0


@dataclass
class ulong2:
    """2D vector with unsigned long components."""

    x: int = 0
    y: int = 0


@dataclass
class sbyte2:
    """2D vector with signed byte components."""

    x: int = 0
    y: int = 0


@dataclass
class short2:
    """2D vector with short components."""

    x: int = 0
    y: int = 0


@dataclass
class int2:
    """2D vector with int components."""

    x: int = 0
    y: int = 0


@dataclass
class long2:
    """2D vector with long components."""

    x: int = 0
    y: int = 0


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

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class double3:
    """3D vector with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0


@dataclass
class byte3:
    """3D vector with byte components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class ushort3:
    """3D vector with unsigned short components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class uint3:
    """3D vector with unsigned int components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class ulong3:
    """3D vector with unsigned long components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class sbyte3:
    """3D vector with signed byte components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class short3:
    """3D vector with short components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class int3:
    """3D vector with int components."""

    x: int = 0
    y: int = 0
    z: int = 0


@dataclass
class long3:
    """3D vector with long components."""

    x: int = 0
    y: int = 0
    z: int = 0


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

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0


@dataclass
class double4:
    """4D vector with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0


@dataclass
class byte4:
    """4D vector with byte components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class ushort4:
    """4D vector with unsigned short components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class uint4:
    """4D vector with unsigned int components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class ulong4:
    """4D vector with unsigned long components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class sbyte4:
    """4D vector with signed byte components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class short4:
    """4D vector with short components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class int4:
    """4D vector with int components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


@dataclass
class long4:
    """4D vector with long components."""

    x: int = 0
    y: int = 0
    z: int = 0
    w: int = 0


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

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0


@dataclass
class doubleQ:
    """Quaternion with double components."""

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 1.0


# =============================================================================
# 2x2 Matrix Types
# =============================================================================


@dataclass
class float2x2:
    """2x2 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m10: float = 0.0
    m11: float = 0.0


@dataclass
class double2x2:
    """2x2 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m10: float = 0.0
    m11: float = 0.0


# =============================================================================
# 3x3 Matrix Types
# =============================================================================


@dataclass
class float3x3:
    """3x3 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0


@dataclass
class double3x3:
    """3x3 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0


# =============================================================================
# 4x4 Matrix Types
# =============================================================================


@dataclass
class float4x4:
    """4x4 matrix with float components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m03: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m13: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0
    m23: float = 0.0
    m30: float = 0.0
    m31: float = 0.0
    m32: float = 0.0
    m33: float = 0.0


@dataclass
class double4x4:
    """4x4 matrix with double components."""

    m00: float = 0.0
    m01: float = 0.0
    m02: float = 0.0
    m03: float = 0.0
    m10: float = 0.0
    m11: float = 0.0
    m12: float = 0.0
    m13: float = 0.0
    m20: float = 0.0
    m21: float = 0.0
    m22: float = 0.0
    m23: float = 0.0
    m30: float = 0.0
    m31: float = 0.0
    m32: float = 0.0
    m33: float = 0.0
