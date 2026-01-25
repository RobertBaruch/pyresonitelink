"""Generated component: UnpackSH4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UnpackSH4Base(GeneratedComponent):
    """Base class for UnpackSH4<T> variants."""

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
class UnpackSH4Bool(UnpackSH4Base):
    """UnpackSH4<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Byte(UnpackSH4Base):
    """UnpackSH4<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ushort(UnpackSH4Base):
    """UnpackSH4<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Uint(UnpackSH4Base):
    """UnpackSH4<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ulong(UnpackSH4Base):
    """UnpackSH4<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Sbyte(UnpackSH4Base):
    """UnpackSH4<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Short(UnpackSH4Base):
    """UnpackSH4<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Int(UnpackSH4Base):
    """UnpackSH4<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Long(UnpackSH4Base):
    """UnpackSH4<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float(UnpackSH4Base):
    """UnpackSH4<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double(UnpackSH4Base):
    """UnpackSH4<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Decimal(UnpackSH4Base):
    """UnpackSH4<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Char(UnpackSH4Base):
    """UnpackSH4<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4String(UnpackSH4Base):
    """UnpackSH4<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Uri(UnpackSH4Base):
    """UnpackSH4<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Bool2(UnpackSH4Base):
    """UnpackSH4<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Byte2(UnpackSH4Base):
    """UnpackSH4<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ushort2(UnpackSH4Base):
    """UnpackSH4<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Uint2(UnpackSH4Base):
    """UnpackSH4<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ulong2(UnpackSH4Base):
    """UnpackSH4<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Sbyte2(UnpackSH4Base):
    """UnpackSH4<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Short2(UnpackSH4Base):
    """UnpackSH4<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Int2(UnpackSH4Base):
    """UnpackSH4<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Long2(UnpackSH4Base):
    """UnpackSH4<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float2(UnpackSH4Base):
    """UnpackSH4<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double2(UnpackSH4Base):
    """UnpackSH4<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Bool3(UnpackSH4Base):
    """UnpackSH4<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Byte3(UnpackSH4Base):
    """UnpackSH4<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ushort3(UnpackSH4Base):
    """UnpackSH4<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Uint3(UnpackSH4Base):
    """UnpackSH4<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ulong3(UnpackSH4Base):
    """UnpackSH4<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Sbyte3(UnpackSH4Base):
    """UnpackSH4<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Short3(UnpackSH4Base):
    """UnpackSH4<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Int3(UnpackSH4Base):
    """UnpackSH4<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Long3(UnpackSH4Base):
    """UnpackSH4<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float3(UnpackSH4Base):
    """UnpackSH4<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double3(UnpackSH4Base):
    """UnpackSH4<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Bool4(UnpackSH4Base):
    """UnpackSH4<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Byte4(UnpackSH4Base):
    """UnpackSH4<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ushort4(UnpackSH4Base):
    """UnpackSH4<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Uint4(UnpackSH4Base):
    """UnpackSH4<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Ulong4(UnpackSH4Base):
    """UnpackSH4<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Sbyte4(UnpackSH4Base):
    """UnpackSH4<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Short4(UnpackSH4Base):
    """UnpackSH4<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Int4(UnpackSH4Base):
    """UnpackSH4<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Long4(UnpackSH4Base):
    """UnpackSH4<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float4(UnpackSH4Base):
    """UnpackSH4<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double4(UnpackSH4Base):
    """UnpackSH4<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float_2x2(UnpackSH4Base):
    """UnpackSH4<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double_2x2(UnpackSH4Base):
    """UnpackSH4<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float_3x3(UnpackSH4Base):
    """UnpackSH4<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double_3x3(UnpackSH4Base):
    """UnpackSH4<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Float_4x4(UnpackSH4Base):
    """UnpackSH4<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Double_4x4(UnpackSH4Base):
    """UnpackSH4<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4FloatQ(UnpackSH4Base):
    """UnpackSH4<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4DoubleQ(UnpackSH4Base):
    """UnpackSH4<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4DateTime(UnpackSH4Base):
    """UnpackSH4<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4TimeSpan(UnpackSH4Base):
    """UnpackSH4<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Color(UnpackSH4Base):
    """UnpackSH4<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ColorX(UnpackSH4Base):
    """UnpackSH4<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ShadowCastMode(UnpackSH4Base):
    """UnpackSH4<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4LightType(UnpackSH4Base):
    """UnpackSH4<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4SessionAccessLevel(UnpackSH4Base):
    """UnpackSH4<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Key(UnpackSH4Base):
    """UnpackSH4<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4HttpStatusCode(UnpackSH4Base):
    """UnpackSH4<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4HeadOutputDevice(UnpackSH4Base):
    """UnpackSH4<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ReflectionProbeClear(UnpackSH4Base):
    """UnpackSH4<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ReflectionProbeType(UnpackSH4Base):
    """UnpackSH4<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ReflectionProbeTimeSlicingMode(UnpackSH4Base):
    """UnpackSH4<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4CameraClearMode(UnpackSH4Base):
    """UnpackSH4<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4CameraPositioningMode(UnpackSH4Base):
    """UnpackSH4<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4CameraProjection(UnpackSH4Base):
    """UnpackSH4<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ZWrite(UnpackSH4Base):
    """UnpackSH4<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4ZTest(UnpackSH4Base):
    """UnpackSH4<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Blend(UnpackSH4Base):
    """UnpackSH4<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4BlendMode(UnpackSH4Base):
    """UnpackSH4<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Culling(UnpackSH4Base):
    """UnpackSH4<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4BodyNode(UnpackSH4Base):
    """UnpackSH4<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4Chirality(UnpackSH4Base):
    """UnpackSH4<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class UnpackSH4DummyEnum(UnpackSH4Base):
    """UnpackSH4<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH4<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


# Type alias for any UnpackSH4 variant
UnpackSH4 = (
    UnpackSH4Bool |
    UnpackSH4Byte |
    UnpackSH4Ushort |
    UnpackSH4Uint |
    UnpackSH4Ulong |
    UnpackSH4Sbyte |
    UnpackSH4Short |
    UnpackSH4Int |
    UnpackSH4Long |
    UnpackSH4Float |
    UnpackSH4Double |
    UnpackSH4Decimal |
    UnpackSH4Char |
    UnpackSH4String |
    UnpackSH4Uri |
    UnpackSH4Bool2 |
    UnpackSH4Byte2 |
    UnpackSH4Ushort2 |
    UnpackSH4Uint2 |
    UnpackSH4Ulong2 |
    UnpackSH4Sbyte2 |
    UnpackSH4Short2 |
    UnpackSH4Int2 |
    UnpackSH4Long2 |
    UnpackSH4Float2 |
    UnpackSH4Double2 |
    UnpackSH4Bool3 |
    UnpackSH4Byte3 |
    UnpackSH4Ushort3 |
    UnpackSH4Uint3 |
    UnpackSH4Ulong3 |
    UnpackSH4Sbyte3 |
    UnpackSH4Short3 |
    UnpackSH4Int3 |
    UnpackSH4Long3 |
    UnpackSH4Float3 |
    UnpackSH4Double3 |
    UnpackSH4Bool4 |
    UnpackSH4Byte4 |
    UnpackSH4Ushort4 |
    UnpackSH4Uint4 |
    UnpackSH4Ulong4 |
    UnpackSH4Sbyte4 |
    UnpackSH4Short4 |
    UnpackSH4Int4 |
    UnpackSH4Long4 |
    UnpackSH4Float4 |
    UnpackSH4Double4 |
    UnpackSH4Float_2x2 |
    UnpackSH4Double_2x2 |
    UnpackSH4Float_3x3 |
    UnpackSH4Double_3x3 |
    UnpackSH4Float_4x4 |
    UnpackSH4Double_4x4 |
    UnpackSH4FloatQ |
    UnpackSH4DoubleQ |
    UnpackSH4DateTime |
    UnpackSH4TimeSpan |
    UnpackSH4Color |
    UnpackSH4ColorX |
    UnpackSH4ShadowCastMode |
    UnpackSH4LightType |
    UnpackSH4SessionAccessLevel |
    UnpackSH4Key |
    UnpackSH4HttpStatusCode |
    UnpackSH4HeadOutputDevice |
    UnpackSH4ReflectionProbeClear |
    UnpackSH4ReflectionProbeType |
    UnpackSH4ReflectionProbeTimeSlicingMode |
    UnpackSH4CameraClearMode |
    UnpackSH4CameraPositioningMode |
    UnpackSH4CameraProjection |
    UnpackSH4ZWrite |
    UnpackSH4ZTest |
    UnpackSH4Blend |
    UnpackSH4BlendMode |
    UnpackSH4Culling |
    UnpackSH4BodyNode |
    UnpackSH4Chirality |
    UnpackSH4DummyEnum
)