"""Generated component: SampleMinMaxSpatialVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleMinMaxSpatialVariableBase(GeneratedComponent):
    """Base class for SampleMinMaxSpatialVariable<T> variants."""

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
class SampleMinMaxSpatialVariableBool(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableByte(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUshort(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUint(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUlong(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableSbyte(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableShort(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableInt(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableLong(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDecimal(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableChar(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableString(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUri(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBool2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableByte2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUshort2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUint2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUlong2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableSbyte2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableShort2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableInt2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableLong2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBool3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableByte3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUshort3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUint3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUlong3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableSbyte3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableShort3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableInt3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableLong3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBool4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableByte4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUshort4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUint4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableUlong4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableSbyte4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableShort4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableInt4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableLong4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat_2x2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble_2x2(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat_3x3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble_3x3(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloat_4x4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDouble_4x4(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableFloatQ(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDoubleQ(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDateTime(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableTimeSpan(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableColor(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableColorX(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableShadowCastMode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableLightType(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableSessionAccessLevel(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableKey(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableHttpStatusCode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableHeadOutputDevice(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableReflectionProbeClear(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableReflectionProbeType(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableReflectionProbeTimeSlicingMode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableCameraClearMode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableCameraPositioningMode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableCameraProjection(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableZWrite(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableZTest(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBlend(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBlendMode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableCulling(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableBodyNode(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableChirality(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleMinMaxSpatialVariableDummyEnum(SampleMinMaxSpatialVariableBase):
    """SampleMinMaxSpatialVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleMinMaxSpatialVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "name": "Name",
        "point": "Point",
    }

    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


# Type alias for any SampleMinMaxSpatialVariable variant
SampleMinMaxSpatialVariable = (
    SampleMinMaxSpatialVariableBool |
    SampleMinMaxSpatialVariableByte |
    SampleMinMaxSpatialVariableUshort |
    SampleMinMaxSpatialVariableUint |
    SampleMinMaxSpatialVariableUlong |
    SampleMinMaxSpatialVariableSbyte |
    SampleMinMaxSpatialVariableShort |
    SampleMinMaxSpatialVariableInt |
    SampleMinMaxSpatialVariableLong |
    SampleMinMaxSpatialVariableFloat |
    SampleMinMaxSpatialVariableDouble |
    SampleMinMaxSpatialVariableDecimal |
    SampleMinMaxSpatialVariableChar |
    SampleMinMaxSpatialVariableString |
    SampleMinMaxSpatialVariableUri |
    SampleMinMaxSpatialVariableBool2 |
    SampleMinMaxSpatialVariableByte2 |
    SampleMinMaxSpatialVariableUshort2 |
    SampleMinMaxSpatialVariableUint2 |
    SampleMinMaxSpatialVariableUlong2 |
    SampleMinMaxSpatialVariableSbyte2 |
    SampleMinMaxSpatialVariableShort2 |
    SampleMinMaxSpatialVariableInt2 |
    SampleMinMaxSpatialVariableLong2 |
    SampleMinMaxSpatialVariableFloat2 |
    SampleMinMaxSpatialVariableDouble2 |
    SampleMinMaxSpatialVariableBool3 |
    SampleMinMaxSpatialVariableByte3 |
    SampleMinMaxSpatialVariableUshort3 |
    SampleMinMaxSpatialVariableUint3 |
    SampleMinMaxSpatialVariableUlong3 |
    SampleMinMaxSpatialVariableSbyte3 |
    SampleMinMaxSpatialVariableShort3 |
    SampleMinMaxSpatialVariableInt3 |
    SampleMinMaxSpatialVariableLong3 |
    SampleMinMaxSpatialVariableFloat3 |
    SampleMinMaxSpatialVariableDouble3 |
    SampleMinMaxSpatialVariableBool4 |
    SampleMinMaxSpatialVariableByte4 |
    SampleMinMaxSpatialVariableUshort4 |
    SampleMinMaxSpatialVariableUint4 |
    SampleMinMaxSpatialVariableUlong4 |
    SampleMinMaxSpatialVariableSbyte4 |
    SampleMinMaxSpatialVariableShort4 |
    SampleMinMaxSpatialVariableInt4 |
    SampleMinMaxSpatialVariableLong4 |
    SampleMinMaxSpatialVariableFloat4 |
    SampleMinMaxSpatialVariableDouble4 |
    SampleMinMaxSpatialVariableFloat_2x2 |
    SampleMinMaxSpatialVariableDouble_2x2 |
    SampleMinMaxSpatialVariableFloat_3x3 |
    SampleMinMaxSpatialVariableDouble_3x3 |
    SampleMinMaxSpatialVariableFloat_4x4 |
    SampleMinMaxSpatialVariableDouble_4x4 |
    SampleMinMaxSpatialVariableFloatQ |
    SampleMinMaxSpatialVariableDoubleQ |
    SampleMinMaxSpatialVariableDateTime |
    SampleMinMaxSpatialVariableTimeSpan |
    SampleMinMaxSpatialVariableColor |
    SampleMinMaxSpatialVariableColorX |
    SampleMinMaxSpatialVariableShadowCastMode |
    SampleMinMaxSpatialVariableLightType |
    SampleMinMaxSpatialVariableSessionAccessLevel |
    SampleMinMaxSpatialVariableKey |
    SampleMinMaxSpatialVariableHttpStatusCode |
    SampleMinMaxSpatialVariableHeadOutputDevice |
    SampleMinMaxSpatialVariableReflectionProbeClear |
    SampleMinMaxSpatialVariableReflectionProbeType |
    SampleMinMaxSpatialVariableReflectionProbeTimeSlicingMode |
    SampleMinMaxSpatialVariableCameraClearMode |
    SampleMinMaxSpatialVariableCameraPositioningMode |
    SampleMinMaxSpatialVariableCameraProjection |
    SampleMinMaxSpatialVariableZWrite |
    SampleMinMaxSpatialVariableZTest |
    SampleMinMaxSpatialVariableBlend |
    SampleMinMaxSpatialVariableBlendMode |
    SampleMinMaxSpatialVariableCulling |
    SampleMinMaxSpatialVariableBodyNode |
    SampleMinMaxSpatialVariableChirality |
    SampleMinMaxSpatialVariableDummyEnum
)