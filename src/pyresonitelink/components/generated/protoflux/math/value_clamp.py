"""Generated component: ValueClamp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ValueClampBase(GeneratedComponent):
    """Base class for ValueClamp<T> variants."""

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
class ValueClampBool(ValueClampBase):
    """ValueClamp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ValueClampByte(ValueClampBase):
    """ValueClamp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ValueClampUshort(ValueClampBase):
    """ValueClamp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ValueClampUint(ValueClampBase):
    """ValueClamp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ValueClampUlong(ValueClampBase):
    """ValueClamp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ValueClampSbyte(ValueClampBase):
    """ValueClamp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ValueClampShort(ValueClampBase):
    """ValueClamp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ValueClampInt(ValueClampBase):
    """ValueClamp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ValueClampLong(ValueClampBase):
    """ValueClamp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ValueClampFloat(ValueClampBase):
    """ValueClamp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ValueClampDouble(ValueClampBase):
    """ValueClamp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ValueClampDecimal(ValueClampBase):
    """ValueClamp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ValueClampChar(ValueClampBase):
    """ValueClamp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ValueClampString(ValueClampBase):
    """ValueClamp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ValueClampUri(ValueClampBase):
    """ValueClamp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ValueClampBool2(ValueClampBase):
    """ValueClamp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ValueClampByte2(ValueClampBase):
    """ValueClamp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ValueClampUshort2(ValueClampBase):
    """ValueClamp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ValueClampUint2(ValueClampBase):
    """ValueClamp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ValueClampUlong2(ValueClampBase):
    """ValueClamp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ValueClampSbyte2(ValueClampBase):
    """ValueClamp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ValueClampShort2(ValueClampBase):
    """ValueClamp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ValueClampInt2(ValueClampBase):
    """ValueClamp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ValueClampLong2(ValueClampBase):
    """ValueClamp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ValueClampFloat2(ValueClampBase):
    """ValueClamp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ValueClampDouble2(ValueClampBase):
    """ValueClamp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ValueClampBool3(ValueClampBase):
    """ValueClamp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ValueClampByte3(ValueClampBase):
    """ValueClamp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ValueClampUshort3(ValueClampBase):
    """ValueClamp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ValueClampUint3(ValueClampBase):
    """ValueClamp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ValueClampUlong3(ValueClampBase):
    """ValueClamp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ValueClampSbyte3(ValueClampBase):
    """ValueClamp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ValueClampShort3(ValueClampBase):
    """ValueClamp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ValueClampInt3(ValueClampBase):
    """ValueClamp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ValueClampLong3(ValueClampBase):
    """ValueClamp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ValueClampFloat3(ValueClampBase):
    """ValueClamp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ValueClampDouble3(ValueClampBase):
    """ValueClamp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ValueClampBool4(ValueClampBase):
    """ValueClamp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ValueClampByte4(ValueClampBase):
    """ValueClamp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ValueClampUshort4(ValueClampBase):
    """ValueClamp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ValueClampUint4(ValueClampBase):
    """ValueClamp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ValueClampUlong4(ValueClampBase):
    """ValueClamp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ValueClampSbyte4(ValueClampBase):
    """ValueClamp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ValueClampShort4(ValueClampBase):
    """ValueClamp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ValueClampInt4(ValueClampBase):
    """ValueClamp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ValueClampLong4(ValueClampBase):
    """ValueClamp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ValueClampFloat4(ValueClampBase):
    """ValueClamp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ValueClampDouble4(ValueClampBase):
    """ValueClamp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ValueClampFloat_2x2(ValueClampBase):
    """ValueClamp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ValueClampDouble_2x2(ValueClampBase):
    """ValueClamp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ValueClampFloat_3x3(ValueClampBase):
    """ValueClamp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ValueClampDouble_3x3(ValueClampBase):
    """ValueClamp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ValueClampFloat_4x4(ValueClampBase):
    """ValueClamp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ValueClampDouble_4x4(ValueClampBase):
    """ValueClamp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ValueClampFloatQ(ValueClampBase):
    """ValueClamp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ValueClampDoubleQ(ValueClampBase):
    """ValueClamp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ValueClampDateTime(ValueClampBase):
    """ValueClamp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ValueClampTimeSpan(ValueClampBase):
    """ValueClamp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ValueClampColor(ValueClampBase):
    """ValueClamp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ValueClampColorX(ValueClampBase):
    """ValueClamp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ValueClampShadowCastMode(ValueClampBase):
    """ValueClamp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ValueClampLightType(ValueClampBase):
    """ValueClamp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ValueClampSessionAccessLevel(ValueClampBase):
    """ValueClamp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ValueClampKey(ValueClampBase):
    """ValueClamp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ValueClampHttpStatusCode(ValueClampBase):
    """ValueClamp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ValueClampHeadOutputDevice(ValueClampBase):
    """ValueClamp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ValueClampReflectionProbeClear(ValueClampBase):
    """ValueClamp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ValueClampReflectionProbeType(ValueClampBase):
    """ValueClamp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ValueClampReflectionProbeTimeSlicingMode(ValueClampBase):
    """ValueClamp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ValueClampCameraClearMode(ValueClampBase):
    """ValueClamp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ValueClampCameraPositioningMode(ValueClampBase):
    """ValueClamp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ValueClampCameraProjection(ValueClampBase):
    """ValueClamp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ValueClampZWrite(ValueClampBase):
    """ValueClamp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ValueClampZTest(ValueClampBase):
    """ValueClamp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ValueClampBlend(ValueClampBase):
    """ValueClamp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ValueClampBlendMode(ValueClampBase):
    """ValueClamp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ValueClampCulling(ValueClampBase):
    """ValueClamp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ValueClampBodyNode(ValueClampBase):
    """ValueClamp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ValueClampChirality(ValueClampBase):
    """ValueClamp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ValueClampDummyEnum(ValueClampBase):
    """ValueClamp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "max": "Max",
        "min": "Min",
        "value": "Value",
    }

    max: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    min: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ValueClamp variant
ValueClamp = (
    ValueClampBool |
    ValueClampByte |
    ValueClampUshort |
    ValueClampUint |
    ValueClampUlong |
    ValueClampSbyte |
    ValueClampShort |
    ValueClampInt |
    ValueClampLong |
    ValueClampFloat |
    ValueClampDouble |
    ValueClampDecimal |
    ValueClampChar |
    ValueClampString |
    ValueClampUri |
    ValueClampBool2 |
    ValueClampByte2 |
    ValueClampUshort2 |
    ValueClampUint2 |
    ValueClampUlong2 |
    ValueClampSbyte2 |
    ValueClampShort2 |
    ValueClampInt2 |
    ValueClampLong2 |
    ValueClampFloat2 |
    ValueClampDouble2 |
    ValueClampBool3 |
    ValueClampByte3 |
    ValueClampUshort3 |
    ValueClampUint3 |
    ValueClampUlong3 |
    ValueClampSbyte3 |
    ValueClampShort3 |
    ValueClampInt3 |
    ValueClampLong3 |
    ValueClampFloat3 |
    ValueClampDouble3 |
    ValueClampBool4 |
    ValueClampByte4 |
    ValueClampUshort4 |
    ValueClampUint4 |
    ValueClampUlong4 |
    ValueClampSbyte4 |
    ValueClampShort4 |
    ValueClampInt4 |
    ValueClampLong4 |
    ValueClampFloat4 |
    ValueClampDouble4 |
    ValueClampFloat_2x2 |
    ValueClampDouble_2x2 |
    ValueClampFloat_3x3 |
    ValueClampDouble_3x3 |
    ValueClampFloat_4x4 |
    ValueClampDouble_4x4 |
    ValueClampFloatQ |
    ValueClampDoubleQ |
    ValueClampDateTime |
    ValueClampTimeSpan |
    ValueClampColor |
    ValueClampColorX |
    ValueClampShadowCastMode |
    ValueClampLightType |
    ValueClampSessionAccessLevel |
    ValueClampKey |
    ValueClampHttpStatusCode |
    ValueClampHeadOutputDevice |
    ValueClampReflectionProbeClear |
    ValueClampReflectionProbeType |
    ValueClampReflectionProbeTimeSlicingMode |
    ValueClampCameraClearMode |
    ValueClampCameraPositioningMode |
    ValueClampCameraProjection |
    ValueClampZWrite |
    ValueClampZTest |
    ValueClampBlend |
    ValueClampBlendMode |
    ValueClampCulling |
    ValueClampBodyNode |
    ValueClampChirality |
    ValueClampDummyEnum
)