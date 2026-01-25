"""Generated component: ContinuouslyChangingValueRelay.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ContinuouslyChangingValueRelayBase(GeneratedComponent):
    """Base class for ContinuouslyChangingValueRelay<T> variants."""

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
class ContinuouslyChangingValueRelayBool(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class ContinuouslyChangingValueRelayByte(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class ContinuouslyChangingValueRelayUshort(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class ContinuouslyChangingValueRelayUint(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class ContinuouslyChangingValueRelayUlong(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class ContinuouslyChangingValueRelaySbyte(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class ContinuouslyChangingValueRelayShort(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class ContinuouslyChangingValueRelayInt(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class ContinuouslyChangingValueRelayLong(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class ContinuouslyChangingValueRelayFloat(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class ContinuouslyChangingValueRelayDouble(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class ContinuouslyChangingValueRelayDecimal(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class ContinuouslyChangingValueRelayChar(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class ContinuouslyChangingValueRelayString(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class ContinuouslyChangingValueRelayUri(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class ContinuouslyChangingValueRelayBool2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class ContinuouslyChangingValueRelayByte2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class ContinuouslyChangingValueRelayUshort2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class ContinuouslyChangingValueRelayUint2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class ContinuouslyChangingValueRelayUlong2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class ContinuouslyChangingValueRelaySbyte2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class ContinuouslyChangingValueRelayShort2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class ContinuouslyChangingValueRelayInt2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class ContinuouslyChangingValueRelayLong2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class ContinuouslyChangingValueRelayFloat2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class ContinuouslyChangingValueRelayDouble2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class ContinuouslyChangingValueRelayBool3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class ContinuouslyChangingValueRelayByte3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class ContinuouslyChangingValueRelayUshort3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class ContinuouslyChangingValueRelayUint3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class ContinuouslyChangingValueRelayUlong3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class ContinuouslyChangingValueRelaySbyte3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class ContinuouslyChangingValueRelayShort3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class ContinuouslyChangingValueRelayInt3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class ContinuouslyChangingValueRelayLong3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class ContinuouslyChangingValueRelayFloat3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class ContinuouslyChangingValueRelayDouble3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class ContinuouslyChangingValueRelayBool4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class ContinuouslyChangingValueRelayByte4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class ContinuouslyChangingValueRelayUshort4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class ContinuouslyChangingValueRelayUint4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class ContinuouslyChangingValueRelayUlong4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class ContinuouslyChangingValueRelaySbyte4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class ContinuouslyChangingValueRelayShort4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class ContinuouslyChangingValueRelayInt4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class ContinuouslyChangingValueRelayLong4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class ContinuouslyChangingValueRelayFloat4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class ContinuouslyChangingValueRelayDouble4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class ContinuouslyChangingValueRelayFloat_2x2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class ContinuouslyChangingValueRelayDouble_2x2(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class ContinuouslyChangingValueRelayFloat_3x3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class ContinuouslyChangingValueRelayDouble_3x3(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class ContinuouslyChangingValueRelayFloat_4x4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class ContinuouslyChangingValueRelayDouble_4x4(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class ContinuouslyChangingValueRelayFloatQ(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class ContinuouslyChangingValueRelayDoubleQ(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class ContinuouslyChangingValueRelayDateTime(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class ContinuouslyChangingValueRelayTimeSpan(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class ContinuouslyChangingValueRelayColor(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class ContinuouslyChangingValueRelayColorX(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class ContinuouslyChangingValueRelayShadowCastMode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class ContinuouslyChangingValueRelayLightType(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class ContinuouslyChangingValueRelaySessionAccessLevel(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class ContinuouslyChangingValueRelayKey(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class ContinuouslyChangingValueRelayHttpStatusCode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class ContinuouslyChangingValueRelayHeadOutputDevice(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class ContinuouslyChangingValueRelayReflectionProbeClear(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class ContinuouslyChangingValueRelayReflectionProbeType(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class ContinuouslyChangingValueRelayReflectionProbeTimeSlicingMode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class ContinuouslyChangingValueRelayCameraClearMode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class ContinuouslyChangingValueRelayCameraPositioningMode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class ContinuouslyChangingValueRelayCameraProjection(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class ContinuouslyChangingValueRelayZWrite(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class ContinuouslyChangingValueRelayZTest(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class ContinuouslyChangingValueRelayBlend(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class ContinuouslyChangingValueRelayBlendMode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class ContinuouslyChangingValueRelayCulling(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class ContinuouslyChangingValueRelayBodyNode(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class ContinuouslyChangingValueRelayChirality(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class ContinuouslyChangingValueRelayDummyEnum(ContinuouslyChangingValueRelayBase):
    """ContinuouslyChangingValueRelay<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "input": "Input",
    }

    input: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any ContinuouslyChangingValueRelay variant
