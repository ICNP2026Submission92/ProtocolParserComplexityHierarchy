ICMP = Type Code Checksum Payload DataLen Data

Payload = ? case *Type
        | 0 Ping
        | 3 Unreachable
        | 4 Quench
        | 5 Redirect
        | 8 PingReply
        | 11 TimeExceeded
        | 12 ParameterProblem
        | 13 Timestamp
        | 15 Info
        | 17 AddressMask
        ?

Ping = Identifier SequenceNumber
PingReply = Identifier SequenceNumber Timestamp
Redirect = GatewayAddress IPHeader
Unreachable = Unused IPHeader
Quench = Unused IPHeader
TimeExceeded = Unused IPHeader
ParameterProblem = Pointer IPHeader
Timestamp = Identifier SequenceNumber OriginateTimestamp ReceiveTimestamp TransmitTimestamp
Info = Identifier SequenceNumber
AddressMask = Identifier SequenceNumber SubnetMask

% Fields
Set(0x00,0x03,0x04,0x05,0x08,0x0B,0x0C,0x0D,0x0F,0x11) : Type
Fix(8)/uint : Code DataLen
Fix(16)/uint : Checksum Identifier SequenceNumber Pointer
Fix(32)/ip4 : GatewayAddress SubnetMask
Fix(32)/uint : OriginateTimestamp ReceiveTimestamp TransmitTimestamp
Fix(64)/uint : Timestamp
Fix(160)/uint : IPHeader
Set(0x00000000) : Unused
Len(*DataLen) : Data