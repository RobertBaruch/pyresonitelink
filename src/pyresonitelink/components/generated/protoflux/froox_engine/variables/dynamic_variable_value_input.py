"""Generated component: DynamicVariableValueInput.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class DynamicVariableValueInputBase(GeneratedComponent):
    """Base class for DynamicVariableValueInput<T> variants."""

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
class DynamicVariableValueInputBool(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputByte(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUshort(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUint(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUlong(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputSbyte(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputShort(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputInt(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputLong(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDecimal(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputChar(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputString(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUri(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBool2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputByte2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUshort2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUint2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUlong2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputSbyte2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputShort2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputInt2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputLong2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBool3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputByte3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUshort3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUint3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUlong3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputSbyte3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputShort3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputInt3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputLong3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBool4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputByte4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUshort4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUint4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputUlong4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputSbyte4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputShort4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputInt4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputLong4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat_2x2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble_2x2(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat_3x3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble_3x3(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloat_4x4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDouble_4x4(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputFloatQ(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDoubleQ(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDateTime(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputTimeSpan(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputColor(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputColorX(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputShadowCastMode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputLightType(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputSessionAccessLevel(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputKey(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputHttpStatusCode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputHeadOutputDevice(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputReflectionProbeClear(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputReflectionProbeType(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputReflectionProbeTimeSlicingMode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputCameraClearMode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputCameraPositioningMode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputCameraProjection(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputZWrite(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputZTest(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBlend(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBlendMode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputCulling(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputBodyNode(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputChirality(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


@dataclass
class DynamicVariableValueInputDummyEnum(DynamicVariableValueInputBase):
    """DynamicVariableValueInput<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DynamicVariableValueInput<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "variable_name": "VariableName",
    }

    variable_name: Reference | None = None  # -> FrooxEngine.ProtoFlux.IGlobalValueProxy<string>


# Type alias for any DynamicVariableValueInput variant
DynamicVariableValueInput = (
    DynamicVariableValueInputBool |
    DynamicVariableValueInputByte |
    DynamicVariableValueInputUshort |
    DynamicVariableValueInputUint |
    DynamicVariableValueInputUlong |
    DynamicVariableValueInputSbyte |
    DynamicVariableValueInputShort |
    DynamicVariableValueInputInt |
    DynamicVariableValueInputLong |
    DynamicVariableValueInputFloat |
    DynamicVariableValueInputDouble |
    DynamicVariableValueInputDecimal |
    DynamicVariableValueInputChar |
    DynamicVariableValueInputString |
    DynamicVariableValueInputUri |
    DynamicVariableValueInputBool2 |
    DynamicVariableValueInputByte2 |
    DynamicVariableValueInputUshort2 |
    DynamicVariableValueInputUint2 |
    DynamicVariableValueInputUlong2 |
    DynamicVariableValueInputSbyte2 |
    DynamicVariableValueInputShort2 |
    DynamicVariableValueInputInt2 |
    DynamicVariableValueInputLong2 |
    DynamicVariableValueInputFloat2 |
    DynamicVariableValueInputDouble2 |
    DynamicVariableValueInputBool3 |
    DynamicVariableValueInputByte3 |
    DynamicVariableValueInputUshort3 |
    DynamicVariableValueInputUint3 |
    DynamicVariableValueInputUlong3 |
    DynamicVariableValueInputSbyte3 |
    DynamicVariableValueInputShort3 |
    DynamicVariableValueInputInt3 |
    DynamicVariableValueInputLong3 |
    DynamicVariableValueInputFloat3 |
    DynamicVariableValueInputDouble3 |
    DynamicVariableValueInputBool4 |
    DynamicVariableValueInputByte4 |
    DynamicVariableValueInputUshort4 |
    DynamicVariableValueInputUint4 |
    DynamicVariableValueInputUlong4 |
    DynamicVariableValueInputSbyte4 |
    DynamicVariableValueInputShort4 |
    DynamicVariableValueInputInt4 |
    DynamicVariableValueInputLong4 |
    DynamicVariableValueInputFloat4 |
    DynamicVariableValueInputDouble4 |
    DynamicVariableValueInputFloat_2x2 |
    DynamicVariableValueInputDouble_2x2 |
    DynamicVariableValueInputFloat_3x3 |
    DynamicVariableValueInputDouble_3x3 |
    DynamicVariableValueInputFloat_4x4 |
    DynamicVariableValueInputDouble_4x4 |
    DynamicVariableValueInputFloatQ |
    DynamicVariableValueInputDoubleQ |
    DynamicVariableValueInputDateTime |
    DynamicVariableValueInputTimeSpan |
    DynamicVariableValueInputColor |
    DynamicVariableValueInputColorX |
    DynamicVariableValueInputShadowCastMode |
    DynamicVariableValueInputLightType |
    DynamicVariableValueInputSessionAccessLevel |
    DynamicVariableValueInputKey |
    DynamicVariableValueInputHttpStatusCode |
    DynamicVariableValueInputHeadOutputDevice |
    DynamicVariableValueInputReflectionProbeClear |
    DynamicVariableValueInputReflectionProbeType |
    DynamicVariableValueInputReflectionProbeTimeSlicingMode |
    DynamicVariableValueInputCameraClearMode |
    DynamicVariableValueInputCameraPositioningMode |
    DynamicVariableValueInputCameraProjection |
    DynamicVariableValueInputZWrite |
    DynamicVariableValueInputZTest |
    DynamicVariableValueInputBlend |
    DynamicVariableValueInputBlendMode |
    DynamicVariableValueInputCulling |
    DynamicVariableValueInputBodyNode |
    DynamicVariableValueInputChirality |
    DynamicVariableValueInputDummyEnum
)