"""Generated component: GlobalToValueOutput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class GlobalToValueOutputBase(GeneratedComponent):
    """Base class for GlobalToValueOutput<T> variants."""

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
class GlobalToValueOutputBool(GlobalToValueOutputBase):
    """GlobalToValueOutput<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<bool>


@dataclass
class GlobalToValueOutputByte(GlobalToValueOutputBase):
    """GlobalToValueOutput<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<byte>


@dataclass
class GlobalToValueOutputUshort(GlobalToValueOutputBase):
    """GlobalToValueOutput<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ushort>


@dataclass
class GlobalToValueOutputUint(GlobalToValueOutputBase):
    """GlobalToValueOutput<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<uint>


@dataclass
class GlobalToValueOutputUlong(GlobalToValueOutputBase):
    """GlobalToValueOutput<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ulong>


@dataclass
class GlobalToValueOutputSbyte(GlobalToValueOutputBase):
    """GlobalToValueOutput<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<sbyte>


@dataclass
class GlobalToValueOutputShort(GlobalToValueOutputBase):
    """GlobalToValueOutput<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<short>


@dataclass
class GlobalToValueOutputInt(GlobalToValueOutputBase):
    """GlobalToValueOutput<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<int>


@dataclass
class GlobalToValueOutputLong(GlobalToValueOutputBase):
    """GlobalToValueOutput<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<long>


@dataclass
class GlobalToValueOutputFloat(GlobalToValueOutputBase):
    """GlobalToValueOutput<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float>


@dataclass
class GlobalToValueOutputDouble(GlobalToValueOutputBase):
    """GlobalToValueOutput<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double>


@dataclass
class GlobalToValueOutputDecimal(GlobalToValueOutputBase):
    """GlobalToValueOutput<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<decimal>


@dataclass
class GlobalToValueOutputChar(GlobalToValueOutputBase):
    """GlobalToValueOutput<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<char>


@dataclass
class GlobalToValueOutputString(GlobalToValueOutputBase):
    """GlobalToValueOutput<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class GlobalToValueOutputUri(GlobalToValueOutputBase):
    """GlobalToValueOutput<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<Uri>


@dataclass
class GlobalToValueOutputBool2(GlobalToValueOutputBase):
    """GlobalToValueOutput<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<bool2>


@dataclass
class GlobalToValueOutputByte2(GlobalToValueOutputBase):
    """GlobalToValueOutput<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<byte2>


@dataclass
class GlobalToValueOutputUshort2(GlobalToValueOutputBase):
    """GlobalToValueOutput<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ushort2>


@dataclass
class GlobalToValueOutputUint2(GlobalToValueOutputBase):
    """GlobalToValueOutput<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<uint2>


@dataclass
class GlobalToValueOutputUlong2(GlobalToValueOutputBase):
    """GlobalToValueOutput<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ulong2>


@dataclass
class GlobalToValueOutputSbyte2(GlobalToValueOutputBase):
    """GlobalToValueOutput<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<sbyte2>


@dataclass
class GlobalToValueOutputShort2(GlobalToValueOutputBase):
    """GlobalToValueOutput<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<short2>


@dataclass
class GlobalToValueOutputInt2(GlobalToValueOutputBase):
    """GlobalToValueOutput<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<int2>


@dataclass
class GlobalToValueOutputLong2(GlobalToValueOutputBase):
    """GlobalToValueOutput<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<long2>


@dataclass
class GlobalToValueOutputFloat2(GlobalToValueOutputBase):
    """GlobalToValueOutput<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float2>


@dataclass
class GlobalToValueOutputDouble2(GlobalToValueOutputBase):
    """GlobalToValueOutput<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double2>


@dataclass
class GlobalToValueOutputBool3(GlobalToValueOutputBase):
    """GlobalToValueOutput<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<bool3>


@dataclass
class GlobalToValueOutputByte3(GlobalToValueOutputBase):
    """GlobalToValueOutput<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<byte3>


@dataclass
class GlobalToValueOutputUshort3(GlobalToValueOutputBase):
    """GlobalToValueOutput<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ushort3>


@dataclass
class GlobalToValueOutputUint3(GlobalToValueOutputBase):
    """GlobalToValueOutput<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<uint3>


@dataclass
class GlobalToValueOutputUlong3(GlobalToValueOutputBase):
    """GlobalToValueOutput<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ulong3>


@dataclass
class GlobalToValueOutputSbyte3(GlobalToValueOutputBase):
    """GlobalToValueOutput<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<sbyte3>


@dataclass
class GlobalToValueOutputShort3(GlobalToValueOutputBase):
    """GlobalToValueOutput<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<short3>


@dataclass
class GlobalToValueOutputInt3(GlobalToValueOutputBase):
    """GlobalToValueOutput<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<int3>


@dataclass
class GlobalToValueOutputLong3(GlobalToValueOutputBase):
    """GlobalToValueOutput<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<long3>


