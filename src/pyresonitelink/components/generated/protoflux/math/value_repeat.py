"""Generated component: ValueRepeat.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueRepeatBase(GeneratedComponent):
    """Base class for ValueRepeat<T> variants."""

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
class ValueRepeatBool(ValueRepeatBase):
    """ValueRepeat<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueRepeatByte(ValueRepeatBase):
    """ValueRepeat<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueRepeatUshort(ValueRepeatBase):
    """ValueRepeat<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueRepeatUint(ValueRepeatBase):
    """ValueRepeat<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueRepeatUlong(ValueRepeatBase):
    """ValueRepeat<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueRepeatSbyte(ValueRepeatBase):
    """ValueRepeat<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueRepeatShort(ValueRepeatBase):
    """ValueRepeat<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueRepeatInt(ValueRepeatBase):
    """ValueRepeat<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueRepeatLong(ValueRepeatBase):
    """ValueRepeat<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueRepeatFloat(ValueRepeatBase):
    """ValueRepeat<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueRepeatDouble(ValueRepeatBase):
    """ValueRepeat<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueRepeatDecimal(ValueRepeatBase):
    """ValueRepeat<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueRepeatChar(ValueRepeatBase):
    """ValueRepeat<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueRepeatString(ValueRepeatBase):
    """ValueRepeat<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueRepeatUri(ValueRepeatBase):
    """ValueRepeat<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueRepeatBool2(ValueRepeatBase):
    """ValueRepeat<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueRepeatByte2(ValueRepeatBase):
    """ValueRepeat<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueRepeatUshort2(ValueRepeatBase):
    """ValueRepeat<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueRepeatUint2(ValueRepeatBase):
    """ValueRepeat<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueRepeatUlong2(ValueRepeatBase):
    """ValueRepeat<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueRepeatSbyte2(ValueRepeatBase):
    """ValueRepeat<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueRepeatShort2(ValueRepeatBase):
    """ValueRepeat<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueRepeatInt2(ValueRepeatBase):
    """ValueRepeat<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueRepeatLong2(ValueRepeatBase):
    """ValueRepeat<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueRepeatFloat2(ValueRepeatBase):
    """ValueRepeat<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueRepeatDouble2(ValueRepeatBase):
    """ValueRepeat<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueRepeatBool3(ValueRepeatBase):
    """ValueRepeat<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueRepeatByte3(ValueRepeatBase):
    """ValueRepeat<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueRepeatUshort3(ValueRepeatBase):
    """ValueRepeat<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueRepeatUint3(ValueRepeatBase):
    """ValueRepeat<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueRepeatUlong3(ValueRepeatBase):
    """ValueRepeat<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueRepeatSbyte3(ValueRepeatBase):
    """ValueRepeat<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueRepeatShort3(ValueRepeatBase):
    """ValueRepeat<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueRepeatInt3(ValueRepeatBase):
    """ValueRepeat<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueRepeatLong3(ValueRepeatBase):
    """ValueRepeat<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueRepeatFloat3(ValueRepeatBase):
    """ValueRepeat<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueRepeatDouble3(ValueRepeatBase):
    """ValueRepeat<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueRepeatBool4(ValueRepeatBase):
    """ValueRepeat<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueRepeatByte4(ValueRepeatBase):
    """ValueRepeat<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueRepeatUshort4(ValueRepeatBase):
    """ValueRepeat<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueRepeatUint4(ValueRepeatBase):
    """ValueRepeat<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueRepeatUlong4(ValueRepeatBase):
    """ValueRepeat<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueRepeatSbyte4(ValueRepeatBase):
    """ValueRepeat<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueRepeatShort4(ValueRepeatBase):
    """ValueRepeat<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueRepeatInt4(ValueRepeatBase):
    """ValueRepeat<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueRepeatLong4(ValueRepeatBase):
    """ValueRepeat<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueRepeatFloat4(ValueRepeatBase):
    """ValueRepeat<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueRepeatDouble4(ValueRepeatBase):
    """ValueRepeat<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueRepeatFloat_2x2(ValueRepeatBase):
    """ValueRepeat<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueRepeatDouble_2x2(ValueRepeatBase):
    """ValueRepeat<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueRepeatFloat_3x3(ValueRepeatBase):
    """ValueRepeat<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueRepeatDouble_3x3(ValueRepeatBase):
    """ValueRepeat<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueRepeatFloat_4x4(ValueRepeatBase):
    """ValueRepeat<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueRepeatDouble_4x4(ValueRepeatBase):
    """ValueRepeat<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueRepeatFloatQ(ValueRepeatBase):
    """ValueRepeat<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueRepeatDoubleQ(ValueRepeatBase):
    """ValueRepeat<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueRepeatDateTime(ValueRepeatBase):
    """ValueRepeat<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueRepeatTimeSpan(ValueRepeatBase):
    """ValueRepeat<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueRepeatColor(ValueRepeatBase):
    """ValueRepeat<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueRepeatColorX(ValueRepeatBase):
    """ValueRepeat<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueRepeatShadowCastMode(ValueRepeatBase):
    """ValueRepeat<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueRepeatLightType(ValueRepeatBase):
    """ValueRepeat<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueRepeatSessionAccessLevel(ValueRepeatBase):
    """ValueRepeat<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueRepeatKey(ValueRepeatBase):
    """ValueRepeat<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueRepeatHttpStatusCode(ValueRepeatBase):
    """ValueRepeat<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueRepeatHeadOutputDevice(ValueRepeatBase):
    """ValueRepeat<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueRepeatReflectionProbeClear(ValueRepeatBase):
    """ValueRepeat<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueRepeatReflectionProbeType(ValueRepeatBase):
    """ValueRepeat<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueRepeatReflectionProbeTimeSlicingMode(ValueRepeatBase):
    """ValueRepeat<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueRepeatCameraClearMode(ValueRepeatBase):
    """ValueRepeat<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueRepeatCameraPositioningMode(ValueRepeatBase):
    """ValueRepeat<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueRepeatCameraProjection(ValueRepeatBase):
    """ValueRepeat<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueRepeatZWrite(ValueRepeatBase):
    """ValueRepeat<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueRepeatZTest(ValueRepeatBase):
    """ValueRepeat<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueRepeatBlend(ValueRepeatBase):
    """ValueRepeat<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueRepeatBlendMode(ValueRepeatBase):
    """ValueRepeat<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueRepeatCulling(ValueRepeatBase):
    """ValueRepeat<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueRepeatBodyNode(ValueRepeatBase):
    """ValueRepeat<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueRepeatChirality(ValueRepeatBase):
    """ValueRepeat<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueRepeatDummyEnum(ValueRepeatBase):
    """ValueRepeat<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueRepeat<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "length": "Length",
        "n": "N",
    }

    length: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    n: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueRepeat variant
ValueRepeat = (
    ValueRepeatBool |
    ValueRepeatByte |
    ValueRepeatUshort |
    ValueRepeatUint |
    ValueRepeatUlong |
    ValueRepeatSbyte |
    ValueRepeatShort |
    ValueRepeatInt |
    ValueRepeatLong |
    ValueRepeatFloat |
    ValueRepeatDouble |
    ValueRepeatDecimal |
    ValueRepeatChar |
    ValueRepeatString |
    ValueRepeatUri |
    ValueRepeatBool2 |
    ValueRepeatByte2 |
    ValueRepeatUshort2 |
    ValueRepeatUint2 |
    ValueRepeatUlong2 |
    ValueRepeatSbyte2 |
    ValueRepeatShort2 |
    ValueRepeatInt2 |
    ValueRepeatLong2 |
    ValueRepeatFloat2 |
    ValueRepeatDouble2 |
    ValueRepeatBool3 |
    ValueRepeatByte3 |
    ValueRepeatUshort3 |
    ValueRepeatUint3 |
    ValueRepeatUlong3 |
    ValueRepeatSbyte3 |
    ValueRepeatShort3 |
    ValueRepeatInt3 |
    ValueRepeatLong3 |
    ValueRepeatFloat3 |
    ValueRepeatDouble3 |
    ValueRepeatBool4 |
    ValueRepeatByte4 |
    ValueRepeatUshort4 |
    ValueRepeatUint4 |
    ValueRepeatUlong4 |
    ValueRepeatSbyte4 |
    ValueRepeatShort4 |
    ValueRepeatInt4 |
    ValueRepeatLong4 |
    ValueRepeatFloat4 |
    ValueRepeatDouble4 |
    ValueRepeatFloat_2x2 |
    ValueRepeatDouble_2x2 |
    ValueRepeatFloat_3x3 |
    ValueRepeatDouble_3x3 |
    ValueRepeatFloat_4x4 |
    ValueRepeatDouble_4x4 |
    ValueRepeatFloatQ |
    ValueRepeatDoubleQ |
    ValueRepeatDateTime |
    ValueRepeatTimeSpan |
    ValueRepeatColor |
    ValueRepeatColorX |
    ValueRepeatShadowCastMode |
    ValueRepeatLightType |
    ValueRepeatSessionAccessLevel |
    ValueRepeatKey |
    ValueRepeatHttpStatusCode |
    ValueRepeatHeadOutputDevice |
    ValueRepeatReflectionProbeClear |
    ValueRepeatReflectionProbeType |
    ValueRepeatReflectionProbeTimeSlicingMode |
    ValueRepeatCameraClearMode |
    ValueRepeatCameraPositioningMode |
    ValueRepeatCameraProjection |
    ValueRepeatZWrite |
    ValueRepeatZTest |
    ValueRepeatBlend |
    ValueRepeatBlendMode |
    ValueRepeatCulling |
    ValueRepeatBodyNode |
    ValueRepeatChirality |
    ValueRepeatDummyEnum
)