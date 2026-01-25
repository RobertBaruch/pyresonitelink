"""Generated component: ShiftEnum.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ShiftEnumBase(GeneratedComponent):
    """Base class for ShiftEnum<T> variants."""

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
class ShiftEnumBool(ShiftEnumBase):
    """ShiftEnum<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ShiftEnumByte(ShiftEnumBase):
    """ShiftEnum<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ShiftEnumUshort(ShiftEnumBase):
    """ShiftEnum<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ShiftEnumUint(ShiftEnumBase):
    """ShiftEnum<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ShiftEnumUlong(ShiftEnumBase):
    """ShiftEnum<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ShiftEnumSbyte(ShiftEnumBase):
    """ShiftEnum<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ShiftEnumShort(ShiftEnumBase):
    """ShiftEnum<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ShiftEnumInt(ShiftEnumBase):
    """ShiftEnum<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ShiftEnumLong(ShiftEnumBase):
    """ShiftEnum<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ShiftEnumFloat(ShiftEnumBase):
    """ShiftEnum<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ShiftEnumDouble(ShiftEnumBase):
    """ShiftEnum<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ShiftEnumDecimal(ShiftEnumBase):
    """ShiftEnum<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ShiftEnumChar(ShiftEnumBase):
    """ShiftEnum<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ShiftEnumString(ShiftEnumBase):
    """ShiftEnum<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ShiftEnumUri(ShiftEnumBase):
    """ShiftEnum<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ShiftEnumBool2(ShiftEnumBase):
    """ShiftEnum<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ShiftEnumByte2(ShiftEnumBase):
    """ShiftEnum<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ShiftEnumUshort2(ShiftEnumBase):
    """ShiftEnum<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ShiftEnumUint2(ShiftEnumBase):
    """ShiftEnum<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ShiftEnumUlong2(ShiftEnumBase):
    """ShiftEnum<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ShiftEnumSbyte2(ShiftEnumBase):
    """ShiftEnum<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ShiftEnumShort2(ShiftEnumBase):
    """ShiftEnum<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ShiftEnumInt2(ShiftEnumBase):
    """ShiftEnum<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ShiftEnumLong2(ShiftEnumBase):
    """ShiftEnum<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ShiftEnumFloat2(ShiftEnumBase):
    """ShiftEnum<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ShiftEnumDouble2(ShiftEnumBase):
    """ShiftEnum<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ShiftEnumBool3(ShiftEnumBase):
    """ShiftEnum<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ShiftEnumByte3(ShiftEnumBase):
    """ShiftEnum<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ShiftEnumUshort3(ShiftEnumBase):
    """ShiftEnum<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ShiftEnumUint3(ShiftEnumBase):
    """ShiftEnum<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ShiftEnumUlong3(ShiftEnumBase):
    """ShiftEnum<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ShiftEnumSbyte3(ShiftEnumBase):
    """ShiftEnum<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ShiftEnumShort3(ShiftEnumBase):
    """ShiftEnum<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ShiftEnumInt3(ShiftEnumBase):
    """ShiftEnum<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ShiftEnumLong3(ShiftEnumBase):
    """ShiftEnum<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ShiftEnumFloat3(ShiftEnumBase):
    """ShiftEnum<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ShiftEnumDouble3(ShiftEnumBase):
    """ShiftEnum<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ShiftEnumBool4(ShiftEnumBase):
    """ShiftEnum<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ShiftEnumByte4(ShiftEnumBase):
    """ShiftEnum<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ShiftEnumUshort4(ShiftEnumBase):
    """ShiftEnum<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ShiftEnumUint4(ShiftEnumBase):
    """ShiftEnum<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ShiftEnumUlong4(ShiftEnumBase):
    """ShiftEnum<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ShiftEnumSbyte4(ShiftEnumBase):
    """ShiftEnum<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ShiftEnumShort4(ShiftEnumBase):
    """ShiftEnum<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ShiftEnumInt4(ShiftEnumBase):
    """ShiftEnum<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ShiftEnumLong4(ShiftEnumBase):
    """ShiftEnum<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ShiftEnumFloat4(ShiftEnumBase):
    """ShiftEnum<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ShiftEnumDouble4(ShiftEnumBase):
    """ShiftEnum<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ShiftEnumFloat_2x2(ShiftEnumBase):
    """ShiftEnum<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ShiftEnumDouble_2x2(ShiftEnumBase):
    """ShiftEnum<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ShiftEnumFloat_3x3(ShiftEnumBase):
    """ShiftEnum<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ShiftEnumDouble_3x3(ShiftEnumBase):
    """ShiftEnum<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ShiftEnumFloat_4x4(ShiftEnumBase):
    """ShiftEnum<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ShiftEnumDouble_4x4(ShiftEnumBase):
    """ShiftEnum<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ShiftEnumFloatQ(ShiftEnumBase):
    """ShiftEnum<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ShiftEnumDoubleQ(ShiftEnumBase):
    """ShiftEnum<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ShiftEnumDateTime(ShiftEnumBase):
    """ShiftEnum<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ShiftEnumTimeSpan(ShiftEnumBase):
    """ShiftEnum<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ShiftEnumColor(ShiftEnumBase):
    """ShiftEnum<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ShiftEnumColorX(ShiftEnumBase):
    """ShiftEnum<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ShiftEnumShadowCastMode(ShiftEnumBase):
    """ShiftEnum<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ShiftEnumLightType(ShiftEnumBase):
    """ShiftEnum<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ShiftEnumSessionAccessLevel(ShiftEnumBase):
    """ShiftEnum<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ShiftEnumKey(ShiftEnumBase):
    """ShiftEnum<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ShiftEnumHttpStatusCode(ShiftEnumBase):
    """ShiftEnum<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ShiftEnumHeadOutputDevice(ShiftEnumBase):
    """ShiftEnum<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ShiftEnumReflectionProbeClear(ShiftEnumBase):
    """ShiftEnum<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ShiftEnumReflectionProbeType(ShiftEnumBase):
    """ShiftEnum<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ShiftEnumReflectionProbeTimeSlicingMode(ShiftEnumBase):
    """ShiftEnum<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ShiftEnumCameraClearMode(ShiftEnumBase):
    """ShiftEnum<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ShiftEnumCameraPositioningMode(ShiftEnumBase):
    """ShiftEnum<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ShiftEnumCameraProjection(ShiftEnumBase):
    """ShiftEnum<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ShiftEnumZWrite(ShiftEnumBase):
    """ShiftEnum<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ShiftEnumZTest(ShiftEnumBase):
    """ShiftEnum<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ShiftEnumBlend(ShiftEnumBase):
    """ShiftEnum<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ShiftEnumBlendMode(ShiftEnumBase):
    """ShiftEnum<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ShiftEnumCulling(ShiftEnumBase):
    """ShiftEnum<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ShiftEnumBodyNode(ShiftEnumBase):
    """ShiftEnum<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ShiftEnumChirality(ShiftEnumBase):
    """ShiftEnum<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ShiftEnumDummyEnum(ShiftEnumBase):
    """ShiftEnum<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.ShiftEnum<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delta": "Delta",
        "value": "Value",
    }

    delta: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ShiftEnum variant
ShiftEnum = (
    ShiftEnumBool |
    ShiftEnumByte |
    ShiftEnumUshort |
    ShiftEnumUint |
    ShiftEnumUlong |
    ShiftEnumSbyte |
    ShiftEnumShort |
    ShiftEnumInt |
    ShiftEnumLong |
    ShiftEnumFloat |
    ShiftEnumDouble |
    ShiftEnumDecimal |
    ShiftEnumChar |
    ShiftEnumString |
    ShiftEnumUri |
    ShiftEnumBool2 |
    ShiftEnumByte2 |
    ShiftEnumUshort2 |
    ShiftEnumUint2 |
    ShiftEnumUlong2 |
    ShiftEnumSbyte2 |
    ShiftEnumShort2 |
    ShiftEnumInt2 |
    ShiftEnumLong2 |
    ShiftEnumFloat2 |
    ShiftEnumDouble2 |
    ShiftEnumBool3 |
    ShiftEnumByte3 |
    ShiftEnumUshort3 |
    ShiftEnumUint3 |
    ShiftEnumUlong3 |
    ShiftEnumSbyte3 |
    ShiftEnumShort3 |
    ShiftEnumInt3 |
    ShiftEnumLong3 |
    ShiftEnumFloat3 |
    ShiftEnumDouble3 |
    ShiftEnumBool4 |
    ShiftEnumByte4 |
    ShiftEnumUshort4 |
    ShiftEnumUint4 |
    ShiftEnumUlong4 |
    ShiftEnumSbyte4 |
    ShiftEnumShort4 |
    ShiftEnumInt4 |
    ShiftEnumLong4 |
    ShiftEnumFloat4 |
    ShiftEnumDouble4 |
    ShiftEnumFloat_2x2 |
    ShiftEnumDouble_2x2 |
    ShiftEnumFloat_3x3 |
    ShiftEnumDouble_3x3 |
    ShiftEnumFloat_4x4 |
    ShiftEnumDouble_4x4 |
    ShiftEnumFloatQ |
    ShiftEnumDoubleQ |
    ShiftEnumDateTime |
    ShiftEnumTimeSpan |
    ShiftEnumColor |
    ShiftEnumColorX |
    ShiftEnumShadowCastMode |
    ShiftEnumLightType |
    ShiftEnumSessionAccessLevel |
    ShiftEnumKey |
    ShiftEnumHttpStatusCode |
    ShiftEnumHeadOutputDevice |
    ShiftEnumReflectionProbeClear |
    ShiftEnumReflectionProbeType |
    ShiftEnumReflectionProbeTimeSlicingMode |
    ShiftEnumCameraClearMode |
    ShiftEnumCameraPositioningMode |
    ShiftEnumCameraProjection |
    ShiftEnumZWrite |
    ShiftEnumZTest |
    ShiftEnumBlend |
    ShiftEnumBlendMode |
    ShiftEnumCulling |
    ShiftEnumBodyNode |
    ShiftEnumChirality |
    ShiftEnumDummyEnum
)