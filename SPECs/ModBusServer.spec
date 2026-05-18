ModBus = Header Payload
Header = ReservedBit FunctionCode
Payload = ? case *FunctionCode
        | 1 RCRequest
        | 2 RDIRequest
        | 3 RHRRequest
        | 4 RIRRequest
        | 11 WMCRequest
        ?

ReadCoils = ? caset *STATE 
        | 1 RCRequest 2
        | 2 RCResponse 1
        ?

ReadDiscreteInputs = ? caset *STATE 
        | 1 RDIRequest 2 
        | 2 RDIResponse 1
        ?

ReadHoldingRegisters = ? caset *STATE 
        | 1 RHRRequest 2
        | 2 RHRResponse 1
        ?

ReadInputRegisters = ? caset *STATE 
        | 1 RIRRequest 2
        | 2 RIRResponse 1
        ?

WriteMultipleCoils = ? caset *STATE 
        | 1 WMCRequest 2
        | 2 WMCResponse 1
        ?

RDIRequest = ReferenceNumber BitCount
RDIResponse = ByteCount Byte^*ByteCount
Byte = Bit^8

RHRRequest = ReferenceNumber WordCount
RHRResponse = ByteCount Register

WMCRequest = ReferenceNumber BitCount ByteCount Bit^*BitCount
WMCResponse = ReferenceNumber BitCount

% Fields
Fix(1) : ReservedBit
Fix(7)/uint : FunctionCode
Fix(8)/uint : ByteCount
Fix(16)/uint : ReferenceNumber WordCount Register