"""Generated component: UnpackSH3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UnpackSH3Base(GeneratedComponent):
    """Base class for UnpackSH3<T> variants."""

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
class UnpackSH3Bool(UnpackSH3Base):
    """UnpackSH3<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Byte(UnpackSH3Base):
    """UnpackSH3<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ushort(UnpackSH3Base):
    """UnpackSH3<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Uint(UnpackSH3Base):
    """UnpackSH3<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ulong(UnpackSH3Base):
    """UnpackSH3<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Sbyte(UnpackSH3Base):
    """UnpackSH3<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Short(UnpackSH3Base):
    """UnpackSH3<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Int(UnpackSH3Base):
    """UnpackSH3<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Long(UnpackSH3Base):
    """UnpackSH3<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float(UnpackSH3Base):
    """UnpackSH3<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double(UnpackSH3Base):
    """UnpackSH3<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Decimal(UnpackSH3Base):
    """UnpackSH3<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Char(UnpackSH3Base):
    """UnpackSH3<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3String(UnpackSH3Base):
    """UnpackSH3<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Uri(UnpackSH3Base):
    """UnpackSH3<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Bool2(UnpackSH3Base):
    """UnpackSH3<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Byte2(UnpackSH3Base):
    """UnpackSH3<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ushort2(UnpackSH3Base):
    """UnpackSH3<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Uint2(UnpackSH3Base):
    """UnpackSH3<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ulong2(UnpackSH3Base):
    """UnpackSH3<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Sbyte2(UnpackSH3Base):
    """UnpackSH3<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Short2(UnpackSH3Base):
    """UnpackSH3<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Int2(UnpackSH3Base):
    """UnpackSH3<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Long2(UnpackSH3Base):
    """UnpackSH3<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float2(UnpackSH3Base):
    """UnpackSH3<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double2(UnpackSH3Base):
    """UnpackSH3<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Bool3(UnpackSH3Base):
    """UnpackSH3<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Byte3(UnpackSH3Base):
    """UnpackSH3<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ushort3(UnpackSH3Base):
    """UnpackSH3<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Uint3(UnpackSH3Base):
    """UnpackSH3<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ulong3(UnpackSH3Base):
    """UnpackSH3<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Sbyte3(UnpackSH3Base):
    """UnpackSH3<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Short3(UnpackSH3Base):
    """UnpackSH3<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Int3(UnpackSH3Base):
    """UnpackSH3<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Long3(UnpackSH3Base):
    """UnpackSH3<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float3(UnpackSH3Base):
    """UnpackSH3<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double3(UnpackSH3Base):
    """UnpackSH3<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Bool4(UnpackSH3Base):
    """UnpackSH3<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Byte4(UnpackSH3Base):
    """UnpackSH3<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ushort4(UnpackSH3Base):
    """UnpackSH3<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Uint4(UnpackSH3Base):
    """UnpackSH3<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Ulong4(UnpackSH3Base):
    """UnpackSH3<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Sbyte4(UnpackSH3Base):
    """UnpackSH3<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Short4(UnpackSH3Base):
    """UnpackSH3<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Int4(UnpackSH3Base):
    """UnpackSH3<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Long4(UnpackSH3Base):
    """UnpackSH3<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float4(UnpackSH3Base):
    """UnpackSH3<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double4(UnpackSH3Base):
    """UnpackSH3<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float_2x2(UnpackSH3Base):
    """UnpackSH3<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double_2x2(UnpackSH3Base):
    """UnpackSH3<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float_3x3(UnpackSH3Base):
    """UnpackSH3<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double_3x3(UnpackSH3Base):
    """UnpackSH3<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Float_4x4(UnpackSH3Base):
    """UnpackSH3<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Double_4x4(UnpackSH3Base):
    """UnpackSH3<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3FloatQ(UnpackSH3Base):
    """UnpackSH3<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3DoubleQ(UnpackSH3Base):
    """UnpackSH3<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3DateTime(UnpackSH3Base):
    """UnpackSH3<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3TimeSpan(UnpackSH3Base):
    """UnpackSH3<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Color(UnpackSH3Base):
    """UnpackSH3<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ColorX(UnpackSH3Base):
    """UnpackSH3<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ShadowCastMode(UnpackSH3Base):
    """UnpackSH3<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3LightType(UnpackSH3Base):
    """UnpackSH3<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3SessionAccessLevel(UnpackSH3Base):
    """UnpackSH3<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Key(UnpackSH3Base):
    """UnpackSH3<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3HttpStatusCode(UnpackSH3Base):
    """UnpackSH3<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3HeadOutputDevice(UnpackSH3Base):
    """UnpackSH3<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ReflectionProbeClear(UnpackSH3Base):
    """UnpackSH3<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ReflectionProbeType(UnpackSH3Base):
    """UnpackSH3<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ReflectionProbeTimeSlicingMode(UnpackSH3Base):
    """UnpackSH3<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3CameraClearMode(UnpackSH3Base):
    """UnpackSH3<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3CameraPositioningMode(UnpackSH3Base):
    """UnpackSH3<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3CameraProjection(UnpackSH3Base):
    """UnpackSH3<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ZWrite(UnpackSH3Base):
    """UnpackSH3<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3ZTest(UnpackSH3Base):
    """UnpackSH3<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Blend(UnpackSH3Base):
    """UnpackSH3<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3BlendMode(UnpackSH3Base):
    """UnpackSH3<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Culling(UnpackSH3Base):
    """UnpackSH3<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3BodyNode(UnpackSH3Base):
    """UnpackSH3<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3Chirality(UnpackSH3Base):
    """UnpackSH3<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class UnpackSH3DummyEnum(UnpackSH3Base):
    """UnpackSH3<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH3<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


# Type alias for any UnpackSH3 variant
UnpackSH3 = (
    UnpackSH3Bool |
    UnpackSH3Byte |
    UnpackSH3Ushort |
    UnpackSH3Uint |
    UnpackSH3Ulong |
    UnpackSH3Sbyte |
    UnpackSH3Short |
    UnpackSH3Int |
    UnpackSH3Long |
    UnpackSH3Float |
    UnpackSH3Double |
    UnpackSH3Decimal |
    UnpackSH3Char |
    UnpackSH3String |
    UnpackSH3Uri |
    UnpackSH3Bool2 |
    UnpackSH3Byte2 |
    UnpackSH3Ushort2 |
    UnpackSH3Uint2 |
    UnpackSH3Ulong2 |
    UnpackSH3Sbyte2 |
    UnpackSH3Short2 |
    UnpackSH3Int2 |
    UnpackSH3Long2 |
    UnpackSH3Float2 |
    UnpackSH3Double2 |
    UnpackSH3Bool3 |
    UnpackSH3Byte3 |
    UnpackSH3Ushort3 |
    UnpackSH3Uint3 |
    UnpackSH3Ulong3 |
    UnpackSH3Sbyte3 |
    UnpackSH3Short3 |
    UnpackSH3Int3 |
    UnpackSH3Long3 |
    UnpackSH3Float3 |
    UnpackSH3Double3 |
    UnpackSH3Bool4 |
    UnpackSH3Byte4 |
    UnpackSH3Ushort4 |
    UnpackSH3Uint4 |
    UnpackSH3Ulong4 |
    UnpackSH3Sbyte4 |
    UnpackSH3Short4 |
    UnpackSH3Int4 |
    UnpackSH3Long4 |
    UnpackSH3Float4 |
    UnpackSH3Double4 |
    UnpackSH3Float_2x2 |
    UnpackSH3Double_2x2 |
    UnpackSH3Float_3x3 |
    UnpackSH3Double_3x3 |
    UnpackSH3Float_4x4 |
    UnpackSH3Double_4x4 |
    UnpackSH3FloatQ |
    UnpackSH3DoubleQ |
    UnpackSH3DateTime |
    UnpackSH3TimeSpan |
    UnpackSH3Color |
    UnpackSH3ColorX |
    UnpackSH3ShadowCastMode |
    UnpackSH3LightType |
    UnpackSH3SessionAccessLevel |
    UnpackSH3Key |
    UnpackSH3HttpStatusCode |
    UnpackSH3HeadOutputDevice |
    UnpackSH3ReflectionProbeClear |
    UnpackSH3ReflectionProbeType |
    UnpackSH3ReflectionProbeTimeSlicingMode |
    UnpackSH3CameraClearMode |
    UnpackSH3CameraPositioningMode |
    UnpackSH3CameraProjection |
    UnpackSH3ZWrite |
    UnpackSH3ZTest |
    UnpackSH3Blend |
    UnpackSH3BlendMode |
    UnpackSH3Culling |
    UnpackSH3BodyNode |
    UnpackSH3Chirality |
    UnpackSH3DummyEnum
)