"""Generated component: TryLongToEnum.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TryLongToEnumBase(GeneratedComponent):
    """Base class for TryLongToEnum<T> variants."""

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
class TryLongToEnumBool(TryLongToEnumBase):
    """TryLongToEnum<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumByte(TryLongToEnumBase):
    """TryLongToEnum<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUshort(TryLongToEnumBase):
    """TryLongToEnum<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUint(TryLongToEnumBase):
    """TryLongToEnum<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUlong(TryLongToEnumBase):
    """TryLongToEnum<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumSbyte(TryLongToEnumBase):
    """TryLongToEnum<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumShort(TryLongToEnumBase):
    """TryLongToEnum<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumInt(TryLongToEnumBase):
    """TryLongToEnum<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumLong(TryLongToEnumBase):
    """TryLongToEnum<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat(TryLongToEnumBase):
    """TryLongToEnum<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble(TryLongToEnumBase):
    """TryLongToEnum<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDecimal(TryLongToEnumBase):
    """TryLongToEnum<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumChar(TryLongToEnumBase):
    """TryLongToEnum<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumString(TryLongToEnumBase):
    """TryLongToEnum<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUri(TryLongToEnumBase):
    """TryLongToEnum<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBool2(TryLongToEnumBase):
    """TryLongToEnum<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumByte2(TryLongToEnumBase):
    """TryLongToEnum<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUshort2(TryLongToEnumBase):
    """TryLongToEnum<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUint2(TryLongToEnumBase):
    """TryLongToEnum<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUlong2(TryLongToEnumBase):
    """TryLongToEnum<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumSbyte2(TryLongToEnumBase):
    """TryLongToEnum<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumShort2(TryLongToEnumBase):
    """TryLongToEnum<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumInt2(TryLongToEnumBase):
    """TryLongToEnum<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumLong2(TryLongToEnumBase):
    """TryLongToEnum<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat2(TryLongToEnumBase):
    """TryLongToEnum<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble2(TryLongToEnumBase):
    """TryLongToEnum<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBool3(TryLongToEnumBase):
    """TryLongToEnum<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumByte3(TryLongToEnumBase):
    """TryLongToEnum<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUshort3(TryLongToEnumBase):
    """TryLongToEnum<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUint3(TryLongToEnumBase):
    """TryLongToEnum<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUlong3(TryLongToEnumBase):
    """TryLongToEnum<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumSbyte3(TryLongToEnumBase):
    """TryLongToEnum<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumShort3(TryLongToEnumBase):
    """TryLongToEnum<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumInt3(TryLongToEnumBase):
    """TryLongToEnum<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumLong3(TryLongToEnumBase):
    """TryLongToEnum<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat3(TryLongToEnumBase):
    """TryLongToEnum<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble3(TryLongToEnumBase):
    """TryLongToEnum<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBool4(TryLongToEnumBase):
    """TryLongToEnum<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumByte4(TryLongToEnumBase):
    """TryLongToEnum<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUshort4(TryLongToEnumBase):
    """TryLongToEnum<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUint4(TryLongToEnumBase):
    """TryLongToEnum<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumUlong4(TryLongToEnumBase):
    """TryLongToEnum<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumSbyte4(TryLongToEnumBase):
    """TryLongToEnum<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumShort4(TryLongToEnumBase):
    """TryLongToEnum<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumInt4(TryLongToEnumBase):
    """TryLongToEnum<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumLong4(TryLongToEnumBase):
    """TryLongToEnum<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat4(TryLongToEnumBase):
    """TryLongToEnum<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble4(TryLongToEnumBase):
    """TryLongToEnum<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat_2x2(TryLongToEnumBase):
    """TryLongToEnum<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble_2x2(TryLongToEnumBase):
    """TryLongToEnum<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat_3x3(TryLongToEnumBase):
    """TryLongToEnum<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble_3x3(TryLongToEnumBase):
    """TryLongToEnum<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloat_4x4(TryLongToEnumBase):
    """TryLongToEnum<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDouble_4x4(TryLongToEnumBase):
    """TryLongToEnum<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumFloatQ(TryLongToEnumBase):
    """TryLongToEnum<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDoubleQ(TryLongToEnumBase):
    """TryLongToEnum<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDateTime(TryLongToEnumBase):
    """TryLongToEnum<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumTimeSpan(TryLongToEnumBase):
    """TryLongToEnum<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumColor(TryLongToEnumBase):
    """TryLongToEnum<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumColorX(TryLongToEnumBase):
    """TryLongToEnum<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumShadowCastMode(TryLongToEnumBase):
    """TryLongToEnum<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumLightType(TryLongToEnumBase):
    """TryLongToEnum<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumSessionAccessLevel(TryLongToEnumBase):
    """TryLongToEnum<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumKey(TryLongToEnumBase):
    """TryLongToEnum<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumHttpStatusCode(TryLongToEnumBase):
    """TryLongToEnum<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumHeadOutputDevice(TryLongToEnumBase):
    """TryLongToEnum<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumReflectionProbeClear(TryLongToEnumBase):
    """TryLongToEnum<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumReflectionProbeType(TryLongToEnumBase):
    """TryLongToEnum<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumReflectionProbeTimeSlicingMode(TryLongToEnumBase):
    """TryLongToEnum<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumCameraClearMode(TryLongToEnumBase):
    """TryLongToEnum<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumCameraPositioningMode(TryLongToEnumBase):
    """TryLongToEnum<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumCameraProjection(TryLongToEnumBase):
    """TryLongToEnum<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumZWrite(TryLongToEnumBase):
    """TryLongToEnum<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumZTest(TryLongToEnumBase):
    """TryLongToEnum<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBlend(TryLongToEnumBase):
    """TryLongToEnum<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBlendMode(TryLongToEnumBase):
    """TryLongToEnum<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumCulling(TryLongToEnumBase):
    """TryLongToEnum<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumBodyNode(TryLongToEnumBase):
    """TryLongToEnum<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumChirality(TryLongToEnumBase):
    """TryLongToEnum<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryLongToEnumDummyEnum(TryLongToEnumBase):
    """TryLongToEnum<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryLongToEnum<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


# Type alias for any TryLongToEnum variant
TryLongToEnum = (
    TryLongToEnumBool |
    TryLongToEnumByte |
    TryLongToEnumUshort |
    TryLongToEnumUint |
    TryLongToEnumUlong |
    TryLongToEnumSbyte |
    TryLongToEnumShort |
    TryLongToEnumInt |
    TryLongToEnumLong |
    TryLongToEnumFloat |
    TryLongToEnumDouble |
    TryLongToEnumDecimal |
    TryLongToEnumChar |
    TryLongToEnumString |
    TryLongToEnumUri |
    TryLongToEnumBool2 |
    TryLongToEnumByte2 |
    TryLongToEnumUshort2 |
    TryLongToEnumUint2 |
    TryLongToEnumUlong2 |
    TryLongToEnumSbyte2 |
    TryLongToEnumShort2 |
    TryLongToEnumInt2 |
    TryLongToEnumLong2 |
    TryLongToEnumFloat2 |
    TryLongToEnumDouble2 |
    TryLongToEnumBool3 |
    TryLongToEnumByte3 |
    TryLongToEnumUshort3 |
    TryLongToEnumUint3 |
    TryLongToEnumUlong3 |
    TryLongToEnumSbyte3 |
    TryLongToEnumShort3 |
    TryLongToEnumInt3 |
    TryLongToEnumLong3 |
    TryLongToEnumFloat3 |
    TryLongToEnumDouble3 |
    TryLongToEnumBool4 |
    TryLongToEnumByte4 |
    TryLongToEnumUshort4 |
    TryLongToEnumUint4 |
    TryLongToEnumUlong4 |
    TryLongToEnumSbyte4 |
    TryLongToEnumShort4 |
    TryLongToEnumInt4 |
    TryLongToEnumLong4 |
    TryLongToEnumFloat4 |
    TryLongToEnumDouble4 |
    TryLongToEnumFloat_2x2 |
    TryLongToEnumDouble_2x2 |
    TryLongToEnumFloat_3x3 |
    TryLongToEnumDouble_3x3 |
    TryLongToEnumFloat_4x4 |
    TryLongToEnumDouble_4x4 |
    TryLongToEnumFloatQ |
    TryLongToEnumDoubleQ |
    TryLongToEnumDateTime |
    TryLongToEnumTimeSpan |
    TryLongToEnumColor |
    TryLongToEnumColorX |
    TryLongToEnumShadowCastMode |
    TryLongToEnumLightType |
    TryLongToEnumSessionAccessLevel |
    TryLongToEnumKey |
    TryLongToEnumHttpStatusCode |
    TryLongToEnumHeadOutputDevice |
    TryLongToEnumReflectionProbeClear |
    TryLongToEnumReflectionProbeType |
    TryLongToEnumReflectionProbeTimeSlicingMode |
    TryLongToEnumCameraClearMode |
    TryLongToEnumCameraPositioningMode |
    TryLongToEnumCameraProjection |
    TryLongToEnumZWrite |
    TryLongToEnumZTest |
    TryLongToEnumBlend |
    TryLongToEnumBlendMode |
    TryLongToEnumCulling |
    TryLongToEnumBodyNode |
    TryLongToEnumChirality |
    TryLongToEnumDummyEnum
)