"""Generated component: FormatQuantity.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FormatQuantityBase(GeneratedComponent):
    """Base class for FormatQuantity<T> variants."""

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
class FormatQuantityBool(FormatQuantityBase):
    """FormatQuantity<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class FormatQuantityByte(FormatQuantityBase):
    """FormatQuantity<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class FormatQuantityUshort(FormatQuantityBase):
    """FormatQuantity<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class FormatQuantityUint(FormatQuantityBase):
    """FormatQuantity<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class FormatQuantityUlong(FormatQuantityBase):
    """FormatQuantity<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class FormatQuantitySbyte(FormatQuantityBase):
    """FormatQuantity<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class FormatQuantityShort(FormatQuantityBase):
    """FormatQuantity<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class FormatQuantityInt(FormatQuantityBase):
    """FormatQuantity<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class FormatQuantityLong(FormatQuantityBase):
    """FormatQuantity<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class FormatQuantityFloat(FormatQuantityBase):
    """FormatQuantity<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class FormatQuantityDouble(FormatQuantityBase):
    """FormatQuantity<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FormatQuantityDecimal(FormatQuantityBase):
    """FormatQuantity<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class FormatQuantityChar(FormatQuantityBase):
    """FormatQuantity<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class FormatQuantityString(FormatQuantityBase):
    """FormatQuantity<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class FormatQuantityUri(FormatQuantityBase):
    """FormatQuantity<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class FormatQuantityBool2(FormatQuantityBase):
    """FormatQuantity<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class FormatQuantityByte2(FormatQuantityBase):
    """FormatQuantity<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class FormatQuantityUshort2(FormatQuantityBase):
    """FormatQuantity<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class FormatQuantityUint2(FormatQuantityBase):
    """FormatQuantity<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class FormatQuantityUlong2(FormatQuantityBase):
    """FormatQuantity<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class FormatQuantitySbyte2(FormatQuantityBase):
    """FormatQuantity<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class FormatQuantityShort2(FormatQuantityBase):
    """FormatQuantity<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class FormatQuantityInt2(FormatQuantityBase):
    """FormatQuantity<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class FormatQuantityLong2(FormatQuantityBase):
    """FormatQuantity<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class FormatQuantityFloat2(FormatQuantityBase):
    """FormatQuantity<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class FormatQuantityDouble2(FormatQuantityBase):
    """FormatQuantity<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class FormatQuantityBool3(FormatQuantityBase):
    """FormatQuantity<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class FormatQuantityByte3(FormatQuantityBase):
    """FormatQuantity<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class FormatQuantityUshort3(FormatQuantityBase):
    """FormatQuantity<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class FormatQuantityUint3(FormatQuantityBase):
    """FormatQuantity<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class FormatQuantityUlong3(FormatQuantityBase):
    """FormatQuantity<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class FormatQuantitySbyte3(FormatQuantityBase):
    """FormatQuantity<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class FormatQuantityShort3(FormatQuantityBase):
    """FormatQuantity<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class FormatQuantityInt3(FormatQuantityBase):
    """FormatQuantity<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class FormatQuantityLong3(FormatQuantityBase):
    """FormatQuantity<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class FormatQuantityFloat3(FormatQuantityBase):
    """FormatQuantity<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class FormatQuantityDouble3(FormatQuantityBase):
    """FormatQuantity<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class FormatQuantityBool4(FormatQuantityBase):
    """FormatQuantity<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class FormatQuantityByte4(FormatQuantityBase):
    """FormatQuantity<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class FormatQuantityUshort4(FormatQuantityBase):
    """FormatQuantity<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class FormatQuantityUint4(FormatQuantityBase):
    """FormatQuantity<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class FormatQuantityUlong4(FormatQuantityBase):
    """FormatQuantity<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class FormatQuantitySbyte4(FormatQuantityBase):
    """FormatQuantity<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class FormatQuantityShort4(FormatQuantityBase):
    """FormatQuantity<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class FormatQuantityInt4(FormatQuantityBase):
    """FormatQuantity<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class FormatQuantityLong4(FormatQuantityBase):
    """FormatQuantity<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class FormatQuantityFloat4(FormatQuantityBase):
    """FormatQuantity<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class FormatQuantityDouble4(FormatQuantityBase):
    """FormatQuantity<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class FormatQuantityFloat_2x2(FormatQuantityBase):
    """FormatQuantity<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class FormatQuantityDouble_2x2(FormatQuantityBase):
    """FormatQuantity<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class FormatQuantityFloat_3x3(FormatQuantityBase):
    """FormatQuantity<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class FormatQuantityDouble_3x3(FormatQuantityBase):
    """FormatQuantity<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class FormatQuantityFloat_4x4(FormatQuantityBase):
    """FormatQuantity<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class FormatQuantityDouble_4x4(FormatQuantityBase):
    """FormatQuantity<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class FormatQuantityFloatQ(FormatQuantityBase):
    """FormatQuantity<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class FormatQuantityDoubleQ(FormatQuantityBase):
    """FormatQuantity<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class FormatQuantityDateTime(FormatQuantityBase):
    """FormatQuantity<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class FormatQuantityTimeSpan(FormatQuantityBase):
    """FormatQuantity<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class FormatQuantityColor(FormatQuantityBase):
    """FormatQuantity<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class FormatQuantityColorX(FormatQuantityBase):
    """FormatQuantity<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class FormatQuantityShadowCastMode(FormatQuantityBase):
    """FormatQuantity<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class FormatQuantityLightType(FormatQuantityBase):
    """FormatQuantity<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class FormatQuantitySessionAccessLevel(FormatQuantityBase):
    """FormatQuantity<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class FormatQuantityKey(FormatQuantityBase):
    """FormatQuantity<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class FormatQuantityHttpStatusCode(FormatQuantityBase):
    """FormatQuantity<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class FormatQuantityHeadOutputDevice(FormatQuantityBase):
    """FormatQuantity<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class FormatQuantityReflectionProbeClear(FormatQuantityBase):
    """FormatQuantity<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class FormatQuantityReflectionProbeType(FormatQuantityBase):
    """FormatQuantity<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class FormatQuantityReflectionProbeTimeSlicingMode(FormatQuantityBase):
    """FormatQuantity<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class FormatQuantityCameraClearMode(FormatQuantityBase):
    """FormatQuantity<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class FormatQuantityCameraPositioningMode(FormatQuantityBase):
    """FormatQuantity<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class FormatQuantityCameraProjection(FormatQuantityBase):
    """FormatQuantity<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class FormatQuantityZWrite(FormatQuantityBase):
    """FormatQuantity<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class FormatQuantityZTest(FormatQuantityBase):
    """FormatQuantity<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class FormatQuantityBlend(FormatQuantityBase):
    """FormatQuantity<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class FormatQuantityBlendMode(FormatQuantityBase):
    """FormatQuantity<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class FormatQuantityCulling(FormatQuantityBase):
    """FormatQuantity<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class FormatQuantityBodyNode(FormatQuantityBase):
    """FormatQuantity<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class FormatQuantityChirality(FormatQuantityBase):
    """FormatQuantity<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class FormatQuantityDummyEnum(FormatQuantityBase):
    """FormatQuantity<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Quantity.FormatQuantity<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "format_number": "FormatNumber",
        "format_unit": "FormatUnit",
        "use_long_names": "UseLongNames",
        "value": "Value",
    }

    format_number: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    format_unit: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    use_long_names: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any FormatQuantity variant
FormatQuantity = (
    FormatQuantityBool |
    FormatQuantityByte |
    FormatQuantityUshort |
    FormatQuantityUint |
    FormatQuantityUlong |
    FormatQuantitySbyte |
    FormatQuantityShort |
    FormatQuantityInt |
    FormatQuantityLong |
    FormatQuantityFloat |
    FormatQuantityDouble |
    FormatQuantityDecimal |
    FormatQuantityChar |
    FormatQuantityString |
    FormatQuantityUri |
    FormatQuantityBool2 |
    FormatQuantityByte2 |
    FormatQuantityUshort2 |
    FormatQuantityUint2 |
    FormatQuantityUlong2 |
    FormatQuantitySbyte2 |
    FormatQuantityShort2 |
    FormatQuantityInt2 |
    FormatQuantityLong2 |
    FormatQuantityFloat2 |
    FormatQuantityDouble2 |
    FormatQuantityBool3 |
    FormatQuantityByte3 |
    FormatQuantityUshort3 |
    FormatQuantityUint3 |
    FormatQuantityUlong3 |
    FormatQuantitySbyte3 |
    FormatQuantityShort3 |
    FormatQuantityInt3 |
    FormatQuantityLong3 |
    FormatQuantityFloat3 |
    FormatQuantityDouble3 |
    FormatQuantityBool4 |
    FormatQuantityByte4 |
    FormatQuantityUshort4 |
    FormatQuantityUint4 |
    FormatQuantityUlong4 |
    FormatQuantitySbyte4 |
    FormatQuantityShort4 |
    FormatQuantityInt4 |
    FormatQuantityLong4 |
    FormatQuantityFloat4 |
    FormatQuantityDouble4 |
    FormatQuantityFloat_2x2 |
    FormatQuantityDouble_2x2 |
    FormatQuantityFloat_3x3 |
    FormatQuantityDouble_3x3 |
    FormatQuantityFloat_4x4 |
    FormatQuantityDouble_4x4 |
    FormatQuantityFloatQ |
    FormatQuantityDoubleQ |
    FormatQuantityDateTime |
    FormatQuantityTimeSpan |
    FormatQuantityColor |
    FormatQuantityColorX |
    FormatQuantityShadowCastMode |
    FormatQuantityLightType |
    FormatQuantitySessionAccessLevel |
    FormatQuantityKey |
    FormatQuantityHttpStatusCode |
    FormatQuantityHeadOutputDevice |
    FormatQuantityReflectionProbeClear |
    FormatQuantityReflectionProbeType |
    FormatQuantityReflectionProbeTimeSlicingMode |
    FormatQuantityCameraClearMode |
    FormatQuantityCameraPositioningMode |
    FormatQuantityCameraProjection |
    FormatQuantityZWrite |
    FormatQuantityZTest |
    FormatQuantityBlend |
    FormatQuantityBlendMode |
    FormatQuantityCulling |
    FormatQuantityBodyNode |
    FormatQuantityChirality |
    FormatQuantityDummyEnum
)