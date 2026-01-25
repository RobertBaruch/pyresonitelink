"""Generated component: PackSH1.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackSH1Base(GeneratedComponent):
    """Base class for PackSH1<T> variants."""

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
class PackSH1Bool(PackSH1Base):
    """PackSH1<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class PackSH1Byte(PackSH1Base):
    """PackSH1<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class PackSH1Ushort(PackSH1Base):
    """PackSH1<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class PackSH1Uint(PackSH1Base):
    """PackSH1<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class PackSH1Ulong(PackSH1Base):
    """PackSH1<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class PackSH1Sbyte(PackSH1Base):
    """PackSH1<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class PackSH1Short(PackSH1Base):
    """PackSH1<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class PackSH1Int(PackSH1Base):
    """PackSH1<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class PackSH1Long(PackSH1Base):
    """PackSH1<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class PackSH1Float(PackSH1Base):
    """PackSH1<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class PackSH1Double(PackSH1Base):
    """PackSH1<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class PackSH1Decimal(PackSH1Base):
    """PackSH1<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class PackSH1Char(PackSH1Base):
    """PackSH1<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class PackSH1String(PackSH1Base):
    """PackSH1<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class PackSH1Uri(PackSH1Base):
    """PackSH1<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class PackSH1Bool2(PackSH1Base):
    """PackSH1<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class PackSH1Byte2(PackSH1Base):
    """PackSH1<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class PackSH1Ushort2(PackSH1Base):
    """PackSH1<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class PackSH1Uint2(PackSH1Base):
    """PackSH1<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class PackSH1Ulong2(PackSH1Base):
    """PackSH1<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class PackSH1Sbyte2(PackSH1Base):
    """PackSH1<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class PackSH1Short2(PackSH1Base):
    """PackSH1<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class PackSH1Int2(PackSH1Base):
    """PackSH1<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class PackSH1Long2(PackSH1Base):
    """PackSH1<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class PackSH1Float2(PackSH1Base):
    """PackSH1<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class PackSH1Double2(PackSH1Base):
    """PackSH1<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class PackSH1Bool3(PackSH1Base):
    """PackSH1<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class PackSH1Byte3(PackSH1Base):
    """PackSH1<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class PackSH1Ushort3(PackSH1Base):
    """PackSH1<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class PackSH1Uint3(PackSH1Base):
    """PackSH1<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class PackSH1Ulong3(PackSH1Base):
    """PackSH1<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class PackSH1Sbyte3(PackSH1Base):
    """PackSH1<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class PackSH1Short3(PackSH1Base):
    """PackSH1<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class PackSH1Int3(PackSH1Base):
    """PackSH1<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class PackSH1Long3(PackSH1Base):
    """PackSH1<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class PackSH1Float3(PackSH1Base):
    """PackSH1<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class PackSH1Double3(PackSH1Base):
    """PackSH1<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class PackSH1Bool4(PackSH1Base):
    """PackSH1<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class PackSH1Byte4(PackSH1Base):
    """PackSH1<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class PackSH1Ushort4(PackSH1Base):
    """PackSH1<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class PackSH1Uint4(PackSH1Base):
    """PackSH1<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class PackSH1Ulong4(PackSH1Base):
    """PackSH1<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class PackSH1Sbyte4(PackSH1Base):
    """PackSH1<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class PackSH1Short4(PackSH1Base):
    """PackSH1<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class PackSH1Int4(PackSH1Base):
    """PackSH1<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class PackSH1Long4(PackSH1Base):
    """PackSH1<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class PackSH1Float4(PackSH1Base):
    """PackSH1<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class PackSH1Double4(PackSH1Base):
    """PackSH1<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class PackSH1Float_2x2(PackSH1Base):
    """PackSH1<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class PackSH1Double_2x2(PackSH1Base):
    """PackSH1<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class PackSH1Float_3x3(PackSH1Base):
    """PackSH1<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class PackSH1Double_3x3(PackSH1Base):
    """PackSH1<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class PackSH1Float_4x4(PackSH1Base):
    """PackSH1<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class PackSH1Double_4x4(PackSH1Base):
    """PackSH1<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class PackSH1FloatQ(PackSH1Base):
    """PackSH1<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class PackSH1DoubleQ(PackSH1Base):
    """PackSH1<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class PackSH1DateTime(PackSH1Base):
    """PackSH1<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class PackSH1TimeSpan(PackSH1Base):
    """PackSH1<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class PackSH1Color(PackSH1Base):
    """PackSH1<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class PackSH1ColorX(PackSH1Base):
    """PackSH1<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class PackSH1ShadowCastMode(PackSH1Base):
    """PackSH1<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class PackSH1LightType(PackSH1Base):
    """PackSH1<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class PackSH1SessionAccessLevel(PackSH1Base):
    """PackSH1<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class PackSH1Key(PackSH1Base):
    """PackSH1<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class PackSH1HttpStatusCode(PackSH1Base):
    """PackSH1<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class PackSH1HeadOutputDevice(PackSH1Base):
    """PackSH1<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class PackSH1ReflectionProbeClear(PackSH1Base):
    """PackSH1<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class PackSH1ReflectionProbeType(PackSH1Base):
    """PackSH1<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class PackSH1ReflectionProbeTimeSlicingMode(PackSH1Base):
    """PackSH1<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class PackSH1CameraClearMode(PackSH1Base):
    """PackSH1<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class PackSH1CameraPositioningMode(PackSH1Base):
    """PackSH1<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class PackSH1CameraProjection(PackSH1Base):
    """PackSH1<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class PackSH1ZWrite(PackSH1Base):
    """PackSH1<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class PackSH1ZTest(PackSH1Base):
    """PackSH1<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class PackSH1Blend(PackSH1Base):
    """PackSH1<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class PackSH1BlendMode(PackSH1Base):
    """PackSH1<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class PackSH1Culling(PackSH1Base):
    """PackSH1<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class PackSH1BodyNode(PackSH1Base):
    """PackSH1<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class PackSH1Chirality(PackSH1Base):
    """PackSH1<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class PackSH1DummyEnum(PackSH1Base):
    """PackSH1<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH1<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any PackSH1 variant
PackSH1 = (
    PackSH1Bool |
    PackSH1Byte |
    PackSH1Ushort |
    PackSH1Uint |
    PackSH1Ulong |
    PackSH1Sbyte |
    PackSH1Short |
    PackSH1Int |
    PackSH1Long |
    PackSH1Float |
    PackSH1Double |
    PackSH1Decimal |
    PackSH1Char |
    PackSH1String |
    PackSH1Uri |
    PackSH1Bool2 |
    PackSH1Byte2 |
    PackSH1Ushort2 |
    PackSH1Uint2 |
    PackSH1Ulong2 |
    PackSH1Sbyte2 |
    PackSH1Short2 |
    PackSH1Int2 |
    PackSH1Long2 |
    PackSH1Float2 |
    PackSH1Double2 |
    PackSH1Bool3 |
    PackSH1Byte3 |
    PackSH1Ushort3 |
    PackSH1Uint3 |
    PackSH1Ulong3 |
    PackSH1Sbyte3 |
    PackSH1Short3 |
    PackSH1Int3 |
    PackSH1Long3 |
    PackSH1Float3 |
    PackSH1Double3 |
    PackSH1Bool4 |
    PackSH1Byte4 |
    PackSH1Ushort4 |
    PackSH1Uint4 |
    PackSH1Ulong4 |
    PackSH1Sbyte4 |
    PackSH1Short4 |
    PackSH1Int4 |
    PackSH1Long4 |
    PackSH1Float4 |
    PackSH1Double4 |
    PackSH1Float_2x2 |
    PackSH1Double_2x2 |
    PackSH1Float_3x3 |
    PackSH1Double_3x3 |
    PackSH1Float_4x4 |
    PackSH1Double_4x4 |
    PackSH1FloatQ |
    PackSH1DoubleQ |
    PackSH1DateTime |
    PackSH1TimeSpan |
    PackSH1Color |
    PackSH1ColorX |
    PackSH1ShadowCastMode |
    PackSH1LightType |
    PackSH1SessionAccessLevel |
    PackSH1Key |
    PackSH1HttpStatusCode |
    PackSH1HeadOutputDevice |
    PackSH1ReflectionProbeClear |
    PackSH1ReflectionProbeType |
    PackSH1ReflectionProbeTimeSlicingMode |
    PackSH1CameraClearMode |
    PackSH1CameraPositioningMode |
    PackSH1CameraProjection |
    PackSH1ZWrite |
    PackSH1ZTest |
    PackSH1Blend |
    PackSH1BlendMode |
    PackSH1Culling |
    PackSH1BodyNode |
    PackSH1Chirality |
    PackSH1DummyEnum
)