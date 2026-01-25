"""Generated component: DynamicVariableValueInputWithEvents.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DynamicVariableValueInputWithEventsBase(GeneratedComponent):
    """Base class for DynamicVariableValueInputWithEvents<T> variants."""

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
class DynamicVariableValueInputWithEventsBool(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsByte(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUshort(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUint(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUlong(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsSbyte(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsShort(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsInt(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsLong(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDecimal(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsChar(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsString(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUri(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBool2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsByte2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUshort2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUint2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUlong2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsSbyte2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsShort2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsInt2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsLong2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBool3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsByte3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUshort3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUint3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUlong3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsSbyte3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsShort3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsInt3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsLong3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBool4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsByte4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUshort4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUint4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsUlong4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsSbyte4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsShort4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsInt4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsLong4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat_2x2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble_2x2(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat_3x3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble_3x3(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloat_4x4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDouble_4x4(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsFloatQ(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDoubleQ(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDateTime(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsTimeSpan(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsColor(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsColorX(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsShadowCastMode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsLightType(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsSessionAccessLevel(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsKey(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsHttpStatusCode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsHeadOutputDevice(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsReflectionProbeClear(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsReflectionProbeType(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsReflectionProbeTimeSlicingMode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsCameraClearMode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsCameraPositioningMode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsCameraProjection(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsZWrite(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsZTest(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBlend(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBlendMode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsCulling(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsBodyNode(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsChirality(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputWithEventsDummyEnum(DynamicVariableValueInputWithEventsBase):
    """DynamicVariableValueInputWithEvents<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInputWithEvents<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "detecting_user": "DetectingUser",
        "on_space_linked": "OnSpaceLinked",
        "on_space_unlinked": "OnSpaceUnlinked",
        "variable_name": "VariableName",
    }

    detecting_user: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.User>
    on_space_linked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    on_space_unlinked: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


# Type alias for any DynamicVariableValueInputWithEvents variant
DynamicVariableValueInputWithEvents = (
    DynamicVariableValueInputWithEventsBool |
    DynamicVariableValueInputWithEventsByte |
    DynamicVariableValueInputWithEventsUshort |
    DynamicVariableValueInputWithEventsUint |
    DynamicVariableValueInputWithEventsUlong |
    DynamicVariableValueInputWithEventsSbyte |
    DynamicVariableValueInputWithEventsShort |
    DynamicVariableValueInputWithEventsInt |
    DynamicVariableValueInputWithEventsLong |
    DynamicVariableValueInputWithEventsFloat |
    DynamicVariableValueInputWithEventsDouble |
    DynamicVariableValueInputWithEventsDecimal |
    DynamicVariableValueInputWithEventsChar |
    DynamicVariableValueInputWithEventsString |
    DynamicVariableValueInputWithEventsUri |
    DynamicVariableValueInputWithEventsBool2 |
    DynamicVariableValueInputWithEventsByte2 |
    DynamicVariableValueInputWithEventsUshort2 |
    DynamicVariableValueInputWithEventsUint2 |
    DynamicVariableValueInputWithEventsUlong2 |
    DynamicVariableValueInputWithEventsSbyte2 |
    DynamicVariableValueInputWithEventsShort2 |
    DynamicVariableValueInputWithEventsInt2 |
    DynamicVariableValueInputWithEventsLong2 |
    DynamicVariableValueInputWithEventsFloat2 |
    DynamicVariableValueInputWithEventsDouble2 |
    DynamicVariableValueInputWithEventsBool3 |
    DynamicVariableValueInputWithEventsByte3 |
    DynamicVariableValueInputWithEventsUshort3 |
    DynamicVariableValueInputWithEventsUint3 |
    DynamicVariableValueInputWithEventsUlong3 |
    DynamicVariableValueInputWithEventsSbyte3 |
    DynamicVariableValueInputWithEventsShort3 |
    DynamicVariableValueInputWithEventsInt3 |
    DynamicVariableValueInputWithEventsLong3 |
    DynamicVariableValueInputWithEventsFloat3 |
    DynamicVariableValueInputWithEventsDouble3 |
    DynamicVariableValueInputWithEventsBool4 |
    DynamicVariableValueInputWithEventsByte4 |
    DynamicVariableValueInputWithEventsUshort4 |
    DynamicVariableValueInputWithEventsUint4 |
    DynamicVariableValueInputWithEventsUlong4 |
    DynamicVariableValueInputWithEventsSbyte4 |
    DynamicVariableValueInputWithEventsShort4 |
    DynamicVariableValueInputWithEventsInt4 |
    DynamicVariableValueInputWithEventsLong4 |
    DynamicVariableValueInputWithEventsFloat4 |
    DynamicVariableValueInputWithEventsDouble4 |
    DynamicVariableValueInputWithEventsFloat_2x2 |
    DynamicVariableValueInputWithEventsDouble_2x2 |
    DynamicVariableValueInputWithEventsFloat_3x3 |
    DynamicVariableValueInputWithEventsDouble_3x3 |
    DynamicVariableValueInputWithEventsFloat_4x4 |
    DynamicVariableValueInputWithEventsDouble_4x4 |
    DynamicVariableValueInputWithEventsFloatQ |
    DynamicVariableValueInputWithEventsDoubleQ |
    DynamicVariableValueInputWithEventsDateTime |
    DynamicVariableValueInputWithEventsTimeSpan |
    DynamicVariableValueInputWithEventsColor |
    DynamicVariableValueInputWithEventsColorX |
    DynamicVariableValueInputWithEventsShadowCastMode |
    DynamicVariableValueInputWithEventsLightType |
    DynamicVariableValueInputWithEventsSessionAccessLevel |
    DynamicVariableValueInputWithEventsKey |
    DynamicVariableValueInputWithEventsHttpStatusCode |
    DynamicVariableValueInputWithEventsHeadOutputDevice |
    DynamicVariableValueInputWithEventsReflectionProbeClear |
    DynamicVariableValueInputWithEventsReflectionProbeType |
    DynamicVariableValueInputWithEventsReflectionProbeTimeSlicingMode |
    DynamicVariableValueInputWithEventsCameraClearMode |
    DynamicVariableValueInputWithEventsCameraPositioningMode |
    DynamicVariableValueInputWithEventsCameraProjection |
    DynamicVariableValueInputWithEventsZWrite |
    DynamicVariableValueInputWithEventsZTest |
    DynamicVariableValueInputWithEventsBlend |
    DynamicVariableValueInputWithEventsBlendMode |
    DynamicVariableValueInputWithEventsCulling |
    DynamicVariableValueInputWithEventsBodyNode |
    DynamicVariableValueInputWithEventsChirality |
    DynamicVariableValueInputWithEventsDummyEnum
)