"""Generated component: ValueMultiplex.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class ValueMultiplexBase(GeneratedComponent):
    """Base class for ValueMultiplex<T> variants."""

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
class ValueMultiplexBool(ValueMultiplexBase):
    """ValueMultiplex<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexByte(ValueMultiplexBase):
    """ValueMultiplex<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUshort(ValueMultiplexBase):
    """ValueMultiplex<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUint(ValueMultiplexBase):
    """ValueMultiplex<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUlong(ValueMultiplexBase):
    """ValueMultiplex<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexSbyte(ValueMultiplexBase):
    """ValueMultiplex<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexShort(ValueMultiplexBase):
    """ValueMultiplex<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexInt(ValueMultiplexBase):
    """ValueMultiplex<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexLong(ValueMultiplexBase):
    """ValueMultiplex<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat(ValueMultiplexBase):
    """ValueMultiplex<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble(ValueMultiplexBase):
    """ValueMultiplex<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDecimal(ValueMultiplexBase):
    """ValueMultiplex<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexChar(ValueMultiplexBase):
    """ValueMultiplex<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexString(ValueMultiplexBase):
    """ValueMultiplex<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUri(ValueMultiplexBase):
    """ValueMultiplex<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBool2(ValueMultiplexBase):
    """ValueMultiplex<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexByte2(ValueMultiplexBase):
    """ValueMultiplex<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUshort2(ValueMultiplexBase):
    """ValueMultiplex<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUint2(ValueMultiplexBase):
    """ValueMultiplex<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUlong2(ValueMultiplexBase):
    """ValueMultiplex<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexSbyte2(ValueMultiplexBase):
    """ValueMultiplex<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexShort2(ValueMultiplexBase):
    """ValueMultiplex<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexInt2(ValueMultiplexBase):
    """ValueMultiplex<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexLong2(ValueMultiplexBase):
    """ValueMultiplex<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat2(ValueMultiplexBase):
    """ValueMultiplex<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble2(ValueMultiplexBase):
    """ValueMultiplex<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBool3(ValueMultiplexBase):
    """ValueMultiplex<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexByte3(ValueMultiplexBase):
    """ValueMultiplex<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUshort3(ValueMultiplexBase):
    """ValueMultiplex<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUint3(ValueMultiplexBase):
    """ValueMultiplex<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUlong3(ValueMultiplexBase):
    """ValueMultiplex<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexSbyte3(ValueMultiplexBase):
    """ValueMultiplex<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexShort3(ValueMultiplexBase):
    """ValueMultiplex<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexInt3(ValueMultiplexBase):
    """ValueMultiplex<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexLong3(ValueMultiplexBase):
    """ValueMultiplex<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat3(ValueMultiplexBase):
    """ValueMultiplex<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble3(ValueMultiplexBase):
    """ValueMultiplex<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBool4(ValueMultiplexBase):
    """ValueMultiplex<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexByte4(ValueMultiplexBase):
    """ValueMultiplex<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUshort4(ValueMultiplexBase):
    """ValueMultiplex<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUint4(ValueMultiplexBase):
    """ValueMultiplex<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexUlong4(ValueMultiplexBase):
    """ValueMultiplex<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexSbyte4(ValueMultiplexBase):
    """ValueMultiplex<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexShort4(ValueMultiplexBase):
    """ValueMultiplex<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexInt4(ValueMultiplexBase):
    """ValueMultiplex<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexLong4(ValueMultiplexBase):
    """ValueMultiplex<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat4(ValueMultiplexBase):
    """ValueMultiplex<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble4(ValueMultiplexBase):
    """ValueMultiplex<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat_2x2(ValueMultiplexBase):
    """ValueMultiplex<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble_2x2(ValueMultiplexBase):
    """ValueMultiplex<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat_3x3(ValueMultiplexBase):
    """ValueMultiplex<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble_3x3(ValueMultiplexBase):
    """ValueMultiplex<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloat_4x4(ValueMultiplexBase):
    """ValueMultiplex<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDouble_4x4(ValueMultiplexBase):
    """ValueMultiplex<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexFloatQ(ValueMultiplexBase):
    """ValueMultiplex<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDoubleQ(ValueMultiplexBase):
    """ValueMultiplex<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDateTime(ValueMultiplexBase):
    """ValueMultiplex<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexTimeSpan(ValueMultiplexBase):
    """ValueMultiplex<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexColor(ValueMultiplexBase):
    """ValueMultiplex<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexColorX(ValueMultiplexBase):
    """ValueMultiplex<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexShadowCastMode(ValueMultiplexBase):
    """ValueMultiplex<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexLightType(ValueMultiplexBase):
    """ValueMultiplex<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexSessionAccessLevel(ValueMultiplexBase):
    """ValueMultiplex<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexKey(ValueMultiplexBase):
    """ValueMultiplex<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexHttpStatusCode(ValueMultiplexBase):
    """ValueMultiplex<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexHeadOutputDevice(ValueMultiplexBase):
    """ValueMultiplex<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexReflectionProbeClear(ValueMultiplexBase):
    """ValueMultiplex<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexReflectionProbeType(ValueMultiplexBase):
    """ValueMultiplex<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexReflectionProbeTimeSlicingMode(ValueMultiplexBase):
    """ValueMultiplex<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexCameraClearMode(ValueMultiplexBase):
    """ValueMultiplex<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexCameraPositioningMode(ValueMultiplexBase):
    """ValueMultiplex<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexCameraProjection(ValueMultiplexBase):
    """ValueMultiplex<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexZWrite(ValueMultiplexBase):
    """ValueMultiplex<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexZTest(ValueMultiplexBase):
    """ValueMultiplex<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBlend(ValueMultiplexBase):
    """ValueMultiplex<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBlendMode(ValueMultiplexBase):
    """ValueMultiplex<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexCulling(ValueMultiplexBase):
    """ValueMultiplex<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexBodyNode(ValueMultiplexBase):
    """ValueMultiplex<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexChirality(ValueMultiplexBase):
    """ValueMultiplex<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


