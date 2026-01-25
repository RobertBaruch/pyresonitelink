"""Generated component: DelayValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DelayValueBase(GeneratedComponent):
    """Base class for DelayValue<T> variants."""

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
class DelayValueBool(DelayValueBase):
    """DelayValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class DelayValueByte(DelayValueBase):
    """DelayValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class DelayValueUshort(DelayValueBase):
    """DelayValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class DelayValueUint(DelayValueBase):
    """DelayValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class DelayValueUlong(DelayValueBase):
    """DelayValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class DelayValueSbyte(DelayValueBase):
    """DelayValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class DelayValueShort(DelayValueBase):
    """DelayValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class DelayValueInt(DelayValueBase):
    """DelayValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class DelayValueLong(DelayValueBase):
    """DelayValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class DelayValueFloat(DelayValueBase):
    """DelayValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class DelayValueDouble(DelayValueBase):
    """DelayValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class DelayValueDecimal(DelayValueBase):
    """DelayValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class DelayValueChar(DelayValueBase):
    """DelayValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class DelayValueString(DelayValueBase):
    """DelayValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class DelayValueUri(DelayValueBase):
    """DelayValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class DelayValueBool2(DelayValueBase):
    """DelayValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class DelayValueByte2(DelayValueBase):
    """DelayValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class DelayValueUshort2(DelayValueBase):
    """DelayValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class DelayValueUint2(DelayValueBase):
    """DelayValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class DelayValueUlong2(DelayValueBase):
    """DelayValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class DelayValueSbyte2(DelayValueBase):
    """DelayValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class DelayValueShort2(DelayValueBase):
    """DelayValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class DelayValueInt2(DelayValueBase):
    """DelayValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class DelayValueLong2(DelayValueBase):
    """DelayValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class DelayValueFloat2(DelayValueBase):
    """DelayValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class DelayValueDouble2(DelayValueBase):
    """DelayValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class DelayValueBool3(DelayValueBase):
    """DelayValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class DelayValueByte3(DelayValueBase):
    """DelayValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class DelayValueUshort3(DelayValueBase):
    """DelayValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class DelayValueUint3(DelayValueBase):
    """DelayValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class DelayValueUlong3(DelayValueBase):
    """DelayValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class DelayValueSbyte3(DelayValueBase):
    """DelayValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class DelayValueShort3(DelayValueBase):
    """DelayValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class DelayValueInt3(DelayValueBase):
    """DelayValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class DelayValueLong3(DelayValueBase):
    """DelayValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class DelayValueFloat3(DelayValueBase):
    """DelayValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class DelayValueDouble3(DelayValueBase):
    """DelayValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class DelayValueBool4(DelayValueBase):
    """DelayValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class DelayValueByte4(DelayValueBase):
    """DelayValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class DelayValueUshort4(DelayValueBase):
    """DelayValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class DelayValueUint4(DelayValueBase):
    """DelayValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class DelayValueUlong4(DelayValueBase):
    """DelayValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class DelayValueSbyte4(DelayValueBase):
    """DelayValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class DelayValueShort4(DelayValueBase):
    """DelayValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class DelayValueInt4(DelayValueBase):
    """DelayValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class DelayValueLong4(DelayValueBase):
    """DelayValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class DelayValueFloat4(DelayValueBase):
    """DelayValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class DelayValueDouble4(DelayValueBase):
    """DelayValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class DelayValueFloat_2x2(DelayValueBase):
    """DelayValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class DelayValueDouble_2x2(DelayValueBase):
    """DelayValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class DelayValueFloat_3x3(DelayValueBase):
    """DelayValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class DelayValueDouble_3x3(DelayValueBase):
    """DelayValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class DelayValueFloat_4x4(DelayValueBase):
    """DelayValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class DelayValueDouble_4x4(DelayValueBase):
    """DelayValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class DelayValueFloatQ(DelayValueBase):
    """DelayValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class DelayValueDoubleQ(DelayValueBase):
    """DelayValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class DelayValueDateTime(DelayValueBase):
    """DelayValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class DelayValueTimeSpan(DelayValueBase):
    """DelayValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class DelayValueColor(DelayValueBase):
    """DelayValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class DelayValueColorX(DelayValueBase):
    """DelayValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class DelayValueShadowCastMode(DelayValueBase):
    """DelayValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class DelayValueLightType(DelayValueBase):
    """DelayValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class DelayValueSessionAccessLevel(DelayValueBase):
    """DelayValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class DelayValueKey(DelayValueBase):
    """DelayValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class DelayValueHttpStatusCode(DelayValueBase):
    """DelayValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class DelayValueHeadOutputDevice(DelayValueBase):
    """DelayValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class DelayValueReflectionProbeClear(DelayValueBase):
    """DelayValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class DelayValueReflectionProbeType(DelayValueBase):
    """DelayValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class DelayValueReflectionProbeTimeSlicingMode(DelayValueBase):
    """DelayValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class DelayValueCameraClearMode(DelayValueBase):
    """DelayValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class DelayValueCameraPositioningMode(DelayValueBase):
    """DelayValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class DelayValueCameraProjection(DelayValueBase):
    """DelayValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class DelayValueZWrite(DelayValueBase):
    """DelayValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class DelayValueZTest(DelayValueBase):
    """DelayValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class DelayValueBlend(DelayValueBase):
    """DelayValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class DelayValueBlendMode(DelayValueBase):
    """DelayValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class DelayValueCulling(DelayValueBase):
    """DelayValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class DelayValueBodyNode(DelayValueBase):
    """DelayValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class DelayValueChirality(DelayValueBase):
    """DelayValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class DelayValueDummyEnum(DelayValueBase):
    """DelayValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "delay_seconds": "DelaySeconds",
        "value": "Value",
    }

    delay_seconds: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any DelayValue variant
DelayValue = (
    DelayValueBool |
    DelayValueByte |
    DelayValueUshort |
    DelayValueUint |
    DelayValueUlong |
    DelayValueSbyte |
    DelayValueShort |
    DelayValueInt |
    DelayValueLong |
    DelayValueFloat |
    DelayValueDouble |
    DelayValueDecimal |
    DelayValueChar |
    DelayValueString |
    DelayValueUri |
    DelayValueBool2 |
    DelayValueByte2 |
    DelayValueUshort2 |
    DelayValueUint2 |
    DelayValueUlong2 |
    DelayValueSbyte2 |
    DelayValueShort2 |
    DelayValueInt2 |
    DelayValueLong2 |
    DelayValueFloat2 |
    DelayValueDouble2 |
    DelayValueBool3 |
    DelayValueByte3 |
    DelayValueUshort3 |
    DelayValueUint3 |
    DelayValueUlong3 |
    DelayValueSbyte3 |
    DelayValueShort3 |
    DelayValueInt3 |
    DelayValueLong3 |
    DelayValueFloat3 |
    DelayValueDouble3 |
    DelayValueBool4 |
    DelayValueByte4 |
    DelayValueUshort4 |
    DelayValueUint4 |
    DelayValueUlong4 |
    DelayValueSbyte4 |
    DelayValueShort4 |
    DelayValueInt4 |
    DelayValueLong4 |
    DelayValueFloat4 |
    DelayValueDouble4 |
    DelayValueFloat_2x2 |
    DelayValueDouble_2x2 |
    DelayValueFloat_3x3 |
    DelayValueDouble_3x3 |
    DelayValueFloat_4x4 |
    DelayValueDouble_4x4 |
    DelayValueFloatQ |
    DelayValueDoubleQ |
    DelayValueDateTime |
    DelayValueTimeSpan |
    DelayValueColor |
    DelayValueColorX |
    DelayValueShadowCastMode |
    DelayValueLightType |
    DelayValueSessionAccessLevel |
    DelayValueKey |
    DelayValueHttpStatusCode |
    DelayValueHeadOutputDevice |
    DelayValueReflectionProbeClear |
    DelayValueReflectionProbeType |
    DelayValueReflectionProbeTimeSlicingMode |
    DelayValueCameraClearMode |
    DelayValueCameraPositioningMode |
    DelayValueCameraProjection |
    DelayValueZWrite |
    DelayValueZTest |
    DelayValueBlend |
    DelayValueBlendMode |
    DelayValueCulling |
    DelayValueBodyNode |
    DelayValueChirality |
    DelayValueDummyEnum
)