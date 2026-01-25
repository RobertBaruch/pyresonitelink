"""Generated component: RandomEnum.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class RandomEnumBase(GeneratedComponent):
    """Base class for RandomEnum<T> variants."""

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
class RandomEnumBool(RandomEnumBase):
    """RandomEnum<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<bool>"

    pass


@dataclass
class RandomEnumByte(RandomEnumBase):
    """RandomEnum<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<byte>"

    pass


@dataclass
class RandomEnumUshort(RandomEnumBase):
    """RandomEnum<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ushort>"

    pass


@dataclass
class RandomEnumUint(RandomEnumBase):
    """RandomEnum<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<uint>"

    pass


@dataclass
class RandomEnumUlong(RandomEnumBase):
    """RandomEnum<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ulong>"

    pass


@dataclass
class RandomEnumSbyte(RandomEnumBase):
    """RandomEnum<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<sbyte>"

    pass


@dataclass
class RandomEnumShort(RandomEnumBase):
    """RandomEnum<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<short>"

    pass


@dataclass
class RandomEnumInt(RandomEnumBase):
    """RandomEnum<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<int>"

    pass


@dataclass
class RandomEnumLong(RandomEnumBase):
    """RandomEnum<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<long>"

    pass


@dataclass
class RandomEnumFloat(RandomEnumBase):
    """RandomEnum<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float>"

    pass


@dataclass
class RandomEnumDouble(RandomEnumBase):
    """RandomEnum<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double>"

    pass


@dataclass
class RandomEnumDecimal(RandomEnumBase):
    """RandomEnum<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<decimal>"

    pass


@dataclass
class RandomEnumChar(RandomEnumBase):
    """RandomEnum<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<char>"

    pass


@dataclass
class RandomEnumString(RandomEnumBase):
    """RandomEnum<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<string>"

    pass


@dataclass
class RandomEnumUri(RandomEnumBase):
    """RandomEnum<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<Uri>"

    pass


@dataclass
class RandomEnumBool2(RandomEnumBase):
    """RandomEnum<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<bool2>"

    pass


@dataclass
class RandomEnumByte2(RandomEnumBase):
    """RandomEnum<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<byte2>"

    pass


@dataclass
class RandomEnumUshort2(RandomEnumBase):
    """RandomEnum<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ushort2>"

    pass


@dataclass
class RandomEnumUint2(RandomEnumBase):
    """RandomEnum<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<uint2>"

    pass


@dataclass
class RandomEnumUlong2(RandomEnumBase):
    """RandomEnum<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ulong2>"

    pass


@dataclass
class RandomEnumSbyte2(RandomEnumBase):
    """RandomEnum<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<sbyte2>"

    pass


@dataclass
class RandomEnumShort2(RandomEnumBase):
    """RandomEnum<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<short2>"

    pass


@dataclass
class RandomEnumInt2(RandomEnumBase):
    """RandomEnum<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<int2>"

    pass


@dataclass
class RandomEnumLong2(RandomEnumBase):
    """RandomEnum<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<long2>"

    pass


@dataclass
class RandomEnumFloat2(RandomEnumBase):
    """RandomEnum<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float2>"

    pass


@dataclass
class RandomEnumDouble2(RandomEnumBase):
    """RandomEnum<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double2>"

    pass


@dataclass
class RandomEnumBool3(RandomEnumBase):
    """RandomEnum<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<bool3>"

    pass


@dataclass
class RandomEnumByte3(RandomEnumBase):
    """RandomEnum<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<byte3>"

    pass


@dataclass
class RandomEnumUshort3(RandomEnumBase):
    """RandomEnum<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ushort3>"

    pass


@dataclass
class RandomEnumUint3(RandomEnumBase):
    """RandomEnum<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<uint3>"

    pass


@dataclass
class RandomEnumUlong3(RandomEnumBase):
    """RandomEnum<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ulong3>"

    pass


@dataclass
class RandomEnumSbyte3(RandomEnumBase):
    """RandomEnum<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<sbyte3>"

    pass


@dataclass
class RandomEnumShort3(RandomEnumBase):
    """RandomEnum<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<short3>"

    pass


