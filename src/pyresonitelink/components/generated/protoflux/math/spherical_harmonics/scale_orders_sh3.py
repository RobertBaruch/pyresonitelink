"""Generated component: ScaleOrdersSH3.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ScaleOrdersSH3Base(GeneratedComponent):
    """Base class for ScaleOrdersSH3<T> variants."""

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
class ScaleOrdersSH3Bool(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Byte(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ushort(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Uint(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ulong(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Sbyte(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Short(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Int(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Long(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Decimal(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Char(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3String(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Uri(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Bool2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Byte2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ushort2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Uint2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ulong2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Sbyte2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Short2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Int2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Long2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Bool3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Byte3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ushort3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Uint3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ulong3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Sbyte3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Short3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Int3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Long3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Bool4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Byte4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ushort4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Uint4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Ulong4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Sbyte4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Short4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Int4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Long4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float_2x2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double_2x2(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float_3x3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double_3x3(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Float_4x4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Double_4x4(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3FloatQ(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3DoubleQ(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3DateTime(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3TimeSpan(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Color(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ColorX(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ShadowCastMode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3LightType(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3SessionAccessLevel(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Key(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3HttpStatusCode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3HeadOutputDevice(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ReflectionProbeClear(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ReflectionProbeType(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ReflectionProbeTimeSlicingMode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3CameraClearMode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3CameraPositioningMode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3CameraProjection(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ZWrite(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3ZTest(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Blend(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3BlendMode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Culling(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3BodyNode(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3Chirality(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


@dataclass
class ScaleOrdersSH3DummyEnum(ScaleOrdersSH3Base):
    """ScaleOrdersSH3<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH3<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "order3": "Order3",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order3: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL3`1>


# Type alias for any ScaleOrdersSH3 variant
ScaleOrdersSH3 = (
    ScaleOrdersSH3Bool |
    ScaleOrdersSH3Byte |
    ScaleOrdersSH3Ushort |
    ScaleOrdersSH3Uint |
    ScaleOrdersSH3Ulong |
    ScaleOrdersSH3Sbyte |
    ScaleOrdersSH3Short |
    ScaleOrdersSH3Int |
    ScaleOrdersSH3Long |
    ScaleOrdersSH3Float |
    ScaleOrdersSH3Double |
    ScaleOrdersSH3Decimal |
    ScaleOrdersSH3Char |
    ScaleOrdersSH3String |
    ScaleOrdersSH3Uri |
    ScaleOrdersSH3Bool2 |
    ScaleOrdersSH3Byte2 |
    ScaleOrdersSH3Ushort2 |
    ScaleOrdersSH3Uint2 |
    ScaleOrdersSH3Ulong2 |
    ScaleOrdersSH3Sbyte2 |
    ScaleOrdersSH3Short2 |
    ScaleOrdersSH3Int2 |
    ScaleOrdersSH3Long2 |
    ScaleOrdersSH3Float2 |
    ScaleOrdersSH3Double2 |
    ScaleOrdersSH3Bool3 |
    ScaleOrdersSH3Byte3 |
    ScaleOrdersSH3Ushort3 |
    ScaleOrdersSH3Uint3 |
    ScaleOrdersSH3Ulong3 |
    ScaleOrdersSH3Sbyte3 |
    ScaleOrdersSH3Short3 |
    ScaleOrdersSH3Int3 |
    ScaleOrdersSH3Long3 |
    ScaleOrdersSH3Float3 |
    ScaleOrdersSH3Double3 |
    ScaleOrdersSH3Bool4 |
    ScaleOrdersSH3Byte4 |
    ScaleOrdersSH3Ushort4 |
    ScaleOrdersSH3Uint4 |
    ScaleOrdersSH3Ulong4 |
    ScaleOrdersSH3Sbyte4 |
    ScaleOrdersSH3Short4 |
    ScaleOrdersSH3Int4 |
    ScaleOrdersSH3Long4 |
    ScaleOrdersSH3Float4 |
    ScaleOrdersSH3Double4 |
    ScaleOrdersSH3Float_2x2 |
    ScaleOrdersSH3Double_2x2 |
    ScaleOrdersSH3Float_3x3 |
    ScaleOrdersSH3Double_3x3 |
    ScaleOrdersSH3Float_4x4 |
    ScaleOrdersSH3Double_4x4 |
    ScaleOrdersSH3FloatQ |
    ScaleOrdersSH3DoubleQ |
    ScaleOrdersSH3DateTime |
    ScaleOrdersSH3TimeSpan |
    ScaleOrdersSH3Color |
    ScaleOrdersSH3ColorX |
    ScaleOrdersSH3ShadowCastMode |
    ScaleOrdersSH3LightType |
    ScaleOrdersSH3SessionAccessLevel |
    ScaleOrdersSH3Key |
    ScaleOrdersSH3HttpStatusCode |
    ScaleOrdersSH3HeadOutputDevice |
    ScaleOrdersSH3ReflectionProbeClear |
    ScaleOrdersSH3ReflectionProbeType |
    ScaleOrdersSH3ReflectionProbeTimeSlicingMode |
    ScaleOrdersSH3CameraClearMode |
    ScaleOrdersSH3CameraPositioningMode |
    ScaleOrdersSH3CameraProjection |
    ScaleOrdersSH3ZWrite |
    ScaleOrdersSH3ZTest |
    ScaleOrdersSH3Blend |
    ScaleOrdersSH3BlendMode |
    ScaleOrdersSH3Culling |
    ScaleOrdersSH3BodyNode |
    ScaleOrdersSH3Chirality |
    ScaleOrdersSH3DummyEnum
)