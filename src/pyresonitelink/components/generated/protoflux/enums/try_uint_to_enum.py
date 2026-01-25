"""Generated component: TryUintToEnum.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TryUintToEnumBase(GeneratedComponent):
    """Base class for TryUintToEnum<T> variants."""

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
class TryUintToEnumBool(TryUintToEnumBase):
    """TryUintToEnum<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumByte(TryUintToEnumBase):
    """TryUintToEnum<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUshort(TryUintToEnumBase):
    """TryUintToEnum<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUint(TryUintToEnumBase):
    """TryUintToEnum<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUlong(TryUintToEnumBase):
    """TryUintToEnum<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumSbyte(TryUintToEnumBase):
    """TryUintToEnum<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumShort(TryUintToEnumBase):
    """TryUintToEnum<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumInt(TryUintToEnumBase):
    """TryUintToEnum<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumLong(TryUintToEnumBase):
    """TryUintToEnum<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat(TryUintToEnumBase):
    """TryUintToEnum<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble(TryUintToEnumBase):
    """TryUintToEnum<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDecimal(TryUintToEnumBase):
    """TryUintToEnum<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumChar(TryUintToEnumBase):
    """TryUintToEnum<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumString(TryUintToEnumBase):
    """TryUintToEnum<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUri(TryUintToEnumBase):
    """TryUintToEnum<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBool2(TryUintToEnumBase):
    """TryUintToEnum<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumByte2(TryUintToEnumBase):
    """TryUintToEnum<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUshort2(TryUintToEnumBase):
    """TryUintToEnum<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUint2(TryUintToEnumBase):
    """TryUintToEnum<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUlong2(TryUintToEnumBase):
    """TryUintToEnum<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumSbyte2(TryUintToEnumBase):
    """TryUintToEnum<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumShort2(TryUintToEnumBase):
    """TryUintToEnum<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumInt2(TryUintToEnumBase):
    """TryUintToEnum<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumLong2(TryUintToEnumBase):
    """TryUintToEnum<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat2(TryUintToEnumBase):
    """TryUintToEnum<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble2(TryUintToEnumBase):
    """TryUintToEnum<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBool3(TryUintToEnumBase):
    """TryUintToEnum<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumByte3(TryUintToEnumBase):
    """TryUintToEnum<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUshort3(TryUintToEnumBase):
    """TryUintToEnum<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUint3(TryUintToEnumBase):
    """TryUintToEnum<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUlong3(TryUintToEnumBase):
    """TryUintToEnum<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumSbyte3(TryUintToEnumBase):
    """TryUintToEnum<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumShort3(TryUintToEnumBase):
    """TryUintToEnum<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumInt3(TryUintToEnumBase):
    """TryUintToEnum<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumLong3(TryUintToEnumBase):
    """TryUintToEnum<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat3(TryUintToEnumBase):
    """TryUintToEnum<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble3(TryUintToEnumBase):
    """TryUintToEnum<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBool4(TryUintToEnumBase):
    """TryUintToEnum<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumByte4(TryUintToEnumBase):
    """TryUintToEnum<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUshort4(TryUintToEnumBase):
    """TryUintToEnum<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUint4(TryUintToEnumBase):
    """TryUintToEnum<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumUlong4(TryUintToEnumBase):
    """TryUintToEnum<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumSbyte4(TryUintToEnumBase):
    """TryUintToEnum<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumShort4(TryUintToEnumBase):
    """TryUintToEnum<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumInt4(TryUintToEnumBase):
    """TryUintToEnum<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumLong4(TryUintToEnumBase):
    """TryUintToEnum<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat4(TryUintToEnumBase):
    """TryUintToEnum<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble4(TryUintToEnumBase):
    """TryUintToEnum<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat_2x2(TryUintToEnumBase):
    """TryUintToEnum<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble_2x2(TryUintToEnumBase):
    """TryUintToEnum<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat_3x3(TryUintToEnumBase):
    """TryUintToEnum<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble_3x3(TryUintToEnumBase):
    """TryUintToEnum<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloat_4x4(TryUintToEnumBase):
    """TryUintToEnum<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDouble_4x4(TryUintToEnumBase):
    """TryUintToEnum<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumFloatQ(TryUintToEnumBase):
    """TryUintToEnum<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDoubleQ(TryUintToEnumBase):
    """TryUintToEnum<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDateTime(TryUintToEnumBase):
    """TryUintToEnum<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumTimeSpan(TryUintToEnumBase):
    """TryUintToEnum<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumColor(TryUintToEnumBase):
    """TryUintToEnum<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumColorX(TryUintToEnumBase):
    """TryUintToEnum<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumShadowCastMode(TryUintToEnumBase):
    """TryUintToEnum<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumLightType(TryUintToEnumBase):
    """TryUintToEnum<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumSessionAccessLevel(TryUintToEnumBase):
    """TryUintToEnum<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumKey(TryUintToEnumBase):
    """TryUintToEnum<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumHttpStatusCode(TryUintToEnumBase):
    """TryUintToEnum<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumHeadOutputDevice(TryUintToEnumBase):
    """TryUintToEnum<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumReflectionProbeClear(TryUintToEnumBase):
    """TryUintToEnum<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumReflectionProbeType(TryUintToEnumBase):
    """TryUintToEnum<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumReflectionProbeTimeSlicingMode(TryUintToEnumBase):
    """TryUintToEnum<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumCameraClearMode(TryUintToEnumBase):
    """TryUintToEnum<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumCameraPositioningMode(TryUintToEnumBase):
    """TryUintToEnum<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumCameraProjection(TryUintToEnumBase):
    """TryUintToEnum<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumZWrite(TryUintToEnumBase):
    """TryUintToEnum<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumZTest(TryUintToEnumBase):
    """TryUintToEnum<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBlend(TryUintToEnumBase):
    """TryUintToEnum<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBlendMode(TryUintToEnumBase):
    """TryUintToEnum<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumCulling(TryUintToEnumBase):
    """TryUintToEnum<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumBodyNode(TryUintToEnumBase):
    """TryUintToEnum<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumChirality(TryUintToEnumBase):
    """TryUintToEnum<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryUintToEnumDummyEnum(TryUintToEnumBase):
    """TryUintToEnum<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryUintToEnum<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "only_defined": "OnlyDefined",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    only_defined: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


# Type alias for any TryUintToEnum variant
TryUintToEnum = (
    TryUintToEnumBool |
    TryUintToEnumByte |
    TryUintToEnumUshort |
    TryUintToEnumUint |
    TryUintToEnumUlong |
    TryUintToEnumSbyte |
    TryUintToEnumShort |
    TryUintToEnumInt |
    TryUintToEnumLong |
    TryUintToEnumFloat |
    TryUintToEnumDouble |
    TryUintToEnumDecimal |
    TryUintToEnumChar |
    TryUintToEnumString |
    TryUintToEnumUri |
    TryUintToEnumBool2 |
    TryUintToEnumByte2 |
    TryUintToEnumUshort2 |
    TryUintToEnumUint2 |
    TryUintToEnumUlong2 |
    TryUintToEnumSbyte2 |
    TryUintToEnumShort2 |
    TryUintToEnumInt2 |
    TryUintToEnumLong2 |
    TryUintToEnumFloat2 |
    TryUintToEnumDouble2 |
    TryUintToEnumBool3 |
    TryUintToEnumByte3 |
    TryUintToEnumUshort3 |
    TryUintToEnumUint3 |
    TryUintToEnumUlong3 |
    TryUintToEnumSbyte3 |
    TryUintToEnumShort3 |
    TryUintToEnumInt3 |
    TryUintToEnumLong3 |
    TryUintToEnumFloat3 |
    TryUintToEnumDouble3 |
    TryUintToEnumBool4 |
    TryUintToEnumByte4 |
    TryUintToEnumUshort4 |
    TryUintToEnumUint4 |
    TryUintToEnumUlong4 |
    TryUintToEnumSbyte4 |
    TryUintToEnumShort4 |
    TryUintToEnumInt4 |
    TryUintToEnumLong4 |
    TryUintToEnumFloat4 |
    TryUintToEnumDouble4 |
    TryUintToEnumFloat_2x2 |
    TryUintToEnumDouble_2x2 |
    TryUintToEnumFloat_3x3 |
    TryUintToEnumDouble_3x3 |
    TryUintToEnumFloat_4x4 |
    TryUintToEnumDouble_4x4 |
    TryUintToEnumFloatQ |
    TryUintToEnumDoubleQ |
    TryUintToEnumDateTime |
    TryUintToEnumTimeSpan |
    TryUintToEnumColor |
    TryUintToEnumColorX |
    TryUintToEnumShadowCastMode |
    TryUintToEnumLightType |
    TryUintToEnumSessionAccessLevel |
    TryUintToEnumKey |
    TryUintToEnumHttpStatusCode |
    TryUintToEnumHeadOutputDevice |
    TryUintToEnumReflectionProbeClear |
    TryUintToEnumReflectionProbeType |
    TryUintToEnumReflectionProbeTimeSlicingMode |
    TryUintToEnumCameraClearMode |
    TryUintToEnumCameraPositioningMode |
    TryUintToEnumCameraProjection |
    TryUintToEnumZWrite |
    TryUintToEnumZTest |
    TryUintToEnumBlend |
    TryUintToEnumBlendMode |
    TryUintToEnumCulling |
    TryUintToEnumBodyNode |
    TryUintToEnumChirality |
    TryUintToEnumDummyEnum
)