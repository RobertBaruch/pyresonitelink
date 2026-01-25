"""Generated component: UnpackSH1.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class UnpackSH1Base(GeneratedComponent):
    """Base class for UnpackSH1<T> variants."""

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
class UnpackSH1Bool(UnpackSH1Base):
    """UnpackSH1<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Byte(UnpackSH1Base):
    """UnpackSH1<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ushort(UnpackSH1Base):
    """UnpackSH1<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Uint(UnpackSH1Base):
    """UnpackSH1<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ulong(UnpackSH1Base):
    """UnpackSH1<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Sbyte(UnpackSH1Base):
    """UnpackSH1<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Short(UnpackSH1Base):
    """UnpackSH1<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Int(UnpackSH1Base):
    """UnpackSH1<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Long(UnpackSH1Base):
    """UnpackSH1<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float(UnpackSH1Base):
    """UnpackSH1<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double(UnpackSH1Base):
    """UnpackSH1<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Decimal(UnpackSH1Base):
    """UnpackSH1<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Char(UnpackSH1Base):
    """UnpackSH1<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1String(UnpackSH1Base):
    """UnpackSH1<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Uri(UnpackSH1Base):
    """UnpackSH1<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Bool2(UnpackSH1Base):
    """UnpackSH1<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Byte2(UnpackSH1Base):
    """UnpackSH1<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ushort2(UnpackSH1Base):
    """UnpackSH1<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Uint2(UnpackSH1Base):
    """UnpackSH1<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ulong2(UnpackSH1Base):
    """UnpackSH1<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Sbyte2(UnpackSH1Base):
    """UnpackSH1<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Short2(UnpackSH1Base):
    """UnpackSH1<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Int2(UnpackSH1Base):
    """UnpackSH1<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Long2(UnpackSH1Base):
    """UnpackSH1<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float2(UnpackSH1Base):
    """UnpackSH1<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double2(UnpackSH1Base):
    """UnpackSH1<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Bool3(UnpackSH1Base):
    """UnpackSH1<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Byte3(UnpackSH1Base):
    """UnpackSH1<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ushort3(UnpackSH1Base):
    """UnpackSH1<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Uint3(UnpackSH1Base):
    """UnpackSH1<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ulong3(UnpackSH1Base):
    """UnpackSH1<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Sbyte3(UnpackSH1Base):
    """UnpackSH1<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Short3(UnpackSH1Base):
    """UnpackSH1<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Int3(UnpackSH1Base):
    """UnpackSH1<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Long3(UnpackSH1Base):
    """UnpackSH1<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float3(UnpackSH1Base):
    """UnpackSH1<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double3(UnpackSH1Base):
    """UnpackSH1<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Bool4(UnpackSH1Base):
    """UnpackSH1<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Byte4(UnpackSH1Base):
    """UnpackSH1<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ushort4(UnpackSH1Base):
    """UnpackSH1<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Uint4(UnpackSH1Base):
    """UnpackSH1<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Ulong4(UnpackSH1Base):
    """UnpackSH1<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Sbyte4(UnpackSH1Base):
    """UnpackSH1<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Short4(UnpackSH1Base):
    """UnpackSH1<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Int4(UnpackSH1Base):
    """UnpackSH1<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Long4(UnpackSH1Base):
    """UnpackSH1<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float4(UnpackSH1Base):
    """UnpackSH1<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double4(UnpackSH1Base):
    """UnpackSH1<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float_2x2(UnpackSH1Base):
    """UnpackSH1<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double_2x2(UnpackSH1Base):
    """UnpackSH1<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float_3x3(UnpackSH1Base):
    """UnpackSH1<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double_3x3(UnpackSH1Base):
    """UnpackSH1<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Float_4x4(UnpackSH1Base):
    """UnpackSH1<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Double_4x4(UnpackSH1Base):
    """UnpackSH1<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1FloatQ(UnpackSH1Base):
    """UnpackSH1<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1DoubleQ(UnpackSH1Base):
    """UnpackSH1<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1DateTime(UnpackSH1Base):
    """UnpackSH1<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1TimeSpan(UnpackSH1Base):
    """UnpackSH1<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Color(UnpackSH1Base):
    """UnpackSH1<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ColorX(UnpackSH1Base):
    """UnpackSH1<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ShadowCastMode(UnpackSH1Base):
    """UnpackSH1<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1LightType(UnpackSH1Base):
    """UnpackSH1<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1SessionAccessLevel(UnpackSH1Base):
    """UnpackSH1<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Key(UnpackSH1Base):
    """UnpackSH1<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1HttpStatusCode(UnpackSH1Base):
    """UnpackSH1<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1HeadOutputDevice(UnpackSH1Base):
    """UnpackSH1<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ReflectionProbeClear(UnpackSH1Base):
    """UnpackSH1<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ReflectionProbeType(UnpackSH1Base):
    """UnpackSH1<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ReflectionProbeTimeSlicingMode(UnpackSH1Base):
    """UnpackSH1<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1CameraClearMode(UnpackSH1Base):
    """UnpackSH1<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1CameraPositioningMode(UnpackSH1Base):
    """UnpackSH1<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1CameraProjection(UnpackSH1Base):
    """UnpackSH1<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ZWrite(UnpackSH1Base):
    """UnpackSH1<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1ZTest(UnpackSH1Base):
    """UnpackSH1<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Blend(UnpackSH1Base):
    """UnpackSH1<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1BlendMode(UnpackSH1Base):
    """UnpackSH1<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Culling(UnpackSH1Base):
    """UnpackSH1<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1BodyNode(UnpackSH1Base):
    """UnpackSH1<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1Chirality(UnpackSH1Base):
    """UnpackSH1<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class UnpackSH1DummyEnum(UnpackSH1Base):
    """UnpackSH1<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.UnpackSH1<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh": "SH",
    }

    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


# Type alias for any UnpackSH1 variant
UnpackSH1 = (
    UnpackSH1Bool |
    UnpackSH1Byte |
    UnpackSH1Ushort |
    UnpackSH1Uint |
    UnpackSH1Ulong |
    UnpackSH1Sbyte |
    UnpackSH1Short |
    UnpackSH1Int |
    UnpackSH1Long |
    UnpackSH1Float |
    UnpackSH1Double |
    UnpackSH1Decimal |
    UnpackSH1Char |
    UnpackSH1String |
    UnpackSH1Uri |
    UnpackSH1Bool2 |
    UnpackSH1Byte2 |
    UnpackSH1Ushort2 |
    UnpackSH1Uint2 |
    UnpackSH1Ulong2 |
    UnpackSH1Sbyte2 |
    UnpackSH1Short2 |
    UnpackSH1Int2 |
    UnpackSH1Long2 |
    UnpackSH1Float2 |
    UnpackSH1Double2 |
    UnpackSH1Bool3 |
    UnpackSH1Byte3 |
    UnpackSH1Ushort3 |
    UnpackSH1Uint3 |
    UnpackSH1Ulong3 |
    UnpackSH1Sbyte3 |
    UnpackSH1Short3 |
    UnpackSH1Int3 |
    UnpackSH1Long3 |
    UnpackSH1Float3 |
    UnpackSH1Double3 |
    UnpackSH1Bool4 |
    UnpackSH1Byte4 |
    UnpackSH1Ushort4 |
    UnpackSH1Uint4 |
    UnpackSH1Ulong4 |
    UnpackSH1Sbyte4 |
    UnpackSH1Short4 |
    UnpackSH1Int4 |
    UnpackSH1Long4 |
    UnpackSH1Float4 |
    UnpackSH1Double4 |
    UnpackSH1Float_2x2 |
    UnpackSH1Double_2x2 |
    UnpackSH1Float_3x3 |
    UnpackSH1Double_3x3 |
    UnpackSH1Float_4x4 |
    UnpackSH1Double_4x4 |
    UnpackSH1FloatQ |
    UnpackSH1DoubleQ |
    UnpackSH1DateTime |
    UnpackSH1TimeSpan |
    UnpackSH1Color |
    UnpackSH1ColorX |
    UnpackSH1ShadowCastMode |
    UnpackSH1LightType |
    UnpackSH1SessionAccessLevel |
    UnpackSH1Key |
    UnpackSH1HttpStatusCode |
    UnpackSH1HeadOutputDevice |
    UnpackSH1ReflectionProbeClear |
    UnpackSH1ReflectionProbeType |
    UnpackSH1ReflectionProbeTimeSlicingMode |
    UnpackSH1CameraClearMode |
    UnpackSH1CameraPositioningMode |
    UnpackSH1CameraProjection |
    UnpackSH1ZWrite |
    UnpackSH1ZTest |
    UnpackSH1Blend |
    UnpackSH1BlendMode |
    UnpackSH1Culling |
    UnpackSH1BodyNode |
    UnpackSH1Chirality |
    UnpackSH1DummyEnum
)