"""Generated component: AsyncDynamicImpulseReceiverWithValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AsyncDynamicImpulseReceiverWithValueBase(GeneratedComponent):
    """Base class for AsyncDynamicImpulseReceiverWithValue<T> variants."""

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
class AsyncDynamicImpulseReceiverWithValueBool(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueByte(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUshort(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUint(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUlong(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueSbyte(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueShort(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueInt(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueLong(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDecimal(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueChar(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueString(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUri(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBool2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueByte2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUshort2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUint2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUlong2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueSbyte2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueShort2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueInt2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueLong2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBool3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueByte3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUshort3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUint3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUlong3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueSbyte3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueShort3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueInt3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueLong3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBool4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueByte4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUshort4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUint4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueUlong4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueSbyte4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueShort4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueInt4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueLong4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat_2x2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble_2x2(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat_3x3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble_3x3(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloat_4x4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDouble_4x4(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueFloatQ(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDoubleQ(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDateTime(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueTimeSpan(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueColor(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueColorX(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueShadowCastMode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueLightType(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueSessionAccessLevel(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueKey(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueHttpStatusCode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueHeadOutputDevice(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueReflectionProbeClear(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueReflectionProbeType(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueReflectionProbeTimeSlicingMode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueCameraClearMode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueCameraPositioningMode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueCameraProjection(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueZWrite(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueZTest(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBlend(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBlendMode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueCulling(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueBodyNode(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueChirality(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class AsyncDynamicImpulseReceiverWithValueDummyEnum(AsyncDynamicImpulseReceiverWithValueBase):
    """AsyncDynamicImpulseReceiverWithValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseReceiverWithValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_triggered": "OnTriggered",
        "tag": "Tag",
    }

    on_triggered: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


# Type alias for any AsyncDynamicImpulseReceiverWithValue variant
AsyncDynamicImpulseReceiverWithValue = (
    AsyncDynamicImpulseReceiverWithValueBool |
    AsyncDynamicImpulseReceiverWithValueByte |
    AsyncDynamicImpulseReceiverWithValueUshort |
    AsyncDynamicImpulseReceiverWithValueUint |
    AsyncDynamicImpulseReceiverWithValueUlong |
    AsyncDynamicImpulseReceiverWithValueSbyte |
    AsyncDynamicImpulseReceiverWithValueShort |
    AsyncDynamicImpulseReceiverWithValueInt |
    AsyncDynamicImpulseReceiverWithValueLong |
    AsyncDynamicImpulseReceiverWithValueFloat |
    AsyncDynamicImpulseReceiverWithValueDouble |
    AsyncDynamicImpulseReceiverWithValueDecimal |
    AsyncDynamicImpulseReceiverWithValueChar |
    AsyncDynamicImpulseReceiverWithValueString |
    AsyncDynamicImpulseReceiverWithValueUri |
    AsyncDynamicImpulseReceiverWithValueBool2 |
    AsyncDynamicImpulseReceiverWithValueByte2 |
    AsyncDynamicImpulseReceiverWithValueUshort2 |
    AsyncDynamicImpulseReceiverWithValueUint2 |
    AsyncDynamicImpulseReceiverWithValueUlong2 |
    AsyncDynamicImpulseReceiverWithValueSbyte2 |
    AsyncDynamicImpulseReceiverWithValueShort2 |
    AsyncDynamicImpulseReceiverWithValueInt2 |
    AsyncDynamicImpulseReceiverWithValueLong2 |
    AsyncDynamicImpulseReceiverWithValueFloat2 |
    AsyncDynamicImpulseReceiverWithValueDouble2 |
    AsyncDynamicImpulseReceiverWithValueBool3 |
    AsyncDynamicImpulseReceiverWithValueByte3 |
    AsyncDynamicImpulseReceiverWithValueUshort3 |
    AsyncDynamicImpulseReceiverWithValueUint3 |
    AsyncDynamicImpulseReceiverWithValueUlong3 |
    AsyncDynamicImpulseReceiverWithValueSbyte3 |
    AsyncDynamicImpulseReceiverWithValueShort3 |
    AsyncDynamicImpulseReceiverWithValueInt3 |
    AsyncDynamicImpulseReceiverWithValueLong3 |
    AsyncDynamicImpulseReceiverWithValueFloat3 |
    AsyncDynamicImpulseReceiverWithValueDouble3 |
    AsyncDynamicImpulseReceiverWithValueBool4 |
    AsyncDynamicImpulseReceiverWithValueByte4 |
    AsyncDynamicImpulseReceiverWithValueUshort4 |
    AsyncDynamicImpulseReceiverWithValueUint4 |
    AsyncDynamicImpulseReceiverWithValueUlong4 |
    AsyncDynamicImpulseReceiverWithValueSbyte4 |
    AsyncDynamicImpulseReceiverWithValueShort4 |
    AsyncDynamicImpulseReceiverWithValueInt4 |
    AsyncDynamicImpulseReceiverWithValueLong4 |
    AsyncDynamicImpulseReceiverWithValueFloat4 |
    AsyncDynamicImpulseReceiverWithValueDouble4 |
    AsyncDynamicImpulseReceiverWithValueFloat_2x2 |
    AsyncDynamicImpulseReceiverWithValueDouble_2x2 |
    AsyncDynamicImpulseReceiverWithValueFloat_3x3 |
    AsyncDynamicImpulseReceiverWithValueDouble_3x3 |
    AsyncDynamicImpulseReceiverWithValueFloat_4x4 |
    AsyncDynamicImpulseReceiverWithValueDouble_4x4 |
    AsyncDynamicImpulseReceiverWithValueFloatQ |
    AsyncDynamicImpulseReceiverWithValueDoubleQ |
    AsyncDynamicImpulseReceiverWithValueDateTime |
    AsyncDynamicImpulseReceiverWithValueTimeSpan |
    AsyncDynamicImpulseReceiverWithValueColor |
    AsyncDynamicImpulseReceiverWithValueColorX |
    AsyncDynamicImpulseReceiverWithValueShadowCastMode |
    AsyncDynamicImpulseReceiverWithValueLightType |
    AsyncDynamicImpulseReceiverWithValueSessionAccessLevel |
    AsyncDynamicImpulseReceiverWithValueKey |
    AsyncDynamicImpulseReceiverWithValueHttpStatusCode |
    AsyncDynamicImpulseReceiverWithValueHeadOutputDevice |
    AsyncDynamicImpulseReceiverWithValueReflectionProbeClear |
    AsyncDynamicImpulseReceiverWithValueReflectionProbeType |
    AsyncDynamicImpulseReceiverWithValueReflectionProbeTimeSlicingMode |
    AsyncDynamicImpulseReceiverWithValueCameraClearMode |
    AsyncDynamicImpulseReceiverWithValueCameraPositioningMode |
    AsyncDynamicImpulseReceiverWithValueCameraProjection |
    AsyncDynamicImpulseReceiverWithValueZWrite |
    AsyncDynamicImpulseReceiverWithValueZTest |
    AsyncDynamicImpulseReceiverWithValueBlend |
    AsyncDynamicImpulseReceiverWithValueBlendMode |
    AsyncDynamicImpulseReceiverWithValueCulling |
    AsyncDynamicImpulseReceiverWithValueBodyNode |
    AsyncDynamicImpulseReceiverWithValueChirality |
    AsyncDynamicImpulseReceiverWithValueDummyEnum
)