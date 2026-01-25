"""Generated component: ReadDynamicValueVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class ReadDynamicValueVariableBase(GeneratedComponent):
    """Base class for ReadDynamicValueVariable<T> variants."""

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
class ReadDynamicValueVariableBool(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableByte(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUshort(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUint(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUlong(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableSbyte(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableShort(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableInt(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableLong(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDecimal(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableChar(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableString(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUri(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBool2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableByte2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUshort2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUint2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUlong2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableSbyte2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableShort2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableInt2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableLong2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBool3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableByte3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUshort3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUint3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUlong3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableSbyte3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableShort3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableInt3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableLong3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBool4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableByte4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUshort4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUint4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableUlong4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableSbyte4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableShort4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableInt4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableLong4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat_2x2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble_2x2(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat_3x3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble_3x3(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloat_4x4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDouble_4x4(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableFloatQ(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDoubleQ(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDateTime(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableTimeSpan(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableColor(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableColorX(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableShadowCastMode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableLightType(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableSessionAccessLevel(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableKey(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableHttpStatusCode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableHeadOutputDevice(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableReflectionProbeClear(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableReflectionProbeType(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableReflectionProbeTimeSlicingMode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableCameraClearMode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableCameraPositioningMode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableCameraProjection(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableZWrite(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableZTest(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBlend(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBlendMode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableCulling(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableBodyNode(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableChirality(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


@dataclass
class ReadDynamicValueVariableDummyEnum(ReadDynamicValueVariableBase):
    """ReadDynamicValueVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.ReadDynamicValueVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "path": "Path",
        "source": "Source",
    }

    path: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    source: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<FrooxEngine.Slot>


# Type alias for any ReadDynamicValueVariable variant
ReadDynamicValueVariable = (
    ReadDynamicValueVariableBool |
    ReadDynamicValueVariableByte |
    ReadDynamicValueVariableUshort |
    ReadDynamicValueVariableUint |
    ReadDynamicValueVariableUlong |
    ReadDynamicValueVariableSbyte |
    ReadDynamicValueVariableShort |
    ReadDynamicValueVariableInt |
    ReadDynamicValueVariableLong |
    ReadDynamicValueVariableFloat |
    ReadDynamicValueVariableDouble |
    ReadDynamicValueVariableDecimal |
    ReadDynamicValueVariableChar |
    ReadDynamicValueVariableString |
    ReadDynamicValueVariableUri |
    ReadDynamicValueVariableBool2 |
    ReadDynamicValueVariableByte2 |
    ReadDynamicValueVariableUshort2 |
    ReadDynamicValueVariableUint2 |
    ReadDynamicValueVariableUlong2 |
    ReadDynamicValueVariableSbyte2 |
    ReadDynamicValueVariableShort2 |
    ReadDynamicValueVariableInt2 |
    ReadDynamicValueVariableLong2 |
    ReadDynamicValueVariableFloat2 |
    ReadDynamicValueVariableDouble2 |
    ReadDynamicValueVariableBool3 |
    ReadDynamicValueVariableByte3 |
    ReadDynamicValueVariableUshort3 |
    ReadDynamicValueVariableUint3 |
    ReadDynamicValueVariableUlong3 |
    ReadDynamicValueVariableSbyte3 |
    ReadDynamicValueVariableShort3 |
    ReadDynamicValueVariableInt3 |
    ReadDynamicValueVariableLong3 |
    ReadDynamicValueVariableFloat3 |
    ReadDynamicValueVariableDouble3 |
    ReadDynamicValueVariableBool4 |
    ReadDynamicValueVariableByte4 |
    ReadDynamicValueVariableUshort4 |
    ReadDynamicValueVariableUint4 |
    ReadDynamicValueVariableUlong4 |
    ReadDynamicValueVariableSbyte4 |
    ReadDynamicValueVariableShort4 |
    ReadDynamicValueVariableInt4 |
    ReadDynamicValueVariableLong4 |
    ReadDynamicValueVariableFloat4 |
    ReadDynamicValueVariableDouble4 |
    ReadDynamicValueVariableFloat_2x2 |
    ReadDynamicValueVariableDouble_2x2 |
    ReadDynamicValueVariableFloat_3x3 |
    ReadDynamicValueVariableDouble_3x3 |
    ReadDynamicValueVariableFloat_4x4 |
    ReadDynamicValueVariableDouble_4x4 |
    ReadDynamicValueVariableFloatQ |
    ReadDynamicValueVariableDoubleQ |
    ReadDynamicValueVariableDateTime |
    ReadDynamicValueVariableTimeSpan |
    ReadDynamicValueVariableColor |
    ReadDynamicValueVariableColorX |
    ReadDynamicValueVariableShadowCastMode |
    ReadDynamicValueVariableLightType |
    ReadDynamicValueVariableSessionAccessLevel |
    ReadDynamicValueVariableKey |
    ReadDynamicValueVariableHttpStatusCode |
    ReadDynamicValueVariableHeadOutputDevice |
    ReadDynamicValueVariableReflectionProbeClear |
    ReadDynamicValueVariableReflectionProbeType |
    ReadDynamicValueVariableReflectionProbeTimeSlicingMode |
    ReadDynamicValueVariableCameraClearMode |
    ReadDynamicValueVariableCameraPositioningMode |
    ReadDynamicValueVariableCameraProjection |
    ReadDynamicValueVariableZWrite |
    ReadDynamicValueVariableZTest |
    ReadDynamicValueVariableBlend |
    ReadDynamicValueVariableBlendMode |
    ReadDynamicValueVariableCulling |
    ReadDynamicValueVariableBodyNode |
    ReadDynamicValueVariableChirality |
    ReadDynamicValueVariableDummyEnum
)