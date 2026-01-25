"""Generated component: ParseQuantity.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ParseQuantityBase(GeneratedComponent):
    """Base class for ParseQuantity<T> variants."""

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
class ParseQuantityBool(ParseQuantityBase):
    """ParseQuantity<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityByte(ParseQuantityBase):
    """ParseQuantity<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUshort(ParseQuantityBase):
    """ParseQuantity<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUint(ParseQuantityBase):
    """ParseQuantity<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUlong(ParseQuantityBase):
    """ParseQuantity<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantitySbyte(ParseQuantityBase):
    """ParseQuantity<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityShort(ParseQuantityBase):
    """ParseQuantity<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityInt(ParseQuantityBase):
    """ParseQuantity<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityLong(ParseQuantityBase):
    """ParseQuantity<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat(ParseQuantityBase):
    """ParseQuantity<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble(ParseQuantityBase):
    """ParseQuantity<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDecimal(ParseQuantityBase):
    """ParseQuantity<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityChar(ParseQuantityBase):
    """ParseQuantity<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityString(ParseQuantityBase):
    """ParseQuantity<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUri(ParseQuantityBase):
    """ParseQuantity<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBool2(ParseQuantityBase):
    """ParseQuantity<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityByte2(ParseQuantityBase):
    """ParseQuantity<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUshort2(ParseQuantityBase):
    """ParseQuantity<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUint2(ParseQuantityBase):
    """ParseQuantity<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUlong2(ParseQuantityBase):
    """ParseQuantity<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantitySbyte2(ParseQuantityBase):
    """ParseQuantity<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityShort2(ParseQuantityBase):
    """ParseQuantity<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityInt2(ParseQuantityBase):
    """ParseQuantity<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityLong2(ParseQuantityBase):
    """ParseQuantity<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat2(ParseQuantityBase):
    """ParseQuantity<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble2(ParseQuantityBase):
    """ParseQuantity<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBool3(ParseQuantityBase):
    """ParseQuantity<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityByte3(ParseQuantityBase):
    """ParseQuantity<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUshort3(ParseQuantityBase):
    """ParseQuantity<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUint3(ParseQuantityBase):
    """ParseQuantity<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUlong3(ParseQuantityBase):
    """ParseQuantity<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantitySbyte3(ParseQuantityBase):
    """ParseQuantity<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityShort3(ParseQuantityBase):
    """ParseQuantity<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityInt3(ParseQuantityBase):
    """ParseQuantity<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityLong3(ParseQuantityBase):
    """ParseQuantity<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat3(ParseQuantityBase):
    """ParseQuantity<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble3(ParseQuantityBase):
    """ParseQuantity<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBool4(ParseQuantityBase):
    """ParseQuantity<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityByte4(ParseQuantityBase):
    """ParseQuantity<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUshort4(ParseQuantityBase):
    """ParseQuantity<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUint4(ParseQuantityBase):
    """ParseQuantity<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityUlong4(ParseQuantityBase):
    """ParseQuantity<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantitySbyte4(ParseQuantityBase):
    """ParseQuantity<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityShort4(ParseQuantityBase):
    """ParseQuantity<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityInt4(ParseQuantityBase):
    """ParseQuantity<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityLong4(ParseQuantityBase):
    """ParseQuantity<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat4(ParseQuantityBase):
    """ParseQuantity<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble4(ParseQuantityBase):
    """ParseQuantity<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat_2x2(ParseQuantityBase):
    """ParseQuantity<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble_2x2(ParseQuantityBase):
    """ParseQuantity<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat_3x3(ParseQuantityBase):
    """ParseQuantity<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble_3x3(ParseQuantityBase):
    """ParseQuantity<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloat_4x4(ParseQuantityBase):
    """ParseQuantity<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDouble_4x4(ParseQuantityBase):
    """ParseQuantity<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityFloatQ(ParseQuantityBase):
    """ParseQuantity<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDoubleQ(ParseQuantityBase):
    """ParseQuantity<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDateTime(ParseQuantityBase):
    """ParseQuantity<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityTimeSpan(ParseQuantityBase):
    """ParseQuantity<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityColor(ParseQuantityBase):
    """ParseQuantity<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityColorX(ParseQuantityBase):
    """ParseQuantity<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityShadowCastMode(ParseQuantityBase):
    """ParseQuantity<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityLightType(ParseQuantityBase):
    """ParseQuantity<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantitySessionAccessLevel(ParseQuantityBase):
    """ParseQuantity<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityKey(ParseQuantityBase):
    """ParseQuantity<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityHttpStatusCode(ParseQuantityBase):
    """ParseQuantity<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityHeadOutputDevice(ParseQuantityBase):
    """ParseQuantity<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityReflectionProbeClear(ParseQuantityBase):
    """ParseQuantity<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityReflectionProbeType(ParseQuantityBase):
    """ParseQuantity<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityReflectionProbeTimeSlicingMode(ParseQuantityBase):
    """ParseQuantity<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityCameraClearMode(ParseQuantityBase):
    """ParseQuantity<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityCameraPositioningMode(ParseQuantityBase):
    """ParseQuantity<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityCameraProjection(ParseQuantityBase):
    """ParseQuantity<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityZWrite(ParseQuantityBase):
    """ParseQuantity<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityZTest(ParseQuantityBase):
    """ParseQuantity<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBlend(ParseQuantityBase):
    """ParseQuantity<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBlendMode(ParseQuantityBase):
    """ParseQuantity<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityCulling(ParseQuantityBase):
    """ParseQuantity<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityBodyNode(ParseQuantityBase):
    """ParseQuantity<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityChirality(ParseQuantityBase):
    """ParseQuantity<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