@dataclass
class RandomEnumInt3(RandomEnumBase):
    """RandomEnum<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<int3>"

    pass


@dataclass
class RandomEnumLong3(RandomEnumBase):
    """RandomEnum<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<long3>"

    pass


@dataclass
class RandomEnumFloat3(RandomEnumBase):
    """RandomEnum<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float3>"

    pass


@dataclass
class RandomEnumDouble3(RandomEnumBase):
    """RandomEnum<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double3>"

    pass


@dataclass
class RandomEnumBool4(RandomEnumBase):
    """RandomEnum<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<bool4>"

    pass


@dataclass
class RandomEnumByte4(RandomEnumBase):
    """RandomEnum<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<byte4>"

    pass


@dataclass
class RandomEnumUshort4(RandomEnumBase):
    """RandomEnum<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ushort4>"

    pass


@dataclass
class RandomEnumUint4(RandomEnumBase):
    """RandomEnum<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<uint4>"

    pass


@dataclass
class RandomEnumUlong4(RandomEnumBase):
    """RandomEnum<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<ulong4>"

    pass


@dataclass
class RandomEnumSbyte4(RandomEnumBase):
    """RandomEnum<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<sbyte4>"

    pass


@dataclass
class RandomEnumShort4(RandomEnumBase):
    """RandomEnum<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<short4>"

    pass


@dataclass
class RandomEnumInt4(RandomEnumBase):
    """RandomEnum<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<int4>"

    pass


@dataclass
class RandomEnumLong4(RandomEnumBase):
    """RandomEnum<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<long4>"

    pass


@dataclass
class RandomEnumFloat4(RandomEnumBase):
    """RandomEnum<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float4>"

    pass


@dataclass
class RandomEnumDouble4(RandomEnumBase):
    """RandomEnum<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double4>"

    pass


@dataclass
class RandomEnumFloat_2x2(RandomEnumBase):
    """RandomEnum<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float2x2>"

    pass


@dataclass
class RandomEnumDouble_2x2(RandomEnumBase):
    """RandomEnum<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double2x2>"

    pass


@dataclass
class RandomEnumFloat_3x3(RandomEnumBase):
    """RandomEnum<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float3x3>"

    pass


@dataclass
class RandomEnumDouble_3x3(RandomEnumBase):
    """RandomEnum<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double3x3>"

    pass


@dataclass
class RandomEnumFloat_4x4(RandomEnumBase):
    """RandomEnum<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<float4x4>"

    pass


@dataclass
class RandomEnumDouble_4x4(RandomEnumBase):
    """RandomEnum<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<double4x4>"

    pass


@dataclass
class RandomEnumFloatQ(RandomEnumBase):
    """RandomEnum<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<floatQ>"

    pass


@dataclass
class RandomEnumDoubleQ(RandomEnumBase):
    """RandomEnum<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<doubleQ>"

    pass


@dataclass
class RandomEnumDateTime(RandomEnumBase):
    """RandomEnum<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[System.Private.CoreLib]System.DateTime>"

    pass


@dataclass
class RandomEnumTimeSpan(RandomEnumBase):
    """RandomEnum<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[System.Private.CoreLib]System.TimeSpan>"

    pass


@dataclass
class RandomEnumColor(RandomEnumBase):
    """RandomEnum<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<color>"

    pass


