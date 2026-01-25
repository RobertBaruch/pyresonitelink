"""Generated component: SampleSpatialVariablePartialDerivative.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class SampleSpatialVariablePartialDerivativeBase(GeneratedComponent):
    """Base class for SampleSpatialVariablePartialDerivative<T> variants."""

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
class SampleSpatialVariablePartialDerivativeBool(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeByte(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUshort(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUint(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUlong(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeSbyte(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeShort(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeInt(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeLong(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDecimal(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeChar(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeString(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUri(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBool2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeByte2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUshort2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUint2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUlong2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeSbyte2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeShort2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeInt2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeLong2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBool3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeByte3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUshort3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUint3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUlong3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeSbyte3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeShort3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeInt3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeLong3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBool4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeByte4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUshort4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUint4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeUlong4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeSbyte4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeShort4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeInt4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeLong4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat_2x2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble_2x2(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat_3x3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble_3x3(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloat_4x4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDouble_4x4(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeFloatQ(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDoubleQ(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDateTime(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeTimeSpan(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeColor(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeColorX(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeShadowCastMode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeLightType(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeSessionAccessLevel(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeKey(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeHttpStatusCode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeHeadOutputDevice(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeReflectionProbeClear(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeReflectionProbeType(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeReflectionProbeTimeSlicingMode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeCameraClearMode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeCameraPositioningMode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeCameraProjection(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeZWrite(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeZTest(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBlend(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBlendMode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeCulling(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeBodyNode(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeChirality(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class SampleSpatialVariablePartialDerivativeDummyEnum(SampleSpatialVariablePartialDerivativeBase):
    """SampleSpatialVariablePartialDerivative<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.SampleSpatialVariablePartialDerivative<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "base_value": "BaseValue",
        "mode": "Mode",
        "name": "Name",
        "orientation": "Orientation",
        "point": "Point",
        "sampling_distance": "SamplingDistance",
    }

    base_value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>
    mode: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ValueSpatialVariableMode>
    name: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeObjectOutput<string>
    orientation: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>
    point: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>
    sampling_distance: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


# Type alias for any SampleSpatialVariablePartialDerivative variant
SampleSpatialVariablePartialDerivative = (
    SampleSpatialVariablePartialDerivativeBool |
    SampleSpatialVariablePartialDerivativeByte |
    SampleSpatialVariablePartialDerivativeUshort |
    SampleSpatialVariablePartialDerivativeUint |
    SampleSpatialVariablePartialDerivativeUlong |
    SampleSpatialVariablePartialDerivativeSbyte |
    SampleSpatialVariablePartialDerivativeShort |
    SampleSpatialVariablePartialDerivativeInt |
    SampleSpatialVariablePartialDerivativeLong |
    SampleSpatialVariablePartialDerivativeFloat |
    SampleSpatialVariablePartialDerivativeDouble |
    SampleSpatialVariablePartialDerivativeDecimal |
    SampleSpatialVariablePartialDerivativeChar |
    SampleSpatialVariablePartialDerivativeString |
    SampleSpatialVariablePartialDerivativeUri |
    SampleSpatialVariablePartialDerivativeBool2 |
    SampleSpatialVariablePartialDerivativeByte2 |
    SampleSpatialVariablePartialDerivativeUshort2 |
    SampleSpatialVariablePartialDerivativeUint2 |
    SampleSpatialVariablePartialDerivativeUlong2 |
    SampleSpatialVariablePartialDerivativeSbyte2 |
    SampleSpatialVariablePartialDerivativeShort2 |
    SampleSpatialVariablePartialDerivativeInt2 |
    SampleSpatialVariablePartialDerivativeLong2 |
    SampleSpatialVariablePartialDerivativeFloat2 |
    SampleSpatialVariablePartialDerivativeDouble2 |
    SampleSpatialVariablePartialDerivativeBool3 |
    SampleSpatialVariablePartialDerivativeByte3 |
    SampleSpatialVariablePartialDerivativeUshort3 |
    SampleSpatialVariablePartialDerivativeUint3 |
    SampleSpatialVariablePartialDerivativeUlong3 |
    SampleSpatialVariablePartialDerivativeSbyte3 |
    SampleSpatialVariablePartialDerivativeShort3 |
    SampleSpatialVariablePartialDerivativeInt3 |
    SampleSpatialVariablePartialDerivativeLong3 |
    SampleSpatialVariablePartialDerivativeFloat3 |
    SampleSpatialVariablePartialDerivativeDouble3 |
    SampleSpatialVariablePartialDerivativeBool4 |
    SampleSpatialVariablePartialDerivativeByte4 |
    SampleSpatialVariablePartialDerivativeUshort4 |
    SampleSpatialVariablePartialDerivativeUint4 |
    SampleSpatialVariablePartialDerivativeUlong4 |
    SampleSpatialVariablePartialDerivativeSbyte4 |
    SampleSpatialVariablePartialDerivativeShort4 |
    SampleSpatialVariablePartialDerivativeInt4 |
    SampleSpatialVariablePartialDerivativeLong4 |
    SampleSpatialVariablePartialDerivativeFloat4 |
    SampleSpatialVariablePartialDerivativeDouble4 |
    SampleSpatialVariablePartialDerivativeFloat_2x2 |
    SampleSpatialVariablePartialDerivativeDouble_2x2 |
    SampleSpatialVariablePartialDerivativeFloat_3x3 |
    SampleSpatialVariablePartialDerivativeDouble_3x3 |
    SampleSpatialVariablePartialDerivativeFloat_4x4 |
    SampleSpatialVariablePartialDerivativeDouble_4x4 |
    SampleSpatialVariablePartialDerivativeFloatQ |
    SampleSpatialVariablePartialDerivativeDoubleQ |
    SampleSpatialVariablePartialDerivativeDateTime |
    SampleSpatialVariablePartialDerivativeTimeSpan |
    SampleSpatialVariablePartialDerivativeColor |
    SampleSpatialVariablePartialDerivativeColorX |
    SampleSpatialVariablePartialDerivativeShadowCastMode |
    SampleSpatialVariablePartialDerivativeLightType |
    SampleSpatialVariablePartialDerivativeSessionAccessLevel |
    SampleSpatialVariablePartialDerivativeKey |
    SampleSpatialVariablePartialDerivativeHttpStatusCode |
    SampleSpatialVariablePartialDerivativeHeadOutputDevice |
    SampleSpatialVariablePartialDerivativeReflectionProbeClear |
    SampleSpatialVariablePartialDerivativeReflectionProbeType |
    SampleSpatialVariablePartialDerivativeReflectionProbeTimeSlicingMode |
    SampleSpatialVariablePartialDerivativeCameraClearMode |
    SampleSpatialVariablePartialDerivativeCameraPositioningMode |
    SampleSpatialVariablePartialDerivativeCameraProjection |
    SampleSpatialVariablePartialDerivativeZWrite |
    SampleSpatialVariablePartialDerivativeZTest |
    SampleSpatialVariablePartialDerivativeBlend |
    SampleSpatialVariablePartialDerivativeBlendMode |
    SampleSpatialVariablePartialDerivativeCulling |
    SampleSpatialVariablePartialDerivativeBodyNode |
    SampleSpatialVariablePartialDerivativeChirality |
    SampleSpatialVariablePartialDerivativeDummyEnum
)