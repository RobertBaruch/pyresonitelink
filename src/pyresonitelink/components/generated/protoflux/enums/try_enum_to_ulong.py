"""Generated component: TryEnumToUlong.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TryEnumToUlongBase(GeneratedComponent):
    """Base class for TryEnumToUlong<T> variants."""

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
class TryEnumToUlongBool(TryEnumToUlongBase):
    """TryEnumToUlong<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class TryEnumToUlongByte(TryEnumToUlongBase):
    """TryEnumToUlong<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class TryEnumToUlongUshort(TryEnumToUlongBase):
    """TryEnumToUlong<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class TryEnumToUlongUint(TryEnumToUlongBase):
    """TryEnumToUlong<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryEnumToUlongUlong(TryEnumToUlongBase):
    """TryEnumToUlong<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class TryEnumToUlongSbyte(TryEnumToUlongBase):
    """TryEnumToUlong<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class TryEnumToUlongShort(TryEnumToUlongBase):
    """TryEnumToUlong<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class TryEnumToUlongInt(TryEnumToUlongBase):
    """TryEnumToUlong<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryEnumToUlongLong(TryEnumToUlongBase):
    """TryEnumToUlong<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryEnumToUlongFloat(TryEnumToUlongBase):
    """TryEnumToUlong<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class TryEnumToUlongDouble(TryEnumToUlongBase):
    """TryEnumToUlong<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class TryEnumToUlongDecimal(TryEnumToUlongBase):
    """TryEnumToUlong<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class TryEnumToUlongChar(TryEnumToUlongBase):
    """TryEnumToUlong<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class TryEnumToUlongString(TryEnumToUlongBase):
    """TryEnumToUlong<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class TryEnumToUlongUri(TryEnumToUlongBase):
    """TryEnumToUlong<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class TryEnumToUlongBool2(TryEnumToUlongBase):
    """TryEnumToUlong<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class TryEnumToUlongByte2(TryEnumToUlongBase):
    """TryEnumToUlong<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class TryEnumToUlongUshort2(TryEnumToUlongBase):
    """TryEnumToUlong<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class TryEnumToUlongUint2(TryEnumToUlongBase):
    """TryEnumToUlong<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class TryEnumToUlongUlong2(TryEnumToUlongBase):
    """TryEnumToUlong<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class TryEnumToUlongSbyte2(TryEnumToUlongBase):
    """TryEnumToUlong<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class TryEnumToUlongShort2(TryEnumToUlongBase):
    """TryEnumToUlong<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class TryEnumToUlongInt2(TryEnumToUlongBase):
    """TryEnumToUlong<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class TryEnumToUlongLong2(TryEnumToUlongBase):
    """TryEnumToUlong<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class TryEnumToUlongFloat2(TryEnumToUlongBase):
    """TryEnumToUlong<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class TryEnumToUlongDouble2(TryEnumToUlongBase):
    """TryEnumToUlong<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class TryEnumToUlongBool3(TryEnumToUlongBase):
    """TryEnumToUlong<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class TryEnumToUlongByte3(TryEnumToUlongBase):
    """TryEnumToUlong<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class TryEnumToUlongUshort3(TryEnumToUlongBase):
    """TryEnumToUlong<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class TryEnumToUlongUint3(TryEnumToUlongBase):
    """TryEnumToUlong<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class TryEnumToUlongUlong3(TryEnumToUlongBase):
    """TryEnumToUlong<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class TryEnumToUlongSbyte3(TryEnumToUlongBase):
    """TryEnumToUlong<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class TryEnumToUlongShort3(TryEnumToUlongBase):
    """TryEnumToUlong<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class TryEnumToUlongInt3(TryEnumToUlongBase):
    """TryEnumToUlong<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class TryEnumToUlongLong3(TryEnumToUlongBase):
    """TryEnumToUlong<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class TryEnumToUlongFloat3(TryEnumToUlongBase):
    """TryEnumToUlong<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class TryEnumToUlongDouble3(TryEnumToUlongBase):
    """TryEnumToUlong<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class TryEnumToUlongBool4(TryEnumToUlongBase):
    """TryEnumToUlong<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class TryEnumToUlongByte4(TryEnumToUlongBase):
    """TryEnumToUlong<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class TryEnumToUlongUshort4(TryEnumToUlongBase):
    """TryEnumToUlong<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class TryEnumToUlongUint4(TryEnumToUlongBase):
    """TryEnumToUlong<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class TryEnumToUlongUlong4(TryEnumToUlongBase):
    """TryEnumToUlong<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class TryEnumToUlongSbyte4(TryEnumToUlongBase):
    """TryEnumToUlong<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class TryEnumToUlongShort4(TryEnumToUlongBase):
    """TryEnumToUlong<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class TryEnumToUlongInt4(TryEnumToUlongBase):
    """TryEnumToUlong<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class TryEnumToUlongLong4(TryEnumToUlongBase):
    """TryEnumToUlong<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class TryEnumToUlongFloat4(TryEnumToUlongBase):
    """TryEnumToUlong<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class TryEnumToUlongDouble4(TryEnumToUlongBase):
    """TryEnumToUlong<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class TryEnumToUlongFloat_2x2(TryEnumToUlongBase):
    """TryEnumToUlong<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class TryEnumToUlongDouble_2x2(TryEnumToUlongBase):
    """TryEnumToUlong<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class TryEnumToUlongFloat_3x3(TryEnumToUlongBase):
    """TryEnumToUlong<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class TryEnumToUlongDouble_3x3(TryEnumToUlongBase):
    """TryEnumToUlong<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class TryEnumToUlongFloat_4x4(TryEnumToUlongBase):
    """TryEnumToUlong<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class TryEnumToUlongDouble_4x4(TryEnumToUlongBase):
    """TryEnumToUlong<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class TryEnumToUlongFloatQ(TryEnumToUlongBase):
    """TryEnumToUlong<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class TryEnumToUlongDoubleQ(TryEnumToUlongBase):
    """TryEnumToUlong<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class TryEnumToUlongDateTime(TryEnumToUlongBase):
    """TryEnumToUlong<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class TryEnumToUlongTimeSpan(TryEnumToUlongBase):
    """TryEnumToUlong<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class TryEnumToUlongColor(TryEnumToUlongBase):
    """TryEnumToUlong<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class TryEnumToUlongColorX(TryEnumToUlongBase):
    """TryEnumToUlong<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class TryEnumToUlongShadowCastMode(TryEnumToUlongBase):
    """TryEnumToUlong<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class TryEnumToUlongLightType(TryEnumToUlongBase):
    """TryEnumToUlong<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class TryEnumToUlongSessionAccessLevel(TryEnumToUlongBase):
    """TryEnumToUlong<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class TryEnumToUlongKey(TryEnumToUlongBase):
    """TryEnumToUlong<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class TryEnumToUlongHttpStatusCode(TryEnumToUlongBase):
    """TryEnumToUlong<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class TryEnumToUlongHeadOutputDevice(TryEnumToUlongBase):
    """TryEnumToUlong<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class TryEnumToUlongReflectionProbeClear(TryEnumToUlongBase):
    """TryEnumToUlong<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class TryEnumToUlongReflectionProbeType(TryEnumToUlongBase):
    """TryEnumToUlong<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class TryEnumToUlongReflectionProbeTimeSlicingMode(TryEnumToUlongBase):
    """TryEnumToUlong<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class TryEnumToUlongCameraClearMode(TryEnumToUlongBase):
    """TryEnumToUlong<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class TryEnumToUlongCameraPositioningMode(TryEnumToUlongBase):
    """TryEnumToUlong<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class TryEnumToUlongCameraProjection(TryEnumToUlongBase):
    """TryEnumToUlong<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class TryEnumToUlongZWrite(TryEnumToUlongBase):
    """TryEnumToUlong<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class TryEnumToUlongZTest(TryEnumToUlongBase):
    """TryEnumToUlong<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class TryEnumToUlongBlend(TryEnumToUlongBase):
    """TryEnumToUlong<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class TryEnumToUlongBlendMode(TryEnumToUlongBase):
    """TryEnumToUlong<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class TryEnumToUlongCulling(TryEnumToUlongBase):
    """TryEnumToUlong<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class TryEnumToUlongBodyNode(TryEnumToUlongBase):
    """TryEnumToUlong<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class TryEnumToUlongChirality(TryEnumToUlongBase):
    """TryEnumToUlong<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class TryEnumToUlongDummyEnum(TryEnumToUlongBase):
    """TryEnumToUlong<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToUlong<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any TryEnumToUlong variant
TryEnumToUlong = (
    TryEnumToUlongBool |
    TryEnumToUlongByte |
    TryEnumToUlongUshort |
    TryEnumToUlongUint |
    TryEnumToUlongUlong |
    TryEnumToUlongSbyte |
    TryEnumToUlongShort |
    TryEnumToUlongInt |
    TryEnumToUlongLong |
    TryEnumToUlongFloat |
    TryEnumToUlongDouble |
    TryEnumToUlongDecimal |
    TryEnumToUlongChar |
    TryEnumToUlongString |
    TryEnumToUlongUri |
    TryEnumToUlongBool2 |
    TryEnumToUlongByte2 |
    TryEnumToUlongUshort2 |
    TryEnumToUlongUint2 |
    TryEnumToUlongUlong2 |
    TryEnumToUlongSbyte2 |
    TryEnumToUlongShort2 |
    TryEnumToUlongInt2 |
    TryEnumToUlongLong2 |
    TryEnumToUlongFloat2 |
    TryEnumToUlongDouble2 |
    TryEnumToUlongBool3 |
    TryEnumToUlongByte3 |
    TryEnumToUlongUshort3 |
    TryEnumToUlongUint3 |
    TryEnumToUlongUlong3 |
    TryEnumToUlongSbyte3 |
    TryEnumToUlongShort3 |
    TryEnumToUlongInt3 |
    TryEnumToUlongLong3 |
    TryEnumToUlongFloat3 |
    TryEnumToUlongDouble3 |
    TryEnumToUlongBool4 |
    TryEnumToUlongByte4 |
    TryEnumToUlongUshort4 |
    TryEnumToUlongUint4 |
    TryEnumToUlongUlong4 |
    TryEnumToUlongSbyte4 |
    TryEnumToUlongShort4 |
    TryEnumToUlongInt4 |
    TryEnumToUlongLong4 |
    TryEnumToUlongFloat4 |
    TryEnumToUlongDouble4 |
    TryEnumToUlongFloat_2x2 |
    TryEnumToUlongDouble_2x2 |
    TryEnumToUlongFloat_3x3 |
    TryEnumToUlongDouble_3x3 |
    TryEnumToUlongFloat_4x4 |
    TryEnumToUlongDouble_4x4 |
    TryEnumToUlongFloatQ |
    TryEnumToUlongDoubleQ |
    TryEnumToUlongDateTime |
    TryEnumToUlongTimeSpan |
    TryEnumToUlongColor |
    TryEnumToUlongColorX |
    TryEnumToUlongShadowCastMode |
    TryEnumToUlongLightType |
    TryEnumToUlongSessionAccessLevel |
    TryEnumToUlongKey |
    TryEnumToUlongHttpStatusCode |
    TryEnumToUlongHeadOutputDevice |
    TryEnumToUlongReflectionProbeClear |
    TryEnumToUlongReflectionProbeType |
    TryEnumToUlongReflectionProbeTimeSlicingMode |
    TryEnumToUlongCameraClearMode |
    TryEnumToUlongCameraPositioningMode |
    TryEnumToUlongCameraProjection |
    TryEnumToUlongZWrite |
    TryEnumToUlongZTest |
    TryEnumToUlongBlend |
    TryEnumToUlongBlendMode |
    TryEnumToUlongCulling |
    TryEnumToUlongBodyNode |
    TryEnumToUlongChirality |
    TryEnumToUlongDummyEnum
)