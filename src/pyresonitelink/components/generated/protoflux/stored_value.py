"""Generated component: StoredValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class StoredValueBase(GeneratedComponent):
    """Base class for StoredValue<T> variants."""

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
class StoredValueBool(StoredValueBase):
    """StoredValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<bool>"

    pass


@dataclass
class StoredValueByte(StoredValueBase):
    """StoredValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<byte>"

    pass


@dataclass
class StoredValueUshort(StoredValueBase):
    """StoredValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ushort>"

    pass


@dataclass
class StoredValueUint(StoredValueBase):
    """StoredValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<uint>"

    pass


@dataclass
class StoredValueUlong(StoredValueBase):
    """StoredValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ulong>"

    pass


@dataclass
class StoredValueSbyte(StoredValueBase):
    """StoredValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<sbyte>"

    pass


@dataclass
class StoredValueShort(StoredValueBase):
    """StoredValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<short>"

    pass


@dataclass
class StoredValueInt(StoredValueBase):
    """StoredValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<int>"

    pass


@dataclass
class StoredValueLong(StoredValueBase):
    """StoredValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<long>"

    pass


@dataclass
class StoredValueFloat(StoredValueBase):
    """StoredValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float>"

    pass


@dataclass
class StoredValueDouble(StoredValueBase):
    """StoredValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double>"

    pass


@dataclass
class StoredValueDecimal(StoredValueBase):
    """StoredValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<decimal>"

    pass


@dataclass
class StoredValueChar(StoredValueBase):
    """StoredValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<char>"

    pass


@dataclass
class StoredValueString(StoredValueBase):
    """StoredValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<string>"

    pass


@dataclass
class StoredValueUri(StoredValueBase):
    """StoredValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<Uri>"

    pass


@dataclass
class StoredValueBool2(StoredValueBase):
    """StoredValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<bool2>"

    pass


@dataclass
class StoredValueByte2(StoredValueBase):
    """StoredValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<byte2>"

    pass


@dataclass
class StoredValueUshort2(StoredValueBase):
    """StoredValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ushort2>"

    pass


@dataclass
class StoredValueUint2(StoredValueBase):
    """StoredValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<uint2>"

    pass


@dataclass
class StoredValueUlong2(StoredValueBase):
    """StoredValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ulong2>"

    pass


@dataclass
class StoredValueSbyte2(StoredValueBase):
    """StoredValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<sbyte2>"

    pass


@dataclass
class StoredValueShort2(StoredValueBase):
    """StoredValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<short2>"

    pass


@dataclass
class StoredValueInt2(StoredValueBase):
    """StoredValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<int2>"

    pass


@dataclass
class StoredValueLong2(StoredValueBase):
    """StoredValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<long2>"

    pass


@dataclass
class StoredValueFloat2(StoredValueBase):
    """StoredValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float2>"

    pass


@dataclass
class StoredValueDouble2(StoredValueBase):
    """StoredValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double2>"

    pass


@dataclass
class StoredValueBool3(StoredValueBase):
    """StoredValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<bool3>"

    pass


@dataclass
class StoredValueByte3(StoredValueBase):
    """StoredValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<byte3>"

    pass


@dataclass
class StoredValueUshort3(StoredValueBase):
    """StoredValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ushort3>"

    pass


@dataclass
class StoredValueUint3(StoredValueBase):
    """StoredValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<uint3>"

    pass


@dataclass
class StoredValueUlong3(StoredValueBase):
    """StoredValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ulong3>"

    pass


@dataclass
class StoredValueSbyte3(StoredValueBase):
    """StoredValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<sbyte3>"

    pass


@dataclass
class StoredValueShort3(StoredValueBase):
    """StoredValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<short3>"

    pass


@dataclass
class StoredValueInt3(StoredValueBase):
    """StoredValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<int3>"

    pass


@dataclass
class StoredValueLong3(StoredValueBase):
    """StoredValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<long3>"

    pass


@dataclass
class StoredValueFloat3(StoredValueBase):
    """StoredValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float3>"

    pass


@dataclass
class StoredValueDouble3(StoredValueBase):
    """StoredValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double3>"

    pass


@dataclass
class StoredValueBool4(StoredValueBase):
    """StoredValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<bool4>"

    pass


@dataclass
class StoredValueByte4(StoredValueBase):
    """StoredValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<byte4>"

    pass


@dataclass
class StoredValueUshort4(StoredValueBase):
    """StoredValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ushort4>"

    pass


@dataclass
class StoredValueUint4(StoredValueBase):
    """StoredValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<uint4>"

    pass


@dataclass
class StoredValueUlong4(StoredValueBase):
    """StoredValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<ulong4>"

    pass


@dataclass
class StoredValueSbyte4(StoredValueBase):
    """StoredValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<sbyte4>"

    pass


@dataclass
class StoredValueShort4(StoredValueBase):
    """StoredValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<short4>"

    pass


@dataclass
class StoredValueInt4(StoredValueBase):
    """StoredValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<int4>"

    pass


@dataclass
class StoredValueLong4(StoredValueBase):
    """StoredValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<long4>"

    pass


@dataclass
class StoredValueFloat4(StoredValueBase):
    """StoredValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float4>"

    pass


@dataclass
class StoredValueDouble4(StoredValueBase):
    """StoredValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double4>"

    pass


@dataclass
class StoredValueFloat_2x2(StoredValueBase):
    """StoredValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float2x2>"

    pass


