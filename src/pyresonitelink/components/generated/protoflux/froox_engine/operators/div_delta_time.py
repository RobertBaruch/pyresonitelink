"""Generated component: DivDeltaTime.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DivDeltaTimeBase(GeneratedComponent):
    """Base class for DivDeltaTime<T> variants."""

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
class DivDeltaTimeBool(DivDeltaTimeBase):
    """DivDeltaTime<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DivDeltaTimeByte(DivDeltaTimeBase):
    """DivDeltaTime<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DivDeltaTimeUshort(DivDeltaTimeBase):
    """DivDeltaTime<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DivDeltaTimeUint(DivDeltaTimeBase):
    """DivDeltaTime<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DivDeltaTimeUlong(DivDeltaTimeBase):
    """DivDeltaTime<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DivDeltaTimeSbyte(DivDeltaTimeBase):
    """DivDeltaTime<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DivDeltaTimeShort(DivDeltaTimeBase):
    """DivDeltaTime<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DivDeltaTimeInt(DivDeltaTimeBase):
    """DivDeltaTime<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DivDeltaTimeLong(DivDeltaTimeBase):
    """DivDeltaTime<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DivDeltaTimeFloat(DivDeltaTimeBase):
    """DivDeltaTime<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DivDeltaTimeDouble(DivDeltaTimeBase):
    """DivDeltaTime<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DivDeltaTimeDecimal(DivDeltaTimeBase):
    """DivDeltaTime<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DivDeltaTimeChar(DivDeltaTimeBase):
    """DivDeltaTime<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DivDeltaTimeString(DivDeltaTimeBase):
    """DivDeltaTime<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DivDeltaTimeUri(DivDeltaTimeBase):
    """DivDeltaTime<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DivDeltaTimeBool2(DivDeltaTimeBase):
    """DivDeltaTime<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DivDeltaTimeByte2(DivDeltaTimeBase):
    """DivDeltaTime<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DivDeltaTimeUshort2(DivDeltaTimeBase):
    """DivDeltaTime<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DivDeltaTimeUint2(DivDeltaTimeBase):
    """DivDeltaTime<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DivDeltaTimeUlong2(DivDeltaTimeBase):
    """DivDeltaTime<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DivDeltaTimeSbyte2(DivDeltaTimeBase):
    """DivDeltaTime<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DivDeltaTimeShort2(DivDeltaTimeBase):
    """DivDeltaTime<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DivDeltaTimeInt2(DivDeltaTimeBase):
    """DivDeltaTime<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DivDeltaTimeLong2(DivDeltaTimeBase):
    """DivDeltaTime<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DivDeltaTimeFloat2(DivDeltaTimeBase):
    """DivDeltaTime<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DivDeltaTimeDouble2(DivDeltaTimeBase):
    """DivDeltaTime<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DivDeltaTimeBool3(DivDeltaTimeBase):
    """DivDeltaTime<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DivDeltaTimeByte3(DivDeltaTimeBase):
    """DivDeltaTime<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DivDeltaTimeUshort3(DivDeltaTimeBase):
    """DivDeltaTime<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DivDeltaTimeUint3(DivDeltaTimeBase):
    """DivDeltaTime<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DivDeltaTimeUlong3(DivDeltaTimeBase):
    """DivDeltaTime<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DivDeltaTimeSbyte3(DivDeltaTimeBase):
    """DivDeltaTime<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DivDeltaTimeShort3(DivDeltaTimeBase):
    """DivDeltaTime<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DivDeltaTimeInt3(DivDeltaTimeBase):
    """DivDeltaTime<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DivDeltaTimeLong3(DivDeltaTimeBase):
    """DivDeltaTime<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DivDeltaTimeFloat3(DivDeltaTimeBase):
    """DivDeltaTime<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DivDeltaTimeDouble3(DivDeltaTimeBase):
    """DivDeltaTime<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DivDeltaTimeBool4(DivDeltaTimeBase):
    """DivDeltaTime<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DivDeltaTimeByte4(DivDeltaTimeBase):
    """DivDeltaTime<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DivDeltaTimeUshort4(DivDeltaTimeBase):
    """DivDeltaTime<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DivDeltaTimeUint4(DivDeltaTimeBase):
    """DivDeltaTime<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DivDeltaTimeUlong4(DivDeltaTimeBase):
    """DivDeltaTime<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DivDeltaTimeSbyte4(DivDeltaTimeBase):
    """DivDeltaTime<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DivDeltaTimeShort4(DivDeltaTimeBase):
    """DivDeltaTime<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DivDeltaTimeInt4(DivDeltaTimeBase):
    """DivDeltaTime<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DivDeltaTimeLong4(DivDeltaTimeBase):
    """DivDeltaTime<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DivDeltaTimeFloat4(DivDeltaTimeBase):
    """DivDeltaTime<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DivDeltaTimeDouble4(DivDeltaTimeBase):
    """DivDeltaTime<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DivDeltaTimeFloat_2x2(DivDeltaTimeBase):
    """DivDeltaTime<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DivDeltaTimeDouble_2x2(DivDeltaTimeBase):
    """DivDeltaTime<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DivDeltaTimeFloat_3x3(DivDeltaTimeBase):
    """DivDeltaTime<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DivDeltaTimeDouble_3x3(DivDeltaTimeBase):
    """DivDeltaTime<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DivDeltaTimeFloat_4x4(DivDeltaTimeBase):
    """DivDeltaTime<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DivDeltaTimeDouble_4x4(DivDeltaTimeBase):
    """DivDeltaTime<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DivDeltaTimeFloatQ(DivDeltaTimeBase):
    """DivDeltaTime<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DivDeltaTimeDoubleQ(DivDeltaTimeBase):
    """DivDeltaTime<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DivDeltaTimeDateTime(DivDeltaTimeBase):
    """DivDeltaTime<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DivDeltaTimeTimeSpan(DivDeltaTimeBase):
    """DivDeltaTime<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DivDeltaTimeColor(DivDeltaTimeBase):
    """DivDeltaTime<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DivDeltaTimeColorX(DivDeltaTimeBase):
    """DivDeltaTime<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DivDeltaTimeShadowCastMode(DivDeltaTimeBase):
    """DivDeltaTime<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DivDeltaTimeLightType(DivDeltaTimeBase):
    """DivDeltaTime<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DivDeltaTimeSessionAccessLevel(DivDeltaTimeBase):
    """DivDeltaTime<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DivDeltaTimeKey(DivDeltaTimeBase):
    """DivDeltaTime<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DivDeltaTimeHttpStatusCode(DivDeltaTimeBase):
    """DivDeltaTime<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DivDeltaTimeHeadOutputDevice(DivDeltaTimeBase):
    """DivDeltaTime<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DivDeltaTimeReflectionProbeClear(DivDeltaTimeBase):
    """DivDeltaTime<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DivDeltaTimeReflectionProbeType(DivDeltaTimeBase):
    """DivDeltaTime<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DivDeltaTimeReflectionProbeTimeSlicingMode(DivDeltaTimeBase):
    """DivDeltaTime<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DivDeltaTimeCameraClearMode(DivDeltaTimeBase):
    """DivDeltaTime<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DivDeltaTimeCameraPositioningMode(DivDeltaTimeBase):
    """DivDeltaTime<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DivDeltaTimeCameraProjection(DivDeltaTimeBase):
    """DivDeltaTime<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DivDeltaTimeZWrite(DivDeltaTimeBase):
    """DivDeltaTime<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DivDeltaTimeZTest(DivDeltaTimeBase):
    """DivDeltaTime<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DivDeltaTimeBlend(DivDeltaTimeBase):
    """DivDeltaTime<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DivDeltaTimeBlendMode(DivDeltaTimeBase):
    """DivDeltaTime<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DivDeltaTimeCulling(DivDeltaTimeBase):
    """DivDeltaTime<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DivDeltaTimeBodyNode(DivDeltaTimeBase):
    """DivDeltaTime<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DivDeltaTimeChirality(DivDeltaTimeBase):
    """DivDeltaTime<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DivDeltaTimeDummyEnum(DivDeltaTimeBase):
    """DivDeltaTime<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.DivDeltaTime<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "a": "A",
    }

    a: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DivDeltaTime variant
DivDeltaTime = (
    DivDeltaTimeBool |
    DivDeltaTimeByte |
    DivDeltaTimeUshort |
    DivDeltaTimeUint |
    DivDeltaTimeUlong |
    DivDeltaTimeSbyte |
    DivDeltaTimeShort |
    DivDeltaTimeInt |
    DivDeltaTimeLong |
    DivDeltaTimeFloat |
    DivDeltaTimeDouble |
    DivDeltaTimeDecimal |
    DivDeltaTimeChar |
    DivDeltaTimeString |
    DivDeltaTimeUri |
    DivDeltaTimeBool2 |
    DivDeltaTimeByte2 |
    DivDeltaTimeUshort2 |
    DivDeltaTimeUint2 |
    DivDeltaTimeUlong2 |
    DivDeltaTimeSbyte2 |
    DivDeltaTimeShort2 |
    DivDeltaTimeInt2 |
    DivDeltaTimeLong2 |
    DivDeltaTimeFloat2 |
    DivDeltaTimeDouble2 |
    DivDeltaTimeBool3 |
    DivDeltaTimeByte3 |
    DivDeltaTimeUshort3 |
    DivDeltaTimeUint3 |
    DivDeltaTimeUlong3 |
    DivDeltaTimeSbyte3 |
    DivDeltaTimeShort3 |
    DivDeltaTimeInt3 |
    DivDeltaTimeLong3 |
    DivDeltaTimeFloat3 |
    DivDeltaTimeDouble3 |
    DivDeltaTimeBool4 |
    DivDeltaTimeByte4 |
    DivDeltaTimeUshort4 |
    DivDeltaTimeUint4 |
    DivDeltaTimeUlong4 |
    DivDeltaTimeSbyte4 |
    DivDeltaTimeShort4 |
    DivDeltaTimeInt4 |
    DivDeltaTimeLong4 |
    DivDeltaTimeFloat4 |
    DivDeltaTimeDouble4 |
    DivDeltaTimeFloat_2x2 |
    DivDeltaTimeDouble_2x2 |
    DivDeltaTimeFloat_3x3 |
    DivDeltaTimeDouble_3x3 |
    DivDeltaTimeFloat_4x4 |
    DivDeltaTimeDouble_4x4 |
    DivDeltaTimeFloatQ |
    DivDeltaTimeDoubleQ |
    DivDeltaTimeDateTime |
    DivDeltaTimeTimeSpan |
    DivDeltaTimeColor |
    DivDeltaTimeColorX |
    DivDeltaTimeShadowCastMode |
    DivDeltaTimeLightType |
    DivDeltaTimeSessionAccessLevel |
    DivDeltaTimeKey |
    DivDeltaTimeHttpStatusCode |
    DivDeltaTimeHeadOutputDevice |
    DivDeltaTimeReflectionProbeClear |
    DivDeltaTimeReflectionProbeType |
    DivDeltaTimeReflectionProbeTimeSlicingMode |
    DivDeltaTimeCameraClearMode |
    DivDeltaTimeCameraPositioningMode |
    DivDeltaTimeCameraProjection |
    DivDeltaTimeZWrite |
    DivDeltaTimeZTest |
    DivDeltaTimeBlend |
    DivDeltaTimeBlendMode |
    DivDeltaTimeCulling |
    DivDeltaTimeBodyNode |
    DivDeltaTimeChirality |
    DivDeltaTimeDummyEnum
)