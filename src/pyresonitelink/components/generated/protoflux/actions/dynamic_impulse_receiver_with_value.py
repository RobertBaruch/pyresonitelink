"""Generated component: DynamicImpulseReceiverWithValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DynamicImpulseReceiverWithValueBase(GeneratedComponent):
    """Base class for DynamicImpulseReceiverWithValue<T> variants."""

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
class DynamicImpulseReceiverWithValueBool(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueByte(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUshort(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUint(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUlong(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueSbyte(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueShort(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueInt(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueLong(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDecimal(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueChar(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueString(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUri(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBool2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueByte2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUshort2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUint2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUlong2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueSbyte2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueShort2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueInt2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueLong2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBool3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueByte3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUshort3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUint3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUlong3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueSbyte3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueShort3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueInt3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueLong3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBool4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueByte4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUshort4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUint4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueUlong4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueSbyte4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueShort4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueInt4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueLong4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat_2x2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble_2x2(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat_3x3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble_3x3(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloat_4x4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDouble_4x4(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueFloatQ(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDoubleQ(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDateTime(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueTimeSpan(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueColor(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueColorX(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueShadowCastMode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueLightType(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueSessionAccessLevel(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueKey(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueHttpStatusCode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueHeadOutputDevice(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueReflectionProbeClear(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueReflectionProbeType(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueReflectionProbeTimeSlicingMode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueCameraClearMode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueCameraPositioningMode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueCameraProjection(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueZWrite(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueZTest(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBlend(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBlendMode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueCulling(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueBodyNode(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueChirality(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicImpulseReceiverWithValueDummyEnum(DynamicImpulseReceiverWithValueBase):
    """DynamicImpulseReceiverWithValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseReceiverWithValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


# Type alias for any DynamicImpulseReceiverWithValue variant
DynamicImpulseReceiverWithValue = (
    DynamicImpulseReceiverWithValueBool |
    DynamicImpulseReceiverWithValueByte |
    DynamicImpulseReceiverWithValueUshort |
    DynamicImpulseReceiverWithValueUint |
    DynamicImpulseReceiverWithValueUlong |
    DynamicImpulseReceiverWithValueSbyte |
    DynamicImpulseReceiverWithValueShort |
    DynamicImpulseReceiverWithValueInt |
    DynamicImpulseReceiverWithValueLong |
    DynamicImpulseReceiverWithValueFloat |
    DynamicImpulseReceiverWithValueDouble |
    DynamicImpulseReceiverWithValueDecimal |
    DynamicImpulseReceiverWithValueChar |
    DynamicImpulseReceiverWithValueString |
    DynamicImpulseReceiverWithValueUri |
    DynamicImpulseReceiverWithValueBool2 |
    DynamicImpulseReceiverWithValueByte2 |
    DynamicImpulseReceiverWithValueUshort2 |
    DynamicImpulseReceiverWithValueUint2 |
    DynamicImpulseReceiverWithValueUlong2 |
    DynamicImpulseReceiverWithValueSbyte2 |
    DynamicImpulseReceiverWithValueShort2 |
    DynamicImpulseReceiverWithValueInt2 |
    DynamicImpulseReceiverWithValueLong2 |
    DynamicImpulseReceiverWithValueFloat2 |
    DynamicImpulseReceiverWithValueDouble2 |
    DynamicImpulseReceiverWithValueBool3 |
    DynamicImpulseReceiverWithValueByte3 |
    DynamicImpulseReceiverWithValueUshort3 |
    DynamicImpulseReceiverWithValueUint3 |
    DynamicImpulseReceiverWithValueUlong3 |
    DynamicImpulseReceiverWithValueSbyte3 |
    DynamicImpulseReceiverWithValueShort3 |
    DynamicImpulseReceiverWithValueInt3 |
    DynamicImpulseReceiverWithValueLong3 |
    DynamicImpulseReceiverWithValueFloat3 |
    DynamicImpulseReceiverWithValueDouble3 |
    DynamicImpulseReceiverWithValueBool4 |
    DynamicImpulseReceiverWithValueByte4 |
    DynamicImpulseReceiverWithValueUshort4 |
    DynamicImpulseReceiverWithValueUint4 |
    DynamicImpulseReceiverWithValueUlong4 |
    DynamicImpulseReceiverWithValueSbyte4 |
    DynamicImpulseReceiverWithValueShort4 |
    DynamicImpulseReceiverWithValueInt4 |
    DynamicImpulseReceiverWithValueLong4 |
    DynamicImpulseReceiverWithValueFloat4 |
    DynamicImpulseReceiverWithValueDouble4 |
    DynamicImpulseReceiverWithValueFloat_2x2 |
    DynamicImpulseReceiverWithValueDouble_2x2 |
    DynamicImpulseReceiverWithValueFloat_3x3 |
    DynamicImpulseReceiverWithValueDouble_3x3 |
    DynamicImpulseReceiverWithValueFloat_4x4 |
    DynamicImpulseReceiverWithValueDouble_4x4 |
    DynamicImpulseReceiverWithValueFloatQ |
    DynamicImpulseReceiverWithValueDoubleQ |
    DynamicImpulseReceiverWithValueDateTime |
    DynamicImpulseReceiverWithValueTimeSpan |
    DynamicImpulseReceiverWithValueColor |
    DynamicImpulseReceiverWithValueColorX |
    DynamicImpulseReceiverWithValueShadowCastMode |
    DynamicImpulseReceiverWithValueLightType |
    DynamicImpulseReceiverWithValueSessionAccessLevel |
    DynamicImpulseReceiverWithValueKey |
    DynamicImpulseReceiverWithValueHttpStatusCode |
    DynamicImpulseReceiverWithValueHeadOutputDevice |
    DynamicImpulseReceiverWithValueReflectionProbeClear |
    DynamicImpulseReceiverWithValueReflectionProbeType |
    DynamicImpulseReceiverWithValueReflectionProbeTimeSlicingMode |
    DynamicImpulseReceiverWithValueCameraClearMode |
    DynamicImpulseReceiverWithValueCameraPositioningMode |
    DynamicImpulseReceiverWithValueCameraProjection |
    DynamicImpulseReceiverWithValueZWrite |
    DynamicImpulseReceiverWithValueZTest |
    DynamicImpulseReceiverWithValueBlend |
    DynamicImpulseReceiverWithValueBlendMode |
    DynamicImpulseReceiverWithValueCulling |
    DynamicImpulseReceiverWithValueBodyNode |
    DynamicImpulseReceiverWithValueChirality |
    DynamicImpulseReceiverWithValueDummyEnum
)