@dataclass
class ParseQuantityDummyEnum(ParseQuantityBase):
    """ParseQuantity<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.ParseQuantity<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_unit": "DefaultUnit",
        "str": "Str",
    }

    default_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    str: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>


# Type alias for any ParseQuantity variant
ParseQuantity = (
    ParseQuantityBool |
    ParseQuantityByte |
    ParseQuantityUshort |
    ParseQuantityUint |
    ParseQuantityUlong |
    ParseQuantitySbyte |
    ParseQuantityShort |
    ParseQuantityInt |
    ParseQuantityLong |
    ParseQuantityFloat |
    ParseQuantityDouble |
    ParseQuantityDecimal |
    ParseQuantityChar |
    ParseQuantityString |
    ParseQuantityUri |
    ParseQuantityBool2 |
    ParseQuantityByte2 |
    ParseQuantityUshort2 |
    ParseQuantityUint2 |
    ParseQuantityUlong2 |
    ParseQuantitySbyte2 |
    ParseQuantityShort2 |
    ParseQuantityInt2 |
    ParseQuantityLong2 |
    ParseQuantityFloat2 |
    ParseQuantityDouble2 |
    ParseQuantityBool3 |
    ParseQuantityByte3 |
    ParseQuantityUshort3 |
    ParseQuantityUint3 |
    ParseQuantityUlong3 |
    ParseQuantitySbyte3 |
    ParseQuantityShort3 |
    ParseQuantityInt3 |
    ParseQuantityLong3 |
    ParseQuantityFloat3 |
    ParseQuantityDouble3 |
    ParseQuantityBool4 |
    ParseQuantityByte4 |
    ParseQuantityUshort4 |
    ParseQuantityUint4 |
    ParseQuantityUlong4 |
    ParseQuantitySbyte4 |
    ParseQuantityShort4 |
    ParseQuantityInt4 |
    ParseQuantityLong4 |
    ParseQuantityFloat4 |
    ParseQuantityDouble4 |
    ParseQuantityFloat_2x2 |
    ParseQuantityDouble_2x2 |
    ParseQuantityFloat_3x3 |
    ParseQuantityDouble_3x3 |
    ParseQuantityFloat_4x4 |
    ParseQuantityDouble_4x4 |
    ParseQuantityFloatQ |
    ParseQuantityDoubleQ |
    ParseQuantityDateTime |
    ParseQuantityTimeSpan |
    ParseQuantityColor |
    ParseQuantityColorX |
    ParseQuantityShadowCastMode |
    ParseQuantityLightType |
    ParseQuantitySessionAccessLevel |
    ParseQuantityKey |
    ParseQuantityHttpStatusCode |
    ParseQuantityHeadOutputDevice |
    ParseQuantityReflectionProbeClear |
    ParseQuantityReflectionProbeType |
    ParseQuantityReflectionProbeTimeSlicingMode |
    ParseQuantityCameraClearMode |
    ParseQuantityCameraPositioningMode |
    ParseQuantityCameraProjection |
    ParseQuantityZWrite |
    ParseQuantityZTest |
    ParseQuantityBlend |
    ParseQuantityBlendMode |
    ParseQuantityCulling |
    ParseQuantityBodyNode |
    ParseQuantityChirality |
    ParseQuantityDummyEnum
)