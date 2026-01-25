"""Generated component: BooleanValueDriver.

Auto-generated from FrooxEngine.BooleanValueDriver_1.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldBool2, FieldBool3, FieldBool4, FieldByte, FieldByte2, FieldByte3, FieldByte4, FieldChar, FieldColor, FieldColorX, FieldDateTime, FieldDecimal, FieldDouble, FieldDouble2, FieldDouble2x2, FieldDouble3, FieldDouble3x3, FieldDouble4, FieldDouble4x4, FieldDoubleQ, FieldFloat, FieldFloat2, FieldFloat2x2, FieldFloat3, FieldFloat3x3, FieldFloat4, FieldFloat4x4, FieldFloatQ, FieldInt, FieldInt2, FieldInt3, FieldInt4, FieldLong, FieldLong2, FieldLong3, FieldLong4, FieldSbyte, FieldSbyte2, FieldSbyte3, FieldSbyte4, FieldShort, FieldShort2, FieldShort3, FieldShort4, FieldString, FieldTimeSpan, FieldUint, FieldUint2, FieldUint3, FieldUint4, FieldUlong, FieldUlong2, FieldUlong3, FieldUlong4, FieldUri, FieldUshort, FieldUshort2, FieldUshort3, FieldUshort4
from pyresonitelink.data.members import Reference


@dataclass
class BooleanValueDriverBase(GeneratedComponent):
    """Base class for BooleanValueDriver<T> variants."""

    SCHEMA_FILE: ClassVar[str] = "FrooxEngine.BooleanValueDriver_1.schema.json"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "enabled": "Enabled",
        "persistent": "persistent",
        "update_order": "UpdateOrder",
    }

    enabled: FieldBool | None = None
    persistent: FieldBool | None = None
    update_order: FieldInt | None = None


@dataclass
class BooleanValueDriverBool(BooleanValueDriverBase):
    """BooleanValueDriver<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<bool>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldBool | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<bool>
    true_value: FieldBool | None = None


@dataclass
class BooleanValueDriverByte(BooleanValueDriverBase):
    """BooleanValueDriver<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<byte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldByte | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<byte>
    true_value: FieldByte | None = None


@dataclass
class BooleanValueDriverUshort(BooleanValueDriverBase):
    """BooleanValueDriver<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ushort>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUshort | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ushort>
    true_value: FieldUshort | None = None


@dataclass
class BooleanValueDriverUint(BooleanValueDriverBase):
    """BooleanValueDriver<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<uint>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUint | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<uint>
    true_value: FieldUint | None = None


@dataclass
class BooleanValueDriverUlong(BooleanValueDriverBase):
    """BooleanValueDriver<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ulong>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUlong | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ulong>
    true_value: FieldUlong | None = None


@dataclass
class BooleanValueDriverSbyte(BooleanValueDriverBase):
    """BooleanValueDriver<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<sbyte>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldSbyte | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<sbyte>
    true_value: FieldSbyte | None = None


@dataclass
class BooleanValueDriverShort(BooleanValueDriverBase):
    """BooleanValueDriver<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<short>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldShort | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<short>
    true_value: FieldShort | None = None


@dataclass
class BooleanValueDriverInt(BooleanValueDriverBase):
    """BooleanValueDriver<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<int>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldInt | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<int>
    true_value: FieldInt | None = None


@dataclass
class BooleanValueDriverLong(BooleanValueDriverBase):
    """BooleanValueDriver<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<long>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldLong | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<long>
    true_value: FieldLong | None = None


@dataclass
class BooleanValueDriverFloat(BooleanValueDriverBase):
    """BooleanValueDriver<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float>
    true_value: FieldFloat | None = None


@dataclass
class BooleanValueDriverDouble(BooleanValueDriverBase):
    """BooleanValueDriver<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double>
    true_value: FieldDouble | None = None


@dataclass
class BooleanValueDriverDecimal(BooleanValueDriverBase):
    """BooleanValueDriver<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<decimal>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDecimal | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<decimal>
    true_value: FieldDecimal | None = None


@dataclass
class BooleanValueDriverChar(BooleanValueDriverBase):
    """BooleanValueDriver<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<char>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldChar | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<char>
    true_value: FieldChar | None = None


