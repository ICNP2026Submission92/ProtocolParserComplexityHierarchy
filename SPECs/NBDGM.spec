NBDGM = MessageType Flags DatagramID SourceIP SourcePort DatagramLength PacketOffset SourceName DestinationName Datagram
Flags = R4 NodeType FirstFragment MoreFragments

% Fields
Bit : FirstFragment MoreFragments
Fix(2)/uint : NodeType
Fix(8)/uint : MessageType
Fix(16)/uint : DatagramID SourcePort DatagramLength PacketOffset
Fix(32) : SourceIP
Del(8,0x00)/halfascii : SourceName DestinationName
Set(0000) : R4
Len(*DatagramLength) : Datagram