ContinuouslyChangingValueRelay = (
    ContinuouslyChangingValueRelayBool |
    ContinuouslyChangingValueRelayByte |
    ContinuouslyChangingValueRelayUshort |
    ContinuouslyChangingValueRelayUint |
    ContinuouslyChangingValueRelayUlong |
    ContinuouslyChangingValueRelaySbyte |
    ContinuouslyChangingValueRelayShort |
    ContinuouslyChangingValueRelayInt |
    ContinuouslyChangingValueRelayLong |
    ContinuouslyChangingValueRelayFloat |
    ContinuouslyChangingValueRelayDouble |
    ContinuouslyChangingValueRelayDecimal |
    ContinuouslyChangingValueRelayChar |
    ContinuouslyChangingValueRelayString |
    ContinuouslyChangingValueRelayUri |
    ContinuouslyChangingValueRelayBool2 |
    ContinuouslyChangingValueRelayByte2 |
    ContinuouslyChangingValueRelayUshort2 |
    ContinuouslyChangingValueRelayUint2 |
    ContinuouslyChangingValueRelayUlong2 |
    ContinuouslyChangingValueRelaySbyte2 |
    ContinuouslyChangingValueRelayShort2 |
    ContinuouslyChangingValueRelayInt2 |
    ContinuouslyChangingValueRelayLong2 |
    ContinuouslyChangingValueRelayFloat2 |
    ContinuouslyChangingValueRelayDouble2 |
    ContinuouslyChangingValueRelayBool3 |
    ContinuouslyChangingValueRelayByte3 |
    ContinuouslyChangingValueRelayUshort3 |
    ContinuouslyChangingValueRelayUint3 |
    ContinuouslyChangingValueRelayUlong3 |
    ContinuouslyChangingValueRelaySbyte3 |
    ContinuouslyChangingValueRelayShort3 |
    ContinuouslyChangingValueRelayInt3 |
    ContinuouslyChangingValueRelayLong3 |
    ContinuouslyChangingValueRelayFloat3 |
    ContinuouslyChangingValueRelayDouble3 |
    ContinuouslyChangingValueRelayBool4 |
    ContinuouslyChangingValueRelayByte4 |
    ContinuouslyChangingValueRelayUshort4 |
    ContinuouslyChangingValueRelayUint4 |
    ContinuouslyChangingValueRelayUlong4 |
    ContinuouslyChangingValueRelaySbyte4 |
    ContinuouslyChangingValueRelayShort4 |
    ContinuouslyChangingValueRelayInt4 |
    ContinuouslyChangingValueRelayLong4 |
    ContinuouslyChangingValueRelayFloat4 |
    ContinuouslyChangingValueRelayDouble4 |
    ContinuouslyChangingValueRelayFloat_2x2 |
    ContinuouslyChangingValueRelayDouble_2x2 |
    ContinuouslyChangingValueRelayFloat_3x3 |
    ContinuouslyChangingValueRelayDouble_3x3 |
    ContinuouslyChangingValueRelayFloat_4x4 |
    ContinuouslyChangingValueRelayDouble_4x4 |
    ContinuouslyChangingValueRelayFloatQ |
    ContinuouslyChangingValueRelayDoubleQ |
    ContinuouslyChangingValueRelayDateTime |
    ContinuouslyChangingValueRelayTimeSpan |
    ContinuouslyChangingValueRelayColor |
    ContinuouslyChangingValueRelayColorX |
    ContinuouslyChangingValueRelayShadowCastMode |
    ContinuouslyChangingValueRelayLightType |
    ContinuouslyChangingValueRelaySessionAccessLevel |
    ContinuouslyChangingValueRelayKey |
    ContinuouslyChangingValueRelayHttpStatusCode |
    ContinuouslyChangingValueRelayHeadOutputDevice |
    ContinuouslyChangingValueRelayReflectionProbeClear |
    ContinuouslyChangingValueRelayReflectionProbeType |
    ContinuouslyChangingValueRelayReflectionProbeTimeSlicingMode |
    ContinuouslyChangingValueRelayCameraClearMode |
    ContinuouslyChangingValueRelayCameraPositioningMode |
    ContinuouslyChangingValueRelayCameraProjection |
    ContinuouslyChangingValueRelayZWrite |
    ContinuouslyChangingValueRelayZTest |
    ContinuouslyChangingValueRelayBlend |
    ContinuouslyChangingValueRelayBlendMode |
    ContinuouslyChangingValueRelayCulling |
    ContinuouslyChangingValueRelayBodyNode |
    ContinuouslyChangingValueRelayChirality |
    ContinuouslyChangingValueRelayDummyEnum
)