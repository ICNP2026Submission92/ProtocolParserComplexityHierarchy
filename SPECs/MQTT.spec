MQTT = MessageType MsgLen Payload

PublishFlags = DUPFlag QosLevel Retain
SubscribeRequestFlags = DUPFlag QosLevel R1


Payload = ? case *MessageType 
        | 1 ConnectMessage
        | 2 ConnectAck
        | 3 PublishMessage
        | 8 SubscribeRequest
        | 12 PingRequest
        | 13 PingResponse
        ?

ConnectMessage = Version ConnectFlags KeepAlive ClientIDLen
ConnectAck = ReservedByte ReturnCode
PublishMessage = PublishFlags TopicLen Message
SubscribeRequest = SubscribeRequestFlags MessageIdentifier TopicLen RequestedQos

ConnectFlags = UserName Password WillRetain QosLevel Will CleanSession R1

% Fields
Bit : DUPFlag UserName Password WillRetain Will CleanSession Retain
Set(0) : R1 PingRequest PingResponse
Fix(2)/uint : QosLevel
Set(0001,0010,0011,1000,1100,1101)/uint : MessageType
Fix(8) : ReservedByte
Fix(8)/uint : MsgLen Version MessageIdentifier RequestedQos
Fix(16)/uint : KeepAlive ReturnCode TopicLen ClientIDLen ProtocolNameLen
EOF : Message