@dataclass
class BooleanValueDriverString(BooleanValueDriverBase):
    """BooleanValueDriver<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<string>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldString | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<string>
    true_value: FieldString | None = None


@dataclass
class BooleanValueDriverUri(BooleanValueDriverBase):
    """BooleanValueDriver<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<Uri>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUri | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<Uri>
    true_value: FieldUri | None = None


@dataclass
class BooleanValueDriverBool2(BooleanValueDriverBase):
    """BooleanValueDriver<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<bool2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldBool2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<bool2>
    true_value: FieldBool2 | None = None


@dataclass
class BooleanValueDriverByte2(BooleanValueDriverBase):
    """BooleanValueDriver<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<byte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldByte2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<byte2>
    true_value: FieldByte2 | None = None


@dataclass
class BooleanValueDriverUshort2(BooleanValueDriverBase):
    """BooleanValueDriver<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ushort2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUshort2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ushort2>
    true_value: FieldUshort2 | None = None


@dataclass
class BooleanValueDriverUint2(BooleanValueDriverBase):
    """BooleanValueDriver<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<uint2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUint2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<uint2>
    true_value: FieldUint2 | None = None


@dataclass
class BooleanValueDriverUlong2(BooleanValueDriverBase):
    """BooleanValueDriver<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ulong2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUlong2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ulong2>
    true_value: FieldUlong2 | None = None


@dataclass
class BooleanValueDriverSbyte2(BooleanValueDriverBase):
    """BooleanValueDriver<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<sbyte2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldSbyte2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<sbyte2>
    true_value: FieldSbyte2 | None = None


@dataclass
class BooleanValueDriverShort2(BooleanValueDriverBase):
    """BooleanValueDriver<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<short2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldShort2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<short2>
    true_value: FieldShort2 | None = None


@dataclass
class BooleanValueDriverInt2(BooleanValueDriverBase):
    """BooleanValueDriver<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<int2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldInt2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<int2>
    true_value: FieldInt2 | None = None


@dataclass
class BooleanValueDriverLong2(BooleanValueDriverBase):
    """BooleanValueDriver<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<long2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldLong2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<long2>
    true_value: FieldLong2 | None = None


@dataclass
class BooleanValueDriverFloat2(BooleanValueDriverBase):
    """BooleanValueDriver<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float2>
    true_value: FieldFloat2 | None = None


@dataclass
class BooleanValueDriverDouble2(BooleanValueDriverBase):
    """BooleanValueDriver<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double2>
    true_value: FieldDouble2 | None = None


@dataclass
class BooleanValueDriverBool3(BooleanValueDriverBase):
    """BooleanValueDriver<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<bool3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldBool3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<bool3>
    true_value: FieldBool3 | None = None


@dataclass
class BooleanValueDriverByte3(BooleanValueDriverBase):
    """BooleanValueDriver<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<byte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldByte3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<byte3>
    true_value: FieldByte3 | None = None


@dataclass
class BooleanValueDriverUshort3(BooleanValueDriverBase):
    """BooleanValueDriver<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ushort3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUshort3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ushort3>
    true_value: FieldUshort3 | None = None


@dataclass
class BooleanValueDriverUint3(BooleanValueDriverBase):
    """BooleanValueDriver<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<uint3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUint3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<uint3>
    true_value: FieldUint3 | None = None


@dataclass
class BooleanValueDriverUlong3(BooleanValueDriverBase):
    """BooleanValueDriver<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ulong3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUlong3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ulong3>
    true_value: FieldUlong3 | None = None


@dataclass
class BooleanValueDriverSbyte3(BooleanValueDriverBase):
    """BooleanValueDriver<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<sbyte3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldSbyte3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<sbyte3>
    true_value: FieldSbyte3 | None = None


@dataclass
class BooleanValueDriverShort3(BooleanValueDriverBase):
    """BooleanValueDriver<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<short3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldShort3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<short3>
    true_value: FieldShort3 | None = None


