"""Generated component: SampleValueSpatialVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleValueSpatialVariableBase(GeneratedComponent):
    """Base class for SampleValueSpatialVariable<T> variants."""

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
class SampleValueSpatialVariableBool(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableByte(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUshort(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUint(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUlong(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableSbyte(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableShort(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableInt(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableLong(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDecimal(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableChar(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableString(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUri(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBool2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableByte2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUshort2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUint2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUlong2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableSbyte2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableShort2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableInt2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableLong2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBool3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableByte3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUshort3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUint3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUlong3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableSbyte3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableShort3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableInt3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableLong3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBool4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableByte4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUshort4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUint4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableUlong4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableSbyte4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableShort4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableInt4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableLong4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat_2x2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble_2x2(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat_3x3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble_3x3(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloat_4x4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDouble_4x4(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableFloatQ(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDoubleQ(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDateTime(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableTimeSpan(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableColor(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableColorX(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableShadowCastMode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableLightType(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableSessionAccessLevel(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableKey(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableHttpStatusCode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableHeadOutputDevice(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableReflectionProbeClear(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableReflectionProbeType(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableReflectionProbeTimeSlicingMode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableCameraClearMode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableCameraPositioningMode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableCameraProjection(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableZWrite(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableZTest(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBlend(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBlendMode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableCulling(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableBodyNode(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableChirality(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleValueSpatialVariableDummyEnum(SampleValueSpatialVariableBase):
    """SampleValueSpatialVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleValueSpatialVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "default_value": "DefaultValue",
        "name": "Name",
        "point": "Point",
    }

    default_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


# Type alias for any SampleValueSpatialVariable variant
SampleValueSpatialVariable = (
    SampleValueSpatialVariableBool |
    SampleValueSpatialVariableByte |
    SampleValueSpatialVariableUshort |
    SampleValueSpatialVariableUint |
    SampleValueSpatialVariableUlong |
    SampleValueSpatialVariableSbyte |
    SampleValueSpatialVariableShort |
    SampleValueSpatialVariableInt |
    SampleValueSpatialVariableLong |
    SampleValueSpatialVariableFloat |
    SampleValueSpatialVariableDouble |
    SampleValueSpatialVariableDecimal |
    SampleValueSpatialVariableChar |
    SampleValueSpatialVariableString |
    SampleValueSpatialVariableUri |
    SampleValueSpatialVariableBool2 |
    SampleValueSpatialVariableByte2 |
    SampleValueSpatialVariableUshort2 |
    SampleValueSpatialVariableUint2 |
    SampleValueSpatialVariableUlong2 |
    SampleValueSpatialVariableSbyte2 |
    SampleValueSpatialVariableShort2 |
    SampleValueSpatialVariableInt2 |
    SampleValueSpatialVariableLong2 |
    SampleValueSpatialVariableFloat2 |
    SampleValueSpatialVariableDouble2 |
    SampleValueSpatialVariableBool3 |
    SampleValueSpatialVariableByte3 |
    SampleValueSpatialVariableUshort3 |
    SampleValueSpatialVariableUint3 |
    SampleValueSpatialVariableUlong3 |
    SampleValueSpatialVariableSbyte3 |
    SampleValueSpatialVariableShort3 |
    SampleValueSpatialVariableInt3 |
    SampleValueSpatialVariableLong3 |
    SampleValueSpatialVariableFloat3 |
    SampleValueSpatialVariableDouble3 |
    SampleValueSpatialVariableBool4 |
    SampleValueSpatialVariableByte4 |
    SampleValueSpatialVariableUshort4 |
    SampleValueSpatialVariableUint4 |
    SampleValueSpatialVariableUlong4 |
    SampleValueSpatialVariableSbyte4 |
    SampleValueSpatialVariableShort4 |
    SampleValueSpatialVariableInt4 |
    SampleValueSpatialVariableLong4 |
    SampleValueSpatialVariableFloat4 |
    SampleValueSpatialVariableDouble4 |
    SampleValueSpatialVariableFloat_2x2 |
    SampleValueSpatialVariableDouble_2x2 |
    SampleValueSpatialVariableFloat_3x3 |
    SampleValueSpatialVariableDouble_3x3 |
    SampleValueSpatialVariableFloat_4x4 |
    SampleValueSpatialVariableDouble_4x4 |
    SampleValueSpatialVariableFloatQ |
    SampleValueSpatialVariableDoubleQ |
    SampleValueSpatialVariableDateTime |
    SampleValueSpatialVariableTimeSpan |
    SampleValueSpatialVariableColor |
    SampleValueSpatialVariableColorX |
    SampleValueSpatialVariableShadowCastMode |
    SampleValueSpatialVariableLightType |
    SampleValueSpatialVariableSessionAccessLevel |
    SampleValueSpatialVariableKey |
    SampleValueSpatialVariableHttpStatusCode |
    SampleValueSpatialVariableHeadOutputDevice |
    SampleValueSpatialVariableReflectionProbeClear |
    SampleValueSpatialVariableReflectionProbeType |
    SampleValueSpatialVariableReflectionProbeTimeSlicingMode |
    SampleValueSpatialVariableCameraClearMode |
    SampleValueSpatialVariableCameraPositioningMode |
    SampleValueSpatialVariableCameraProjection |
    SampleValueSpatialVariableZWrite |
    SampleValueSpatialVariableZTest |
    SampleValueSpatialVariableBlend |
    SampleValueSpatialVariableBlendMode |
    SampleValueSpatialVariableCulling |
    SampleValueSpatialVariableBodyNode |
    SampleValueSpatialVariableChirality |
    SampleValueSpatialVariableDummyEnum
)