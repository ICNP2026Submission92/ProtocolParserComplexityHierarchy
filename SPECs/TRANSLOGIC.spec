TRANSLOGIC = MessageType Payload

Payload = ? case *MessageType
          | 1 SendRequest
          | 2 ReceiveRequest
          | 3 StatusUpdate
          | 4 ErrorReport
          ?

SendRequest = SenderID ReceiverID CarrierID Timestamp
ReceiveRequest = ReceiverID CarrierID Timestamp
StatusUpdate = CarrierID StatusCode Timestamp
ErrorReport = CarrierID ErrorCode Timestamp

% Fields
Set(0x01,0x02,0x03,0x04) : MessageType
Fix(16)/uint : SenderID ReceiverID CarrierID StatusCode ErrorCode
Fix(32)/uint : Timestamp