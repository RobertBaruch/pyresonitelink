"""Generated component: FireOnLocalValueChange.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt
from pyresonitelink.data.members import Reference


@dataclass
class FireOnLocalValueChangeBase(GeneratedComponent):
    """Base class for FireOnLocalValueChange<T> variants."""

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
class FireOnLocalValueChangeBool(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool>


@dataclass
class FireOnLocalValueChangeByte(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte>


@dataclass
class FireOnLocalValueChangeUshort(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort>


@dataclass
class FireOnLocalValueChangeUint(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint>


@dataclass
class FireOnLocalValueChangeUlong(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong>


@dataclass
class FireOnLocalValueChangeSbyte(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte>


@dataclass
class FireOnLocalValueChangeShort(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short>


@dataclass
class FireOnLocalValueChangeInt(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int>


@dataclass
class FireOnLocalValueChangeLong(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long>


@dataclass
class FireOnLocalValueChangeFloat(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float>


@dataclass
class FireOnLocalValueChangeDouble(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double>


@dataclass
class FireOnLocalValueChangeDecimal(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<decimal>


@dataclass
class FireOnLocalValueChangeChar(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<char>


@dataclass
class FireOnLocalValueChangeString(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<string>


@dataclass
class FireOnLocalValueChangeUri(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<Uri>


@dataclass
class FireOnLocalValueChangeBool2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool2>


@dataclass
class FireOnLocalValueChangeByte2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte2>


@dataclass
class FireOnLocalValueChangeUshort2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort2>


@dataclass
class FireOnLocalValueChangeUint2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint2>


@dataclass
class FireOnLocalValueChangeUlong2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong2>


@dataclass
class FireOnLocalValueChangeSbyte2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte2>


@dataclass
class FireOnLocalValueChangeShort2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short2>


@dataclass
class FireOnLocalValueChangeInt2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int2>


@dataclass
class FireOnLocalValueChangeLong2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long2>


@dataclass
class FireOnLocalValueChangeFloat2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2>


@dataclass
class FireOnLocalValueChangeDouble2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2>


@dataclass
class FireOnLocalValueChangeBool3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool3>


@dataclass
class FireOnLocalValueChangeByte3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte3>


@dataclass
class FireOnLocalValueChangeUshort3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort3>


@dataclass
class FireOnLocalValueChangeUint3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint3>


@dataclass
class FireOnLocalValueChangeUlong3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong3>


@dataclass
class FireOnLocalValueChangeSbyte3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte3>


@dataclass
class FireOnLocalValueChangeShort3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short3>


@dataclass
class FireOnLocalValueChangeInt3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int3>


@dataclass
class FireOnLocalValueChangeLong3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long3>


@dataclass
class FireOnLocalValueChangeFloat3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3>


@dataclass
class FireOnLocalValueChangeDouble3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3>


@dataclass
class FireOnLocalValueChangeBool4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<bool4>


@dataclass
class FireOnLocalValueChangeByte4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<byte4>


@dataclass
class FireOnLocalValueChangeUshort4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ushort4>


@dataclass
class FireOnLocalValueChangeUint4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<uint4>


@dataclass
class FireOnLocalValueChangeUlong4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<ulong4>


@dataclass
class FireOnLocalValueChangeSbyte4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<sbyte4>


@dataclass
class FireOnLocalValueChangeShort4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<short4>


@dataclass
class FireOnLocalValueChangeInt4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<int4>


@dataclass
class FireOnLocalValueChangeLong4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<long4>


@dataclass
class FireOnLocalValueChangeFloat4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4>


@dataclass
class FireOnLocalValueChangeDouble4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4>


@dataclass
class FireOnLocalValueChangeFloat_2x2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float2x2>


@dataclass
class FireOnLocalValueChangeDouble_2x2(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double2x2>


@dataclass
class FireOnLocalValueChangeFloat_3x3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float3x3>


@dataclass
class FireOnLocalValueChangeDouble_3x3(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double3x3>


@dataclass
class FireOnLocalValueChangeFloat_4x4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>


@dataclass
class FireOnLocalValueChangeDouble_4x4(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<double4x4>


@dataclass
class FireOnLocalValueChangeFloatQ(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>


@dataclass
class FireOnLocalValueChangeDoubleQ(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<doubleQ>


@dataclass
class FireOnLocalValueChangeDateTime(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.DateTime>


@dataclass
class FireOnLocalValueChangeTimeSpan(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Private.CoreLib]System.TimeSpan>


@dataclass
class FireOnLocalValueChangeColor(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<color>


@dataclass
class FireOnLocalValueChangeColorX(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<colorX>


@dataclass
class FireOnLocalValueChangeShadowCastMode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ShadowCastMode>


@dataclass
class FireOnLocalValueChangeLightType(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.LightType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.LightType>


@dataclass
class FireOnLocalValueChangeSessionAccessLevel(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>


@dataclass
class FireOnLocalValueChangeKey(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.Key>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>


@dataclass
class FireOnLocalValueChangeHttpStatusCode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[System.Net.Primitives]System.Net.HttpStatusCode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[System.Net.Primitives]System.Net.HttpStatusCode>


@dataclass
class FireOnLocalValueChangeHeadOutputDevice(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>


@dataclass
class FireOnLocalValueChangeReflectionProbeClear(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>


@dataclass
class FireOnLocalValueChangeReflectionProbeType(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>


@dataclass
class FireOnLocalValueChangeReflectionProbeTimeSlicingMode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>


@dataclass
class FireOnLocalValueChangeCameraClearMode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraClearMode>


@dataclass
class FireOnLocalValueChangeCameraPositioningMode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.CameraPositioningMode>


@dataclass
class FireOnLocalValueChangeCameraProjection(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.CameraProjection>


@dataclass
class FireOnLocalValueChangeZWrite(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.ZWrite>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZWrite>


@dataclass
class FireOnLocalValueChangeZTest(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.ZTest>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.ZTest>


@dataclass
class FireOnLocalValueChangeBlend(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.Blend>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Blend>


@dataclass
class FireOnLocalValueChangeBlendMode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.BlendMode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.BlendMode>


@dataclass
class FireOnLocalValueChangeCulling(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[FrooxEngine]FrooxEngine.Culling>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<FrooxEngine.Culling>


@dataclass
class FireOnLocalValueChangeBodyNode(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.BodyNode>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.BodyNode>


@dataclass
class FireOnLocalValueChangeChirality(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<[Renderite.Shared]Renderite.Shared.Chirality>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>


@dataclass
class FireOnLocalValueChangeDummyEnum(FireOnLocalValueChangeBase):
    """FireOnLocalValueChange<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.FireOnLocalValueChange<DummyEnum>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "on_change": "OnChange",
        "value": "Value",
    }

    on_change: Reference | None = None  # -> FrooxEngine.ProtoFlux.ISyncNodeOperation
    value: Reference | None = None  # -> FrooxEngine.ProtoFlux.INodeValueOutput<DummyEnum>


