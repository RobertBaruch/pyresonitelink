"""Generated component: LocalValue.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class LocalValueBase(GeneratedComponent):
    """Base class for LocalValue<T> variants."""

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
class LocalValueBool(LocalValueBase):
    """LocalValue<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<bool>"

    pass


@dataclass
class LocalValueByte(LocalValueBase):
    """LocalValue<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<byte>"

    pass


@dataclass
class LocalValueUshort(LocalValueBase):
    """LocalValue<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ushort>"

    pass


@dataclass
class LocalValueUint(LocalValueBase):
    """LocalValue<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<uint>"

    pass


@dataclass
class LocalValueUlong(LocalValueBase):
    """LocalValue<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ulong>"

    pass


@dataclass
class LocalValueSbyte(LocalValueBase):
    """LocalValue<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<sbyte>"

    pass


@dataclass
class LocalValueShort(LocalValueBase):
    """LocalValue<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<short>"

    pass


@dataclass
class LocalValueInt(LocalValueBase):
    """LocalValue<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<int>"

    pass


@dataclass
class LocalValueLong(LocalValueBase):
    """LocalValue<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<long>"

    pass


@dataclass
class LocalValueFloat(LocalValueBase):
    """LocalValue<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float>"

    pass


@dataclass
class LocalValueDouble(LocalValueBase):
    """LocalValue<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double>"

    pass


@dataclass
class LocalValueDecimal(LocalValueBase):
    """LocalValue<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<decimal>"

    pass


@dataclass
class LocalValueChar(LocalValueBase):
    """LocalValue<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<char>"

    pass


@dataclass
class LocalValueString(LocalValueBase):
    """LocalValue<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<string>"

    pass


@dataclass
class LocalValueUri(LocalValueBase):
    """LocalValue<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<Uri>"

    pass


@dataclass
class LocalValueBool2(LocalValueBase):
    """LocalValue<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<bool2>"

    pass


@dataclass
class LocalValueByte2(LocalValueBase):
    """LocalValue<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<byte2>"

    pass


@dataclass
class LocalValueUshort2(LocalValueBase):
    """LocalValue<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ushort2>"

    pass


@dataclass
class LocalValueUint2(LocalValueBase):
    """LocalValue<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<uint2>"

    pass


@dataclass
class LocalValueUlong2(LocalValueBase):
    """LocalValue<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ulong2>"

    pass


@dataclass
class LocalValueSbyte2(LocalValueBase):
    """LocalValue<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<sbyte2>"

    pass


@dataclass
class LocalValueShort2(LocalValueBase):
    """LocalValue<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<short2>"

    pass


@dataclass
class LocalValueInt2(LocalValueBase):
    """LocalValue<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<int2>"

    pass


@dataclass
class LocalValueLong2(LocalValueBase):
    """LocalValue<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<long2>"

    pass


@dataclass
class LocalValueFloat2(LocalValueBase):
    """LocalValue<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float2>"

    pass


@dataclass
class LocalValueDouble2(LocalValueBase):
    """LocalValue<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double2>"

    pass


@dataclass
class LocalValueBool3(LocalValueBase):
    """LocalValue<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<bool3>"

    pass


@dataclass
class LocalValueByte3(LocalValueBase):
    """LocalValue<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<byte3>"

    pass


@dataclass
class LocalValueUshort3(LocalValueBase):
    """LocalValue<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ushort3>"

    pass


@dataclass
class LocalValueUint3(LocalValueBase):
    """LocalValue<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<uint3>"

    pass


@dataclass
class LocalValueUlong3(LocalValueBase):
    """LocalValue<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ulong3>"

    pass


@dataclass
class LocalValueSbyte3(LocalValueBase):
    """LocalValue<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<sbyte3>"

    pass


@dataclass
class LocalValueShort3(LocalValueBase):
    """LocalValue<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<short3>"

    pass


@dataclass
class LocalValueInt3(LocalValueBase):
    """LocalValue<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<int3>"

    pass


@dataclass
class LocalValueLong3(LocalValueBase):
    """LocalValue<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<long3>"

    pass


@dataclass
class LocalValueFloat3(LocalValueBase):
    """LocalValue<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float3>"

    pass


@dataclass
class LocalValueDouble3(LocalValueBase):
    """LocalValue<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double3>"

    pass


@dataclass
class LocalValueBool4(LocalValueBase):
    """LocalValue<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<bool4>"

    pass


@dataclass
class LocalValueByte4(LocalValueBase):
    """LocalValue<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<byte4>"

    pass


@dataclass
class LocalValueUshort4(LocalValueBase):
    """LocalValue<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ushort4>"

    pass


@dataclass
class LocalValueUint4(LocalValueBase):
    """LocalValue<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<uint4>"

    pass


@dataclass
class LocalValueUlong4(LocalValueBase):
    """LocalValue<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<ulong4>"

    pass


@dataclass
class LocalValueSbyte4(LocalValueBase):
    """LocalValue<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<sbyte4>"

    pass


@dataclass
class LocalValueShort4(LocalValueBase):
    """LocalValue<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<short4>"

    pass


@dataclass
class LocalValueInt4(LocalValueBase):
    """LocalValue<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<int4>"

    pass


@dataclass
class LocalValueLong4(LocalValueBase):
    """LocalValue<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<long4>"

    pass


@dataclass
class LocalValueFloat4(LocalValueBase):
    """LocalValue<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float4>"

    pass


@dataclass
class LocalValueDouble4(LocalValueBase):
    """LocalValue<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double4>"

    pass


@dataclass
class LocalValueFloat_2x2(LocalValueBase):
    """LocalValue<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float2x2>"

    pass


