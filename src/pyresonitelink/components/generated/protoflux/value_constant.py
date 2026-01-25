"""Generated component: ValueConstant.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class ValueConstantBase(GeneratedComponent):
    """Base class for ValueConstant<T> variants."""

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
class ValueConstantBool(ValueConstantBase):
    """ValueConstant<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<bool>"

    pass


@dataclass
class ValueConstantByte(ValueConstantBase):
    """ValueConstant<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<byte>"

    pass


@dataclass
class ValueConstantUshort(ValueConstantBase):
    """ValueConstant<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ushort>"

    pass


@dataclass
class ValueConstantUint(ValueConstantBase):
    """ValueConstant<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<uint>"

    pass


@dataclass
class ValueConstantUlong(ValueConstantBase):
    """ValueConstant<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ulong>"

    pass


@dataclass
class ValueConstantSbyte(ValueConstantBase):
    """ValueConstant<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<sbyte>"

    pass


@dataclass
class ValueConstantShort(ValueConstantBase):
    """ValueConstant<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<short>"

    pass


@dataclass
class ValueConstantInt(ValueConstantBase):
    """ValueConstant<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<int>"

    pass


@dataclass
class ValueConstantLong(ValueConstantBase):
    """ValueConstant<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<long>"

    pass


@dataclass
class ValueConstantFloat(ValueConstantBase):
    """ValueConstant<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float>"

    pass


@dataclass
class ValueConstantDouble(ValueConstantBase):
    """ValueConstant<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double>"

    pass


@dataclass
class ValueConstantDecimal(ValueConstantBase):
    """ValueConstant<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<decimal>"

    pass


@dataclass
class ValueConstantChar(ValueConstantBase):
    """ValueConstant<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<char>"

    pass


@dataclass
class ValueConstantString(ValueConstantBase):
    """ValueConstant<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<string>"

    pass


@dataclass
class ValueConstantUri(ValueConstantBase):
    """ValueConstant<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<Uri>"

    pass


@dataclass
class ValueConstantBool2(ValueConstantBase):
    """ValueConstant<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<bool2>"

    pass


@dataclass
class ValueConstantByte2(ValueConstantBase):
    """ValueConstant<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<byte2>"

    pass


@dataclass
class ValueConstantUshort2(ValueConstantBase):
    """ValueConstant<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ushort2>"

    pass


@dataclass
class ValueConstantUint2(ValueConstantBase):
    """ValueConstant<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<uint2>"

    pass


@dataclass
class ValueConstantUlong2(ValueConstantBase):
    """ValueConstant<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ulong2>"

    pass


@dataclass
class ValueConstantSbyte2(ValueConstantBase):
    """ValueConstant<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<sbyte2>"

    pass


@dataclass
class ValueConstantShort2(ValueConstantBase):
    """ValueConstant<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<short2>"

    pass


@dataclass
class ValueConstantInt2(ValueConstantBase):
    """ValueConstant<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<int2>"

    pass


@dataclass
class ValueConstantLong2(ValueConstantBase):
    """ValueConstant<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<long2>"

    pass


@dataclass
class ValueConstantFloat2(ValueConstantBase):
    """ValueConstant<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float2>"

    pass


@dataclass
class ValueConstantDouble2(ValueConstantBase):
    """ValueConstant<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double2>"

    pass


@dataclass
class ValueConstantBool3(ValueConstantBase):
    """ValueConstant<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<bool3>"

    pass


@dataclass
class ValueConstantByte3(ValueConstantBase):
    """ValueConstant<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<byte3>"

    pass


@dataclass
class ValueConstantUshort3(ValueConstantBase):
    """ValueConstant<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ushort3>"

    pass


@dataclass
class ValueConstantUint3(ValueConstantBase):
    """ValueConstant<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<uint3>"

    pass


@dataclass
class ValueConstantUlong3(ValueConstantBase):
    """ValueConstant<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ulong3>"

    pass


@dataclass
class ValueConstantSbyte3(ValueConstantBase):
    """ValueConstant<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<sbyte3>"

    pass


@dataclass
class ValueConstantShort3(ValueConstantBase):
    """ValueConstant<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<short3>"

    pass


