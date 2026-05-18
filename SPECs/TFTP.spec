TFTP = Opcode Payload

Payload = ? case *Opcode
          | 1 ReadRequest
          | 2 WriteRequest
          | 3 DataPacket
          | 4 Acknowledgement
          | 5 Error
          | 6 Options
          ?

ReadRequest = SourceFile Type Options
WriteRequest = SourceFile Type Options
DataPacket = Block Data
Acknowledgement = Block
Options = Name Value
Error = ErrorCode ErrorMessage

% Fields
Set(0x0001,0x0002,0x0003,0x0004,0x0005,0x0006) : Opcode
Fix(16)/uint : Block ErrorCode
Del(8,0x00)/ascii : SourceFile Type Name Value ErrorMessage
EOF : Data
