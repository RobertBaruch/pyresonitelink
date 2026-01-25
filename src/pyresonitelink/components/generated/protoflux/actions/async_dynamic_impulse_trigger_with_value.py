"""Generated component: AsyncDynamicImpulseTriggerWithValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class AsyncDynamicImpulseTriggerWithValueBase(GeneratedComponent):
    """Base class for AsyncDynamicImpulseTriggerWithValue<T> variants."""

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
class AsyncDynamicImpulseTriggerWithValueBool(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class AsyncDynamicImpulseTriggerWithValueByte(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUshort(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUint(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUlong(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class AsyncDynamicImpulseTriggerWithValueSbyte(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class AsyncDynamicImpulseTriggerWithValueShort(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class AsyncDynamicImpulseTriggerWithValueInt(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class AsyncDynamicImpulseTriggerWithValueLong(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDecimal(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class AsyncDynamicImpulseTriggerWithValueChar(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class AsyncDynamicImpulseTriggerWithValueString(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUri(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBool2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueByte2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUshort2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUint2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUlong2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueSbyte2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueShort2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueInt2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueLong2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBool3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueByte3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUshort3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUint3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUlong3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueSbyte3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueShort3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueInt3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueLong3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBool4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueByte4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUshort4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUint4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueUlong4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueSbyte4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueShort4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueInt4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueLong4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat_2x2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble_2x2(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat_3x3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble_3x3(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloat_4x4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDouble_4x4(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class AsyncDynamicImpulseTriggerWithValueFloatQ(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDoubleQ(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDateTime(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class AsyncDynamicImpulseTriggerWithValueTimeSpan(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class AsyncDynamicImpulseTriggerWithValueColor(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class AsyncDynamicImpulseTriggerWithValueColorX(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class AsyncDynamicImpulseTriggerWithValueShadowCastMode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueLightType(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class AsyncDynamicImpulseTriggerWithValueSessionAccessLevel(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class AsyncDynamicImpulseTriggerWithValueKey(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class AsyncDynamicImpulseTriggerWithValueHttpStatusCode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueHeadOutputDevice(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class AsyncDynamicImpulseTriggerWithValueReflectionProbeClear(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class AsyncDynamicImpulseTriggerWithValueReflectionProbeType(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class AsyncDynamicImpulseTriggerWithValueReflectionProbeTimeSlicingMode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueCameraClearMode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueCameraPositioningMode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueCameraProjection(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class AsyncDynamicImpulseTriggerWithValueZWrite(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class AsyncDynamicImpulseTriggerWithValueZTest(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBlend(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBlendMode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueCulling(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class AsyncDynamicImpulseTriggerWithValueBodyNode(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class AsyncDynamicImpulseTriggerWithValueChirality(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class AsyncDynamicImpulseTriggerWithValueDummyEnum(AsyncDynamicImpulseTriggerWithValueBase):
    """AsyncDynamicImpulseTriggerWithValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTriggerWithValue<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "exclude_disabled": "ExcludeDisabled",
        "next": "Next",
        "tag": "Tag",
        "target_hierarchy": "TargetHierarchy",
        "value": "Value",
    }

    exclude_disabled: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    next: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    tag: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target_hierarchy: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any AsyncDynamicImpulseTriggerWithValue variant