@dataclass
class ValueConstantInt3(ValueConstantBase):
    """ValueConstant<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<int3>"

    pass


@dataclass
class ValueConstantLong3(ValueConstantBase):
    """ValueConstant<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<long3>"

    pass


@dataclass
class ValueConstantFloat3(ValueConstantBase):
    """ValueConstant<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float3>"

    pass


@dataclass
class ValueConstantDouble3(ValueConstantBase):
    """ValueConstant<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double3>"

    pass


@dataclass
class ValueConstantBool4(ValueConstantBase):
    """ValueConstant<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<bool4>"

    pass


@dataclass
class ValueConstantByte4(ValueConstantBase):
    """ValueConstant<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<byte4>"

    pass


@dataclass
class ValueConstantUshort4(ValueConstantBase):
    """ValueConstant<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ushort4>"

    pass


@dataclass
class ValueConstantUint4(ValueConstantBase):
    """ValueConstant<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<uint4>"

    pass


@dataclass
class ValueConstantUlong4(ValueConstantBase):
    """ValueConstant<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<ulong4>"

    pass


@dataclass
class ValueConstantSbyte4(ValueConstantBase):
    """ValueConstant<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<sbyte4>"

    pass


@dataclass
class ValueConstantShort4(ValueConstantBase):
    """ValueConstant<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<short4>"

    pass


@dataclass
class ValueConstantInt4(ValueConstantBase):
    """ValueConstant<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<int4>"

    pass


@dataclass
class ValueConstantLong4(ValueConstantBase):
    """ValueConstant<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<long4>"

    pass


@dataclass
class ValueConstantFloat4(ValueConstantBase):
    """ValueConstant<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float4>"

    pass


@dataclass
class ValueConstantDouble4(ValueConstantBase):
    """ValueConstant<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double4>"

    pass


@dataclass
class ValueConstantFloat_2x2(ValueConstantBase):
    """ValueConstant<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float2x2>"

    pass


@dataclass
class ValueConstantDouble_2x2(ValueConstantBase):
    """ValueConstant<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double2x2>"

    pass


@dataclass
class ValueConstantFloat_3x3(ValueConstantBase):
    """ValueConstant<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float3x3>"

    pass


@dataclass
class ValueConstantDouble_3x3(ValueConstantBase):
    """ValueConstant<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double3x3>"

    pass


@dataclass
class ValueConstantFloat_4x4(ValueConstantBase):
    """ValueConstant<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<float4x4>"

    pass


@dataclass
class ValueConstantDouble_4x4(ValueConstantBase):
    """ValueConstant<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<double4x4>"

    pass


@dataclass
class ValueConstantFloatQ(ValueConstantBase):
    """ValueConstant<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<floatQ>"

    pass


@dataclass
class ValueConstantDoubleQ(ValueConstantBase):
    """ValueConstant<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<doubleQ>"

    pass


@dataclass
class ValueConstantDateTime(ValueConstantBase):
    """ValueConstant<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[System.Private.CoreLib]System.DateTime>"

    pass


@dataclass
class ValueConstantTimeSpan(ValueConstantBase):
    """ValueConstant<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[System.Private.CoreLib]System.TimeSpan>"

    pass


@dataclass
class ValueConstantColor(ValueConstantBase):
    """ValueConstant<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<color>"

    pass