@dataclass
class BooleanValueDriverInt3(BooleanValueDriverBase):
    """BooleanValueDriver<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<int3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldInt3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<int3>
    true_value: FieldInt3 | None = None


@dataclass
class BooleanValueDriverLong3(BooleanValueDriverBase):
    """BooleanValueDriver<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<long3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldLong3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<long3>
    true_value: FieldLong3 | None = None


@dataclass
class BooleanValueDriverFloat3(BooleanValueDriverBase):
    """BooleanValueDriver<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float3>
    true_value: FieldFloat3 | None = None


@dataclass
class BooleanValueDriverDouble3(BooleanValueDriverBase):
    """BooleanValueDriver<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double3>
    true_value: FieldDouble3 | None = None


@dataclass
class BooleanValueDriverBool4(BooleanValueDriverBase):
    """BooleanValueDriver<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<bool4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldBool4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<bool4>
    true_value: FieldBool4 | None = None


@dataclass
class BooleanValueDriverByte4(BooleanValueDriverBase):
    """BooleanValueDriver<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<byte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldByte4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<byte4>
    true_value: FieldByte4 | None = None


@dataclass
class BooleanValueDriverUshort4(BooleanValueDriverBase):
    """BooleanValueDriver<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ushort4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUshort4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ushort4>
    true_value: FieldUshort4 | None = None


@dataclass
class BooleanValueDriverUint4(BooleanValueDriverBase):
    """BooleanValueDriver<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<uint4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUint4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<uint4>
    true_value: FieldUint4 | None = None


@dataclass
class BooleanValueDriverUlong4(BooleanValueDriverBase):
    """BooleanValueDriver<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<ulong4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldUlong4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<ulong4>
    true_value: FieldUlong4 | None = None


@dataclass
class BooleanValueDriverSbyte4(BooleanValueDriverBase):
    """BooleanValueDriver<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<sbyte4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldSbyte4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<sbyte4>
    true_value: FieldSbyte4 | None = None


@dataclass
class BooleanValueDriverShort4(BooleanValueDriverBase):
    """BooleanValueDriver<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<short4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldShort4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<short4>
    true_value: FieldShort4 | None = None


@dataclass
class BooleanValueDriverInt4(BooleanValueDriverBase):
    """BooleanValueDriver<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<int4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldInt4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<int4>
    true_value: FieldInt4 | None = None


@dataclass
class BooleanValueDriverLong4(BooleanValueDriverBase):
    """BooleanValueDriver<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<long4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldLong4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<long4>
    true_value: FieldLong4 | None = None


@dataclass
class BooleanValueDriverFloat4(BooleanValueDriverBase):
    """BooleanValueDriver<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float4>
    true_value: FieldFloat4 | None = None


@dataclass
class BooleanValueDriverDouble4(BooleanValueDriverBase):
    """BooleanValueDriver<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double4>
    true_value: FieldDouble4 | None = None


@dataclass
class BooleanValueDriverFloat_2x2(BooleanValueDriverBase):
    """BooleanValueDriver<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat2x2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float2x2>
    true_value: FieldFloat2x2 | None = None


@dataclass
class BooleanValueDriverDouble_2x2(BooleanValueDriverBase):
    """BooleanValueDriver<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double2x2>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble2x2 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double2x2>
    true_value: FieldDouble2x2 | None = None


@dataclass
class BooleanValueDriverFloat_3x3(BooleanValueDriverBase):
    """BooleanValueDriver<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat3x3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float3x3>
    true_value: FieldFloat3x3 | None = None


@dataclass
class BooleanValueDriverDouble_3x3(BooleanValueDriverBase):
    """BooleanValueDriver<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double3x3>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble3x3 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double3x3>
    true_value: FieldDouble3x3 | None = None


@dataclass
class BooleanValueDriverFloat_4x4(BooleanValueDriverBase):
    """BooleanValueDriver<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<float4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloat4x4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<float4x4>
    true_value: FieldFloat4x4 | None = None


@dataclass
class BooleanValueDriverDouble_4x4(BooleanValueDriverBase):
    """BooleanValueDriver<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<double4x4>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDouble4x4 | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<double4x4>
    true_value: FieldDouble4x4 | None = None


@dataclass
class BooleanValueDriverFloatQ(BooleanValueDriverBase):
    """BooleanValueDriver<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<floatQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldFloatQ | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<floatQ>
    true_value: FieldFloatQ | None = None


