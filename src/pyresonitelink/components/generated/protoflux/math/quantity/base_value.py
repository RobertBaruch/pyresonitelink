"""Generated component: BaseValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class BaseValueBase(GeneratedComponent):
    """Base class for BaseValue<T> variants."""

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
class BaseValueBool(BaseValueBase):
    """BaseValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class BaseValueByte(BaseValueBase):
    """BaseValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class BaseValueUshort(BaseValueBase):
    """BaseValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class BaseValueUint(BaseValueBase):
    """BaseValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class BaseValueUlong(BaseValueBase):
    """BaseValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class BaseValueSbyte(BaseValueBase):
    """BaseValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class BaseValueShort(BaseValueBase):
    """BaseValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class BaseValueInt(BaseValueBase):
    """BaseValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class BaseValueLong(BaseValueBase):
    """BaseValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class BaseValueFloat(BaseValueBase):
    """BaseValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class BaseValueDouble(BaseValueBase):
    """BaseValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class BaseValueDecimal(BaseValueBase):
    """BaseValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class BaseValueChar(BaseValueBase):
    """BaseValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class BaseValueString(BaseValueBase):
    """BaseValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class BaseValueUri(BaseValueBase):
    """BaseValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class BaseValueBool2(BaseValueBase):
    """BaseValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class BaseValueByte2(BaseValueBase):
    """BaseValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class BaseValueUshort2(BaseValueBase):
    """BaseValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class BaseValueUint2(BaseValueBase):
    """BaseValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class BaseValueUlong2(BaseValueBase):
    """BaseValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class BaseValueSbyte2(BaseValueBase):
    """BaseValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class BaseValueShort2(BaseValueBase):
    """BaseValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class BaseValueInt2(BaseValueBase):
    """BaseValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class BaseValueLong2(BaseValueBase):
    """BaseValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class BaseValueFloat2(BaseValueBase):
    """BaseValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class BaseValueDouble2(BaseValueBase):
    """BaseValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class BaseValueBool3(BaseValueBase):
    """BaseValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class BaseValueByte3(BaseValueBase):
    """BaseValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class BaseValueUshort3(BaseValueBase):
    """BaseValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class BaseValueUint3(BaseValueBase):
    """BaseValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class BaseValueUlong3(BaseValueBase):
    """BaseValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class BaseValueSbyte3(BaseValueBase):
    """BaseValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class BaseValueShort3(BaseValueBase):
    """BaseValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class BaseValueInt3(BaseValueBase):
    """BaseValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class BaseValueLong3(BaseValueBase):
    """BaseValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class BaseValueFloat3(BaseValueBase):
    """BaseValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class BaseValueDouble3(BaseValueBase):
    """BaseValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class BaseValueBool4(BaseValueBase):
    """BaseValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class BaseValueByte4(BaseValueBase):
    """BaseValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class BaseValueUshort4(BaseValueBase):
    """BaseValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class BaseValueUint4(BaseValueBase):
    """BaseValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class BaseValueUlong4(BaseValueBase):
    """BaseValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class BaseValueSbyte4(BaseValueBase):
    """BaseValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class BaseValueShort4(BaseValueBase):
    """BaseValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class BaseValueInt4(BaseValueBase):
    """BaseValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class BaseValueLong4(BaseValueBase):
    """BaseValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class BaseValueFloat4(BaseValueBase):
    """BaseValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class BaseValueDouble4(BaseValueBase):
    """BaseValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class BaseValueFloat_2x2(BaseValueBase):
    """BaseValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class BaseValueDouble_2x2(BaseValueBase):
    """BaseValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class BaseValueFloat_3x3(BaseValueBase):
    """BaseValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class BaseValueDouble_3x3(BaseValueBase):
    """BaseValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class BaseValueFloat_4x4(BaseValueBase):
    """BaseValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class BaseValueDouble_4x4(BaseValueBase):
    """BaseValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class BaseValueFloatQ(BaseValueBase):
    """BaseValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class BaseValueDoubleQ(BaseValueBase):
    """BaseValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class BaseValueDateTime(BaseValueBase):
    """BaseValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class BaseValueTimeSpan(BaseValueBase):
    """BaseValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class BaseValueColor(BaseValueBase):
    """BaseValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class BaseValueColorX(BaseValueBase):
    """BaseValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class BaseValueShadowCastMode(BaseValueBase):
    """BaseValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class BaseValueLightType(BaseValueBase):
    """BaseValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class BaseValueSessionAccessLevel(BaseValueBase):
    """BaseValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class BaseValueKey(BaseValueBase):
    """BaseValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class BaseValueHttpStatusCode(BaseValueBase):
    """BaseValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class BaseValueHeadOutputDevice(BaseValueBase):
    """BaseValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class BaseValueReflectionProbeClear(BaseValueBase):
    """BaseValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class BaseValueReflectionProbeType(BaseValueBase):
    """BaseValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class BaseValueReflectionProbeTimeSlicingMode(BaseValueBase):
    """BaseValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class BaseValueCameraClearMode(BaseValueBase):
    """BaseValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class BaseValueCameraPositioningMode(BaseValueBase):
    """BaseValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class BaseValueCameraProjection(BaseValueBase):
    """BaseValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class BaseValueZWrite(BaseValueBase):
    """BaseValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class BaseValueZTest(BaseValueBase):
    """BaseValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class BaseValueBlend(BaseValueBase):
    """BaseValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class BaseValueBlendMode(BaseValueBase):
    """BaseValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class BaseValueCulling(BaseValueBase):
    """BaseValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class BaseValueBodyNode(BaseValueBase):
    """BaseValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class BaseValueChirality(BaseValueBase):
    """BaseValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class BaseValueDummyEnum(BaseValueBase):
    """BaseValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.BaseValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "value": "Value",
    }

    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any BaseValue variant
BaseValue = (
    BaseValueBool |
    BaseValueByte |
    BaseValueUshort |
    BaseValueUint |
    BaseValueUlong |
    BaseValueSbyte |
    BaseValueShort |
    BaseValueInt |
    BaseValueLong |
    BaseValueFloat |
    BaseValueDouble |
    BaseValueDecimal |
    BaseValueChar |
    BaseValueString |
    BaseValueUri |
    BaseValueBool2 |
    BaseValueByte2 |
    BaseValueUshort2 |
    BaseValueUint2 |
    BaseValueUlong2 |
    BaseValueSbyte2 |
    BaseValueShort2 |
    BaseValueInt2 |
    BaseValueLong2 |
    BaseValueFloat2 |
    BaseValueDouble2 |
    BaseValueBool3 |
    BaseValueByte3 |
    BaseValueUshort3 |
    BaseValueUint3 |
    BaseValueUlong3 |
    BaseValueSbyte3 |
    BaseValueShort3 |
    BaseValueInt3 |
    BaseValueLong3 |
    BaseValueFloat3 |
    BaseValueDouble3 |
    BaseValueBool4 |
    BaseValueByte4 |
    BaseValueUshort4 |
    BaseValueUint4 |
    BaseValueUlong4 |
    BaseValueSbyte4 |
    BaseValueShort4 |
    BaseValueInt4 |
    BaseValueLong4 |
    BaseValueFloat4 |
    BaseValueDouble4 |
    BaseValueFloat_2x2 |
    BaseValueDouble_2x2 |
    BaseValueFloat_3x3 |
    BaseValueDouble_3x3 |
    BaseValueFloat_4x4 |
    BaseValueDouble_4x4 |
    BaseValueFloatQ |
    BaseValueDoubleQ |
    BaseValueDateTime |
    BaseValueTimeSpan |
    BaseValueColor |
    BaseValueColorX |
    BaseValueShadowCastMode |
    BaseValueLightType |
    BaseValueSessionAccessLevel |
    BaseValueKey |
    BaseValueHttpStatusCode |
    BaseValueHeadOutputDevice |
    BaseValueReflectionProbeClear |
    BaseValueReflectionProbeType |
    BaseValueReflectionProbeTimeSlicingMode |
    BaseValueCameraClearMode |
    BaseValueCameraPositioningMode |
    BaseValueCameraProjection |
    BaseValueZWrite |
    BaseValueZTest |
    BaseValueBlend |
    BaseValueBlendMode |
    BaseValueCulling |
    BaseValueBodyNode |
    BaseValueChirality |
    BaseValueDummyEnum
)