@dataclass
class LocalValueDouble_2x2(LocalValueBase):
    """LocalValue<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double2x2>"

    pass


@dataclass
class LocalValueFloat_3x3(LocalValueBase):
    """LocalValue<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float3x3>"

    pass


@dataclass
class LocalValueDouble_3x3(LocalValueBase):
    """LocalValue<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double3x3>"

    pass


@dataclass
class LocalValueFloat_4x4(LocalValueBase):
    """LocalValue<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<float4x4>"

    pass


@dataclass
class LocalValueDouble_4x4(LocalValueBase):
    """LocalValue<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<double4x4>"

    pass


@dataclass
class LocalValueFloatQ(LocalValueBase):
    """LocalValue<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<floatQ>"

    pass


@dataclass
class LocalValueDoubleQ(LocalValueBase):
    """LocalValue<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<doubleQ>"

    pass


@dataclass
class LocalValueDateTime(LocalValueBase):
    """LocalValue<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[System.Private.CoreLib]System.DateTime>"

    pass


@dataclass
class LocalValueTimeSpan(LocalValueBase):
    """LocalValue<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[System.Private.CoreLib]System.TimeSpan>"

    pass


@dataclass
class LocalValueColor(LocalValueBase):
    """LocalValue<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<color>"

    pass


@dataclass
class LocalValueColorX(LocalValueBase):
    """LocalValue<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<colorX>"

    pass


@dataclass
class LocalValueShadowCastMode(LocalValueBase):
    """LocalValue<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class LocalValueLightType(LocalValueBase):
    """LocalValue<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class LocalValueSessionAccessLevel(LocalValueBase):
    """LocalValue<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class LocalValueKey(LocalValueBase):
    """LocalValue<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class LocalValueHttpStatusCode(LocalValueBase):
    """LocalValue<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class LocalValueHeadOutputDevice(LocalValueBase):
    """LocalValue<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class LocalValueReflectionProbeClear(LocalValueBase):
    """LocalValue<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class LocalValueReflectionProbeType(LocalValueBase):
    """LocalValue<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class LocalValueReflectionProbeTimeSlicingMode(LocalValueBase):
    """LocalValue<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class LocalValueCameraClearMode(LocalValueBase):
    """LocalValue<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class LocalValueCameraPositioningMode(LocalValueBase):
    """LocalValue<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class LocalValueCameraProjection(LocalValueBase):
    """LocalValue<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class LocalValueZWrite(LocalValueBase):
    """LocalValue<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class LocalValueZTest(LocalValueBase):
    """LocalValue<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class LocalValueBlend(LocalValueBase):
    """LocalValue<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class LocalValueBlendMode(LocalValueBase):
    """LocalValue<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class LocalValueCulling(LocalValueBase):
    """LocalValue<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class LocalValueBodyNode(LocalValueBase):
    """LocalValue<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class LocalValueChirality(LocalValueBase):
    """LocalValue<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class LocalValueDummyEnum(LocalValueBase):
    """LocalValue<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.LocalValue<DummyEnum>"

    pass


# Type alias for any LocalValue variant
LocalValue = (
    LocalValueBool |
    LocalValueByte |
    LocalValueUshort |
    LocalValueUint |
    LocalValueUlong |
    LocalValueSbyte |
    LocalValueShort |
    LocalValueInt |
    LocalValueLong |
    LocalValueFloat |
    LocalValueDouble |
    LocalValueDecimal |
    LocalValueChar |
    LocalValueString |
    LocalValueUri |
    LocalValueBool2 |
    LocalValueByte2 |
    LocalValueUshort2 |
    LocalValueUint2 |
    LocalValueUlong2 |
    LocalValueSbyte2 |
    LocalValueShort2 |
    LocalValueInt2 |
    LocalValueLong2 |
    LocalValueFloat2 |
    LocalValueDouble2 |
    LocalValueBool3 |
    LocalValueByte3 |
    LocalValueUshort3 |
    LocalValueUint3 |
    LocalValueUlong3 |
    LocalValueSbyte3 |
    LocalValueShort3 |
    LocalValueInt3 |
    LocalValueLong3 |
    LocalValueFloat3 |
    LocalValueDouble3 |
    LocalValueBool4 |
    LocalValueByte4 |
    LocalValueUshort4 |
    LocalValueUint4 |
    LocalValueUlong4 |
    LocalValueSbyte4 |
    LocalValueShort4 |
    LocalValueInt4 |
    LocalValueLong4 |
    LocalValueFloat4 |
    LocalValueDouble4 |
    LocalValueFloat_2x2 |
    LocalValueDouble_2x2 |
    LocalValueFloat_3x3 |
    LocalValueDouble_3x3 |
    LocalValueFloat_4x4 |
    LocalValueDouble_4x4 |
    LocalValueFloatQ |
    LocalValueDoubleQ |
    LocalValueDateTime |
    LocalValueTimeSpan |
    LocalValueColor |
    LocalValueColorX |
    LocalValueShadowCastMode |
    LocalValueLightType |
    LocalValueSessionAccessLevel |
    LocalValueKey |
    LocalValueHttpStatusCode |
    LocalValueHeadOutputDevice |
    LocalValueReflectionProbeClear |
    LocalValueReflectionProbeType |
    LocalValueReflectionProbeTimeSlicingMode |
    LocalValueCameraClearMode |
    LocalValueCameraPositioningMode |
    LocalValueCameraProjection |
    LocalValueZWrite |
    LocalValueZTest |
    LocalValueBlend |
    LocalValueBlendMode |
    LocalValueCulling |
    LocalValueBodyNode |
    LocalValueChirality |
    LocalValueDummyEnum
)