@dataclass
class BooleanValueDriverDoubleQ(BooleanValueDriverBase):
    """BooleanValueDriver<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<doubleQ>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDoubleQ | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<doubleQ>
    true_value: FieldDoubleQ | None = None


@dataclass
class BooleanValueDriverDateTime(BooleanValueDriverBase):
    """BooleanValueDriver<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<[System.Private.CoreLib]System.DateTime>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldDateTime | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.DateTime>
    true_value: FieldDateTime | None = None


@dataclass
class BooleanValueDriverTimeSpan(BooleanValueDriverBase):
    """BooleanValueDriver<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<[System.Private.CoreLib]System.TimeSpan>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldTimeSpan | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<[System.Private.CoreLib]System.TimeSpan>
    true_value: FieldTimeSpan | None = None


@dataclass
class BooleanValueDriverColor(BooleanValueDriverBase):
    """BooleanValueDriver<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<color>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldColor | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<color>
    true_value: FieldColor | None = None


@dataclass
class BooleanValueDriverColorX(BooleanValueDriverBase):
    """BooleanValueDriver<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[FrooxEngine]FrooxEngine.BooleanValueDriver<colorX>"

    _MEMBER_NAME_MAP: ClassVar[dict[str, str]] = {
        "false_value": "FalseValue",
        "state": "State",
        "target_field": "TargetField",
        "true_value": "TrueValue",
    }

    false_value: FieldColorX | None = None
    state: FieldBool | None = None
    target_field: Reference | None = None  # -> FrooxEngine.IField<colorX>
    true_value: FieldColorX | None = None


# Type alias for any BooleanValueDriver variant
BooleanValueDriver = (
    BooleanValueDriverBool |
    BooleanValueDriverByte |
    BooleanValueDriverUshort |
    BooleanValueDriverUint |
    BooleanValueDriverUlong |
    BooleanValueDriverSbyte |
    BooleanValueDriverShort |
    BooleanValueDriverInt |
    BooleanValueDriverLong |
    BooleanValueDriverFloat |
    BooleanValueDriverDouble |
    BooleanValueDriverDecimal |
    BooleanValueDriverChar |
    BooleanValueDriverString |
    BooleanValueDriverUri |
    BooleanValueDriverBool2 |
    BooleanValueDriverByte2 |
    BooleanValueDriverUshort2 |
    BooleanValueDriverUint2 |
    BooleanValueDriverUlong2 |
    BooleanValueDriverSbyte2 |
    BooleanValueDriverShort2 |
    BooleanValueDriverInt2 |
    BooleanValueDriverLong2 |
    BooleanValueDriverFloat2 |
    BooleanValueDriverDouble2 |
    BooleanValueDriverBool3 |
    BooleanValueDriverByte3 |
    BooleanValueDriverUshort3 |
    BooleanValueDriverUint3 |
    BooleanValueDriverUlong3 |
    BooleanValueDriverSbyte3 |
    BooleanValueDriverShort3 |
    BooleanValueDriverInt3 |
    BooleanValueDriverLong3 |
    BooleanValueDriverFloat3 |
    BooleanValueDriverDouble3 |
    BooleanValueDriverBool4 |
    BooleanValueDriverByte4 |
    BooleanValueDriverUshort4 |
    BooleanValueDriverUint4 |
    BooleanValueDriverUlong4 |
    BooleanValueDriverSbyte4 |
    BooleanValueDriverShort4 |
    BooleanValueDriverInt4 |
    BooleanValueDriverLong4 |
    BooleanValueDriverFloat4 |
    BooleanValueDriverDouble4 |
    BooleanValueDriverFloat_2x2 |
    BooleanValueDriverDouble_2x2 |
    BooleanValueDriverFloat_3x3 |
    BooleanValueDriverDouble_3x3 |
    BooleanValueDriverFloat_4x4 |
    BooleanValueDriverDouble_4x4 |
    BooleanValueDriverFloatQ |
    BooleanValueDriverDoubleQ |
    BooleanValueDriverDateTime |
    BooleanValueDriverTimeSpan |
    BooleanValueDriverColor |
    BooleanValueDriverColorX
)