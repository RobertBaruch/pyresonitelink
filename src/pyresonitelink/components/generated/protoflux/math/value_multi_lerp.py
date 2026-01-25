"""Generated component: ValueMultiLerp.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class ValueMultiLerpBase(GeneratedComponent):
    """Base class for ValueMultiLerp<T> variants."""

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
class ValueMultiLerpBool(ValueMultiLerpBase):
    """ValueMultiLerp<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpByte(ValueMultiLerpBase):
    """ValueMultiLerp<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUshort(ValueMultiLerpBase):
    """ValueMultiLerp<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUint(ValueMultiLerpBase):
    """ValueMultiLerp<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUlong(ValueMultiLerpBase):
    """ValueMultiLerp<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpSbyte(ValueMultiLerpBase):
    """ValueMultiLerp<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpShort(ValueMultiLerpBase):
    """ValueMultiLerp<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpInt(ValueMultiLerpBase):
    """ValueMultiLerp<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpLong(ValueMultiLerpBase):
    """ValueMultiLerp<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat(ValueMultiLerpBase):
    """ValueMultiLerp<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble(ValueMultiLerpBase):
    """ValueMultiLerp<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDecimal(ValueMultiLerpBase):
    """ValueMultiLerp<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpChar(ValueMultiLerpBase):
    """ValueMultiLerp<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpString(ValueMultiLerpBase):
    """ValueMultiLerp<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUri(ValueMultiLerpBase):
    """ValueMultiLerp<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBool2(ValueMultiLerpBase):
    """ValueMultiLerp<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpByte2(ValueMultiLerpBase):
    """ValueMultiLerp<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUshort2(ValueMultiLerpBase):
    """ValueMultiLerp<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUint2(ValueMultiLerpBase):
    """ValueMultiLerp<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUlong2(ValueMultiLerpBase):
    """ValueMultiLerp<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpSbyte2(ValueMultiLerpBase):
    """ValueMultiLerp<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpShort2(ValueMultiLerpBase):
    """ValueMultiLerp<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpInt2(ValueMultiLerpBase):
    """ValueMultiLerp<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpLong2(ValueMultiLerpBase):
    """ValueMultiLerp<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat2(ValueMultiLerpBase):
    """ValueMultiLerp<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble2(ValueMultiLerpBase):
    """ValueMultiLerp<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBool3(ValueMultiLerpBase):
    """ValueMultiLerp<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpByte3(ValueMultiLerpBase):
    """ValueMultiLerp<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUshort3(ValueMultiLerpBase):
    """ValueMultiLerp<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUint3(ValueMultiLerpBase):
    """ValueMultiLerp<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUlong3(ValueMultiLerpBase):
    """ValueMultiLerp<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpSbyte3(ValueMultiLerpBase):
    """ValueMultiLerp<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpShort3(ValueMultiLerpBase):
    """ValueMultiLerp<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpInt3(ValueMultiLerpBase):
    """ValueMultiLerp<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpLong3(ValueMultiLerpBase):
    """ValueMultiLerp<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat3(ValueMultiLerpBase):
    """ValueMultiLerp<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble3(ValueMultiLerpBase):
    """ValueMultiLerp<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBool4(ValueMultiLerpBase):
    """ValueMultiLerp<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpByte4(ValueMultiLerpBase):
    """ValueMultiLerp<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUshort4(ValueMultiLerpBase):
    """ValueMultiLerp<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUint4(ValueMultiLerpBase):
    """ValueMultiLerp<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpUlong4(ValueMultiLerpBase):
    """ValueMultiLerp<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpSbyte4(ValueMultiLerpBase):
    """ValueMultiLerp<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpShort4(ValueMultiLerpBase):
    """ValueMultiLerp<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpInt4(ValueMultiLerpBase):
    """ValueMultiLerp<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpLong4(ValueMultiLerpBase):
    """ValueMultiLerp<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat4(ValueMultiLerpBase):
    """ValueMultiLerp<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble4(ValueMultiLerpBase):
    """ValueMultiLerp<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat_2x2(ValueMultiLerpBase):
    """ValueMultiLerp<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble_2x2(ValueMultiLerpBase):
    """ValueMultiLerp<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat_3x3(ValueMultiLerpBase):
    """ValueMultiLerp<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble_3x3(ValueMultiLerpBase):
    """ValueMultiLerp<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloat_4x4(ValueMultiLerpBase):
    """ValueMultiLerp<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDouble_4x4(ValueMultiLerpBase):
    """ValueMultiLerp<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpFloatQ(ValueMultiLerpBase):
    """ValueMultiLerp<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDoubleQ(ValueMultiLerpBase):
    """ValueMultiLerp<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDateTime(ValueMultiLerpBase):
    """ValueMultiLerp<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpTimeSpan(ValueMultiLerpBase):
    """ValueMultiLerp<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpColor(ValueMultiLerpBase):
    """ValueMultiLerp<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpColorX(ValueMultiLerpBase):
    """ValueMultiLerp<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpShadowCastMode(ValueMultiLerpBase):
    """ValueMultiLerp<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpLightType(ValueMultiLerpBase):
    """ValueMultiLerp<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpSessionAccessLevel(ValueMultiLerpBase):
    """ValueMultiLerp<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpKey(ValueMultiLerpBase):
    """ValueMultiLerp<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpHttpStatusCode(ValueMultiLerpBase):
    """ValueMultiLerp<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpHeadOutputDevice(ValueMultiLerpBase):
    """ValueMultiLerp<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpReflectionProbeClear(ValueMultiLerpBase):
    """ValueMultiLerp<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpReflectionProbeType(ValueMultiLerpBase):
    """ValueMultiLerp<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpReflectionProbeTimeSlicingMode(ValueMultiLerpBase):
    """ValueMultiLerp<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpCameraClearMode(ValueMultiLerpBase):
    """ValueMultiLerp<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpCameraPositioningMode(ValueMultiLerpBase):
    """ValueMultiLerp<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpCameraProjection(ValueMultiLerpBase):
    """ValueMultiLerp<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpZWrite(ValueMultiLerpBase):
    """ValueMultiLerp<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpZTest(ValueMultiLerpBase):
    """ValueMultiLerp<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBlend(ValueMultiLerpBase):
    """ValueMultiLerp<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBlendMode(ValueMultiLerpBase):
    """ValueMultiLerp<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpCulling(ValueMultiLerpBase):
    """ValueMultiLerp<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpBodyNode(ValueMultiLerpBase):
    """ValueMultiLerp<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpChirality(ValueMultiLerpBase):
    """ValueMultiLerp<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


