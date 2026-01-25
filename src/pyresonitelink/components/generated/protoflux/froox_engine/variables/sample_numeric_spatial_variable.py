"""Generated component: SampleNumericSpatialVariable.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleNumericSpatialVariableBase(GeneratedComponent):
    """Base class for SampleNumericSpatialVariable<T> variants."""

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
class SampleNumericSpatialVariableBool(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableByte(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUshort(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUint(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUlong(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableSbyte(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableShort(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableInt(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableLong(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDecimal(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableChar(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableString(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUri(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBool2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableByte2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUshort2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUint2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUlong2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableSbyte2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableShort2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableInt2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableLong2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBool3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableByte3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUshort3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUint3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUlong3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableSbyte3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableShort3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableInt3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableLong3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBool4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableByte4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUshort4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUint4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableUlong4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableSbyte4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableShort4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableInt4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableLong4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat_2x2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble_2x2(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat_3x3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble_3x3(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloat_4x4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDouble_4x4(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableFloatQ(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDoubleQ(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDateTime(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableTimeSpan(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableColor(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableColorX(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableShadowCastMode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableLightType(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableSessionAccessLevel(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableKey(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableHttpStatusCode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableHeadOutputDevice(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableReflectionProbeClear(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableReflectionProbeType(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableReflectionProbeTimeSlicingMode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableCameraClearMode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableCameraPositioningMode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableCameraProjection(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableZWrite(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableZTest(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBlend(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBlendMode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableCulling(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableBodyNode(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableChirality(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class SampleNumericSpatialVariableDummyEnum(SampleNumericSpatialVariableBase):
    """SampleNumericSpatialVariable<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleNumericSpatialVariable<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "point": "Point",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


# Type alias for any SampleNumericSpatialVariable variant
SampleNumericSpatialVariable = (
    SampleNumericSpatialVariableBool |
    SampleNumericSpatialVariableByte |
    SampleNumericSpatialVariableUshort |
    SampleNumericSpatialVariableUint |
    SampleNumericSpatialVariableUlong |
    SampleNumericSpatialVariableSbyte |
    SampleNumericSpatialVariableShort |
    SampleNumericSpatialVariableInt |
    SampleNumericSpatialVariableLong |
    SampleNumericSpatialVariableFloat |
    SampleNumericSpatialVariableDouble |
    SampleNumericSpatialVariableDecimal |
    SampleNumericSpatialVariableChar |
    SampleNumericSpatialVariableString |
    SampleNumericSpatialVariableUri |
    SampleNumericSpatialVariableBool2 |
    SampleNumericSpatialVariableByte2 |
    SampleNumericSpatialVariableUshort2 |
    SampleNumericSpatialVariableUint2 |
    SampleNumericSpatialVariableUlong2 |
    SampleNumericSpatialVariableSbyte2 |
    SampleNumericSpatialVariableShort2 |
    SampleNumericSpatialVariableInt2 |
    SampleNumericSpatialVariableLong2 |
    SampleNumericSpatialVariableFloat2 |
    SampleNumericSpatialVariableDouble2 |
    SampleNumericSpatialVariableBool3 |
    SampleNumericSpatialVariableByte3 |
    SampleNumericSpatialVariableUshort3 |
    SampleNumericSpatialVariableUint3 |
    SampleNumericSpatialVariableUlong3 |
    SampleNumericSpatialVariableSbyte3 |
    SampleNumericSpatialVariableShort3 |
    SampleNumericSpatialVariableInt3 |
    SampleNumericSpatialVariableLong3 |
    SampleNumericSpatialVariableFloat3 |
    SampleNumericSpatialVariableDouble3 |
    SampleNumericSpatialVariableBool4 |
    SampleNumericSpatialVariableByte4 |
    SampleNumericSpatialVariableUshort4 |
    SampleNumericSpatialVariableUint4 |
    SampleNumericSpatialVariableUlong4 |
    SampleNumericSpatialVariableSbyte4 |
    SampleNumericSpatialVariableShort4 |
    SampleNumericSpatialVariableInt4 |
    SampleNumericSpatialVariableLong4 |
    SampleNumericSpatialVariableFloat4 |
    SampleNumericSpatialVariableDouble4 |
    SampleNumericSpatialVariableFloat_2x2 |
    SampleNumericSpatialVariableDouble_2x2 |
    SampleNumericSpatialVariableFloat_3x3 |
    SampleNumericSpatialVariableDouble_3x3 |
    SampleNumericSpatialVariableFloat_4x4 |
    SampleNumericSpatialVariableDouble_4x4 |
    SampleNumericSpatialVariableFloatQ |
    SampleNumericSpatialVariableDoubleQ |
    SampleNumericSpatialVariableDateTime |
    SampleNumericSpatialVariableTimeSpan |
    SampleNumericSpatialVariableColor |
    SampleNumericSpatialVariableColorX |
    SampleNumericSpatialVariableShadowCastMode |
    SampleNumericSpatialVariableLightType |
    SampleNumericSpatialVariableSessionAccessLevel |
    SampleNumericSpatialVariableKey |
    SampleNumericSpatialVariableHttpStatusCode |
    SampleNumericSpatialVariableHeadOutputDevice |
    SampleNumericSpatialVariableReflectionProbeClear |
    SampleNumericSpatialVariableReflectionProbeType |
    SampleNumericSpatialVariableReflectionProbeTimeSlicingMode |
    SampleNumericSpatialVariableCameraClearMode |
    SampleNumericSpatialVariableCameraPositioningMode |
    SampleNumericSpatialVariableCameraProjection |
    SampleNumericSpatialVariableZWrite |
    SampleNumericSpatialVariableZTest |
    SampleNumericSpatialVariableBlend |
    SampleNumericSpatialVariableBlendMode |
    SampleNumericSpatialVariableCulling |
    SampleNumericSpatialVariableBodyNode |
    SampleNumericSpatialVariableChirality |
    SampleNumericSpatialVariableDummyEnum
)