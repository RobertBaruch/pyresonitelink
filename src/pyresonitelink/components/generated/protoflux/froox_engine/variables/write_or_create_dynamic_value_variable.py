"""Generated component: WriteOrCreateDynamicValueVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class WriteOrCreateDynamicValueVariableBase(GeneratedComponent):
    """Base class for WriteOrCreateDynamicValueVariable<T> variants."""

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
class WriteOrCreateDynamicValueVariableBool(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class WriteOrCreateDynamicValueVariableByte(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class WriteOrCreateDynamicValueVariableUshort(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class WriteOrCreateDynamicValueVariableUint(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class WriteOrCreateDynamicValueVariableUlong(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class WriteOrCreateDynamicValueVariableSbyte(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class WriteOrCreateDynamicValueVariableShort(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class WriteOrCreateDynamicValueVariableInt(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class WriteOrCreateDynamicValueVariableLong(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class WriteOrCreateDynamicValueVariableFloat(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class WriteOrCreateDynamicValueVariableDouble(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class WriteOrCreateDynamicValueVariableDecimal(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class WriteOrCreateDynamicValueVariableChar(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class WriteOrCreateDynamicValueVariableString(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class WriteOrCreateDynamicValueVariableUri(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class WriteOrCreateDynamicValueVariableBool2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class WriteOrCreateDynamicValueVariableByte2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class WriteOrCreateDynamicValueVariableUshort2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class WriteOrCreateDynamicValueVariableUint2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class WriteOrCreateDynamicValueVariableUlong2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class WriteOrCreateDynamicValueVariableSbyte2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class WriteOrCreateDynamicValueVariableShort2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class WriteOrCreateDynamicValueVariableInt2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class WriteOrCreateDynamicValueVariableLong2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class WriteOrCreateDynamicValueVariableFloat2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class WriteOrCreateDynamicValueVariableDouble2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class WriteOrCreateDynamicValueVariableBool3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class WriteOrCreateDynamicValueVariableByte3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class WriteOrCreateDynamicValueVariableUshort3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class WriteOrCreateDynamicValueVariableUint3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class WriteOrCreateDynamicValueVariableUlong3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class WriteOrCreateDynamicValueVariableSbyte3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class WriteOrCreateDynamicValueVariableShort3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class WriteOrCreateDynamicValueVariableInt3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class WriteOrCreateDynamicValueVariableLong3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class WriteOrCreateDynamicValueVariableFloat3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class WriteOrCreateDynamicValueVariableDouble3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class WriteOrCreateDynamicValueVariableBool4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class WriteOrCreateDynamicValueVariableByte4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class WriteOrCreateDynamicValueVariableUshort4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class WriteOrCreateDynamicValueVariableUint4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class WriteOrCreateDynamicValueVariableUlong4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class WriteOrCreateDynamicValueVariableSbyte4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class WriteOrCreateDynamicValueVariableShort4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class WriteOrCreateDynamicValueVariableInt4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class WriteOrCreateDynamicValueVariableLong4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class WriteOrCreateDynamicValueVariableFloat4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class WriteOrCreateDynamicValueVariableDouble4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class WriteOrCreateDynamicValueVariableFloat_2x2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class WriteOrCreateDynamicValueVariableDouble_2x2(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class WriteOrCreateDynamicValueVariableFloat_3x3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class WriteOrCreateDynamicValueVariableDouble_3x3(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class WriteOrCreateDynamicValueVariableFloat_4x4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class WriteOrCreateDynamicValueVariableDouble_4x4(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class WriteOrCreateDynamicValueVariableFloatQ(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class WriteOrCreateDynamicValueVariableDoubleQ(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class WriteOrCreateDynamicValueVariableDateTime(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class WriteOrCreateDynamicValueVariableTimeSpan(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class WriteOrCreateDynamicValueVariableColor(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class WriteOrCreateDynamicValueVariableColorX(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class WriteOrCreateDynamicValueVariableShadowCastMode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class WriteOrCreateDynamicValueVariableLightType(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class WriteOrCreateDynamicValueVariableSessionAccessLevel(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class WriteOrCreateDynamicValueVariableKey(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class WriteOrCreateDynamicValueVariableHttpStatusCode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class WriteOrCreateDynamicValueVariableHeadOutputDevice(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class WriteOrCreateDynamicValueVariableReflectionProbeClear(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class WriteOrCreateDynamicValueVariableReflectionProbeType(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class WriteOrCreateDynamicValueVariableReflectionProbeTimeSlicingMode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class WriteOrCreateDynamicValueVariableCameraClearMode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class WriteOrCreateDynamicValueVariableCameraPositioningMode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class WriteOrCreateDynamicValueVariableCameraProjection(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class WriteOrCreateDynamicValueVariableZWrite(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class WriteOrCreateDynamicValueVariableZTest(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class WriteOrCreateDynamicValueVariableBlend(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class WriteOrCreateDynamicValueVariableBlendMode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class WriteOrCreateDynamicValueVariableCulling(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class WriteOrCreateDynamicValueVariableBodyNode(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class WriteOrCreateDynamicValueVariableChirality(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class WriteOrCreateDynamicValueVariableDummyEnum(WriteOrCreateDynamicValueVariableBase):
    """WriteOrCreateDynamicValueVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.WriteOrCreateDynamicValueVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "on_written": "OnWritten",
        "path": "Path",
        "target": "Target",
        "value": "Value",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_written: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any WriteOrCreateDynamicValueVariable variant