@dataclass
class RandomEnumColorX(RandomEnumBase):
    """RandomEnum<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<colorX>"

    pass


@dataclass
class RandomEnumShadowCastMode(RandomEnumBase):
    """RandomEnum<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class RandomEnumLightType(RandomEnumBase):
    """RandomEnum<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class RandomEnumSessionAccessLevel(RandomEnumBase):
    """RandomEnum<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class RandomEnumKey(RandomEnumBase):
    """RandomEnum<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class RandomEnumHttpStatusCode(RandomEnumBase):
    """RandomEnum<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class RandomEnumHeadOutputDevice(RandomEnumBase):
    """RandomEnum<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class RandomEnumReflectionProbeClear(RandomEnumBase):
    """RandomEnum<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class RandomEnumReflectionProbeType(RandomEnumBase):
    """RandomEnum<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class RandomEnumReflectionProbeTimeSlicingMode(RandomEnumBase):
    """RandomEnum<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class RandomEnumCameraClearMode(RandomEnumBase):
    """RandomEnum<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class RandomEnumCameraPositioningMode(RandomEnumBase):
    """RandomEnum<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class RandomEnumCameraProjection(RandomEnumBase):
    """RandomEnum<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class RandomEnumZWrite(RandomEnumBase):
    """RandomEnum<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class RandomEnumZTest(RandomEnumBase):
    """RandomEnum<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class RandomEnumBlend(RandomEnumBase):
    """RandomEnum<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class RandomEnumBlendMode(RandomEnumBase):
    """RandomEnum<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class RandomEnumCulling(RandomEnumBase):
    """RandomEnum<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class RandomEnumBodyNode(RandomEnumBase):
    """RandomEnum<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class RandomEnumChirality(RandomEnumBase):
    """RandomEnum<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class RandomEnumDummyEnum(RandomEnumBase):
    """RandomEnum<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Random.RandomEnum<DummyEnum>"

    pass


# Type alias for any RandomEnum variant
RandomEnum = (
    RandomEnumBool |
    RandomEnumByte |
    RandomEnumUshort |
    RandomEnumUint |
    RandomEnumUlong |
    RandomEnumSbyte |
    RandomEnumShort |
    RandomEnumInt |
    RandomEnumLong |
    RandomEnumFloat |
    RandomEnumDouble |
    RandomEnumDecimal |
    RandomEnumChar |
    RandomEnumString |
    RandomEnumUri |
    RandomEnumBool2 |
    RandomEnumByte2 |
    RandomEnumUshort2 |
    RandomEnumUint2 |
    RandomEnumUlong2 |
    RandomEnumSbyte2 |
    RandomEnumShort2 |
    RandomEnumInt2 |
    RandomEnumLong2 |
    RandomEnumFloat2 |
    RandomEnumDouble2 |
    RandomEnumBool3 |
    RandomEnumByte3 |
    RandomEnumUshort3 |
    RandomEnumUint3 |
    RandomEnumUlong3 |
    RandomEnumSbyte3 |
    RandomEnumShort3 |
    RandomEnumInt3 |
    RandomEnumLong3 |
    RandomEnumFloat3 |
    RandomEnumDouble3 |
    RandomEnumBool4 |
    RandomEnumByte4 |
    RandomEnumUshort4 |
    RandomEnumUint4 |
    RandomEnumUlong4 |
    RandomEnumSbyte4 |
    RandomEnumShort4 |
    RandomEnumInt4 |
    RandomEnumLong4 |
    RandomEnumFloat4 |
    RandomEnumDouble4 |
    RandomEnumFloat_2x2 |
    RandomEnumDouble_2x2 |
    RandomEnumFloat_3x3 |
    RandomEnumDouble_3x3 |
    RandomEnumFloat_4x4 |
    RandomEnumDouble_4x4 |
    RandomEnumFloatQ |
    RandomEnumDoubleQ |
    RandomEnumDateTime |
    RandomEnumTimeSpan |
    RandomEnumColor |
    RandomEnumColorX |
    RandomEnumShadowCastMode |
    RandomEnumLightType |
    RandomEnumSessionAccessLevel |
    RandomEnumKey |
    RandomEnumHttpStatusCode |
    RandomEnumHeadOutputDevice |
    RandomEnumReflectionProbeClear |
    RandomEnumReflectionProbeType |
    RandomEnumReflectionProbeTimeSlicingMode |
    RandomEnumCameraClearMode |
    RandomEnumCameraPositioningMode |
    RandomEnumCameraProjection |
    RandomEnumZWrite |
    RandomEnumZTest |
    RandomEnumBlend |
    RandomEnumBlendMode |
    RandomEnumCulling |
    RandomEnumBodyNode |
    RandomEnumChirality |
    RandomEnumDummyEnum
)