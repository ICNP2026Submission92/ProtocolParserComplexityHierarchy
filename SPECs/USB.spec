USB = ID Type TransferType Endpoint Device BusID DeviceSetupRequest Data Sec Usec Status Length DataLength UnusedSetupHeader Interval StartFrame CopyTransferFlags NumberISODescriptors
Endpoint = Direction R3 EndpointNumber
CopyTransferFlags = R8 AlignedTempBuffer DMASgCombined SetupMapLocal SetupMapSingle MapLocal DMAMapSg DMAMapPage DMAMapSingle R6 DirIn FreeBuffer NoInterrupt ZeroPacket NoFSBR R2 NoTransferDMA IsoAsap ShortNotOk

% Fields
Bit : Direction AlignedTempBuffer DMASgCombined SetupMapLocal SetupMapSingle MapLocal DMAMapSg DMAMapPage DMAMapSingle DirIn FreeBuffer NoInterrupt ZeroPacket NoFSBR NoTransferDMA IsoAsap ShortNotOk
Fix(4) : EndpointNumber
Fix(64) : ID
Set(0x43)/ascii : Type
Set(0x01) : TransferType
Fix(8)/uint : Device
Fix(8) : DeviceSetupRequest Data 
Fix(16)/uint/LE : BusID
Fix(64)/uint/LE : Sec
Fix(32)/uint/LE : Usec Status Length DataLength Interval StartFrame NumberISODescriptors
Fix(64) : UnusedSetupHeader