@dataclass
class ValueConstantColorX(ValueConstantBase):
    """ValueConstant<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<colorX>"

    pass


@dataclass
class ValueConstantShadowCastMode(ValueConstantBase):
    """ValueConstant<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class ValueConstantLightType(ValueConstantBase):
    """ValueConstant<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class ValueConstantSessionAccessLevel(ValueConstantBase):
    """ValueConstant<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class ValueConstantKey(ValueConstantBase):
    """ValueConstant<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class ValueConstantHttpStatusCode(ValueConstantBase):
    """ValueConstant<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class ValueConstantHeadOutputDevice(ValueConstantBase):
    """ValueConstant<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class ValueConstantReflectionProbeClear(ValueConstantBase):
    """ValueConstant<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class ValueConstantReflectionProbeType(ValueConstantBase):
    """ValueConstant<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class ValueConstantReflectionProbeTimeSlicingMode(ValueConstantBase):
    """ValueConstant<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class ValueConstantCameraClearMode(ValueConstantBase):
    """ValueConstant<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class ValueConstantCameraPositioningMode(ValueConstantBase):
    """ValueConstant<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class ValueConstantCameraProjection(ValueConstantBase):
    """ValueConstant<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class ValueConstantZWrite(ValueConstantBase):
    """ValueConstant<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class ValueConstantZTest(ValueConstantBase):
    """ValueConstant<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class ValueConstantBlend(ValueConstantBase):
    """ValueConstant<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class ValueConstantBlendMode(ValueConstantBase):
    """ValueConstant<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class ValueConstantCulling(ValueConstantBase):
    """ValueConstant<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class ValueConstantBodyNode(ValueConstantBase):
    """ValueConstant<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class ValueConstantChirality(ValueConstantBase):
    """ValueConstant<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class ValueConstantDummyEnum(ValueConstantBase):
    """ValueConstant<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConstant<DummyEnum>"

    pass


# Type alias for any ValueConstant variant
ValueConstant = (
    ValueConstantBool |
    ValueConstantByte |
    ValueConstantUshort |
    ValueConstantUint |
    ValueConstantUlong |
    ValueConstantSbyte |
    ValueConstantShort |
    ValueConstantInt |
    ValueConstantLong |
    ValueConstantFloat |
    ValueConstantDouble |
    ValueConstantDecimal |
    ValueConstantChar |
    ValueConstantString |
    ValueConstantUri |
    ValueConstantBool2 |
    ValueConstantByte2 |
    ValueConstantUshort2 |
    ValueConstantUint2 |
    ValueConstantUlong2 |
    ValueConstantSbyte2 |
    ValueConstantShort2 |
    ValueConstantInt2 |
    ValueConstantLong2 |
    ValueConstantFloat2 |
    ValueConstantDouble2 |
    ValueConstantBool3 |
    ValueConstantByte3 |
    ValueConstantUshort3 |
    ValueConstantUint3 |
    ValueConstantUlong3 |
    ValueConstantSbyte3 |
    ValueConstantShort3 |
    ValueConstantInt3 |
    ValueConstantLong3 |
    ValueConstantFloat3 |
    ValueConstantDouble3 |
    ValueConstantBool4 |
    ValueConstantByte4 |
    ValueConstantUshort4 |
    ValueConstantUint4 |
    ValueConstantUlong4 |
    ValueConstantSbyte4 |
    ValueConstantShort4 |
    ValueConstantInt4 |
    ValueConstantLong4 |
    ValueConstantFloat4 |
    ValueConstantDouble4 |
    ValueConstantFloat_2x2 |
    ValueConstantDouble_2x2 |
    ValueConstantFloat_3x3 |
    ValueConstantDouble_3x3 |
    ValueConstantFloat_4x4 |
    ValueConstantDouble_4x4 |
    ValueConstantFloatQ |
    ValueConstantDoubleQ |
    ValueConstantDateTime |
    ValueConstantTimeSpan |
    ValueConstantColor |
    ValueConstantColorX |
    ValueConstantShadowCastMode |
    ValueConstantLightType |
    ValueConstantSessionAccessLevel |
    ValueConstantKey |
    ValueConstantHttpStatusCode |
    ValueConstantHeadOutputDevice |
    ValueConstantReflectionProbeClear |
    ValueConstantReflectionProbeType |
    ValueConstantReflectionProbeTimeSlicingMode |
    ValueConstantCameraClearMode |
    ValueConstantCameraPositioningMode |
    ValueConstantCameraProjection |
    ValueConstantZWrite |
    ValueConstantZTest |
    ValueConstantBlend |
    ValueConstantBlendMode |
    ValueConstantCulling |
    ValueConstantBodyNode |
    ValueConstantChirality |
    ValueConstantDummyEnum
)