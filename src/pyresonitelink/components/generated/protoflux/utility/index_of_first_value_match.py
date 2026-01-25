"""Generated component: IndexOfFirstValueMatch.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference, SyncList


@dataclass
class IndexOfFirstValueMatchBase(GeneratedComponent):
    """Base class for IndexOfFirstValueMatch<T> variants."""

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
class IndexOfFirstValueMatchBool(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchByte(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUshort(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUint(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUlong(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchSbyte(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchShort(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchInt(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchLong(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDecimal(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchChar(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchString(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUri(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBool2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchByte2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUshort2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUint2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUlong2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchSbyte2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchShort2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchInt2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchLong2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBool3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchByte3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUshort3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUint3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUlong3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchSbyte3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchShort3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchInt3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchLong3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBool4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchByte4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUshort4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUint4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchUlong4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchSbyte4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchShort4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchInt4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchLong4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat_2x2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble_2x2(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat_3x3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble_3x3(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloat_4x4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDouble_4x4(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchFloatQ(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDoubleQ(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDateTime(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchTimeSpan(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchColor(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchColorX(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchShadowCastMode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchLightType(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchSessionAccessLevel(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchKey(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchHttpStatusCode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchHeadOutputDevice(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchReflectionProbeClear(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchReflectionProbeType(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchReflectionProbeTimeSlicingMode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchCameraClearMode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchCameraPositioningMode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchCameraProjection(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchZWrite(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchZTest(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBlend(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBlendMode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchCulling(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchBodyNode(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchChirality(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    values: SyncList | None = None


@dataclass
class IndexOfFirstValueMatchDummyEnum(IndexOfFirstValueMatchBase):
    """IndexOfFirstValueMatch<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Utility.IndexOfFirstValueMatch<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "match": "Match",
        "values": "Values",
    }

    match: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    values: SyncList | None = None


# Type alias for any IndexOfFirstValueMatch variant
IndexOfFirstValueMatch = (
    IndexOfFirstValueMatchBool |
    IndexOfFirstValueMatchByte |
    IndexOfFirstValueMatchUshort |
    IndexOfFirstValueMatchUint |
    IndexOfFirstValueMatchUlong |
    IndexOfFirstValueMatchSbyte |
    IndexOfFirstValueMatchShort |
    IndexOfFirstValueMatchInt |
    IndexOfFirstValueMatchLong |
    IndexOfFirstValueMatchFloat |
    IndexOfFirstValueMatchDouble |
    IndexOfFirstValueMatchDecimal |
    IndexOfFirstValueMatchChar |
    IndexOfFirstValueMatchString |
    IndexOfFirstValueMatchUri |
    IndexOfFirstValueMatchBool2 |
    IndexOfFirstValueMatchByte2 |
    IndexOfFirstValueMatchUshort2 |
    IndexOfFirstValueMatchUint2 |
    IndexOfFirstValueMatchUlong2 |
    IndexOfFirstValueMatchSbyte2 |
    IndexOfFirstValueMatchShort2 |
    IndexOfFirstValueMatchInt2 |
    IndexOfFirstValueMatchLong2 |
    IndexOfFirstValueMatchFloat2 |
    IndexOfFirstValueMatchDouble2 |
    IndexOfFirstValueMatchBool3 |
    IndexOfFirstValueMatchByte3 |
    IndexOfFirstValueMatchUshort3 |
    IndexOfFirstValueMatchUint3 |
    IndexOfFirstValueMatchUlong3 |
    IndexOfFirstValueMatchSbyte3 |
    IndexOfFirstValueMatchShort3 |
    IndexOfFirstValueMatchInt3 |
    IndexOfFirstValueMatchLong3 |
    IndexOfFirstValueMatchFloat3 |
    IndexOfFirstValueMatchDouble3 |
    IndexOfFirstValueMatchBool4 |
    IndexOfFirstValueMatchByte4 |
    IndexOfFirstValueMatchUshort4 |
    IndexOfFirstValueMatchUint4 |
    IndexOfFirstValueMatchUlong4 |
    IndexOfFirstValueMatchSbyte4 |
    IndexOfFirstValueMatchShort4 |
    IndexOfFirstValueMatchInt4 |
    IndexOfFirstValueMatchLong4 |
    IndexOfFirstValueMatchFloat4 |
    IndexOfFirstValueMatchDouble4 |
    IndexOfFirstValueMatchFloat_2x2 |
    IndexOfFirstValueMatchDouble_2x2 |
    IndexOfFirstValueMatchFloat_3x3 |
    IndexOfFirstValueMatchDouble_3x3 |
    IndexOfFirstValueMatchFloat_4x4 |
    IndexOfFirstValueMatchDouble_4x4 |
    IndexOfFirstValueMatchFloatQ |
    IndexOfFirstValueMatchDoubleQ |
    IndexOfFirstValueMatchDateTime |
    IndexOfFirstValueMatchTimeSpan |
    IndexOfFirstValueMatchColor |
    IndexOfFirstValueMatchColorX |
    IndexOfFirstValueMatchShadowCastMode |
    IndexOfFirstValueMatchLightType |
    IndexOfFirstValueMatchSessionAccessLevel |
    IndexOfFirstValueMatchKey |
    IndexOfFirstValueMatchHttpStatusCode |
    IndexOfFirstValueMatchHeadOutputDevice |
    IndexOfFirstValueMatchReflectionProbeClear |
    IndexOfFirstValueMatchReflectionProbeType |
    IndexOfFirstValueMatchReflectionProbeTimeSlicingMode |
    IndexOfFirstValueMatchCameraClearMode |
    IndexOfFirstValueMatchCameraPositioningMode |
    IndexOfFirstValueMatchCameraProjection |
    IndexOfFirstValueMatchZWrite |
    IndexOfFirstValueMatchZTest |
    IndexOfFirstValueMatchBlend |
    IndexOfFirstValueMatchBlendMode |
    IndexOfFirstValueMatchCulling |
    IndexOfFirstValueMatchBodyNode |
    IndexOfFirstValueMatchChirality |
    IndexOfFirstValueMatchDummyEnum
)