"""Generated component: DataModelValueFieldStore.

Auto-generated from protoflux.schema.json
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from pyresonitelink.components.generated._base import GeneratedComponent
from pyresonitelink.data.fields import FieldBool, FieldInt


@dataclass
class DataModelValueFieldStoreBase(GeneratedComponent):
    """Base class for DataModelValueFieldStore<T> variants."""

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
class DataModelValueFieldStoreBool(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<bool> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<bool>"

    pass


@dataclass
class DataModelValueFieldStoreByte(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<byte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<byte>"

    pass


@dataclass
class DataModelValueFieldStoreUshort(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ushort> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ushort>"

    pass


@dataclass
class DataModelValueFieldStoreUint(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<uint> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<uint>"

    pass


@dataclass
class DataModelValueFieldStoreUlong(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ulong> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ulong>"

    pass


@dataclass
class DataModelValueFieldStoreSbyte(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<sbyte> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<sbyte>"

    pass


@dataclass
class DataModelValueFieldStoreShort(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<short> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<short>"

    pass


@dataclass
class DataModelValueFieldStoreInt(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<int> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<int>"

    pass


@dataclass
class DataModelValueFieldStoreLong(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<long> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<long>"

    pass


@dataclass
class DataModelValueFieldStoreFloat(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float>"

    pass


@dataclass
class DataModelValueFieldStoreDouble(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double>"

    pass


@dataclass
class DataModelValueFieldStoreDecimal(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<decimal> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<decimal>"

    pass


@dataclass
class DataModelValueFieldStoreChar(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<char> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<char>"

    pass


@dataclass
class DataModelValueFieldStoreString(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<string> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<string>"

    pass


@dataclass
class DataModelValueFieldStoreUri(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<Uri> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<Uri>"

    pass


@dataclass
class DataModelValueFieldStoreBool2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<bool2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<bool2>"

    pass


@dataclass
class DataModelValueFieldStoreByte2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<byte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<byte2>"

    pass


@dataclass
class DataModelValueFieldStoreUshort2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ushort2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ushort2>"

    pass


@dataclass
class DataModelValueFieldStoreUint2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<uint2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<uint2>"

    pass


@dataclass
class DataModelValueFieldStoreUlong2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ulong2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ulong2>"

    pass


@dataclass
class DataModelValueFieldStoreSbyte2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<sbyte2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<sbyte2>"

    pass


@dataclass
class DataModelValueFieldStoreShort2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<short2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<short2>"

    pass


@dataclass
class DataModelValueFieldStoreInt2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<int2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<int2>"

    pass


@dataclass
class DataModelValueFieldStoreLong2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<long2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<long2>"

    pass


@dataclass
class DataModelValueFieldStoreFloat2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float2>"

    pass


@dataclass
class DataModelValueFieldStoreDouble2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double2>"

    pass


@dataclass
class DataModelValueFieldStoreBool3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<bool3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<bool3>"

    pass


@dataclass
class DataModelValueFieldStoreByte3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<byte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<byte3>"

    pass


@dataclass
class DataModelValueFieldStoreUshort3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ushort3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ushort3>"

    pass


@dataclass
class DataModelValueFieldStoreUint3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<uint3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<uint3>"

    pass


@dataclass
class DataModelValueFieldStoreUlong3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ulong3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ulong3>"

    pass


@dataclass
class DataModelValueFieldStoreSbyte3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<sbyte3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<sbyte3>"

    pass


@dataclass
class DataModelValueFieldStoreShort3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<short3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<short3>"

    pass


@dataclass
class DataModelValueFieldStoreInt3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<int3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<int3>"

    pass


@dataclass
class DataModelValueFieldStoreLong3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<long3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<long3>"

    pass


@dataclass
class DataModelValueFieldStoreFloat3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float3>"

    pass


@dataclass
class DataModelValueFieldStoreDouble3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double3>"

    pass


@dataclass
class DataModelValueFieldStoreBool4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<bool4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<bool4>"

    pass


@dataclass
class DataModelValueFieldStoreByte4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<byte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<byte4>"

    pass


@dataclass
class DataModelValueFieldStoreUshort4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ushort4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ushort4>"

    pass


@dataclass
class DataModelValueFieldStoreUint4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<uint4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<uint4>"

    pass


@dataclass
class DataModelValueFieldStoreUlong4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ulong4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<ulong4>"

    pass


@dataclass
class DataModelValueFieldStoreSbyte4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<sbyte4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<sbyte4>"

    pass


@dataclass
class DataModelValueFieldStoreShort4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<short4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<short4>"

    pass


@dataclass
class DataModelValueFieldStoreInt4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<int4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<int4>"

    pass


@dataclass
class DataModelValueFieldStoreLong4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<long4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<long4>"

    pass


@dataclass
class DataModelValueFieldStoreFloat4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float4>"

    pass


@dataclass
class DataModelValueFieldStoreDouble4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double4>"

    pass


@dataclass
class DataModelValueFieldStoreFloat_2x2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float2x2>"

    pass


@dataclass
class DataModelValueFieldStoreDouble_2x2(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double2x2> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double2x2>"

    pass


@dataclass
class DataModelValueFieldStoreFloat_3x3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float3x3>"

    pass


@dataclass
class DataModelValueFieldStoreDouble_3x3(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double3x3> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double3x3>"

    pass


@dataclass
class DataModelValueFieldStoreFloat_4x4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<float4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<float4x4>"

    pass


@dataclass
class DataModelValueFieldStoreDouble_4x4(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<double4x4> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<double4x4>"

    pass


@dataclass
class DataModelValueFieldStoreFloatQ(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<floatQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<floatQ>"

    pass


@dataclass
class DataModelValueFieldStoreDoubleQ(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<doubleQ> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<doubleQ>"

    pass


@dataclass
class DataModelValueFieldStoreDateTime(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<DateTime> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[System.Private.CoreLib]System.DateTime>"

    pass


@dataclass
class DataModelValueFieldStoreTimeSpan(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<TimeSpan> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[System.Private.CoreLib]System.TimeSpan>"

    pass


@dataclass
class DataModelValueFieldStoreColor(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<color> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<color>"

    pass


@dataclass
class DataModelValueFieldStoreColorX(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<colorX> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<colorX>"

    pass


@dataclass
class DataModelValueFieldStoreShadowCastMode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ShadowCastMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.ShadowCastMode>"

    pass


@dataclass
class DataModelValueFieldStoreLightType(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<LightType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.LightType>"

    pass


@dataclass
class DataModelValueFieldStoreSessionAccessLevel(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<SessionAccessLevel> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[SkyFrost.Base.Models]SkyFrost.Base.SessionAccessLevel>"

    pass


@dataclass
class DataModelValueFieldStoreKey(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<Key> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.Key>"

    pass


@dataclass
class DataModelValueFieldStoreHttpStatusCode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<HttpStatusCode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[System.Net.Primitives]System.Net.HttpStatusCode>"

    pass


@dataclass
class DataModelValueFieldStoreHeadOutputDevice(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<HeadOutputDevice> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.HeadOutputDevice>"

    pass


@dataclass
class DataModelValueFieldStoreReflectionProbeClear(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ReflectionProbeClear> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.ReflectionProbeClear>"

    pass


@dataclass
class DataModelValueFieldStoreReflectionProbeType(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ReflectionProbeType> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.ReflectionProbeType>"

    pass


@dataclass
class DataModelValueFieldStoreReflectionProbeTimeSlicingMode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ReflectionProbeTimeSlicingMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.ReflectionProbeTimeSlicingMode>"

    pass


@dataclass
class DataModelValueFieldStoreCameraClearMode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<CameraClearMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.CameraClearMode>"

    pass


@dataclass
class DataModelValueFieldStoreCameraPositioningMode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<CameraPositioningMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.CameraPositioningMode>"

    pass


@dataclass
class DataModelValueFieldStoreCameraProjection(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<CameraProjection> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.CameraProjection>"

    pass


@dataclass
class DataModelValueFieldStoreZWrite(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ZWrite> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.ZWrite>"

    pass


@dataclass
class DataModelValueFieldStoreZTest(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<ZTest> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.ZTest>"

    pass


@dataclass
class DataModelValueFieldStoreBlend(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<Blend> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.Blend>"

    pass


@dataclass
class DataModelValueFieldStoreBlendMode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<BlendMode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.BlendMode>"

    pass


@dataclass
class DataModelValueFieldStoreCulling(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<Culling> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[FrooxEngine]FrooxEngine.Culling>"

    pass


@dataclass
class DataModelValueFieldStoreBodyNode(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<BodyNode> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.BodyNode>"

    pass


@dataclass
class DataModelValueFieldStoreChirality(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<Chirality> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<[Renderite.Shared]Renderite.Shared.Chirality>"

    pass


@dataclass
class DataModelValueFieldStoreDummyEnum(DataModelValueFieldStoreBase):
    """DataModelValueFieldStore<DummyEnum> component."""

    COMPONENT_TYPE: ClassVar[str] = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Variables.DataModelValueFieldStore<DummyEnum>"

    pass


# Type alias for any DataModelValueFieldStore variant
DataModelValueFieldStore = (
    DataModelValueFieldStoreBool |
    DataModelValueFieldStoreByte |
    DataModelValueFieldStoreUshort |
    DataModelValueFieldStoreUint |
    DataModelValueFieldStoreUlong |
    DataModelValueFieldStoreSbyte |
    DataModelValueFieldStoreShort |
    DataModelValueFieldStoreInt |
    DataModelValueFieldStoreLong |
    DataModelValueFieldStoreFloat |
    DataModelValueFieldStoreDouble |
    DataModelValueFieldStoreDecimal |
    DataModelValueFieldStoreChar |
    DataModelValueFieldStoreString |
    DataModelValueFieldStoreUri |
    DataModelValueFieldStoreBool2 |
    DataModelValueFieldStoreByte2 |
    DataModelValueFieldStoreUshort2 |
    DataModelValueFieldStoreUint2 |
    DataModelValueFieldStoreUlong2 |
    DataModelValueFieldStoreSbyte2 |
    DataModelValueFieldStoreShort2 |
    DataModelValueFieldStoreInt2 |
    DataModelValueFieldStoreLong2 |
    DataModelValueFieldStoreFloat2 |
    DataModelValueFieldStoreDouble2 |
    DataModelValueFieldStoreBool3 |
    DataModelValueFieldStoreByte3 |
    DataModelValueFieldStoreUshort3 |
    DataModelValueFieldStoreUint3 |
    DataModelValueFieldStoreUlong3 |
    DataModelValueFieldStoreSbyte3 |
    DataModelValueFieldStoreShort3 |
    DataModelValueFieldStoreInt3 |
    DataModelValueFieldStoreLong3 |
    DataModelValueFieldStoreFloat3 |
    DataModelValueFieldStoreDouble3 |
    DataModelValueFieldStoreBool4 |
    DataModelValueFieldStoreByte4 |
    DataModelValueFieldStoreUshort4 |
    DataModelValueFieldStoreUint4 |
    DataModelValueFieldStoreUlong4 |
    DataModelValueFieldStoreSbyte4 |
    DataModelValueFieldStoreShort4 |
    DataModelValueFieldStoreInt4 |
    DataModelValueFieldStoreLong4 |
    DataModelValueFieldStoreFloat4 |
    DataModelValueFieldStoreDouble4 |
    DataModelValueFieldStoreFloat_2x2 |
    DataModelValueFieldStoreDouble_2x2 |
    DataModelValueFieldStoreFloat_3x3 |
    DataModelValueFieldStoreDouble_3x3 |
    DataModelValueFieldStoreFloat_4x4 |
    DataModelValueFieldStoreDouble_4x4 |
    DataModelValueFieldStoreFloatQ |
    DataModelValueFieldStoreDoubleQ |
    DataModelValueFieldStoreDateTime |
    DataModelValueFieldStoreTimeSpan |
    DataModelValueFieldStoreColor |
    DataModelValueFieldStoreColorX |
    DataModelValueFieldStoreShadowCastMode |
    DataModelValueFieldStoreLightType |
    DataModelValueFieldStoreSessionAccessLevel |
    DataModelValueFieldStoreKey |
    DataModelValueFieldStoreHttpStatusCode |
    DataModelValueFieldStoreHeadOutputDevice |
    DataModelValueFieldStoreReflectionProbeClear |
    DataModelValueFieldStoreReflectionProbeType |
    DataModelValueFieldStoreReflectionProbeTimeSlicingMode |
    DataModelValueFieldStoreCameraClearMode |
    DataModelValueFieldStoreCameraPositioningMode |
    DataModelValueFieldStoreCameraProjection |
    DataModelValueFieldStoreZWrite |
    DataModelValueFieldStoreZTest |
    DataModelValueFieldStoreBlend |
    DataModelValueFieldStoreBlendMode |
    DataModelValueFieldStoreCulling |
    DataModelValueFieldStoreBodyNode |
    DataModelValueFieldStoreChirality |
    DataModelValueFieldStoreDummyEnum
)