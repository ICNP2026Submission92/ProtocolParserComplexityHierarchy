ModBus = Header WMCRequest
Header = R1 FunctionCode
WMCRequest = ReferenceNumber BitCount ByteCount

% Fields
Set(0) : R1
Set(0000001,0000010,0000011,0000100,0001011) : FunctionCode
Fix(8)/uint : ByteCount BitCount
Fix(16)/uint : ReferenceNumber WordCount