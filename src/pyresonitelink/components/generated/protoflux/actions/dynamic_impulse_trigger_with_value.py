"""Generated component: DynamicImpulseTriggerWithValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DynamicImpulseTriggerWithValueBase(GeneratedComponent):
    """Base class for DynamicImpulseTriggerWithValue<T> variants."""

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
class DynamicImpulseTriggerWithValueBool(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<bool>"

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
class DynamicImpulseTriggerWithValueByte(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<byte>"

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
class DynamicImpulseTriggerWithValueUshort(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ushort>"

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
class DynamicImpulseTriggerWithValueUint(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<uint>"

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
class DynamicImpulseTriggerWithValueUlong(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ulong>"

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
class DynamicImpulseTriggerWithValueSbyte(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<sbyte>"

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
class DynamicImpulseTriggerWithValueShort(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<short>"

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
class DynamicImpulseTriggerWithValueInt(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<int>"

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
class DynamicImpulseTriggerWithValueLong(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<long>"

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
class DynamicImpulseTriggerWithValueFloat(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float>"

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
class DynamicImpulseTriggerWithValueDouble(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double>"

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
class DynamicImpulseTriggerWithValueDecimal(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<decimal>"

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
class DynamicImpulseTriggerWithValueChar(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<char>"

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
class DynamicImpulseTriggerWithValueString(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<string>"

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
class DynamicImpulseTriggerWithValueUri(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<Uri>"

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
class DynamicImpulseTriggerWithValueBool2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<bool2>"

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
class DynamicImpulseTriggerWithValueByte2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<byte2>"

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
class DynamicImpulseTriggerWithValueUshort2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ushort2>"

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
class DynamicImpulseTriggerWithValueUint2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<uint2>"

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
class DynamicImpulseTriggerWithValueUlong2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ulong2>"

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
class DynamicImpulseTriggerWithValueSbyte2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<sbyte2>"

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
class DynamicImpulseTriggerWithValueShort2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<short2>"

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
class DynamicImpulseTriggerWithValueInt2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<int2>"

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
class DynamicImpulseTriggerWithValueLong2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<long2>"

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
class DynamicImpulseTriggerWithValueFloat2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float2>"

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
class DynamicImpulseTriggerWithValueDouble2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double2>"

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
class DynamicImpulseTriggerWithValueBool3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<bool3>"

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
class DynamicImpulseTriggerWithValueByte3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<byte3>"

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
class DynamicImpulseTriggerWithValueUshort3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ushort3>"

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
class DynamicImpulseTriggerWithValueUint3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<uint3>"

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
class DynamicImpulseTriggerWithValueUlong3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ulong3>"

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
class DynamicImpulseTriggerWithValueSbyte3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<sbyte3>"

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
class DynamicImpulseTriggerWithValueShort3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<short3>"

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
class DynamicImpulseTriggerWithValueInt3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<int3>"

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
class DynamicImpulseTriggerWithValueLong3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<long3>"

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
class DynamicImpulseTriggerWithValueFloat3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float3>"

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
class DynamicImpulseTriggerWithValueDouble3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double3>"

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
class DynamicImpulseTriggerWithValueBool4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<bool4>"

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
class DynamicImpulseTriggerWithValueByte4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<byte4>"

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
class DynamicImpulseTriggerWithValueUshort4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ushort4>"

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
class DynamicImpulseTriggerWithValueUint4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<uint4>"

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
class DynamicImpulseTriggerWithValueUlong4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<ulong4>"

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
class DynamicImpulseTriggerWithValueSbyte4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<sbyte4>"

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
class DynamicImpulseTriggerWithValueShort4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<short4>"

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
class DynamicImpulseTriggerWithValueInt4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<int4>"

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
class DynamicImpulseTriggerWithValueLong4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<long4>"

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
class DynamicImpulseTriggerWithValueFloat4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float4>"

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
class DynamicImpulseTriggerWithValueDouble4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double4>"

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
class DynamicImpulseTriggerWithValueFloat_2x2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float2x2>"

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
class DynamicImpulseTriggerWithValueDouble_2x2(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double2x2>"

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
class DynamicImpulseTriggerWithValueFloat_3x3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float3x3>"

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
class DynamicImpulseTriggerWithValueDouble_3x3(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double3x3>"

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
class DynamicImpulseTriggerWithValueFloat_4x4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<float4x4>"

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
class DynamicImpulseTriggerWithValueDouble_4x4(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<double4x4>"

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
class DynamicImpulseTriggerWithValueFloatQ(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<floatQ>"

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
class DynamicImpulseTriggerWithValueDoubleQ(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<doubleQ>"

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
class DynamicImpulseTriggerWithValueDateTime(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[System.Private.CoreLib]System.DateTime>"

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
class DynamicImpulseTriggerWithValueTimeSpan(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[System.Private.CoreLib]System.TimeSpan>"

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
class DynamicImpulseTriggerWithValueColor(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<color>"

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
class DynamicImpulseTriggerWithValueColorX(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<colorX>"

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
class DynamicImpulseTriggerWithValueShadowCastMode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

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
class DynamicImpulseTriggerWithValueLightType(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.LightType>"

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
class DynamicImpulseTriggerWithValueSessionAccessLevel(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

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
class DynamicImpulseTriggerWithValueKey(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.Key>"

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
class DynamicImpulseTriggerWithValueHttpStatusCode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

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
class DynamicImpulseTriggerWithValueHeadOutputDevice(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

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
class DynamicImpulseTriggerWithValueReflectionProbeClear(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

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
class DynamicImpulseTriggerWithValueReflectionProbeType(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

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
class DynamicImpulseTriggerWithValueReflectionProbeTimeSlicingMode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

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
class DynamicImpulseTriggerWithValueCameraClearMode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

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
class DynamicImpulseTriggerWithValueCameraPositioningMode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

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
class DynamicImpulseTriggerWithValueCameraProjection(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

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
class DynamicImpulseTriggerWithValueZWrite(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.ZWrite>"

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
class DynamicImpulseTriggerWithValueZTest(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.ZTest>"

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
class DynamicImpulseTriggerWithValueBlend(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.Blend>"

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
class DynamicImpulseTriggerWithValueBlendMode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.BlendMode>"

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
class DynamicImpulseTriggerWithValueCulling(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[FrooxEngine]FrooxEngine.Culling>"

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
class DynamicImpulseTriggerWithValueBodyNode(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

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
class DynamicImpulseTriggerWithValueChirality(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<[Renderite.Shared]Renderite.Shared.Chirality>"

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
class DynamicImpulseTriggerWithValueDummyEnum(DynamicImpulseTriggerWithValueBase):
    """DynamicImpulseTriggerWithValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.DynamicImpulseTriggerWithValue<DummyEnum>"

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


