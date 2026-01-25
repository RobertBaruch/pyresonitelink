"""Generated component: ScaleOrdersSH4.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ScaleOrdersSH4Base(GeneratedComponent):
    """Base class for ScaleOrdersSH4<T> variants."""

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
class ScaleOrdersSH4Bool(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Byte(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ushort(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Uint(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ulong(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Sbyte(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Short(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Int(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Long(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Decimal(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Char(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4String(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Uri(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Bool2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Byte2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ushort2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Uint2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ulong2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Sbyte2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Short2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Int2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Long2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Bool3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Byte3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ushort3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Uint3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ulong3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Sbyte3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Short3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Int3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Long3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Bool4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Byte4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ushort4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Uint4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Ulong4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Sbyte4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Short4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Int4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Long4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float_2x2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double_2x2(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float_3x3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double_3x3(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Float_4x4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Double_4x4(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4FloatQ(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4DoubleQ(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4DateTime(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4TimeSpan(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Color(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ColorX(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ShadowCastMode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4LightType(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4SessionAccessLevel(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Key(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4HttpStatusCode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4HeadOutputDevice(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ReflectionProbeClear(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ReflectionProbeType(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ReflectionProbeTimeSlicingMode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4CameraClearMode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4CameraPositioningMode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4CameraProjection(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ZWrite(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4ZTest(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Blend(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4BlendMode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Culling(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4BodyNode(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4Chirality(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


@dataclass
class ScaleOrdersSH4DummyEnum(ScaleOrdersSH4Base):
    """ScaleOrdersSH4<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH4<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "order4": "Order4",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order4: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL4`1>


# Type alias for any ScaleOrdersSH4 variant
ScaleOrdersSH4 = (
    ScaleOrdersSH4Bool |
    ScaleOrdersSH4Byte |
    ScaleOrdersSH4Ushort |
    ScaleOrdersSH4Uint |
    ScaleOrdersSH4Ulong |
    ScaleOrdersSH4Sbyte |
    ScaleOrdersSH4Short |
    ScaleOrdersSH4Int |
    ScaleOrdersSH4Long |
    ScaleOrdersSH4Float |
    ScaleOrdersSH4Double |
    ScaleOrdersSH4Decimal |
    ScaleOrdersSH4Char |
    ScaleOrdersSH4String |
    ScaleOrdersSH4Uri |
    ScaleOrdersSH4Bool2 |
    ScaleOrdersSH4Byte2 |
    ScaleOrdersSH4Ushort2 |
    ScaleOrdersSH4Uint2 |
    ScaleOrdersSH4Ulong2 |
    ScaleOrdersSH4Sbyte2 |
    ScaleOrdersSH4Short2 |
    ScaleOrdersSH4Int2 |
    ScaleOrdersSH4Long2 |
    ScaleOrdersSH4Float2 |
    ScaleOrdersSH4Double2 |
    ScaleOrdersSH4Bool3 |
    ScaleOrdersSH4Byte3 |
    ScaleOrdersSH4Ushort3 |
    ScaleOrdersSH4Uint3 |
    ScaleOrdersSH4Ulong3 |
    ScaleOrdersSH4Sbyte3 |
    ScaleOrdersSH4Short3 |
    ScaleOrdersSH4Int3 |
    ScaleOrdersSH4Long3 |
    ScaleOrdersSH4Float3 |
    ScaleOrdersSH4Double3 |
    ScaleOrdersSH4Bool4 |
    ScaleOrdersSH4Byte4 |
    ScaleOrdersSH4Ushort4 |
    ScaleOrdersSH4Uint4 |
    ScaleOrdersSH4Ulong4 |
    ScaleOrdersSH4Sbyte4 |
    ScaleOrdersSH4Short4 |
    ScaleOrdersSH4Int4 |
    ScaleOrdersSH4Long4 |
    ScaleOrdersSH4Float4 |
    ScaleOrdersSH4Double4 |
    ScaleOrdersSH4Float_2x2 |
    ScaleOrdersSH4Double_2x2 |
    ScaleOrdersSH4Float_3x3 |
    ScaleOrdersSH4Double_3x3 |
    ScaleOrdersSH4Float_4x4 |
    ScaleOrdersSH4Double_4x4 |
    ScaleOrdersSH4FloatQ |
    ScaleOrdersSH4DoubleQ |
    ScaleOrdersSH4DateTime |
    ScaleOrdersSH4TimeSpan |
    ScaleOrdersSH4Color |
    ScaleOrdersSH4ColorX |
    ScaleOrdersSH4ShadowCastMode |
    ScaleOrdersSH4LightType |
    ScaleOrdersSH4SessionAccessLevel |
    ScaleOrdersSH4Key |
    ScaleOrdersSH4HttpStatusCode |
    ScaleOrdersSH4HeadOutputDevice |
    ScaleOrdersSH4ReflectionProbeClear |
    ScaleOrdersSH4ReflectionProbeType |
    ScaleOrdersSH4ReflectionProbeTimeSlicingMode |
    ScaleOrdersSH4CameraClearMode |
    ScaleOrdersSH4CameraPositioningMode |
    ScaleOrdersSH4CameraProjection |
    ScaleOrdersSH4ZWrite |
    ScaleOrdersSH4ZTest |
    ScaleOrdersSH4Blend |
    ScaleOrdersSH4BlendMode |
    ScaleOrdersSH4Culling |
    ScaleOrdersSH4BodyNode |
    ScaleOrdersSH4Chirality |
    ScaleOrdersSH4DummyEnum
)