@dataclass
class GlobalToValueOutputFloat3(GlobalToValueOutputBase):
    """GlobalToValueOutput<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float3>


@dataclass
class GlobalToValueOutputDouble3(GlobalToValueOutputBase):
    """GlobalToValueOutput<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double3>


@dataclass
class GlobalToValueOutputBool4(GlobalToValueOutputBase):
    """GlobalToValueOutput<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<bool4>


@dataclass
class GlobalToValueOutputByte4(GlobalToValueOutputBase):
    """GlobalToValueOutput<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<byte4>


@dataclass
class GlobalToValueOutputUshort4(GlobalToValueOutputBase):
    """GlobalToValueOutput<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ushort4>


@dataclass
class GlobalToValueOutputUint4(GlobalToValueOutputBase):
    """GlobalToValueOutput<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<uint4>


@dataclass
class GlobalToValueOutputUlong4(GlobalToValueOutputBase):
    """GlobalToValueOutput<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<ulong4>


@dataclass
class GlobalToValueOutputSbyte4(GlobalToValueOutputBase):
    """GlobalToValueOutput<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<sbyte4>


@dataclass
class GlobalToValueOutputShort4(GlobalToValueOutputBase):
    """GlobalToValueOutput<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<short4>


@dataclass
class GlobalToValueOutputInt4(GlobalToValueOutputBase):
    """GlobalToValueOutput<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<int4>


@dataclass
class GlobalToValueOutputLong4(GlobalToValueOutputBase):
    """GlobalToValueOutput<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<long4>


@dataclass
class GlobalToValueOutputFloat4(GlobalToValueOutputBase):
    """GlobalToValueOutput<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float4>


@dataclass
class GlobalToValueOutputDouble4(GlobalToValueOutputBase):
    """GlobalToValueOutput<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double4>


@dataclass
class GlobalToValueOutputFloat_2x2(GlobalToValueOutputBase):
    """GlobalToValueOutput<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float2x2>


@dataclass
class GlobalToValueOutputDouble_2x2(GlobalToValueOutputBase):
    """GlobalToValueOutput<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double2x2>


@dataclass
class GlobalToValueOutputFloat_3x3(GlobalToValueOutputBase):
    """GlobalToValueOutput<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float3x3>


@dataclass
class GlobalToValueOutputDouble_3x3(GlobalToValueOutputBase):
    """GlobalToValueOutput<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double3x3>


@dataclass
class GlobalToValueOutputFloat_4x4(GlobalToValueOutputBase):
    """GlobalToValueOutput<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<float4x4>


@dataclass
class GlobalToValueOutputDouble_4x4(GlobalToValueOutputBase):
    """GlobalToValueOutput<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<double4x4>


@dataclass
class GlobalToValueOutputFloatQ(GlobalToValueOutputBase):
    """GlobalToValueOutput<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<floatQ>


@dataclass
class GlobalToValueOutputDoubleQ(GlobalToValueOutputBase):
    """GlobalToValueOutput<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<doubleQ>


@dataclass
class GlobalToValueOutputDateTime(GlobalToValueOutputBase):
    """GlobalToValueOutput<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[System.Private.CoreLib]System.DateTime>


@dataclass
class GlobalToValueOutputTimeSpan(GlobalToValueOutputBase):
    """GlobalToValueOutput<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class GlobalToValueOutputColor(GlobalToValueOutputBase):
    """GlobalToValueOutput<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<color>


@dataclass
class GlobalToValueOutputColorX(GlobalToValueOutputBase):
    """GlobalToValueOutput<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<colorX>


@dataclass
class GlobalToValueOutputShadowCastMode(GlobalToValueOutputBase):
    """GlobalToValueOutput<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class GlobalToValueOutputLightType(GlobalToValueOutputBase):
    """GlobalToValueOutput<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class GlobalToValueOutputSessionAccessLevel(GlobalToValueOutputBase):
    """GlobalToValueOutput<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class GlobalToValueOutputKey(GlobalToValueOutputBase):
    """GlobalToValueOutput<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class GlobalToValueOutputHttpStatusCode(GlobalToValueOutputBase):
    """GlobalToValueOutput<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class GlobalToValueOutputHeadOutputDevice(GlobalToValueOutputBase):
    """GlobalToValueOutput<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class GlobalToValueOutputReflectionProbeClear(GlobalToValueOutputBase):
    """GlobalToValueOutput<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class GlobalToValueOutputReflectionProbeType(GlobalToValueOutputBase):
    """GlobalToValueOutput<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class GlobalToValueOutputReflectionProbeTimeSlicingMode(GlobalToValueOutputBase):
    """GlobalToValueOutput<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class GlobalToValueOutputCameraClearMode(GlobalToValueOutputBase):
    """GlobalToValueOutput<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class GlobalToValueOutputCameraPositioningMode(GlobalToValueOutputBase):
    """GlobalToValueOutput<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.CameraPositioningMode>


