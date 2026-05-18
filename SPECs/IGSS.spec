% Field Logic
IGSS = Header Payload

Header = MessageType MessageLength SourceID DestinationID Timestamp

Payload = ? case *MessageType
    | 1 ReadRequest
    | 2 WriteRequest
    | 3 DataPacket
    | 4 Acknowledgement
    | 5 Error
    | 6 Option
    ?

ReadRequest = Address Quantity
WriteRequest = Address Value
DataPacket = Data
Acknowledgement = Status
Error = ErrorCode ErrorMessage
Option = OptionType OptionValue

% Fields
Fix(8)/uint : MessageType Status OptionType
Fix(16)/uint : MessageLength ErrorCode
Fix(32)/uint : SourceID DestinationID Quantity Value
Fix(64)/uint : Timestamp
Fix(16)/uint : Address
EOF : Data
Del(8,0x00)/ascii : ErrorMessage OptionValue
