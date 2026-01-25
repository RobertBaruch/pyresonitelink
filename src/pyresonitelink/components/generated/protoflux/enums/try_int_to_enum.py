"""Generated component: TryIntToEnum.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TryIntToEnumBase(GeneratedComponent):
    """Base class for TryIntToEnum<T> variants."""

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
class TryIntToEnumBool(TryIntToEnumBase):
    """TryIntToEnum<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumByte(TryIntToEnumBase):
    """TryIntToEnum<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUshort(TryIntToEnumBase):
    """TryIntToEnum<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUint(TryIntToEnumBase):
    """TryIntToEnum<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUlong(TryIntToEnumBase):
    """TryIntToEnum<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumSbyte(TryIntToEnumBase):
    """TryIntToEnum<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumShort(TryIntToEnumBase):
    """TryIntToEnum<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumInt(TryIntToEnumBase):
    """TryIntToEnum<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumLong(TryIntToEnumBase):
    """TryIntToEnum<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat(TryIntToEnumBase):
    """TryIntToEnum<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble(TryIntToEnumBase):
    """TryIntToEnum<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDecimal(TryIntToEnumBase):
    """TryIntToEnum<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumChar(TryIntToEnumBase):
    """TryIntToEnum<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumString(TryIntToEnumBase):
    """TryIntToEnum<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUri(TryIntToEnumBase):
    """TryIntToEnum<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBool2(TryIntToEnumBase):
    """TryIntToEnum<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumByte2(TryIntToEnumBase):
    """TryIntToEnum<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUshort2(TryIntToEnumBase):
    """TryIntToEnum<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUint2(TryIntToEnumBase):
    """TryIntToEnum<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUlong2(TryIntToEnumBase):
    """TryIntToEnum<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumSbyte2(TryIntToEnumBase):
    """TryIntToEnum<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumShort2(TryIntToEnumBase):
    """TryIntToEnum<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumInt2(TryIntToEnumBase):
    """TryIntToEnum<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumLong2(TryIntToEnumBase):
    """TryIntToEnum<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat2(TryIntToEnumBase):
    """TryIntToEnum<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble2(TryIntToEnumBase):
    """TryIntToEnum<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBool3(TryIntToEnumBase):
    """TryIntToEnum<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumByte3(TryIntToEnumBase):
    """TryIntToEnum<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUshort3(TryIntToEnumBase):
    """TryIntToEnum<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUint3(TryIntToEnumBase):
    """TryIntToEnum<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUlong3(TryIntToEnumBase):
    """TryIntToEnum<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumSbyte3(TryIntToEnumBase):
    """TryIntToEnum<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumShort3(TryIntToEnumBase):
    """TryIntToEnum<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumInt3(TryIntToEnumBase):
    """TryIntToEnum<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumLong3(TryIntToEnumBase):
    """TryIntToEnum<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat3(TryIntToEnumBase):
    """TryIntToEnum<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble3(TryIntToEnumBase):
    """TryIntToEnum<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBool4(TryIntToEnumBase):
    """TryIntToEnum<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumByte4(TryIntToEnumBase):
    """TryIntToEnum<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUshort4(TryIntToEnumBase):
    """TryIntToEnum<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUint4(TryIntToEnumBase):
    """TryIntToEnum<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumUlong4(TryIntToEnumBase):
    """TryIntToEnum<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumSbyte4(TryIntToEnumBase):
    """TryIntToEnum<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumShort4(TryIntToEnumBase):
    """TryIntToEnum<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumInt4(TryIntToEnumBase):
    """TryIntToEnum<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumLong4(TryIntToEnumBase):
    """TryIntToEnum<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat4(TryIntToEnumBase):
    """TryIntToEnum<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble4(TryIntToEnumBase):
    """TryIntToEnum<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat_2x2(TryIntToEnumBase):
    """TryIntToEnum<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble_2x2(TryIntToEnumBase):
    """TryIntToEnum<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat_3x3(TryIntToEnumBase):
    """TryIntToEnum<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble_3x3(TryIntToEnumBase):
    """TryIntToEnum<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloat_4x4(TryIntToEnumBase):
    """TryIntToEnum<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDouble_4x4(TryIntToEnumBase):
    """TryIntToEnum<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumFloatQ(TryIntToEnumBase):
    """TryIntToEnum<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDoubleQ(TryIntToEnumBase):
    """TryIntToEnum<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDateTime(TryIntToEnumBase):
    """TryIntToEnum<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumTimeSpan(TryIntToEnumBase):
    """TryIntToEnum<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumColor(TryIntToEnumBase):
    """TryIntToEnum<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumColorX(TryIntToEnumBase):
    """TryIntToEnum<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumShadowCastMode(TryIntToEnumBase):
    """TryIntToEnum<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumLightType(TryIntToEnumBase):
    """TryIntToEnum<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumSessionAccessLevel(TryIntToEnumBase):
    """TryIntToEnum<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumKey(TryIntToEnumBase):
    """TryIntToEnum<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumHttpStatusCode(TryIntToEnumBase):
    """TryIntToEnum<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumHeadOutputDevice(TryIntToEnumBase):
    """TryIntToEnum<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumReflectionProbeClear(TryIntToEnumBase):
    """TryIntToEnum<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumReflectionProbeType(TryIntToEnumBase):
    """TryIntToEnum<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumReflectionProbeTimeSlicingMode(TryIntToEnumBase):
    """TryIntToEnum<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumCameraClearMode(TryIntToEnumBase):
    """TryIntToEnum<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumCameraPositioningMode(TryIntToEnumBase):
    """TryIntToEnum<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumCameraProjection(TryIntToEnumBase):
    """TryIntToEnum<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumZWrite(TryIntToEnumBase):
    """TryIntToEnum<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumZTest(TryIntToEnumBase):
    """TryIntToEnum<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBlend(TryIntToEnumBase):
    """TryIntToEnum<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBlendMode(TryIntToEnumBase):
    """TryIntToEnum<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumCulling(TryIntToEnumBase):
    """TryIntToEnum<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumBodyNode(TryIntToEnumBase):
    """TryIntToEnum<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumChirality(TryIntToEnumBase):
    """TryIntToEnum<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryIntToEnumDummyEnum(TryIntToEnumBase):
    """TryIntToEnum<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryIntToEnum<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


# Type alias for any TryIntToEnum variant
TryIntToEnum = (
    TryIntToEnumBool |
    TryIntToEnumByte |
    TryIntToEnumUshort |
    TryIntToEnumUint |
    TryIntToEnumUlong |
    TryIntToEnumSbyte |
    TryIntToEnumShort |
    TryIntToEnumInt |
    TryIntToEnumLong |
    TryIntToEnumFloat |
    TryIntToEnumDouble |
    TryIntToEnumDecimal |
    TryIntToEnumChar |
    TryIntToEnumString |
    TryIntToEnumUri |
    TryIntToEnumBool2 |
    TryIntToEnumByte2 |
    TryIntToEnumUshort2 |
    TryIntToEnumUint2 |
    TryIntToEnumUlong2 |
    TryIntToEnumSbyte2 |
    TryIntToEnumShort2 |
    TryIntToEnumInt2 |
    TryIntToEnumLong2 |
    TryIntToEnumFloat2 |
    TryIntToEnumDouble2 |
    TryIntToEnumBool3 |
    TryIntToEnumByte3 |
    TryIntToEnumUshort3 |
    TryIntToEnumUint3 |
    TryIntToEnumUlong3 |
    TryIntToEnumSbyte3 |
    TryIntToEnumShort3 |
    TryIntToEnumInt3 |
    TryIntToEnumLong3 |
    TryIntToEnumFloat3 |
    TryIntToEnumDouble3 |
    TryIntToEnumBool4 |
    TryIntToEnumByte4 |
    TryIntToEnumUshort4 |
    TryIntToEnumUint4 |
    TryIntToEnumUlong4 |
    TryIntToEnumSbyte4 |
    TryIntToEnumShort4 |
    TryIntToEnumInt4 |
    TryIntToEnumLong4 |
    TryIntToEnumFloat4 |
    TryIntToEnumDouble4 |
    TryIntToEnumFloat_2x2 |
    TryIntToEnumDouble_2x2 |
    TryIntToEnumFloat_3x3 |
    TryIntToEnumDouble_3x3 |
    TryIntToEnumFloat_4x4 |
    TryIntToEnumDouble_4x4 |
    TryIntToEnumFloatQ |
    TryIntToEnumDoubleQ |
    TryIntToEnumDateTime |
    TryIntToEnumTimeSpan |
    TryIntToEnumColor |
    TryIntToEnumColorX |
    TryIntToEnumShadowCastMode |
    TryIntToEnumLightType |
    TryIntToEnumSessionAccessLevel |
    TryIntToEnumKey |
    TryIntToEnumHttpStatusCode |
    TryIntToEnumHeadOutputDevice |
    TryIntToEnumReflectionProbeClear |
    TryIntToEnumReflectionProbeType |
    TryIntToEnumReflectionProbeTimeSlicingMode |
    TryIntToEnumCameraClearMode |
    TryIntToEnumCameraPositioningMode |
    TryIntToEnumCameraProjection |
    TryIntToEnumZWrite |
    TryIntToEnumZTest |
    TryIntToEnumBlend |
    TryIntToEnumBlendMode |
    TryIntToEnumCulling |
    TryIntToEnumBodyNode |
    TryIntToEnumChirality |
    TryIntToEnumDummyEnum
)