"""Generated component: FromBaseValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FromBaseValueBase(GeneratedComponent):
    """Base class for FromBaseValue<T> variants."""

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
class FromBaseValueBool(FromBaseValueBase):
    """FromBaseValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueByte(FromBaseValueBase):
    """FromBaseValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUshort(FromBaseValueBase):
    """FromBaseValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUint(FromBaseValueBase):
    """FromBaseValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUlong(FromBaseValueBase):
    """FromBaseValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueSbyte(FromBaseValueBase):
    """FromBaseValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueShort(FromBaseValueBase):
    """FromBaseValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueInt(FromBaseValueBase):
    """FromBaseValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueLong(FromBaseValueBase):
    """FromBaseValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat(FromBaseValueBase):
    """FromBaseValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble(FromBaseValueBase):
    """FromBaseValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDecimal(FromBaseValueBase):
    """FromBaseValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueChar(FromBaseValueBase):
    """FromBaseValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueString(FromBaseValueBase):
    """FromBaseValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUri(FromBaseValueBase):
    """FromBaseValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBool2(FromBaseValueBase):
    """FromBaseValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueByte2(FromBaseValueBase):
    """FromBaseValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUshort2(FromBaseValueBase):
    """FromBaseValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUint2(FromBaseValueBase):
    """FromBaseValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUlong2(FromBaseValueBase):
    """FromBaseValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueSbyte2(FromBaseValueBase):
    """FromBaseValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueShort2(FromBaseValueBase):
    """FromBaseValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueInt2(FromBaseValueBase):
    """FromBaseValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueLong2(FromBaseValueBase):
    """FromBaseValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat2(FromBaseValueBase):
    """FromBaseValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble2(FromBaseValueBase):
    """FromBaseValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBool3(FromBaseValueBase):
    """FromBaseValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueByte3(FromBaseValueBase):
    """FromBaseValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUshort3(FromBaseValueBase):
    """FromBaseValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUint3(FromBaseValueBase):
    """FromBaseValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUlong3(FromBaseValueBase):
    """FromBaseValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueSbyte3(FromBaseValueBase):
    """FromBaseValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueShort3(FromBaseValueBase):
    """FromBaseValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueInt3(FromBaseValueBase):
    """FromBaseValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueLong3(FromBaseValueBase):
    """FromBaseValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat3(FromBaseValueBase):
    """FromBaseValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble3(FromBaseValueBase):
    """FromBaseValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBool4(FromBaseValueBase):
    """FromBaseValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueByte4(FromBaseValueBase):
    """FromBaseValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUshort4(FromBaseValueBase):
    """FromBaseValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUint4(FromBaseValueBase):
    """FromBaseValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueUlong4(FromBaseValueBase):
    """FromBaseValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueSbyte4(FromBaseValueBase):
    """FromBaseValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueShort4(FromBaseValueBase):
    """FromBaseValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueInt4(FromBaseValueBase):
    """FromBaseValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueLong4(FromBaseValueBase):
    """FromBaseValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat4(FromBaseValueBase):
    """FromBaseValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble4(FromBaseValueBase):
    """FromBaseValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat_2x2(FromBaseValueBase):
    """FromBaseValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble_2x2(FromBaseValueBase):
    """FromBaseValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat_3x3(FromBaseValueBase):
    """FromBaseValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble_3x3(FromBaseValueBase):
    """FromBaseValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloat_4x4(FromBaseValueBase):
    """FromBaseValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDouble_4x4(FromBaseValueBase):
    """FromBaseValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueFloatQ(FromBaseValueBase):
    """FromBaseValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDoubleQ(FromBaseValueBase):
    """FromBaseValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDateTime(FromBaseValueBase):
    """FromBaseValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueTimeSpan(FromBaseValueBase):
    """FromBaseValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueColor(FromBaseValueBase):
    """FromBaseValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueColorX(FromBaseValueBase):
    """FromBaseValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueShadowCastMode(FromBaseValueBase):
    """FromBaseValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueLightType(FromBaseValueBase):
    """FromBaseValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueSessionAccessLevel(FromBaseValueBase):
    """FromBaseValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueKey(FromBaseValueBase):
    """FromBaseValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueHttpStatusCode(FromBaseValueBase):
    """FromBaseValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueHeadOutputDevice(FromBaseValueBase):
    """FromBaseValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueReflectionProbeClear(FromBaseValueBase):
    """FromBaseValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueReflectionProbeType(FromBaseValueBase):
    """FromBaseValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueReflectionProbeTimeSlicingMode(FromBaseValueBase):
    """FromBaseValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueCameraClearMode(FromBaseValueBase):
    """FromBaseValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueCameraPositioningMode(FromBaseValueBase):
    """FromBaseValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueCameraProjection(FromBaseValueBase):
    """FromBaseValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueZWrite(FromBaseValueBase):
    """FromBaseValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueZTest(FromBaseValueBase):
    """FromBaseValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBlend(FromBaseValueBase):
    """FromBaseValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBlendMode(FromBaseValueBase):
    """FromBaseValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueCulling(FromBaseValueBase):
    """FromBaseValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueBodyNode(FromBaseValueBase):
    """FromBaseValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueChirality(FromBaseValueBase):
    """FromBaseValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FromBaseValueDummyEnum(FromBaseValueBase):
    """FromBaseValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FromBaseValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


# Type alias for any FromBaseValue variant
FromBaseValue = (
    FromBaseValueBool |
    FromBaseValueByte |
    FromBaseValueUshort |
    FromBaseValueUint |
    FromBaseValueUlong |
    FromBaseValueSbyte |
    FromBaseValueShort |
    FromBaseValueInt |
    FromBaseValueLong |
    FromBaseValueFloat |
    FromBaseValueDouble |
    FromBaseValueDecimal |
    FromBaseValueChar |
    FromBaseValueString |
    FromBaseValueUri |
    FromBaseValueBool2 |
    FromBaseValueByte2 |
    FromBaseValueUshort2 |
    FromBaseValueUint2 |
    FromBaseValueUlong2 |
    FromBaseValueSbyte2 |
    FromBaseValueShort2 |
    FromBaseValueInt2 |
    FromBaseValueLong2 |
    FromBaseValueFloat2 |
    FromBaseValueDouble2 |
    FromBaseValueBool3 |
    FromBaseValueByte3 |
    FromBaseValueUshort3 |
    FromBaseValueUint3 |
    FromBaseValueUlong3 |
    FromBaseValueSbyte3 |
    FromBaseValueShort3 |
    FromBaseValueInt3 |
    FromBaseValueLong3 |
    FromBaseValueFloat3 |
    FromBaseValueDouble3 |
    FromBaseValueBool4 |
    FromBaseValueByte4 |
    FromBaseValueUshort4 |
    FromBaseValueUint4 |
    FromBaseValueUlong4 |
    FromBaseValueSbyte4 |
    FromBaseValueShort4 |
    FromBaseValueInt4 |
    FromBaseValueLong4 |
    FromBaseValueFloat4 |
    FromBaseValueDouble4 |
    FromBaseValueFloat_2x2 |
    FromBaseValueDouble_2x2 |
    FromBaseValueFloat_3x3 |
    FromBaseValueDouble_3x3 |
    FromBaseValueFloat_4x4 |
    FromBaseValueDouble_4x4 |
    FromBaseValueFloatQ |
    FromBaseValueDoubleQ |
    FromBaseValueDateTime |
    FromBaseValueTimeSpan |
    FromBaseValueColor |
    FromBaseValueColorX |
    FromBaseValueShadowCastMode |
    FromBaseValueLightType |
    FromBaseValueSessionAccessLevel |
    FromBaseValueKey |
    FromBaseValueHttpStatusCode |
    FromBaseValueHeadOutputDevice |
    FromBaseValueReflectionProbeClear |
    FromBaseValueReflectionProbeType |
    FromBaseValueReflectionProbeTimeSlicingMode |
    FromBaseValueCameraClearMode |
    FromBaseValueCameraPositioningMode |
    FromBaseValueCameraProjection |
    FromBaseValueZWrite |
    FromBaseValueZTest |
    FromBaseValueBlend |
    FromBaseValueBlendMode |
    FromBaseValueCulling |
    FromBaseValueBodyNode |
    FromBaseValueChirality |
    FromBaseValueDummyEnum
)