"""Generated component: PackSH3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackSH3Base(GeneratedComponent):
    """Base class for PackSH3<T> variants."""

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
class PackSH3Bool(PackSH3Base):
    """PackSH3<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class PackSH3Byte(PackSH3Base):
    """PackSH3<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class PackSH3Ushort(PackSH3Base):
    """PackSH3<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class PackSH3Uint(PackSH3Base):
    """PackSH3<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class PackSH3Ulong(PackSH3Base):
    """PackSH3<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class PackSH3Sbyte(PackSH3Base):
    """PackSH3<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class PackSH3Short(PackSH3Base):
    """PackSH3<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class PackSH3Int(PackSH3Base):
    """PackSH3<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class PackSH3Long(PackSH3Base):
    """PackSH3<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class PackSH3Float(PackSH3Base):
    """PackSH3<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class PackSH3Double(PackSH3Base):
    """PackSH3<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class PackSH3Decimal(PackSH3Base):
    """PackSH3<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class PackSH3Char(PackSH3Base):
    """PackSH3<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class PackSH3String(PackSH3Base):
    """PackSH3<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class PackSH3Uri(PackSH3Base):
    """PackSH3<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class PackSH3Bool2(PackSH3Base):
    """PackSH3<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class PackSH3Byte2(PackSH3Base):
    """PackSH3<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class PackSH3Ushort2(PackSH3Base):
    """PackSH3<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class PackSH3Uint2(PackSH3Base):
    """PackSH3<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class PackSH3Ulong2(PackSH3Base):
    """PackSH3<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class PackSH3Sbyte2(PackSH3Base):
    """PackSH3<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class PackSH3Short2(PackSH3Base):
    """PackSH3<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class PackSH3Int2(PackSH3Base):
    """PackSH3<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class PackSH3Long2(PackSH3Base):
    """PackSH3<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class PackSH3Float2(PackSH3Base):
    """PackSH3<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class PackSH3Double2(PackSH3Base):
    """PackSH3<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class PackSH3Bool3(PackSH3Base):
    """PackSH3<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class PackSH3Byte3(PackSH3Base):
    """PackSH3<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class PackSH3Ushort3(PackSH3Base):
    """PackSH3<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class PackSH3Uint3(PackSH3Base):
    """PackSH3<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class PackSH3Ulong3(PackSH3Base):
    """PackSH3<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class PackSH3Sbyte3(PackSH3Base):
    """PackSH3<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class PackSH3Short3(PackSH3Base):
    """PackSH3<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class PackSH3Int3(PackSH3Base):
    """PackSH3<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class PackSH3Long3(PackSH3Base):
    """PackSH3<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class PackSH3Float3(PackSH3Base):
    """PackSH3<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class PackSH3Double3(PackSH3Base):
    """PackSH3<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class PackSH3Bool4(PackSH3Base):
    """PackSH3<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class PackSH3Byte4(PackSH3Base):
    """PackSH3<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class PackSH3Ushort4(PackSH3Base):
    """PackSH3<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class PackSH3Uint4(PackSH3Base):
    """PackSH3<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class PackSH3Ulong4(PackSH3Base):
    """PackSH3<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class PackSH3Sbyte4(PackSH3Base):
    """PackSH3<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class PackSH3Short4(PackSH3Base):
    """PackSH3<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class PackSH3Int4(PackSH3Base):
    """PackSH3<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class PackSH3Long4(PackSH3Base):
    """PackSH3<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class PackSH3Float4(PackSH3Base):
    """PackSH3<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class PackSH3Double4(PackSH3Base):
    """PackSH3<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class PackSH3Float_2x2(PackSH3Base):
    """PackSH3<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class PackSH3Double_2x2(PackSH3Base):
    """PackSH3<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class PackSH3Float_3x3(PackSH3Base):
    """PackSH3<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class PackSH3Double_3x3(PackSH3Base):
    """PackSH3<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class PackSH3Float_4x4(PackSH3Base):
    """PackSH3<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class PackSH3Double_4x4(PackSH3Base):
    """PackSH3<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class PackSH3FloatQ(PackSH3Base):
    """PackSH3<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class PackSH3DoubleQ(PackSH3Base):
    """PackSH3<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class PackSH3DateTime(PackSH3Base):
    """PackSH3<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class PackSH3TimeSpan(PackSH3Base):
    """PackSH3<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class PackSH3Color(PackSH3Base):
    """PackSH3<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class PackSH3ColorX(PackSH3Base):
    """PackSH3<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class PackSH3ShadowCastMode(PackSH3Base):
    """PackSH3<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class PackSH3LightType(PackSH3Base):
    """PackSH3<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class PackSH3SessionAccessLevel(PackSH3Base):
    """PackSH3<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class PackSH3Key(PackSH3Base):
    """PackSH3<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class PackSH3HttpStatusCode(PackSH3Base):
    """PackSH3<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class PackSH3HeadOutputDevice(PackSH3Base):
    """PackSH3<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class PackSH3ReflectionProbeClear(PackSH3Base):
    """PackSH3<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class PackSH3ReflectionProbeType(PackSH3Base):
    """PackSH3<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class PackSH3ReflectionProbeTimeSlicingMode(PackSH3Base):
    """PackSH3<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class PackSH3CameraClearMode(PackSH3Base):
    """PackSH3<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class PackSH3CameraPositioningMode(PackSH3Base):
    """PackSH3<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class PackSH3CameraProjection(PackSH3Base):
    """PackSH3<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class PackSH3ZWrite(PackSH3Base):
    """PackSH3<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class PackSH3ZTest(PackSH3Base):
    """PackSH3<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class PackSH3Blend(PackSH3Base):
    """PackSH3<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class PackSH3BlendMode(PackSH3Base):
    """PackSH3<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class PackSH3Culling(PackSH3Base):
    """PackSH3<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class PackSH3BodyNode(PackSH3Base):
    """PackSH3<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class PackSH3Chirality(PackSH3Base):
    """PackSH3<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class PackSH3DummyEnum(PackSH3Base):
    """PackSH3<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.PackSH3<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "sh0": "SH0",
        "sh1": "SH1",
        "sh10": "SH10",
        "sh11": "SH11",
        "sh12": "SH12",
        "sh13": "SH13",
        "sh14": "SH14",
        "sh15": "SH15",
        "sh2": "SH2",
        "sh3": "SH3",
        "sh4": "SH4",
        "sh5": "SH5",
        "sh6": "SH6",
        "sh7": "SH7",
        "sh8": "SH8",
        "sh9": "SH9",
    }

    sh0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh10: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh11: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh12: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh13: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh14: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh15: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh5: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh6: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh7: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh8: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    sh9: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any PackSH3 variant
PackSH3 = (
    PackSH3Bool |
    PackSH3Byte |
    PackSH3Ushort |
    PackSH3Uint |
    PackSH3Ulong |
    PackSH3Sbyte |
    PackSH3Short |
    PackSH3Int |
    PackSH3Long |
    PackSH3Float |
    PackSH3Double |
    PackSH3Decimal |
    PackSH3Char |
    PackSH3String |
    PackSH3Uri |
    PackSH3Bool2 |
    PackSH3Byte2 |
    PackSH3Ushort2 |
    PackSH3Uint2 |
    PackSH3Ulong2 |
    PackSH3Sbyte2 |
    PackSH3Short2 |
    PackSH3Int2 |
    PackSH3Long2 |
    PackSH3Float2 |
    PackSH3Double2 |
    PackSH3Bool3 |
    PackSH3Byte3 |
    PackSH3Ushort3 |
    PackSH3Uint3 |
    PackSH3Ulong3 |
    PackSH3Sbyte3 |
    PackSH3Short3 |
    PackSH3Int3 |
    PackSH3Long3 |
    PackSH3Float3 |
    PackSH3Double3 |
    PackSH3Bool4 |
    PackSH3Byte4 |
    PackSH3Ushort4 |
    PackSH3Uint4 |
    PackSH3Ulong4 |
    PackSH3Sbyte4 |
    PackSH3Short4 |
    PackSH3Int4 |
    PackSH3Long4 |
    PackSH3Float4 |
    PackSH3Double4 |
    PackSH3Float_2x2 |
    PackSH3Double_2x2 |
    PackSH3Float_3x3 |
    PackSH3Double_3x3 |
    PackSH3Float_4x4 |
    PackSH3Double_4x4 |
    PackSH3FloatQ |
    PackSH3DoubleQ |
    PackSH3DateTime |
    PackSH3TimeSpan |
    PackSH3Color |
    PackSH3ColorX |
    PackSH3ShadowCastMode |
    PackSH3LightType |
    PackSH3SessionAccessLevel |
    PackSH3Key |
    PackSH3HttpStatusCode |
    PackSH3HeadOutputDevice |
    PackSH3ReflectionProbeClear |
    PackSH3ReflectionProbeType |
    PackSH3ReflectionProbeTimeSlicingMode |
    PackSH3CameraClearMode |
    PackSH3CameraPositioningMode |
    PackSH3CameraProjection |
    PackSH3ZWrite |
    PackSH3ZTest |
    PackSH3Blend |
    PackSH3BlendMode |
    PackSH3Culling |
    PackSH3BodyNode |
    PackSH3Chirality |
    PackSH3DummyEnum
)