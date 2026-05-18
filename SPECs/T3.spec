T3 = Header Payload

Header = ProtocolVersion MessageType PacketLength HeaderChecksum Flags

Payload = ? case *MessageType
          | 1 Request
          | 2 Response
          | 3 Ping
          | 4 Pong
          ?

Request = RequestID Operation Parameters
Response = ResponseID Status Data
Ping = None
Pong = None

% Fields
Set(0x0001,0x0002,0x0003,0x0004)/uint : MessageType
Fix(16)/uint : ProtocolVersion PacketLength HeaderChecksum Flags RequestID ResponseID Status Operation
Len(*PacketLength) : Parameters Data
EOF : None