@dataclass
class ValueMultiLerpDummyEnum(ValueMultiLerpBase):
    """ValueMultiLerp<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueMultiLerp<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "lerp": "Lerp",
        "operands": "Operands",
    }

    lerp: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    operands: SyncList | None = None


# Type alias for any ValueMultiLerp variant
ValueMultiLerp = (
    ValueMultiLerpBool |
    ValueMultiLerpByte |
    ValueMultiLerpUshort |
    ValueMultiLerpUint |
    ValueMultiLerpUlong |
    ValueMultiLerpSbyte |
    ValueMultiLerpShort |
    ValueMultiLerpInt |
    ValueMultiLerpLong |
    ValueMultiLerpFloat |
    ValueMultiLerpDouble |
    ValueMultiLerpDecimal |
    ValueMultiLerpChar |
    ValueMultiLerpString |
    ValueMultiLerpUri |
    ValueMultiLerpBool2 |
    ValueMultiLerpByte2 |
    ValueMultiLerpUshort2 |
    ValueMultiLerpUint2 |
    ValueMultiLerpUlong2 |
    ValueMultiLerpSbyte2 |
    ValueMultiLerpShort2 |
    ValueMultiLerpInt2 |
    ValueMultiLerpLong2 |
    ValueMultiLerpFloat2 |
    ValueMultiLerpDouble2 |
    ValueMultiLerpBool3 |
    ValueMultiLerpByte3 |
    ValueMultiLerpUshort3 |
    ValueMultiLerpUint3 |
    ValueMultiLerpUlong3 |
    ValueMultiLerpSbyte3 |
    ValueMultiLerpShort3 |
    ValueMultiLerpInt3 |
    ValueMultiLerpLong3 |
    ValueMultiLerpFloat3 |
    ValueMultiLerpDouble3 |
    ValueMultiLerpBool4 |
    ValueMultiLerpByte4 |
    ValueMultiLerpUshort4 |
    ValueMultiLerpUint4 |
    ValueMultiLerpUlong4 |
    ValueMultiLerpSbyte4 |
    ValueMultiLerpShort4 |
    ValueMultiLerpInt4 |
    ValueMultiLerpLong4 |
    ValueMultiLerpFloat4 |
    ValueMultiLerpDouble4 |
    ValueMultiLerpFloat_2x2 |
    ValueMultiLerpDouble_2x2 |
    ValueMultiLerpFloat_3x3 |
    ValueMultiLerpDouble_3x3 |
    ValueMultiLerpFloat_4x4 |
    ValueMultiLerpDouble_4x4 |
    ValueMultiLerpFloatQ |
    ValueMultiLerpDoubleQ |
    ValueMultiLerpDateTime |
    ValueMultiLerpTimeSpan |
    ValueMultiLerpColor |
    ValueMultiLerpColorX |
    ValueMultiLerpShadowCastMode |
    ValueMultiLerpLightType |
    ValueMultiLerpSessionAccessLevel |
    ValueMultiLerpKey |
    ValueMultiLerpHttpStatusCode |
    ValueMultiLerpHeadOutputDevice |
    ValueMultiLerpReflectionProbeClear |
    ValueMultiLerpReflectionProbeType |
    ValueMultiLerpReflectionProbeTimeSlicingMode |
    ValueMultiLerpCameraClearMode |
    ValueMultiLerpCameraPositioningMode |
    ValueMultiLerpCameraProjection |
    ValueMultiLerpZWrite |
    ValueMultiLerpZTest |
    ValueMultiLerpBlend |
    ValueMultiLerpBlendMode |
    ValueMultiLerpCulling |
    ValueMultiLerpBodyNode |
    ValueMultiLerpChirality |
    ValueMultiLerpDummyEnum
)