# Type alias for any FireOnLocalValueChange variant
FireOnLocalValueChange = (
    FireOnLocalValueChangeBool |
    FireOnLocalValueChangeByte |
    FireOnLocalValueChangeUshort |
    FireOnLocalValueChangeUint |
    FireOnLocalValueChangeUlong |
    FireOnLocalValueChangeSbyte |
    FireOnLocalValueChangeShort |
    FireOnLocalValueChangeInt |
    FireOnLocalValueChangeLong |
    FireOnLocalValueChangeFloat |
    FireOnLocalValueChangeDouble |
    FireOnLocalValueChangeDecimal |
    FireOnLocalValueChangeChar |
    FireOnLocalValueChangeString |
    FireOnLocalValueChangeUri |
    FireOnLocalValueChangeBool2 |
    FireOnLocalValueChangeByte2 |
    FireOnLocalValueChangeUshort2 |
    FireOnLocalValueChangeUint2 |
    FireOnLocalValueChangeUlong2 |
    FireOnLocalValueChangeSbyte2 |
    FireOnLocalValueChangeShort2 |
    FireOnLocalValueChangeInt2 |
    FireOnLocalValueChangeLong2 |
    FireOnLocalValueChangeFloat2 |
    FireOnLocalValueChangeDouble2 |
    FireOnLocalValueChangeBool3 |
    FireOnLocalValueChangeByte3 |
    FireOnLocalValueChangeUshort3 |
    FireOnLocalValueChangeUint3 |
    FireOnLocalValueChangeUlong3 |
    FireOnLocalValueChangeSbyte3 |
    FireOnLocalValueChangeShort3 |
    FireOnLocalValueChangeInt3 |
    FireOnLocalValueChangeLong3 |
    FireOnLocalValueChangeFloat3 |
    FireOnLocalValueChangeDouble3 |
    FireOnLocalValueChangeBool4 |
    FireOnLocalValueChangeByte4 |
    FireOnLocalValueChangeUshort4 |
    FireOnLocalValueChangeUint4 |
    FireOnLocalValueChangeUlong4 |
    FireOnLocalValueChangeSbyte4 |
    FireOnLocalValueChangeShort4 |
    FireOnLocalValueChangeInt4 |
    FireOnLocalValueChangeLong4 |
    FireOnLocalValueChangeFloat4 |
    FireOnLocalValueChangeDouble4 |
    FireOnLocalValueChangeFloat_2x2 |
    FireOnLocalValueChangeDouble_2x2 |
    FireOnLocalValueChangeFloat_3x3 |
    FireOnLocalValueChangeDouble_3x3 |
    FireOnLocalValueChangeFloat_4x4 |
    FireOnLocalValueChangeDouble_4x4 |
    FireOnLocalValueChangeFloatQ |
    FireOnLocalValueChangeDoubleQ |
    FireOnLocalValueChangeDateTime |
    FireOnLocalValueChangeTimeSpan |
    FireOnLocalValueChangeColor |
    FireOnLocalValueChangeColorX |
    FireOnLocalValueChangeShadowCastMode |
    FireOnLocalValueChangeLightType |
    FireOnLocalValueChangeSessionAccessLevel |
    FireOnLocalValueChangeKey |
    FireOnLocalValueChangeHttpStatusCode |
    FireOnLocalValueChangeHeadOutputDevice |
    FireOnLocalValueChangeReflectionProbeClear |
    FireOnLocalValueChangeReflectionProbeType |
    FireOnLocalValueChangeReflectionProbeTimeSlicingMode |
    FireOnLocalValueChangeCameraClearMode |
    FireOnLocalValueChangeCameraPositioningMode |
    FireOnLocalValueChangeCameraProjection |
    FireOnLocalValueChangeZWrite |
    FireOnLocalValueChangeZTest |
    FireOnLocalValueChangeBlend |
    FireOnLocalValueChangeBlendMode |
    FireOnLocalValueChangeCulling |
    FireOnLocalValueChangeBodyNode |
    FireOnLocalValueChangeChirality |
    FireOnLocalValueChangeDummyEnum
)