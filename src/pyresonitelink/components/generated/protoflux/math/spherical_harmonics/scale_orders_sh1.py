"""Generated component: ScaleOrdersSH1.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ScaleOrdersSH1Base(GeneratedComponent):
    """Base class for ScaleOrdersSH1<T> variants."""

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
class ScaleOrdersSH1Bool(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Byte(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ushort(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Uint(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ulong(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Sbyte(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Short(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Int(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Long(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Decimal(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Char(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1String(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Uri(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Bool2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Byte2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ushort2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Uint2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ulong2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Sbyte2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Short2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Int2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Long2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Bool3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Byte3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ushort3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Uint3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ulong3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Sbyte3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Short3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Int3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Long3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Bool4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Byte4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ushort4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Uint4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Ulong4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Sbyte4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Short4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Int4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Long4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float_2x2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double_2x2(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float_3x3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double_3x3(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Float_4x4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Double_4x4(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1FloatQ(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1DoubleQ(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1DateTime(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1TimeSpan(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Color(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ColorX(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ShadowCastMode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1LightType(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1SessionAccessLevel(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Key(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1HttpStatusCode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1HeadOutputDevice(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ReflectionProbeClear(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ReflectionProbeType(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ReflectionProbeTimeSlicingMode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1CameraClearMode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1CameraPositioningMode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1CameraProjection(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ZWrite(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1ZTest(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Blend(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1BlendMode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Culling(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1BodyNode(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1Chirality(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


@dataclass
class ScaleOrdersSH1DummyEnum(ScaleOrdersSH1Base):
    """ScaleOrdersSH1<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.SphericalHarmonics.ScaleOrdersSH1<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "order0": "Order0",
        "order1": "Order1",
        "sh": "SH",
    }

    order0: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    order1: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    sh: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<SphericalHarmonicsL1`1>


# Type alias for any ScaleOrdersSH1 variant
ScaleOrdersSH1 = (
    ScaleOrdersSH1Bool |
    ScaleOrdersSH1Byte |
    ScaleOrdersSH1Ushort |
    ScaleOrdersSH1Uint |
    ScaleOrdersSH1Ulong |
    ScaleOrdersSH1Sbyte |
    ScaleOrdersSH1Short |
    ScaleOrdersSH1Int |
    ScaleOrdersSH1Long |
    ScaleOrdersSH1Float |
    ScaleOrdersSH1Double |
    ScaleOrdersSH1Decimal |
    ScaleOrdersSH1Char |
    ScaleOrdersSH1String |
    ScaleOrdersSH1Uri |
    ScaleOrdersSH1Bool2 |
    ScaleOrdersSH1Byte2 |
    ScaleOrdersSH1Ushort2 |
    ScaleOrdersSH1Uint2 |
    ScaleOrdersSH1Ulong2 |
    ScaleOrdersSH1Sbyte2 |
    ScaleOrdersSH1Short2 |
    ScaleOrdersSH1Int2 |
    ScaleOrdersSH1Long2 |
    ScaleOrdersSH1Float2 |
    ScaleOrdersSH1Double2 |
    ScaleOrdersSH1Bool3 |
    ScaleOrdersSH1Byte3 |
    ScaleOrdersSH1Ushort3 |
    ScaleOrdersSH1Uint3 |
    ScaleOrdersSH1Ulong3 |
    ScaleOrdersSH1Sbyte3 |
    ScaleOrdersSH1Short3 |
    ScaleOrdersSH1Int3 |
    ScaleOrdersSH1Long3 |
    ScaleOrdersSH1Float3 |
    ScaleOrdersSH1Double3 |
    ScaleOrdersSH1Bool4 |
    ScaleOrdersSH1Byte4 |
    ScaleOrdersSH1Ushort4 |
    ScaleOrdersSH1Uint4 |
    ScaleOrdersSH1Ulong4 |
    ScaleOrdersSH1Sbyte4 |
    ScaleOrdersSH1Short4 |
    ScaleOrdersSH1Int4 |
    ScaleOrdersSH1Long4 |
    ScaleOrdersSH1Float4 |
    ScaleOrdersSH1Double4 |
    ScaleOrdersSH1Float_2x2 |
    ScaleOrdersSH1Double_2x2 |
    ScaleOrdersSH1Float_3x3 |
    ScaleOrdersSH1Double_3x3 |
    ScaleOrdersSH1Float_4x4 |
    ScaleOrdersSH1Double_4x4 |
    ScaleOrdersSH1FloatQ |
    ScaleOrdersSH1DoubleQ |
    ScaleOrdersSH1DateTime |
    ScaleOrdersSH1TimeSpan |
    ScaleOrdersSH1Color |
    ScaleOrdersSH1ColorX |
    ScaleOrdersSH1ShadowCastMode |
    ScaleOrdersSH1LightType |
    ScaleOrdersSH1SessionAccessLevel |
    ScaleOrdersSH1Key |
    ScaleOrdersSH1HttpStatusCode |
    ScaleOrdersSH1HeadOutputDevice |
    ScaleOrdersSH1ReflectionProbeClear |
    ScaleOrdersSH1ReflectionProbeType |
    ScaleOrdersSH1ReflectionProbeTimeSlicingMode |
    ScaleOrdersSH1CameraClearMode |
    ScaleOrdersSH1CameraPositioningMode |
    ScaleOrdersSH1CameraProjection |
    ScaleOrdersSH1ZWrite |
    ScaleOrdersSH1ZTest |
    ScaleOrdersSH1Blend |
    ScaleOrdersSH1BlendMode |
    ScaleOrdersSH1Culling |
    ScaleOrdersSH1BodyNode |
    ScaleOrdersSH1Chirality |
    ScaleOrdersSH1DummyEnum
)