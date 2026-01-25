"""Generated component: TryEnumToShort.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class TryEnumToShortBase(GeneratedComponent):
    """Base class for TryEnumToShort<T> variants."""

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
class TryEnumToShortBool(TryEnumToShortBase):
    """TryEnumToShort<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class TryEnumToShortByte(TryEnumToShortBase):
    """TryEnumToShort<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class TryEnumToShortUshort(TryEnumToShortBase):
    """TryEnumToShort<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class TryEnumToShortUint(TryEnumToShortBase):
    """TryEnumToShort<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class TryEnumToShortUlong(TryEnumToShortBase):
    """TryEnumToShort<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class TryEnumToShortSbyte(TryEnumToShortBase):
    """TryEnumToShort<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class TryEnumToShortShort(TryEnumToShortBase):
    """TryEnumToShort<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class TryEnumToShortInt(TryEnumToShortBase):
    """TryEnumToShort<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class TryEnumToShortLong(TryEnumToShortBase):
    """TryEnumToShort<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class TryEnumToShortFloat(TryEnumToShortBase):
    """TryEnumToShort<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class TryEnumToShortDouble(TryEnumToShortBase):
    """TryEnumToShort<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class TryEnumToShortDecimal(TryEnumToShortBase):
    """TryEnumToShort<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class TryEnumToShortChar(TryEnumToShortBase):
    """TryEnumToShort<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class TryEnumToShortString(TryEnumToShortBase):
    """TryEnumToShort<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class TryEnumToShortUri(TryEnumToShortBase):
    """TryEnumToShort<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class TryEnumToShortBool2(TryEnumToShortBase):
    """TryEnumToShort<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class TryEnumToShortByte2(TryEnumToShortBase):
    """TryEnumToShort<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class TryEnumToShortUshort2(TryEnumToShortBase):
    """TryEnumToShort<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class TryEnumToShortUint2(TryEnumToShortBase):
    """TryEnumToShort<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class TryEnumToShortUlong2(TryEnumToShortBase):
    """TryEnumToShort<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class TryEnumToShortSbyte2(TryEnumToShortBase):
    """TryEnumToShort<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class TryEnumToShortShort2(TryEnumToShortBase):
    """TryEnumToShort<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class TryEnumToShortInt2(TryEnumToShortBase):
    """TryEnumToShort<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class TryEnumToShortLong2(TryEnumToShortBase):
    """TryEnumToShort<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class TryEnumToShortFloat2(TryEnumToShortBase):
    """TryEnumToShort<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class TryEnumToShortDouble2(TryEnumToShortBase):
    """TryEnumToShort<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class TryEnumToShortBool3(TryEnumToShortBase):
    """TryEnumToShort<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class TryEnumToShortByte3(TryEnumToShortBase):
    """TryEnumToShort<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class TryEnumToShortUshort3(TryEnumToShortBase):
    """TryEnumToShort<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class TryEnumToShortUint3(TryEnumToShortBase):
    """TryEnumToShort<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class TryEnumToShortUlong3(TryEnumToShortBase):
    """TryEnumToShort<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class TryEnumToShortSbyte3(TryEnumToShortBase):
    """TryEnumToShort<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class TryEnumToShortShort3(TryEnumToShortBase):
    """TryEnumToShort<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class TryEnumToShortInt3(TryEnumToShortBase):
    """TryEnumToShort<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class TryEnumToShortLong3(TryEnumToShortBase):
    """TryEnumToShort<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class TryEnumToShortFloat3(TryEnumToShortBase):
    """TryEnumToShort<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class TryEnumToShortDouble3(TryEnumToShortBase):
    """TryEnumToShort<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class TryEnumToShortBool4(TryEnumToShortBase):
    """TryEnumToShort<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class TryEnumToShortByte4(TryEnumToShortBase):
    """TryEnumToShort<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class TryEnumToShortUshort4(TryEnumToShortBase):
    """TryEnumToShort<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class TryEnumToShortUint4(TryEnumToShortBase):
    """TryEnumToShort<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class TryEnumToShortUlong4(TryEnumToShortBase):
    """TryEnumToShort<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class TryEnumToShortSbyte4(TryEnumToShortBase):
    """TryEnumToShort<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class TryEnumToShortShort4(TryEnumToShortBase):
    """TryEnumToShort<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class TryEnumToShortInt4(TryEnumToShortBase):
    """TryEnumToShort<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class TryEnumToShortLong4(TryEnumToShortBase):
    """TryEnumToShort<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class TryEnumToShortFloat4(TryEnumToShortBase):
    """TryEnumToShort<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class TryEnumToShortDouble4(TryEnumToShortBase):
    """TryEnumToShort<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class TryEnumToShortFloat_2x2(TryEnumToShortBase):
    """TryEnumToShort<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class TryEnumToShortDouble_2x2(TryEnumToShortBase):
    """TryEnumToShort<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class TryEnumToShortFloat_3x3(TryEnumToShortBase):
    """TryEnumToShort<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class TryEnumToShortDouble_3x3(TryEnumToShortBase):
    """TryEnumToShort<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class TryEnumToShortFloat_4x4(TryEnumToShortBase):
    """TryEnumToShort<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class TryEnumToShortDouble_4x4(TryEnumToShortBase):
    """TryEnumToShort<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class TryEnumToShortFloatQ(TryEnumToShortBase):
    """TryEnumToShort<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class TryEnumToShortDoubleQ(TryEnumToShortBase):
    """TryEnumToShort<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class TryEnumToShortDateTime(TryEnumToShortBase):
    """TryEnumToShort<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class TryEnumToShortTimeSpan(TryEnumToShortBase):
    """TryEnumToShort<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class TryEnumToShortColor(TryEnumToShortBase):
    """TryEnumToShort<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class TryEnumToShortColorX(TryEnumToShortBase):
    """TryEnumToShort<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class TryEnumToShortShadowCastMode(TryEnumToShortBase):
    """TryEnumToShort<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class TryEnumToShortLightType(TryEnumToShortBase):
    """TryEnumToShort<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class TryEnumToShortSessionAccessLevel(TryEnumToShortBase):
    """TryEnumToShort<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class TryEnumToShortKey(TryEnumToShortBase):
    """TryEnumToShort<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class TryEnumToShortHttpStatusCode(TryEnumToShortBase):
    """TryEnumToShort<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class TryEnumToShortHeadOutputDevice(TryEnumToShortBase):
    """TryEnumToShort<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class TryEnumToShortReflectionProbeClear(TryEnumToShortBase):
    """TryEnumToShort<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class TryEnumToShortReflectionProbeType(TryEnumToShortBase):
    """TryEnumToShort<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class TryEnumToShortReflectionProbeTimeSlicingMode(TryEnumToShortBase):
    """TryEnumToShort<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class TryEnumToShortCameraClearMode(TryEnumToShortBase):
    """TryEnumToShort<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class TryEnumToShortCameraPositioningMode(TryEnumToShortBase):
    """TryEnumToShort<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class TryEnumToShortCameraProjection(TryEnumToShortBase):
    """TryEnumToShort<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class TryEnumToShortZWrite(TryEnumToShortBase):
    """TryEnumToShort<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class TryEnumToShortZTest(TryEnumToShortBase):
    """TryEnumToShort<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class TryEnumToShortBlend(TryEnumToShortBase):
    """TryEnumToShort<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class TryEnumToShortBlendMode(TryEnumToShortBase):
    """TryEnumToShort<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class TryEnumToShortCulling(TryEnumToShortBase):
    """TryEnumToShort<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class TryEnumToShortBodyNode(TryEnumToShortBase):
    """TryEnumToShort<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class TryEnumToShortChirality(TryEnumToShortBase):
    """TryEnumToShort<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class TryEnumToShortDummyEnum(TryEnumToShortBase):
    """TryEnumToShort<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Enums.TryEnumToShort<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "fail_value": "FailValue",
        "value": "Value",
    }

    fail_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any TryEnumToShort variant
TryEnumToShort = (
    TryEnumToShortBool |
    TryEnumToShortByte |
    TryEnumToShortUshort |
    TryEnumToShortUint |
    TryEnumToShortUlong |
    TryEnumToShortSbyte |
    TryEnumToShortShort |
    TryEnumToShortInt |
    TryEnumToShortLong |
    TryEnumToShortFloat |
    TryEnumToShortDouble |
    TryEnumToShortDecimal |
    TryEnumToShortChar |
    TryEnumToShortString |
    TryEnumToShortUri |
    TryEnumToShortBool2 |
    TryEnumToShortByte2 |
    TryEnumToShortUshort2 |
    TryEnumToShortUint2 |
    TryEnumToShortUlong2 |
    TryEnumToShortSbyte2 |
    TryEnumToShortShort2 |
    TryEnumToShortInt2 |
    TryEnumToShortLong2 |
    TryEnumToShortFloat2 |
    TryEnumToShortDouble2 |
    TryEnumToShortBool3 |
    TryEnumToShortByte3 |
    TryEnumToShortUshort3 |
    TryEnumToShortUint3 |
    TryEnumToShortUlong3 |
    TryEnumToShortSbyte3 |
    TryEnumToShortShort3 |
    TryEnumToShortInt3 |
    TryEnumToShortLong3 |
    TryEnumToShortFloat3 |
    TryEnumToShortDouble3 |
    TryEnumToShortBool4 |
    TryEnumToShortByte4 |
    TryEnumToShortUshort4 |
    TryEnumToShortUint4 |
    TryEnumToShortUlong4 |
    TryEnumToShortSbyte4 |
    TryEnumToShortShort4 |
    TryEnumToShortInt4 |
    TryEnumToShortLong4 |
    TryEnumToShortFloat4 |
    TryEnumToShortDouble4 |
    TryEnumToShortFloat_2x2 |
    TryEnumToShortDouble_2x2 |
    TryEnumToShortFloat_3x3 |
    TryEnumToShortDouble_3x3 |
    TryEnumToShortFloat_4x4 |
    TryEnumToShortDouble_4x4 |
    TryEnumToShortFloatQ |
    TryEnumToShortDoubleQ |
    TryEnumToShortDateTime |
    TryEnumToShortTimeSpan |
    TryEnumToShortColor |
    TryEnumToShortColorX |
    TryEnumToShortShadowCastMode |
    TryEnumToShortLightType |
    TryEnumToShortSessionAccessLevel |
    TryEnumToShortKey |
    TryEnumToShortHttpStatusCode |
    TryEnumToShortHeadOutputDevice |
    TryEnumToShortReflectionProbeClear |
    TryEnumToShortReflectionProbeType |
    TryEnumToShortReflectionProbeTimeSlicingMode |
    TryEnumToShortCameraClearMode |
    TryEnumToShortCameraPositioningMode |
    TryEnumToShortCameraProjection |
    TryEnumToShortZWrite |
    TryEnumToShortZTest |
    TryEnumToShortBlend |
    TryEnumToShortBlendMode |
    TryEnumToShortCulling |
    TryEnumToShortBodyNode |
    TryEnumToShortChirality |
    TryEnumToShortDummyEnum
)