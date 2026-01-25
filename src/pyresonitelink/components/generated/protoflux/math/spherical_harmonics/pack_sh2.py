"""Generated component: PackSH2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackSH2Base(GeneratedComponent):
    """Base class for PackSH2<T> variants."""

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
class PackSH2Bool(PackSH2Base):
    """PackSH2<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class PackSH2Byte(PackSH2Base):
    """PackSH2<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class PackSH2Ushort(PackSH2Base):
    """PackSH2<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class PackSH2Uint(PackSH2Base):
    """PackSH2<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class PackSH2Ulong(PackSH2Base):
    """PackSH2<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class PackSH2Sbyte(PackSH2Base):
    """PackSH2<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class PackSH2Short(PackSH2Base):
    """PackSH2<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class PackSH2Int(PackSH2Base):
    """PackSH2<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class PackSH2Long(PackSH2Base):
    """PackSH2<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class PackSH2Float(PackSH2Base):
    """PackSH2<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class PackSH2Double(PackSH2Base):
    """PackSH2<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class PackSH2Decimal(PackSH2Base):
    """PackSH2<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class PackSH2Char(PackSH2Base):
    """PackSH2<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class PackSH2String(PackSH2Base):
    """PackSH2<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class PackSH2Uri(PackSH2Base):
    """PackSH2<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class PackSH2Bool2(PackSH2Base):
    """PackSH2<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class PackSH2Byte2(PackSH2Base):
    """PackSH2<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class PackSH2Ushort2(PackSH2Base):
    """PackSH2<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class PackSH2Uint2(PackSH2Base):
    """PackSH2<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class PackSH2Ulong2(PackSH2Base):
    """PackSH2<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class PackSH2Sbyte2(PackSH2Base):
    """PackSH2<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class PackSH2Short2(PackSH2Base):
    """PackSH2<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class PackSH2Int2(PackSH2Base):
    """PackSH2<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class PackSH2Long2(PackSH2Base):
    """PackSH2<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class PackSH2Float2(PackSH2Base):
    """PackSH2<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class PackSH2Double2(PackSH2Base):
    """PackSH2<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class PackSH2Bool3(PackSH2Base):
    """PackSH2<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class PackSH2Byte3(PackSH2Base):
    """PackSH2<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class PackSH2Ushort3(PackSH2Base):
    """PackSH2<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class PackSH2Uint3(PackSH2Base):
    """PackSH2<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class PackSH2Ulong3(PackSH2Base):
    """PackSH2<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class PackSH2Sbyte3(PackSH2Base):
    """PackSH2<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class PackSH2Short3(PackSH2Base):
    """PackSH2<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class PackSH2Int3(PackSH2Base):
    """PackSH2<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class PackSH2Long3(PackSH2Base):
    """PackSH2<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class PackSH2Float3(PackSH2Base):
    """PackSH2<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class PackSH2Double3(PackSH2Base):
    """PackSH2<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class PackSH2Bool4(PackSH2Base):
    """PackSH2<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class PackSH2Byte4(PackSH2Base):
    """PackSH2<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class PackSH2Ushort4(PackSH2Base):
    """PackSH2<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class PackSH2Uint4(PackSH2Base):
    """PackSH2<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class PackSH2Ulong4(PackSH2Base):
    """PackSH2<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class PackSH2Sbyte4(PackSH2Base):
    """PackSH2<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class PackSH2Short4(PackSH2Base):
    """PackSH2<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class PackSH2Int4(PackSH2Base):
    """PackSH2<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class PackSH2Long4(PackSH2Base):
    """PackSH2<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class PackSH2Float4(PackSH2Base):
    """PackSH2<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class PackSH2Double4(PackSH2Base):
    """PackSH2<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class PackSH2Float_2x2(PackSH2Base):
    """PackSH2<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class PackSH2Double_2x2(PackSH2Base):
    """PackSH2<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class PackSH2Float_3x3(PackSH2Base):
    """PackSH2<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class PackSH2Double_3x3(PackSH2Base):
    """PackSH2<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class PackSH2Float_4x4(PackSH2Base):
    """PackSH2<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class PackSH2Double_4x4(PackSH2Base):
    """PackSH2<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class PackSH2FloatQ(PackSH2Base):
    """PackSH2<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class PackSH2DoubleQ(PackSH2Base):
    """PackSH2<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class PackSH2DateTime(PackSH2Base):
    """PackSH2<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class PackSH2TimeSpan(PackSH2Base):
    """PackSH2<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class PackSH2Color(PackSH2Base):
    """PackSH2<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class PackSH2ColorX(PackSH2Base):
    """PackSH2<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class PackSH2ShadowCastMode(PackSH2Base):
    """PackSH2<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class PackSH2LightType(PackSH2Base):
    """PackSH2<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class PackSH2SessionAccessLevel(PackSH2Base):
    """PackSH2<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class PackSH2Key(PackSH2Base):
    """PackSH2<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class PackSH2HttpStatusCode(PackSH2Base):
    """PackSH2<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class PackSH2HeadOutputDevice(PackSH2Base):
    """PackSH2<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class PackSH2ReflectionProbeClear(PackSH2Base):
    """PackSH2<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class PackSH2ReflectionProbeType(PackSH2Base):
    """PackSH2<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class PackSH2ReflectionProbeTimeSlicingMode(PackSH2Base):
    """PackSH2<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class PackSH2CameraClearMode(PackSH2Base):
    """PackSH2<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class PackSH2CameraPositioningMode(PackSH2Base):
    """PackSH2<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class PackSH2CameraProjection(PackSH2Base):
    """PackSH2<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class PackSH2ZWrite(PackSH2Base):
    """PackSH2<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class PackSH2ZTest(PackSH2Base):
    """PackSH2<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class PackSH2Blend(PackSH2Base):
    """PackSH2<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class PackSH2BlendMode(PackSH2Base):
    """PackSH2<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class PackSH2Culling(PackSH2Base):
    """PackSH2<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class PackSH2BodyNode(PackSH2Base):
    """PackSH2<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class PackSH2Chirality(PackSH2Base):
    """PackSH2<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class PackSH2DummyEnum(PackSH2Base):
    """PackSH2<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH2<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any PackSH2 variant
PackSH2 = (
    PackSH2Bool |
    PackSH2Byte |
    PackSH2Ushort |
    PackSH2Uint |
    PackSH2Ulong |
    PackSH2Sbyte |
    PackSH2Short |
    PackSH2Int |
    PackSH2Long |
    PackSH2Float |
    PackSH2Double |
    PackSH2Decimal |
    PackSH2Char |
    PackSH2String |
    PackSH2Uri |
    PackSH2Bool2 |
    PackSH2Byte2 |
    PackSH2Ushort2 |
    PackSH2Uint2 |
    PackSH2Ulong2 |
    PackSH2Sbyte2 |
    PackSH2Short2 |
    PackSH2Int2 |
    PackSH2Long2 |
    PackSH2Float2 |
    PackSH2Double2 |
    PackSH2Bool3 |
    PackSH2Byte3 |
    PackSH2Ushort3 |
    PackSH2Uint3 |
    PackSH2Ulong3 |
    PackSH2Sbyte3 |
    PackSH2Short3 |
    PackSH2Int3 |
    PackSH2Long3 |
    PackSH2Float3 |
    PackSH2Double3 |
    PackSH2Bool4 |
    PackSH2Byte4 |
    PackSH2Ushort4 |
    PackSH2Uint4 |
    PackSH2Ulong4 |
    PackSH2Sbyte4 |
    PackSH2Short4 |
    PackSH2Int4 |
    PackSH2Long4 |
    PackSH2Float4 |
    PackSH2Double4 |
    PackSH2Float_2x2 |
    PackSH2Double_2x2 |
    PackSH2Float_3x3 |
    PackSH2Double_3x3 |
    PackSH2Float_4x4 |
    PackSH2Double_4x4 |
    PackSH2FloatQ |
    PackSH2DoubleQ |
    PackSH2DateTime |
    PackSH2TimeSpan |
    PackSH2Color |
    PackSH2ColorX |
    PackSH2ShadowCastMode |
    PackSH2LightType |
    PackSH2SessionAccessLevel |
    PackSH2Key |
    PackSH2HttpStatusCode |
    PackSH2HeadOutputDevice |
    PackSH2ReflectionProbeClear |
    PackSH2ReflectionProbeType |
    PackSH2ReflectionProbeTimeSlicingMode |
    PackSH2CameraClearMode |
    PackSH2CameraPositioningMode |
    PackSH2CameraProjection |
    PackSH2ZWrite |
    PackSH2ZTest |
    PackSH2Blend |
    PackSH2BlendMode |
    PackSH2Culling |
    PackSH2BodyNode |
    PackSH2Chirality |
    PackSH2DummyEnum
)