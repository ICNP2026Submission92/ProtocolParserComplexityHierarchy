DNP3 = DataLinkLayer TransportControl
DataLinkLayer = StartBytes Length Control Destination Source DataLinkHeaderChecksum Payload
Control = Direction Primary FrameCountBit FrameCountValid ControlFunctionCode
TransportControl = FIR FIN CON UNS Sequence

% Fields
Bit : FIR FIN CON UNS Direction Primary FrameCountBit FrameCountValid
Fix(4) : ControlFunctionCode Sequence
Fix(8)/uint : Length
Fix(16) : HeaderChecksum StartBytes DataLinkHeaderChecksum
Fix(16)/uint : Destination Source
Len(*Length) : Payload