AsyncDynamicImpulseTriggerWithValue = (
    AsyncDynamicImpulseTriggerWithValueBool |
    AsyncDynamicImpulseTriggerWithValueByte |
    AsyncDynamicImpulseTriggerWithValueUshort |
    AsyncDynamicImpulseTriggerWithValueUint |
    AsyncDynamicImpulseTriggerWithValueUlong |
    AsyncDynamicImpulseTriggerWithValueSbyte |
    AsyncDynamicImpulseTriggerWithValueShort |
    AsyncDynamicImpulseTriggerWithValueInt |
    AsyncDynamicImpulseTriggerWithValueLong |
    AsyncDynamicImpulseTriggerWithValueFloat |
    AsyncDynamicImpulseTriggerWithValueDouble |
    AsyncDynamicImpulseTriggerWithValueDecimal |
    AsyncDynamicImpulseTriggerWithValueChar |
    AsyncDynamicImpulseTriggerWithValueString |
    AsyncDynamicImpulseTriggerWithValueUri |
    AsyncDynamicImpulseTriggerWithValueBool2 |
    AsyncDynamicImpulseTriggerWithValueByte2 |
    AsyncDynamicImpulseTriggerWithValueUshort2 |
    AsyncDynamicImpulseTriggerWithValueUint2 |
    AsyncDynamicImpulseTriggerWithValueUlong2 |
    AsyncDynamicImpulseTriggerWithValueSbyte2 |
    AsyncDynamicImpulseTriggerWithValueShort2 |
    AsyncDynamicImpulseTriggerWithValueInt2 |
    AsyncDynamicImpulseTriggerWithValueLong2 |
    AsyncDynamicImpulseTriggerWithValueFloat2 |
    AsyncDynamicImpulseTriggerWithValueDouble2 |
    AsyncDynamicImpulseTriggerWithValueBool3 |
    AsyncDynamicImpulseTriggerWithValueByte3 |
    AsyncDynamicImpulseTriggerWithValueUshort3 |
    AsyncDynamicImpulseTriggerWithValueUint3 |
    AsyncDynamicImpulseTriggerWithValueUlong3 |
    AsyncDynamicImpulseTriggerWithValueSbyte3 |
    AsyncDynamicImpulseTriggerWithValueShort3 |
    AsyncDynamicImpulseTriggerWithValueInt3 |
    AsyncDynamicImpulseTriggerWithValueLong3 |
    AsyncDynamicImpulseTriggerWithValueFloat3 |
    AsyncDynamicImpulseTriggerWithValueDouble3 |
    AsyncDynamicImpulseTriggerWithValueBool4 |
    AsyncDynamicImpulseTriggerWithValueByte4 |
    AsyncDynamicImpulseTriggerWithValueUshort4 |
    AsyncDynamicImpulseTriggerWithValueUint4 |
    AsyncDynamicImpulseTriggerWithValueUlong4 |
    AsyncDynamicImpulseTriggerWithValueSbyte4 |
    AsyncDynamicImpulseTriggerWithValueShort4 |
    AsyncDynamicImpulseTriggerWithValueInt4 |
    AsyncDynamicImpulseTriggerWithValueLong4 |
    AsyncDynamicImpulseTriggerWithValueFloat4 |
    AsyncDynamicImpulseTriggerWithValueDouble4 |
    AsyncDynamicImpulseTriggerWithValueFloat_2x2 |
    AsyncDynamicImpulseTriggerWithValueDouble_2x2 |
    AsyncDynamicImpulseTriggerWithValueFloat_3x3 |
    AsyncDynamicImpulseTriggerWithValueDouble_3x3 |
    AsyncDynamicImpulseTriggerWithValueFloat_4x4 |
    AsyncDynamicImpulseTriggerWithValueDouble_4x4 |
    AsyncDynamicImpulseTriggerWithValueFloatQ |
    AsyncDynamicImpulseTriggerWithValueDoubleQ |
    AsyncDynamicImpulseTriggerWithValueDateTime |
    AsyncDynamicImpulseTriggerWithValueTimeSpan |
    AsyncDynamicImpulseTriggerWithValueColor |
    AsyncDynamicImpulseTriggerWithValueColorX |
    AsyncDynamicImpulseTriggerWithValueShadowCastMode |
    AsyncDynamicImpulseTriggerWithValueLightType |
    AsyncDynamicImpulseTriggerWithValueSessionAccessLevel |
    AsyncDynamicImpulseTriggerWithValueKey |
    AsyncDynamicImpulseTriggerWithValueHttpStatusCode |
    AsyncDynamicImpulseTriggerWithValueHeadOutputDevice |
    AsyncDynamicImpulseTriggerWithValueReflectionProbeClear |
    AsyncDynamicImpulseTriggerWithValueReflectionProbeType |
    AsyncDynamicImpulseTriggerWithValueReflectionProbeTimeSlicingMode |
    AsyncDynamicImpulseTriggerWithValueCameraClearMode |
    AsyncDynamicImpulseTriggerWithValueCameraPositioningMode |
    AsyncDynamicImpulseTriggerWithValueCameraProjection |
    AsyncDynamicImpulseTriggerWithValueZWrite |
    AsyncDynamicImpulseTriggerWithValueZTest |
    AsyncDynamicImpulseTriggerWithValueBlend |
    AsyncDynamicImpulseTriggerWithValueBlendMode |
    AsyncDynamicImpulseTriggerWithValueCulling |
    AsyncDynamicImpulseTriggerWithValueBodyNode |
    AsyncDynamicImpulseTriggerWithValueChirality |
    AsyncDynamicImpulseTriggerWithValueDummyEnum
)