WriteOrCreateDynamicValueVariable = (
    WriteOrCreateDynamicValueVariableBool |
    WriteOrCreateDynamicValueVariableByte |
    WriteOrCreateDynamicValueVariableUshort |
    WriteOrCreateDynamicValueVariableUint |
    WriteOrCreateDynamicValueVariableUlong |
    WriteOrCreateDynamicValueVariableSbyte |
    WriteOrCreateDynamicValueVariableShort |
    WriteOrCreateDynamicValueVariableInt |
    WriteOrCreateDynamicValueVariableLong |
    WriteOrCreateDynamicValueVariableFloat |
    WriteOrCreateDynamicValueVariableDouble |
    WriteOrCreateDynamicValueVariableDecimal |
    WriteOrCreateDynamicValueVariableChar |
    WriteOrCreateDynamicValueVariableString |
    WriteOrCreateDynamicValueVariableUri |
    WriteOrCreateDynamicValueVariableBool2 |
    WriteOrCreateDynamicValueVariableByte2 |
    WriteOrCreateDynamicValueVariableUshort2 |
    WriteOrCreateDynamicValueVariableUint2 |
    WriteOrCreateDynamicValueVariableUlong2 |
    WriteOrCreateDynamicValueVariableSbyte2 |
    WriteOrCreateDynamicValueVariableShort2 |
    WriteOrCreateDynamicValueVariableInt2 |
    WriteOrCreateDynamicValueVariableLong2 |
    WriteOrCreateDynamicValueVariableFloat2 |
    WriteOrCreateDynamicValueVariableDouble2 |
    WriteOrCreateDynamicValueVariableBool3 |
    WriteOrCreateDynamicValueVariableByte3 |
    WriteOrCreateDynamicValueVariableUshort3 |
    WriteOrCreateDynamicValueVariableUint3 |
    WriteOrCreateDynamicValueVariableUlong3 |
    WriteOrCreateDynamicValueVariableSbyte3 |
    WriteOrCreateDynamicValueVariableShort3 |
    WriteOrCreateDynamicValueVariableInt3 |
    WriteOrCreateDynamicValueVariableLong3 |
    WriteOrCreateDynamicValueVariableFloat3 |
    WriteOrCreateDynamicValueVariableDouble3 |
    WriteOrCreateDynamicValueVariableBool4 |
    WriteOrCreateDynamicValueVariableByte4 |
    WriteOrCreateDynamicValueVariableUshort4 |
    WriteOrCreateDynamicValueVariableUint4 |
    WriteOrCreateDynamicValueVariableUlong4 |
    WriteOrCreateDynamicValueVariableSbyte4 |
    WriteOrCreateDynamicValueVariableShort4 |
    WriteOrCreateDynamicValueVariableInt4 |
    WriteOrCreateDynamicValueVariableLong4 |
    WriteOrCreateDynamicValueVariableFloat4 |
    WriteOrCreateDynamicValueVariableDouble4 |
    WriteOrCreateDynamicValueVariableFloat_2x2 |
    WriteOrCreateDynamicValueVariableDouble_2x2 |
    WriteOrCreateDynamicValueVariableFloat_3x3 |
    WriteOrCreateDynamicValueVariableDouble_3x3 |
    WriteOrCreateDynamicValueVariableFloat_4x4 |
    WriteOrCreateDynamicValueVariableDouble_4x4 |
    WriteOrCreateDynamicValueVariableFloatQ |
    WriteOrCreateDynamicValueVariableDoubleQ |
    WriteOrCreateDynamicValueVariableDateTime |
    WriteOrCreateDynamicValueVariableTimeSpan |
    WriteOrCreateDynamicValueVariableColor |
    WriteOrCreateDynamicValueVariableColorX |
    WriteOrCreateDynamicValueVariableShadowCastMode |
    WriteOrCreateDynamicValueVariableLightType |
    WriteOrCreateDynamicValueVariableSessionAccessLevel |
    WriteOrCreateDynamicValueVariableKey |
    WriteOrCreateDynamicValueVariableHttpStatusCode |
    WriteOrCreateDynamicValueVariableHeadOutputDevice |
    WriteOrCreateDynamicValueVariableReflectionProbeClear |
    WriteOrCreateDynamicValueVariableReflectionProbeType |
    WriteOrCreateDynamicValueVariableReflectionProbeTimeSlicingMode |
    WriteOrCreateDynamicValueVariableCameraClearMode |
    WriteOrCreateDynamicValueVariableCameraPositioningMode |
    WriteOrCreateDynamicValueVariableCameraProjection |
    WriteOrCreateDynamicValueVariableZWrite |
    WriteOrCreateDynamicValueVariableZTest |
    WriteOrCreateDynamicValueVariableBlend |
    WriteOrCreateDynamicValueVariableBlendMode |
    WriteOrCreateDynamicValueVariableCulling |
    WriteOrCreateDynamicValueVariableBodyNode |
    WriteOrCreateDynamicValueVariableChirality |
    WriteOrCreateDynamicValueVariableDummyEnum
)