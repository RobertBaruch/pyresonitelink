"""Generated component: UnpackSH2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UnpackSH2Base(GeneratedComponent):
    """Base class for UnpackSH2<T> variants."""

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
class UnpackSH2Bool(UnpackSH2Base):
    """UnpackSH2<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Byte(UnpackSH2Base):
    """UnpackSH2<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ushort(UnpackSH2Base):
    """UnpackSH2<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Uint(UnpackSH2Base):
    """UnpackSH2<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ulong(UnpackSH2Base):
    """UnpackSH2<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Sbyte(UnpackSH2Base):
    """UnpackSH2<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Short(UnpackSH2Base):
    """UnpackSH2<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Int(UnpackSH2Base):
    """UnpackSH2<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Long(UnpackSH2Base):
    """UnpackSH2<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float(UnpackSH2Base):
    """UnpackSH2<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double(UnpackSH2Base):
    """UnpackSH2<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Decimal(UnpackSH2Base):
    """UnpackSH2<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Char(UnpackSH2Base):
    """UnpackSH2<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2String(UnpackSH2Base):
    """UnpackSH2<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Uri(UnpackSH2Base):
    """UnpackSH2<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Bool2(UnpackSH2Base):
    """UnpackSH2<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Byte2(UnpackSH2Base):
    """UnpackSH2<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ushort2(UnpackSH2Base):
    """UnpackSH2<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Uint2(UnpackSH2Base):
    """UnpackSH2<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ulong2(UnpackSH2Base):
    """UnpackSH2<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Sbyte2(UnpackSH2Base):
    """UnpackSH2<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Short2(UnpackSH2Base):
    """UnpackSH2<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Int2(UnpackSH2Base):
    """UnpackSH2<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Long2(UnpackSH2Base):
    """UnpackSH2<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float2(UnpackSH2Base):
    """UnpackSH2<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double2(UnpackSH2Base):
    """UnpackSH2<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Bool3(UnpackSH2Base):
    """UnpackSH2<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Byte3(UnpackSH2Base):
    """UnpackSH2<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ushort3(UnpackSH2Base):
    """UnpackSH2<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Uint3(UnpackSH2Base):
    """UnpackSH2<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ulong3(UnpackSH2Base):
    """UnpackSH2<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Sbyte3(UnpackSH2Base):
    """UnpackSH2<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Short3(UnpackSH2Base):
    """UnpackSH2<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Int3(UnpackSH2Base):
    """UnpackSH2<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Long3(UnpackSH2Base):
    """UnpackSH2<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float3(UnpackSH2Base):
    """UnpackSH2<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double3(UnpackSH2Base):
    """UnpackSH2<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Bool4(UnpackSH2Base):
    """UnpackSH2<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Byte4(UnpackSH2Base):
    """UnpackSH2<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ushort4(UnpackSH2Base):
    """UnpackSH2<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Uint4(UnpackSH2Base):
    """UnpackSH2<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Ulong4(UnpackSH2Base):
    """UnpackSH2<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Sbyte4(UnpackSH2Base):
    """UnpackSH2<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Short4(UnpackSH2Base):
    """UnpackSH2<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Int4(UnpackSH2Base):
    """UnpackSH2<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Long4(UnpackSH2Base):
    """UnpackSH2<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float4(UnpackSH2Base):
    """UnpackSH2<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double4(UnpackSH2Base):
    """UnpackSH2<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float_2x2(UnpackSH2Base):
    """UnpackSH2<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double_2x2(UnpackSH2Base):
    """UnpackSH2<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float_3x3(UnpackSH2Base):
    """UnpackSH2<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double_3x3(UnpackSH2Base):
    """UnpackSH2<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Float_4x4(UnpackSH2Base):
    """UnpackSH2<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Double_4x4(UnpackSH2Base):
    """UnpackSH2<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2FloatQ(UnpackSH2Base):
    """UnpackSH2<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2DoubleQ(UnpackSH2Base):
    """UnpackSH2<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2DateTime(UnpackSH2Base):
    """UnpackSH2<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2TimeSpan(UnpackSH2Base):
    """UnpackSH2<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Color(UnpackSH2Base):
    """UnpackSH2<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ColorX(UnpackSH2Base):
    """UnpackSH2<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ShadowCastMode(UnpackSH2Base):
    """UnpackSH2<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2LightType(UnpackSH2Base):
    """UnpackSH2<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2SessionAccessLevel(UnpackSH2Base):
    """UnpackSH2<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Key(UnpackSH2Base):
    """UnpackSH2<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2HttpStatusCode(UnpackSH2Base):
    """UnpackSH2<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2HeadOutputDevice(UnpackSH2Base):
    """UnpackSH2<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ReflectionProbeClear(UnpackSH2Base):
    """UnpackSH2<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ReflectionProbeType(UnpackSH2Base):
    """UnpackSH2<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ReflectionProbeTimeSlicingMode(UnpackSH2Base):
    """UnpackSH2<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2CameraClearMode(UnpackSH2Base):
    """UnpackSH2<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2CameraPositioningMode(UnpackSH2Base):
    """UnpackSH2<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2CameraProjection(UnpackSH2Base):
    """UnpackSH2<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ZWrite(UnpackSH2Base):
    """UnpackSH2<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2ZTest(UnpackSH2Base):
    """UnpackSH2<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Blend(UnpackSH2Base):
    """UnpackSH2<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2BlendMode(UnpackSH2Base):
    """UnpackSH2<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Culling(UnpackSH2Base):
    """UnpackSH2<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2BodyNode(UnpackSH2Base):
    """UnpackSH2<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2Chirality(UnpackSH2Base):
    """UnpackSH2<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class UnpackSH2DummyEnum(UnpackSH2Base):
    """UnpackSH2<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH2<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


# Type alias for any UnpackSH2 variant
UnpackSH2 = (
    UnpackSH2Bool |
    UnpackSH2Byte |
    UnpackSH2Ushort |
    UnpackSH2Uint |
    UnpackSH2Ulong |
    UnpackSH2Sbyte |
    UnpackSH2Short |
    UnpackSH2Int |
    UnpackSH2Long |
    UnpackSH2Float |
    UnpackSH2Double |
    UnpackSH2Decimal |
    UnpackSH2Char |
    UnpackSH2String |
    UnpackSH2Uri |
    UnpackSH2Bool2 |
    UnpackSH2Byte2 |
    UnpackSH2Ushort2 |
    UnpackSH2Uint2 |
    UnpackSH2Ulong2 |
    UnpackSH2Sbyte2 |
    UnpackSH2Short2 |
    UnpackSH2Int2 |
    UnpackSH2Long2 |
    UnpackSH2Float2 |
    UnpackSH2Double2 |
    UnpackSH2Bool3 |
    UnpackSH2Byte3 |
    UnpackSH2Ushort3 |
    UnpackSH2Uint3 |
    UnpackSH2Ulong3 |
    UnpackSH2Sbyte3 |
    UnpackSH2Short3 |
    UnpackSH2Int3 |
    UnpackSH2Long3 |
    UnpackSH2Float3 |
    UnpackSH2Double3 |
    UnpackSH2Bool4 |
    UnpackSH2Byte4 |
    UnpackSH2Ushort4 |
    UnpackSH2Uint4 |
    UnpackSH2Ulong4 |
    UnpackSH2Sbyte4 |
    UnpackSH2Short4 |
    UnpackSH2Int4 |
    UnpackSH2Long4 |
    UnpackSH2Float4 |
    UnpackSH2Double4 |
    UnpackSH2Float_2x2 |
    UnpackSH2Double_2x2 |
    UnpackSH2Float_3x3 |
    UnpackSH2Double_3x3 |
    UnpackSH2Float_4x4 |
    UnpackSH2Double_4x4 |
    UnpackSH2FloatQ |
    UnpackSH2DoubleQ |
    UnpackSH2DateTime |
    UnpackSH2TimeSpan |
    UnpackSH2Color |
    UnpackSH2ColorX |
    UnpackSH2ShadowCastMode |
    UnpackSH2LightType |
    UnpackSH2SessionAccessLevel |
    UnpackSH2Key |
    UnpackSH2HttpStatusCode |
    UnpackSH2HeadOutputDevice |
    UnpackSH2ReflectionProbeClear |
    UnpackSH2ReflectionProbeType |
    UnpackSH2ReflectionProbeTimeSlicingMode |
    UnpackSH2CameraClearMode |
    UnpackSH2CameraPositioningMode |
    UnpackSH2CameraProjection |
    UnpackSH2ZWrite |
    UnpackSH2ZTest |
    UnpackSH2Blend |
    UnpackSH2BlendMode |
    UnpackSH2Culling |
    UnpackSH2BodyNode |
    UnpackSH2Chirality |
    UnpackSH2DummyEnum
)