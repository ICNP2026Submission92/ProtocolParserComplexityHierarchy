SSRP = Header Payload

Header = Version PacketLength PacketType

Payload = ? case *PacketType
          | 0x01 Request
          | 0x02 Response
          ?

Request = RequestType Instance
Response = ResponseType

Instance = Name TCPPort UDPPort Flags

% Fields
Set(0x01,0x02) : PacketType
Fix(8)/uint : Version PacketType RequestType ResponseType Flags
Fix(16)/uint : PacketLength TCPPort UDPPort
Del(8,0x00)/ascii : Name