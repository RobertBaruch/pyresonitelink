"""Generated component: PackNullable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class PackNullableBase(GeneratedComponent):
    """Base class for PackNullable<T> variants."""

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
class PackNullableBool(PackNullableBase):
    """PackNullable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class PackNullableByte(PackNullableBase):
    """PackNullable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class PackNullableUshort(PackNullableBase):
    """PackNullable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class PackNullableUint(PackNullableBase):
    """PackNullable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class PackNullableUlong(PackNullableBase):
    """PackNullable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class PackNullableSbyte(PackNullableBase):
    """PackNullable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class PackNullableShort(PackNullableBase):
    """PackNullable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class PackNullableInt(PackNullableBase):
    """PackNullable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class PackNullableLong(PackNullableBase):
    """PackNullable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class PackNullableFloat(PackNullableBase):
    """PackNullable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class PackNullableDouble(PackNullableBase):
    """PackNullable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class PackNullableDecimal(PackNullableBase):
    """PackNullable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class PackNullableChar(PackNullableBase):
    """PackNullable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class PackNullableString(PackNullableBase):
    """PackNullable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class PackNullableUri(PackNullableBase):
    """PackNullable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class PackNullableBool2(PackNullableBase):
    """PackNullable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class PackNullableByte2(PackNullableBase):
    """PackNullable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class PackNullableUshort2(PackNullableBase):
    """PackNullable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class PackNullableUint2(PackNullableBase):
    """PackNullable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class PackNullableUlong2(PackNullableBase):
    """PackNullable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class PackNullableSbyte2(PackNullableBase):
    """PackNullable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class PackNullableShort2(PackNullableBase):
    """PackNullable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class PackNullableInt2(PackNullableBase):
    """PackNullable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class PackNullableLong2(PackNullableBase):
    """PackNullable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class PackNullableFloat2(PackNullableBase):
    """PackNullable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class PackNullableDouble2(PackNullableBase):
    """PackNullable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class PackNullableBool3(PackNullableBase):
    """PackNullable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class PackNullableByte3(PackNullableBase):
    """PackNullable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class PackNullableUshort3(PackNullableBase):
    """PackNullable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class PackNullableUint3(PackNullableBase):
    """PackNullable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class PackNullableUlong3(PackNullableBase):
    """PackNullable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class PackNullableSbyte3(PackNullableBase):
    """PackNullable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class PackNullableShort3(PackNullableBase):
    """PackNullable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class PackNullableInt3(PackNullableBase):
    """PackNullable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class PackNullableLong3(PackNullableBase):
    """PackNullable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class PackNullableFloat3(PackNullableBase):
    """PackNullable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class PackNullableDouble3(PackNullableBase):
    """PackNullable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class PackNullableBool4(PackNullableBase):
    """PackNullable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class PackNullableByte4(PackNullableBase):
    """PackNullable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class PackNullableUshort4(PackNullableBase):
    """PackNullable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class PackNullableUint4(PackNullableBase):
    """PackNullable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class PackNullableUlong4(PackNullableBase):
    """PackNullable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class PackNullableSbyte4(PackNullableBase):
    """PackNullable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class PackNullableShort4(PackNullableBase):
    """PackNullable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class PackNullableInt4(PackNullableBase):
    """PackNullable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class PackNullableLong4(PackNullableBase):
    """PackNullable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class PackNullableFloat4(PackNullableBase):
    """PackNullable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class PackNullableDouble4(PackNullableBase):
    """PackNullable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class PackNullableFloat_2x2(PackNullableBase):
    """PackNullable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class PackNullableDouble_2x2(PackNullableBase):
    """PackNullable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class PackNullableFloat_3x3(PackNullableBase):
    """PackNullable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class PackNullableDouble_3x3(PackNullableBase):
    """PackNullable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class PackNullableFloat_4x4(PackNullableBase):
    """PackNullable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class PackNullableDouble_4x4(PackNullableBase):
    """PackNullable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class PackNullableFloatQ(PackNullableBase):
    """PackNullable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class PackNullableDoubleQ(PackNullableBase):
    """PackNullable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class PackNullableDateTime(PackNullableBase):
    """PackNullable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class PackNullableTimeSpan(PackNullableBase):
    """PackNullable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class PackNullableColor(PackNullableBase):
    """PackNullable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class PackNullableColorX(PackNullableBase):
    """PackNullable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class PackNullableShadowCastMode(PackNullableBase):
    """PackNullable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class PackNullableLightType(PackNullableBase):
    """PackNullable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class PackNullableSessionAccessLevel(PackNullableBase):
    """PackNullable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class PackNullableKey(PackNullableBase):
    """PackNullable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class PackNullableHttpStatusCode(PackNullableBase):
    """PackNullable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class PackNullableHeadOutputDevice(PackNullableBase):
    """PackNullable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class PackNullableReflectionProbeClear(PackNullableBase):
    """PackNullable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class PackNullableReflectionProbeType(PackNullableBase):
    """PackNullable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class PackNullableReflectionProbeTimeSlicingMode(PackNullableBase):
    """PackNullable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class PackNullableCameraClearMode(PackNullableBase):
    """PackNullable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class PackNullableCameraPositioningMode(PackNullableBase):
    """PackNullable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class PackNullableCameraProjection(PackNullableBase):
    """PackNullable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class PackNullableZWrite(PackNullableBase):
    """PackNullable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class PackNullableZTest(PackNullableBase):
    """PackNullable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class PackNullableBlend(PackNullableBase):
    """PackNullable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class PackNullableBlendMode(PackNullableBase):
    """PackNullable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class PackNullableCulling(PackNullableBase):
    """PackNullable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class PackNullableBodyNode(PackNullableBase):
    """PackNullable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class PackNullableChirality(PackNullableBase):
    """PackNullable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class PackNullableDummyEnum(PackNullableBase):
    """PackNullable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.PackNullable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "has_value": "HasValue",
        "value": "Value",
    }

    has_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any PackNullable variant
PackNullable = (
    PackNullableBool |
    PackNullableByte |
    PackNullableUshort |
    PackNullableUint |
    PackNullableUlong |
    PackNullableSbyte |
    PackNullableShort |
    PackNullableInt |
    PackNullableLong |
    PackNullableFloat |
    PackNullableDouble |
    PackNullableDecimal |
    PackNullableChar |
    PackNullableString |
    PackNullableUri |
    PackNullableBool2 |
    PackNullableByte2 |
    PackNullableUshort2 |
    PackNullableUint2 |
    PackNullableUlong2 |
    PackNullableSbyte2 |
    PackNullableShort2 |
    PackNullableInt2 |
    PackNullableLong2 |
    PackNullableFloat2 |
    PackNullableDouble2 |
    PackNullableBool3 |
    PackNullableByte3 |
    PackNullableUshort3 |
    PackNullableUint3 |
    PackNullableUlong3 |
    PackNullableSbyte3 |
    PackNullableShort3 |
    PackNullableInt3 |
    PackNullableLong3 |
    PackNullableFloat3 |
    PackNullableDouble3 |
    PackNullableBool4 |
    PackNullableByte4 |
    PackNullableUshort4 |
    PackNullableUint4 |
    PackNullableUlong4 |
    PackNullableSbyte4 |
    PackNullableShort4 |
    PackNullableInt4 |
    PackNullableLong4 |
    PackNullableFloat4 |
    PackNullableDouble4 |
    PackNullableFloat_2x2 |
    PackNullableDouble_2x2 |
    PackNullableFloat_3x3 |
    PackNullableDouble_3x3 |
    PackNullableFloat_4x4 |
    PackNullableDouble_4x4 |
    PackNullableFloatQ |
    PackNullableDoubleQ |
    PackNullableDateTime |
    PackNullableTimeSpan |
    PackNullableColor |
    PackNullableColorX |
    PackNullableShadowCastMode |
    PackNullableLightType |
    PackNullableSessionAccessLevel |
    PackNullableKey |
    PackNullableHttpStatusCode |
    PackNullableHeadOutputDevice |
    PackNullableReflectionProbeClear |
    PackNullableReflectionProbeType |
    PackNullableReflectionProbeTimeSlicingMode |
    PackNullableCameraClearMode |
    PackNullableCameraPositioningMode |
    PackNullableCameraProjection |
    PackNullableZWrite |
    PackNullableZTest |
    PackNullableBlend |
    PackNullableBlendMode |
    PackNullableCulling |
    PackNullableBodyNode |
    PackNullableChirality |
    PackNullableDummyEnum
)