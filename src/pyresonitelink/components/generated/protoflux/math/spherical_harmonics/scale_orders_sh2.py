"""Generated component: ScaleOrdersSH2.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ScaleOrdersSH2Base(GeneratedComponent):
    """Base class for ScaleOrdersSH2<T> variants."""

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
class ScaleOrdersSH2Bool(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Byte(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ushort(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Uint(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ulong(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Sbyte(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Short(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Int(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Long(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Decimal(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Char(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2String(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Uri(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Bool2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Byte2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ushort2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Uint2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ulong2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Sbyte2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Short2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Int2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Long2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Bool3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Byte3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ushort3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Uint3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ulong3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Sbyte3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Short3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Int3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Long3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Bool4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Byte4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ushort4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Uint4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Ulong4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Sbyte4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Short4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Int4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Long4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float_2x2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double_2x2(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float_3x3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double_3x3(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Float_4x4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Double_4x4(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2FloatQ(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2DoubleQ(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2DateTime(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2TimeSpan(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Color(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ColorX(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ShadowCastMode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2LightType(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2SessionAccessLevel(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Key(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2HttpStatusCode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2HeadOutputDevice(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ReflectionProbeClear(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ReflectionProbeType(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ReflectionProbeTimeSlicingMode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2CameraClearMode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2CameraPositioningMode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2CameraProjection(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ZWrite(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2ZTest(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Blend(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2BlendMode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Culling(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2BodyNode(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2Chirality(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


@dataclass
class ScaleOrdersSH2DummyEnum(ScaleOrdersSH2Base):
    """ScaleOrdersSH2<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH2<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "order2": "Order2",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order2: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL2`1>


# Type alias for any ScaleOrdersSH2 variant
ScaleOrdersSH2 = (
    ScaleOrdersSH2Bool |
    ScaleOrdersSH2Byte |
    ScaleOrdersSH2Ushort |
    ScaleOrdersSH2Uint |
    ScaleOrdersSH2Ulong |
    ScaleOrdersSH2Sbyte |
    ScaleOrdersSH2Short |
    ScaleOrdersSH2Int |
    ScaleOrdersSH2Long |
    ScaleOrdersSH2Float |
    ScaleOrdersSH2Double |
    ScaleOrdersSH2Decimal |
    ScaleOrdersSH2Char |
    ScaleOrdersSH2String |
    ScaleOrdersSH2Uri |
    ScaleOrdersSH2Bool2 |
    ScaleOrdersSH2Byte2 |
    ScaleOrdersSH2Ushort2 |
    ScaleOrdersSH2Uint2 |
    ScaleOrdersSH2Ulong2 |
    ScaleOrdersSH2Sbyte2 |
    ScaleOrdersSH2Short2 |
    ScaleOrdersSH2Int2 |
    ScaleOrdersSH2Long2 |
    ScaleOrdersSH2Float2 |
    ScaleOrdersSH2Double2 |
    ScaleOrdersSH2Bool3 |
    ScaleOrdersSH2Byte3 |
    ScaleOrdersSH2Ushort3 |
    ScaleOrdersSH2Uint3 |
    ScaleOrdersSH2Ulong3 |
    ScaleOrdersSH2Sbyte3 |
    ScaleOrdersSH2Short3 |
    ScaleOrdersSH2Int3 |
    ScaleOrdersSH2Long3 |
    ScaleOrdersSH2Float3 |
    ScaleOrdersSH2Double3 |
    ScaleOrdersSH2Bool4 |
    ScaleOrdersSH2Byte4 |
    ScaleOrdersSH2Ushort4 |
    ScaleOrdersSH2Uint4 |
    ScaleOrdersSH2Ulong4 |
    ScaleOrdersSH2Sbyte4 |
    ScaleOrdersSH2Short4 |
    ScaleOrdersSH2Int4 |
    ScaleOrdersSH2Long4 |
    ScaleOrdersSH2Float4 |
    ScaleOrdersSH2Double4 |
    ScaleOrdersSH2Float_2x2 |
    ScaleOrdersSH2Double_2x2 |
    ScaleOrdersSH2Float_3x3 |
    ScaleOrdersSH2Double_3x3 |
    ScaleOrdersSH2Float_4x4 |
    ScaleOrdersSH2Double_4x4 |
    ScaleOrdersSH2FloatQ |
    ScaleOrdersSH2DoubleQ |
    ScaleOrdersSH2DateTime |
    ScaleOrdersSH2TimeSpan |
    ScaleOrdersSH2Color |
    ScaleOrdersSH2ColorX |
    ScaleOrdersSH2ShadowCastMode |
    ScaleOrdersSH2LightType |
    ScaleOrdersSH2SessionAccessLevel |
    ScaleOrdersSH2Key |
    ScaleOrdersSH2HttpStatusCode |
    ScaleOrdersSH2HeadOutputDevice |
    ScaleOrdersSH2ReflectionProbeClear |
    ScaleOrdersSH2ReflectionProbeType |
    ScaleOrdersSH2ReflectionProbeTimeSlicingMode |
    ScaleOrdersSH2CameraClearMode |
    ScaleOrdersSH2CameraPositioningMode |
    ScaleOrdersSH2CameraProjection |
    ScaleOrdersSH2ZWrite |
    ScaleOrdersSH2ZTest |
    ScaleOrdersSH2Blend |
    ScaleOrdersSH2BlendMode |
    ScaleOrdersSH2Culling |
    ScaleOrdersSH2BodyNode |
    ScaleOrdersSH2Chirality |
    ScaleOrdersSH2DummyEnum
)