@dataclass
class GlobalToValueOutputCameraProjection(GlobalToValueOutputBase):
    """GlobalToValueOutput<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class GlobalToValueOutputZWrite(GlobalToValueOutputBase):
    """GlobalToValueOutput<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.ZWrite>


@dataclass
class GlobalToValueOutputZTest(GlobalToValueOutputBase):
    """GlobalToValueOutput<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.ZTest>


@dataclass
class GlobalToValueOutputBlend(GlobalToValueOutputBase):
    """GlobalToValueOutput<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.Blend>


@dataclass
class GlobalToValueOutputBlendMode(GlobalToValueOutputBase):
    """GlobalToValueOutput<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.BlendMode>


@dataclass
class GlobalToValueOutputCulling(GlobalToValueOutputBase):
    """GlobalToValueOutput<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<FrooxEngine.Culling>


@dataclass
class GlobalToValueOutputBodyNode(GlobalToValueOutputBase):
    """GlobalToValueOutput<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class GlobalToValueOutputChirality(GlobalToValueOutputBase):
    """GlobalToValueOutput<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class GlobalToValueOutputDummyEnum(GlobalToValueOutputBase):
    """GlobalToValueOutput<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.GlobalToValueOutput<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "global_": "Global",
    }

    global_: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<DummyEnum>


# Type alias for any GlobalToValueOutput variant
GlobalToValueOutput = (
    GlobalToValueOutputBool |
    GlobalToValueOutputByte |
    GlobalToValueOutputUshort |
    GlobalToValueOutputUint |
    GlobalToValueOutputUlong |
    GlobalToValueOutputSbyte |
    GlobalToValueOutputShort |
    GlobalToValueOutputInt |
    GlobalToValueOutputLong |
    GlobalToValueOutputFloat |
    GlobalToValueOutputDouble |
    GlobalToValueOutputDecimal |
    GlobalToValueOutputChar |
    GlobalToValueOutputString |
    GlobalToValueOutputUri |
    GlobalToValueOutputBool2 |
    GlobalToValueOutputByte2 |
    GlobalToValueOutputUshort2 |
    GlobalToValueOutputUint2 |
    GlobalToValueOutputUlong2 |
    GlobalToValueOutputSbyte2 |
    GlobalToValueOutputShort2 |
    GlobalToValueOutputInt2 |
    GlobalToValueOutputLong2 |
    GlobalToValueOutputFloat2 |
    GlobalToValueOutputDouble2 |
    GlobalToValueOutputBool3 |
    GlobalToValueOutputByte3 |
    GlobalToValueOutputUshort3 |
    GlobalToValueOutputUint3 |
    GlobalToValueOutputUlong3 |
    GlobalToValueOutputSbyte3 |
    GlobalToValueOutputShort3 |
    GlobalToValueOutputInt3 |
    GlobalToValueOutputLong3 |
    GlobalToValueOutputFloat3 |
    GlobalToValueOutputDouble3 |
    GlobalToValueOutputBool4 |
    GlobalToValueOutputByte4 |
    GlobalToValueOutputUshort4 |
    GlobalToValueOutputUint4 |
    GlobalToValueOutputUlong4 |
    GlobalToValueOutputSbyte4 |
    GlobalToValueOutputShort4 |
    GlobalToValueOutputInt4 |
    GlobalToValueOutputLong4 |
    GlobalToValueOutputFloat4 |
    GlobalToValueOutputDouble4 |
    GlobalToValueOutputFloat_2x2 |
    GlobalToValueOutputDouble_2x2 |
    GlobalToValueOutputFloat_3x3 |
    GlobalToValueOutputDouble_3x3 |
    GlobalToValueOutputFloat_4x4 |
    GlobalToValueOutputDouble_4x4 |
    GlobalToValueOutputFloatQ |
    GlobalToValueOutputDoubleQ |
    GlobalToValueOutputDateTime |
    GlobalToValueOutputTimeSpan |
    GlobalToValueOutputColor |
    GlobalToValueOutputColorX |
    GlobalToValueOutputShadowCastMode |
    GlobalToValueOutputLightType |
    GlobalToValueOutputSessionAccessLevel |
    GlobalToValueOutputKey |
    GlobalToValueOutputHttpStatusCode |
    GlobalToValueOutputHeadOutputDevice |
    GlobalToValueOutputReflectionProbeClear |
    GlobalToValueOutputReflectionProbeType |
    GlobalToValueOutputReflectionProbeTimeSlicingMode |
    GlobalToValueOutputCameraClearMode |
    GlobalToValueOutputCameraPositioningMode |
    GlobalToValueOutputCameraProjection |
    GlobalToValueOutputZWrite |
    GlobalToValueOutputZTest |
    GlobalToValueOutputBlend |
    GlobalToValueOutputBlendMode |
    GlobalToValueOutputCulling |
    GlobalToValueOutputBodyNode |
    GlobalToValueOutputChirality |
    GlobalToValueOutputDummyEnum
)