@dataclass
class ValueMultiplexDummyEnum(ValueMultiplexBase):
    """ValueMultiplex<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueMultiplex<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "index": "Index",
        "inputs": "Inputs",
    }

    index: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    inputs: SyncList | None = None


# Type alias for any ValueMultiplex variant
ValueMultiplex = (
    ValueMultiplexBool |
    ValueMultiplexByte |
    ValueMultiplexUshort |
    ValueMultiplexUint |
    ValueMultiplexUlong |
    ValueMultiplexSbyte |
    ValueMultiplexShort |
    ValueMultiplexInt |
    ValueMultiplexLong |
    ValueMultiplexFloat |
    ValueMultiplexDouble |
    ValueMultiplexDecimal |
    ValueMultiplexChar |
    ValueMultiplexString |
    ValueMultiplexUri |
    ValueMultiplexBool2 |
    ValueMultiplexByte2 |
    ValueMultiplexUshort2 |
    ValueMultiplexUint2 |
    ValueMultiplexUlong2 |
    ValueMultiplexSbyte2 |
    ValueMultiplexShort2 |
    ValueMultiplexInt2 |
    ValueMultiplexLong2 |
    ValueMultiplexFloat2 |
    ValueMultiplexDouble2 |
    ValueMultiplexBool3 |
    ValueMultiplexByte3 |
    ValueMultiplexUshort3 |
    ValueMultiplexUint3 |
    ValueMultiplexUlong3 |
    ValueMultiplexSbyte3 |
    ValueMultiplexShort3 |
    ValueMultiplexInt3 |
    ValueMultiplexLong3 |
    ValueMultiplexFloat3 |
    ValueMultiplexDouble3 |
    ValueMultiplexBool4 |
    ValueMultiplexByte4 |
    ValueMultiplexUshort4 |
    ValueMultiplexUint4 |
    ValueMultiplexUlong4 |
    ValueMultiplexSbyte4 |
    ValueMultiplexShort4 |
    ValueMultiplexInt4 |
    ValueMultiplexLong4 |
    ValueMultiplexFloat4 |
    ValueMultiplexDouble4 |
    ValueMultiplexFloat_2x2 |
    ValueMultiplexDouble_2x2 |
    ValueMultiplexFloat_3x3 |
    ValueMultiplexDouble_3x3 |
    ValueMultiplexFloat_4x4 |
    ValueMultiplexDouble_4x4 |
    ValueMultiplexFloatQ |
    ValueMultiplexDoubleQ |
    ValueMultiplexDateTime |
    ValueMultiplexTimeSpan |
    ValueMultiplexColor |
    ValueMultiplexColorX |
    ValueMultiplexShadowCastMode |
    ValueMultiplexLightType |
    ValueMultiplexSessionAccessLevel |
    ValueMultiplexKey |
    ValueMultiplexHttpStatusCode |
    ValueMultiplexHeadOutputDevice |
    ValueMultiplexReflectionProbeClear |
    ValueMultiplexReflectionProbeType |
    ValueMultiplexReflectionProbeTimeSlicingMode |
    ValueMultiplexCameraClearMode |
    ValueMultiplexCameraPositioningMode |
    ValueMultiplexCameraProjection |
    ValueMultiplexZWrite |
    ValueMultiplexZTest |
    ValueMultiplexBlend |
    ValueMultiplexBlendMode |
    ValueMultiplexCulling |
    ValueMultiplexBodyNode |
    ValueMultiplexChirality |
    ValueMultiplexDummyEnum
)