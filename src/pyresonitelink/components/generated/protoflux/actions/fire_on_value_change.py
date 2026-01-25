"""Generated component: FireOnValueChange.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FireOnValueChangeBase(GeneratedComponent):
    """Base class for FireOnValueChange<T> variants."""

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
class FireOnValueChangeBool(FireOnValueChangeBase):
    """FireOnValueChange<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class FireOnValueChangeByte(FireOnValueChangeBase):
    """FireOnValueChange<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class FireOnValueChangeUshort(FireOnValueChangeBase):
    """FireOnValueChange<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class FireOnValueChangeUint(FireOnValueChangeBase):
    """FireOnValueChange<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class FireOnValueChangeUlong(FireOnValueChangeBase):
    """FireOnValueChange<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class FireOnValueChangeSbyte(FireOnValueChangeBase):
    """FireOnValueChange<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class FireOnValueChangeShort(FireOnValueChangeBase):
    """FireOnValueChange<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class FireOnValueChangeInt(FireOnValueChangeBase):
    """FireOnValueChange<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class FireOnValueChangeLong(FireOnValueChangeBase):
    """FireOnValueChange<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class FireOnValueChangeFloat(FireOnValueChangeBase):
    """FireOnValueChange<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class FireOnValueChangeDouble(FireOnValueChangeBase):
    """FireOnValueChange<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FireOnValueChangeDecimal(FireOnValueChangeBase):
    """FireOnValueChange<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class FireOnValueChangeChar(FireOnValueChangeBase):
    """FireOnValueChange<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class FireOnValueChangeString(FireOnValueChangeBase):
    """FireOnValueChange<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class FireOnValueChangeUri(FireOnValueChangeBase):
    """FireOnValueChange<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class FireOnValueChangeBool2(FireOnValueChangeBase):
    """FireOnValueChange<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class FireOnValueChangeByte2(FireOnValueChangeBase):
    """FireOnValueChange<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class FireOnValueChangeUshort2(FireOnValueChangeBase):
    """FireOnValueChange<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class FireOnValueChangeUint2(FireOnValueChangeBase):
    """FireOnValueChange<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class FireOnValueChangeUlong2(FireOnValueChangeBase):
    """FireOnValueChange<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class FireOnValueChangeSbyte2(FireOnValueChangeBase):
    """FireOnValueChange<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class FireOnValueChangeShort2(FireOnValueChangeBase):
    """FireOnValueChange<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class FireOnValueChangeInt2(FireOnValueChangeBase):
    """FireOnValueChange<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class FireOnValueChangeLong2(FireOnValueChangeBase):
    """FireOnValueChange<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class FireOnValueChangeFloat2(FireOnValueChangeBase):
    """FireOnValueChange<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class FireOnValueChangeDouble2(FireOnValueChangeBase):
    """FireOnValueChange<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class FireOnValueChangeBool3(FireOnValueChangeBase):
    """FireOnValueChange<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class FireOnValueChangeByte3(FireOnValueChangeBase):
    """FireOnValueChange<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class FireOnValueChangeUshort3(FireOnValueChangeBase):
    """FireOnValueChange<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class FireOnValueChangeUint3(FireOnValueChangeBase):
    """FireOnValueChange<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class FireOnValueChangeUlong3(FireOnValueChangeBase):
    """FireOnValueChange<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class FireOnValueChangeSbyte3(FireOnValueChangeBase):
    """FireOnValueChange<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class FireOnValueChangeShort3(FireOnValueChangeBase):
    """FireOnValueChange<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class FireOnValueChangeInt3(FireOnValueChangeBase):
    """FireOnValueChange<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class FireOnValueChangeLong3(FireOnValueChangeBase):
    """FireOnValueChange<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class FireOnValueChangeFloat3(FireOnValueChangeBase):
    """FireOnValueChange<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class FireOnValueChangeDouble3(FireOnValueChangeBase):
    """FireOnValueChange<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class FireOnValueChangeBool4(FireOnValueChangeBase):
    """FireOnValueChange<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class FireOnValueChangeByte4(FireOnValueChangeBase):
    """FireOnValueChange<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class FireOnValueChangeUshort4(FireOnValueChangeBase):
    """FireOnValueChange<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class FireOnValueChangeUint4(FireOnValueChangeBase):
    """FireOnValueChange<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class FireOnValueChangeUlong4(FireOnValueChangeBase):
    """FireOnValueChange<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class FireOnValueChangeSbyte4(FireOnValueChangeBase):
    """FireOnValueChange<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class FireOnValueChangeShort4(FireOnValueChangeBase):
    """FireOnValueChange<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class FireOnValueChangeInt4(FireOnValueChangeBase):
    """FireOnValueChange<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class FireOnValueChangeLong4(FireOnValueChangeBase):
    """FireOnValueChange<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class FireOnValueChangeFloat4(FireOnValueChangeBase):
    """FireOnValueChange<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class FireOnValueChangeDouble4(FireOnValueChangeBase):
    """FireOnValueChange<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class FireOnValueChangeFloat_2x2(FireOnValueChangeBase):
    """FireOnValueChange<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class FireOnValueChangeDouble_2x2(FireOnValueChangeBase):
    """FireOnValueChange<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class FireOnValueChangeFloat_3x3(FireOnValueChangeBase):
    """FireOnValueChange<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class FireOnValueChangeDouble_3x3(FireOnValueChangeBase):
    """FireOnValueChange<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class FireOnValueChangeFloat_4x4(FireOnValueChangeBase):
    """FireOnValueChange<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class FireOnValueChangeDouble_4x4(FireOnValueChangeBase):
    """FireOnValueChange<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class FireOnValueChangeFloatQ(FireOnValueChangeBase):
    """FireOnValueChange<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class FireOnValueChangeDoubleQ(FireOnValueChangeBase):
    """FireOnValueChange<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class FireOnValueChangeDateTime(FireOnValueChangeBase):
    """FireOnValueChange<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class FireOnValueChangeTimeSpan(FireOnValueChangeBase):
    """FireOnValueChange<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class FireOnValueChangeColor(FireOnValueChangeBase):
    """FireOnValueChange<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class FireOnValueChangeColorX(FireOnValueChangeBase):
    """FireOnValueChange<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class FireOnValueChangeShadowCastMode(FireOnValueChangeBase):
    """FireOnValueChange<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class FireOnValueChangeLightType(FireOnValueChangeBase):
    """FireOnValueChange<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class FireOnValueChangeSessionAccessLevel(FireOnValueChangeBase):
    """FireOnValueChange<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class FireOnValueChangeKey(FireOnValueChangeBase):
    """FireOnValueChange<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class FireOnValueChangeHttpStatusCode(FireOnValueChangeBase):
    """FireOnValueChange<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class FireOnValueChangeHeadOutputDevice(FireOnValueChangeBase):
    """FireOnValueChange<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class FireOnValueChangeReflectionProbeClear(FireOnValueChangeBase):
    """FireOnValueChange<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class FireOnValueChangeReflectionProbeType(FireOnValueChangeBase):
    """FireOnValueChange<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class FireOnValueChangeReflectionProbeTimeSlicingMode(FireOnValueChangeBase):
    """FireOnValueChange<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class FireOnValueChangeCameraClearMode(FireOnValueChangeBase):
    """FireOnValueChange<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class FireOnValueChangeCameraPositioningMode(FireOnValueChangeBase):
    """FireOnValueChange<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class FireOnValueChangeCameraProjection(FireOnValueChangeBase):
    """FireOnValueChange<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class FireOnValueChangeZWrite(FireOnValueChangeBase):
    """FireOnValueChange<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class FireOnValueChangeZTest(FireOnValueChangeBase):
    """FireOnValueChange<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class FireOnValueChangeBlend(FireOnValueChangeBase):
    """FireOnValueChange<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class FireOnValueChangeBlendMode(FireOnValueChangeBase):
    """FireOnValueChange<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class FireOnValueChangeCulling(FireOnValueChangeBase):
    """FireOnValueChange<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class FireOnValueChangeBodyNode(FireOnValueChangeBase):
    """FireOnValueChange<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class FireOnValueChangeChirality(FireOnValueChangeBase):
    """FireOnValueChange<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class FireOnValueChangeDummyEnum(FireOnValueChangeBase):
    """FireOnValueChange<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnValueChange<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_changed": "OnChanged",
        "only_for_user": "OnlyForUser",
        "value": "Value",
    }

    on_changed: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    only_for_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any FireOnValueChange variant
FireOnValueChange = (
    FireOnValueChangeBool |
    FireOnValueChangeByte |
    FireOnValueChangeUshort |
    FireOnValueChangeUint |
    FireOnValueChangeUlong |
    FireOnValueChangeSbyte |
    FireOnValueChangeShort |
    FireOnValueChangeInt |
    FireOnValueChangeLong |
    FireOnValueChangeFloat |
    FireOnValueChangeDouble |
    FireOnValueChangeDecimal |
    FireOnValueChangeChar |
    FireOnValueChangeString |
    FireOnValueChangeUri |
    FireOnValueChangeBool2 |
    FireOnValueChangeByte2 |
    FireOnValueChangeUshort2 |
    FireOnValueChangeUint2 |
    FireOnValueChangeUlong2 |
    FireOnValueChangeSbyte2 |
    FireOnValueChangeShort2 |
    FireOnValueChangeInt2 |
    FireOnValueChangeLong2 |
    FireOnValueChangeFloat2 |
    FireOnValueChangeDouble2 |
    FireOnValueChangeBool3 |
    FireOnValueChangeByte3 |
    FireOnValueChangeUshort3 |
    FireOnValueChangeUint3 |
    FireOnValueChangeUlong3 |
    FireOnValueChangeSbyte3 |
    FireOnValueChangeShort3 |
    FireOnValueChangeInt3 |
    FireOnValueChangeLong3 |
    FireOnValueChangeFloat3 |
    FireOnValueChangeDouble3 |
    FireOnValueChangeBool4 |
    FireOnValueChangeByte4 |
    FireOnValueChangeUshort4 |
    FireOnValueChangeUint4 |
    FireOnValueChangeUlong4 |
    FireOnValueChangeSbyte4 |
    FireOnValueChangeShort4 |
    FireOnValueChangeInt4 |
    FireOnValueChangeLong4 |
    FireOnValueChangeFloat4 |
    FireOnValueChangeDouble4 |
    FireOnValueChangeFloat_2x2 |
    FireOnValueChangeDouble_2x2 |
    FireOnValueChangeFloat_3x3 |
    FireOnValueChangeDouble_3x3 |
    FireOnValueChangeFloat_4x4 |
    FireOnValueChangeDouble_4x4 |
    FireOnValueChangeFloatQ |
    FireOnValueChangeDoubleQ |
    FireOnValueChangeDateTime |
    FireOnValueChangeTimeSpan |
    FireOnValueChangeColor |
    FireOnValueChangeColorX |
    FireOnValueChangeShadowCastMode |
    FireOnValueChangeLightType |
    FireOnValueChangeSessionAccessLevel |
    FireOnValueChangeKey |
    FireOnValueChangeHttpStatusCode |
    FireOnValueChangeHeadOutputDevice |
    FireOnValueChangeReflectionProbeClear |
    FireOnValueChangeReflectionProbeType |
    FireOnValueChangeReflectionProbeTimeSlicingMode |
    FireOnValueChangeCameraClearMode |
    FireOnValueChangeCameraPositioningMode |
    FireOnValueChangeCameraProjection |
    FireOnValueChangeZWrite |
    FireOnValueChangeZTest |
    FireOnValueChangeBlend |
    FireOnValueChangeBlendMode |
    FireOnValueChangeCulling |
    FireOnValueChangeBodyNode |
    FireOnValueChangeChirality |
    FireOnValueChangeDummyEnum
)