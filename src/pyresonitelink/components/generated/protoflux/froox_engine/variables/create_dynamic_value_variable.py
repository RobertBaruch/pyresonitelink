"""Generated component: CreateDynamicValueVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class CreateDynamicValueVariableBase(GeneratedComponent):
    """Base class for CreateDynamicValueVariable<T> variants."""

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
class CreateDynamicValueVariableBool(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableByte(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUshort(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUint(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUlong(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableSbyte(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableShort(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableInt(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableLong(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDecimal(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableChar(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableString(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUri(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBool2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableByte2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUshort2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUint2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUlong2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableSbyte2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableShort2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableInt2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableLong2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBool3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableByte3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUshort3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUint3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUlong3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableSbyte3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableShort3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableInt3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableLong3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBool4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableByte4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUshort4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUint4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableUlong4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableSbyte4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableShort4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableInt4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableLong4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat_2x2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble_2x2(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat_3x3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble_3x3(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloat_4x4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDouble_4x4(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableFloatQ(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDoubleQ(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDateTime(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableTimeSpan(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableColor(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableColorX(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableShadowCastMode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableLightType(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableSessionAccessLevel(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableKey(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableHttpStatusCode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableHeadOutputDevice(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableReflectionProbeClear(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableReflectionProbeType(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableReflectionProbeTimeSlicingMode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableCameraClearMode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableCameraPositioningMode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableCameraProjection(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableZWrite(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableZTest(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBlend(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBlendMode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableCulling(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableBodyNode(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableChirality(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class CreateDynamicValueVariableDummyEnum(CreateDynamicValueVariableBase):
    """CreateDynamicValueVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.CreateDynamicValueVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "create_directly_on_target": "CreateDirectlyOnTarget",
        "create_non_persistent": "CreateNonPersistent",
        "initial_value": "InitialValue",
        "on_already_exists": "OnAlreadyExists",
        "on_created": "OnCreated",
        "on_failed": "OnFailed",
        "on_not_found": "OnNotFound",
        "path": "Path",
        "target": "Target",
    }

    create_directly_on_target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    create_non_persistent: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    initial_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    on_already_exists: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_created: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_failed: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    on_not_found: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeOperation
    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    target: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


# Type alias for any CreateDynamicValueVariable variant
CreateDynamicValueVariable = (
    CreateDynamicValueVariableBool |
    CreateDynamicValueVariableByte |
    CreateDynamicValueVariableUshort |
    CreateDynamicValueVariableUint |
    CreateDynamicValueVariableUlong |
    CreateDynamicValueVariableSbyte |
    CreateDynamicValueVariableShort |
    CreateDynamicValueVariableInt |
    CreateDynamicValueVariableLong |
    CreateDynamicValueVariableFloat |
    CreateDynamicValueVariableDouble |
    CreateDynamicValueVariableDecimal |
    CreateDynamicValueVariableChar |
    CreateDynamicValueVariableString |
    CreateDynamicValueVariableUri |
    CreateDynamicValueVariableBool2 |
    CreateDynamicValueVariableByte2 |
    CreateDynamicValueVariableUshort2 |
    CreateDynamicValueVariableUint2 |
    CreateDynamicValueVariableUlong2 |
    CreateDynamicValueVariableSbyte2 |
    CreateDynamicValueVariableShort2 |
    CreateDynamicValueVariableInt2 |
    CreateDynamicValueVariableLong2 |
    CreateDynamicValueVariableFloat2 |
    CreateDynamicValueVariableDouble2 |
    CreateDynamicValueVariableBool3 |
    CreateDynamicValueVariableByte3 |
    CreateDynamicValueVariableUshort3 |
    CreateDynamicValueVariableUint3 |
    CreateDynamicValueVariableUlong3 |
    CreateDynamicValueVariableSbyte3 |
    CreateDynamicValueVariableShort3 |
    CreateDynamicValueVariableInt3 |
    CreateDynamicValueVariableLong3 |
    CreateDynamicValueVariableFloat3 |
    CreateDynamicValueVariableDouble3 |
    CreateDynamicValueVariableBool4 |
    CreateDynamicValueVariableByte4 |
    CreateDynamicValueVariableUshort4 |
    CreateDynamicValueVariableUint4 |
    CreateDynamicValueVariableUlong4 |
    CreateDynamicValueVariableSbyte4 |
    CreateDynamicValueVariableShort4 |
    CreateDynamicValueVariableInt4 |
    CreateDynamicValueVariableLong4 |
    CreateDynamicValueVariableFloat4 |
    CreateDynamicValueVariableDouble4 |
    CreateDynamicValueVariableFloat_2x2 |
    CreateDynamicValueVariableDouble_2x2 |
    CreateDynamicValueVariableFloat_3x3 |
    CreateDynamicValueVariableDouble_3x3 |
    CreateDynamicValueVariableFloat_4x4 |
    CreateDynamicValueVariableDouble_4x4 |
    CreateDynamicValueVariableFloatQ |
    CreateDynamicValueVariableDoubleQ |
    CreateDynamicValueVariableDateTime |
    CreateDynamicValueVariableTimeSpan |
    CreateDynamicValueVariableColor |
    CreateDynamicValueVariableColorX |
    CreateDynamicValueVariableShadowCastMode |
    CreateDynamicValueVariableLightType |
    CreateDynamicValueVariableSessionAccessLevel |
    CreateDynamicValueVariableKey |
    CreateDynamicValueVariableHttpStatusCode |
    CreateDynamicValueVariableHeadOutputDevice |
    CreateDynamicValueVariableReflectionProbeClear |
    CreateDynamicValueVariableReflectionProbeType |
    CreateDynamicValueVariableReflectionProbeTimeSlicingMode |
    CreateDynamicValueVariableCameraClearMode |
    CreateDynamicValueVariableCameraPositioningMode |
    CreateDynamicValueVariableCameraProjection |
    CreateDynamicValueVariableZWrite |
    CreateDynamicValueVariableZTest |
    CreateDynamicValueVariableBlend |
    CreateDynamicValueVariableBlendMode |
    CreateDynamicValueVariableCulling |
    CreateDynamicValueVariableBodyNode |
    CreateDynamicValueVariableChirality |
    CreateDynamicValueVariableDummyEnum
)