# Type alias for any DynamicImpulseTriggerWithValue variant
DynamicImpulseTriggerWithValue = (
    DynamicImpulseTriggerWithValueBool |
    DynamicImpulseTriggerWithValueByte |
    DynamicImpulseTriggerWithValueUshort |
    DynamicImpulseTriggerWithValueUint |
    DynamicImpulseTriggerWithValueUlong |
    DynamicImpulseTriggerWithValueSbyte |
    DynamicImpulseTriggerWithValueShort |
    DynamicImpulseTriggerWithValueInt |
    DynamicImpulseTriggerWithValueLong |
    DynamicImpulseTriggerWithValueFloat |
    DynamicImpulseTriggerWithValueDouble |
    DynamicImpulseTriggerWithValueDecimal |
    DynamicImpulseTriggerWithValueChar |
    DynamicImpulseTriggerWithValueString |
    DynamicImpulseTriggerWithValueUri |
    DynamicImpulseTriggerWithValueBool2 |
    DynamicImpulseTriggerWithValueByte2 |
    DynamicImpulseTriggerWithValueUshort2 |
    DynamicImpulseTriggerWithValueUint2 |
    DynamicImpulseTriggerWithValueUlong2 |
    DynamicImpulseTriggerWithValueSbyte2 |
    DynamicImpulseTriggerWithValueShort2 |
    DynamicImpulseTriggerWithValueInt2 |
    DynamicImpulseTriggerWithValueLong2 |
    DynamicImpulseTriggerWithValueFloat2 |
    DynamicImpulseTriggerWithValueDouble2 |
    DynamicImpulseTriggerWithValueBool3 |
    DynamicImpulseTriggerWithValueByte3 |
    DynamicImpulseTriggerWithValueUshort3 |
    DynamicImpulseTriggerWithValueUint3 |
    DynamicImpulseTriggerWithValueUlong3 |
    DynamicImpulseTriggerWithValueSbyte3 |
    DynamicImpulseTriggerWithValueShort3 |
    DynamicImpulseTriggerWithValueInt3 |
    DynamicImpulseTriggerWithValueLong3 |
    DynamicImpulseTriggerWithValueFloat3 |
    DynamicImpulseTriggerWithValueDouble3 |
    DynamicImpulseTriggerWithValueBool4 |
    DynamicImpulseTriggerWithValueByte4 |
    DynamicImpulseTriggerWithValueUshort4 |
    DynamicImpulseTriggerWithValueUint4 |
    DynamicImpulseTriggerWithValueUlong4 |
    DynamicImpulseTriggerWithValueSbyte4 |
    DynamicImpulseTriggerWithValueShort4 |
    DynamicImpulseTriggerWithValueInt4 |
    DynamicImpulseTriggerWithValueLong4 |
    DynamicImpulseTriggerWithValueFloat4 |
    DynamicImpulseTriggerWithValueDouble4 |
    DynamicImpulseTriggerWithValueFloat_2x2 |
    DynamicImpulseTriggerWithValueDouble_2x2 |
    DynamicImpulseTriggerWithValueFloat_3x3 |
    DynamicImpulseTriggerWithValueDouble_3x3 |
    DynamicImpulseTriggerWithValueFloat_4x4 |
    DynamicImpulseTriggerWithValueDouble_4x4 |
    DynamicImpulseTriggerWithValueFloatQ |
    DynamicImpulseTriggerWithValueDoubleQ |
    DynamicImpulseTriggerWithValueDateTime |
    DynamicImpulseTriggerWithValueTimeSpan |
    DynamicImpulseTriggerWithValueColor |
    DynamicImpulseTriggerWithValueColorX |
    DynamicImpulseTriggerWithValueShadowCastMode |
    DynamicImpulseTriggerWithValueLightType |
    DynamicImpulseTriggerWithValueSessionAccessLevel |
    DynamicImpulseTriggerWithValueKey |
    DynamicImpulseTriggerWithValueHttpStatusCode |
    DynamicImpulseTriggerWithValueHeadOutputDevice |
    DynamicImpulseTriggerWithValueReflectionProbeClear |
    DynamicImpulseTriggerWithValueReflectionProbeType |
    DynamicImpulseTriggerWithValueReflectionProbeTimeSlicingMode |
    DynamicImpulseTriggerWithValueCameraClearMode |
    DynamicImpulseTriggerWithValueCameraPositioningMode |
    DynamicImpulseTriggerWithValueCameraProjection |
    DynamicImpulseTriggerWithValueZWrite |
    DynamicImpulseTriggerWithValueZTest |
    DynamicImpulseTriggerWithValueBlend |
    DynamicImpulseTriggerWithValueBlendMode |
    DynamicImpulseTriggerWithValueCulling |
    DynamicImpulseTriggerWithValueBodyNode |
    DynamicImpulseTriggerWithValueChirality |
    DynamicImpulseTriggerWithValueDummyEnum
)