@dataclass
class StoredValueDouble_2x2(StoredValueBase):
    """StoredValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double2x2>"

    pass


@dataclass
class StoredValueFloat_3x3(StoredValueBase):
    """StoredValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float3x3>"

    pass


@dataclass
class StoredValueDouble_3x3(StoredValueBase):
    """StoredValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double3x3>"

    pass


@dataclass
class StoredValueFloat_4x4(StoredValueBase):
    """StoredValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<float4x4>"

    pass


@dataclass
class StoredValueDouble_4x4(StoredValueBase):
    """StoredValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<double4x4>"

    pass


@dataclass
class StoredValueFloatQ(StoredValueBase):
    """StoredValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<floatQ>"

    pass


@dataclass
class StoredValueDoubleQ(StoredValueBase):
    """StoredValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<doubleQ>"

    pass


@dataclass
class StoredValueDateTime(StoredValueBase):
    """StoredValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[System.Private.CoreLib]System.DateTime>"

    pass


@dataclass
class StoredValueTimeSpan(StoredValueBase):
    """StoredValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[System.Private.CoreLib]System.TimeSpan>"

    pass


@dataclass
class StoredValueColor(StoredValueBase):
    """StoredValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<color>"

    pass


@dataclass
class StoredValueColorX(StoredValueBase):
    """StoredValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<colorX>"

    pass


@dataclass
class StoredValueShadowCastMode(StoredValueBase):
    """StoredValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class StoredValueLightType(StoredValueBase):
    """StoredValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class StoredValueSessionAccessLevel(StoredValueBase):
    """StoredValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class StoredValueKey(StoredValueBase):
    """StoredValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class StoredValueHttpStatusCode(StoredValueBase):
    """StoredValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class StoredValueHeadOutputDevice(StoredValueBase):
    """StoredValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class StoredValueReflectionProbeClear(StoredValueBase):
    """StoredValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class StoredValueReflectionProbeType(StoredValueBase):
    """StoredValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class StoredValueReflectionProbeTimeSlicingMode(StoredValueBase):
    """StoredValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class StoredValueCameraClearMode(StoredValueBase):
    """StoredValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class StoredValueCameraPositioningMode(StoredValueBase):
    """StoredValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class StoredValueCameraProjection(StoredValueBase):
    """StoredValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class StoredValueZWrite(StoredValueBase):
    """StoredValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class StoredValueZTest(StoredValueBase):
    """StoredValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class StoredValueBlend(StoredValueBase):
    """StoredValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class StoredValueBlendMode(StoredValueBase):
    """StoredValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class StoredValueCulling(StoredValueBase):
    """StoredValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class StoredValueBodyNode(StoredValueBase):
    """StoredValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class StoredValueChirality(StoredValueBase):
    """StoredValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class StoredValueDummyEnum(StoredValueBase):
    """StoredValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.StoredValue<DummyEnum>"

    pass


# Type alias for any StoredValue variant
StoredValue = (
    StoredValueBool |
    StoredValueByte |
    StoredValueUshort |
    StoredValueUint |
    StoredValueUlong |
    StoredValueSbyte |
    StoredValueShort |
    StoredValueInt |
    StoredValueLong |
    StoredValueFloat |
    StoredValueDouble |
    StoredValueDecimal |
    StoredValueChar |
    StoredValueString |
    StoredValueUri |
    StoredValueBool2 |
    StoredValueByte2 |
    StoredValueUshort2 |
    StoredValueUint2 |
    StoredValueUlong2 |
    StoredValueSbyte2 |
    StoredValueShort2 |
    StoredValueInt2 |
    StoredValueLong2 |
    StoredValueFloat2 |
    StoredValueDouble2 |
    StoredValueBool3 |
    StoredValueByte3 |
    StoredValueUshort3 |
    StoredValueUint3 |
    StoredValueUlong3 |
    StoredValueSbyte3 |
    StoredValueShort3 |
    StoredValueInt3 |
    StoredValueLong3 |
    StoredValueFloat3 |
    StoredValueDouble3 |
    StoredValueBool4 |
    StoredValueByte4 |
    StoredValueUshort4 |
    StoredValueUint4 |
    StoredValueUlong4 |
    StoredValueSbyte4 |
    StoredValueShort4 |
    StoredValueInt4 |
    StoredValueLong4 |
    StoredValueFloat4 |
    StoredValueDouble4 |
    StoredValueFloat_2x2 |
    StoredValueDouble_2x2 |
    StoredValueFloat_3x3 |
    StoredValueDouble_3x3 |
    StoredValueFloat_4x4 |
    StoredValueDouble_4x4 |
    StoredValueFloatQ |
    StoredValueDoubleQ |
    StoredValueDateTime |
    StoredValueTimeSpan |
    StoredValueColor |
    StoredValueColorX |
    StoredValueShadowCastMode |
    StoredValueLightType |
    StoredValueSessionAccessLevel |
    StoredValueKey |
    StoredValueHttpStatusCode |
    StoredValueHeadOutputDevice |
    StoredValueReflectionProbeClear |
    StoredValueReflectionProbeType |
    StoredValueReflectionProbeTimeSlicingMode |
    StoredValueCameraClearMode |
    StoredValueCameraPositioningMode |
    StoredValueCameraProjection |
    StoredValueZWrite |
    StoredValueZTest |
    StoredValueBlend |
    StoredValueBlendMode |
    StoredValueCulling |
    StoredValueBodyNode |
    StoredValueChirality |
    StoredValueDummyEnum
)