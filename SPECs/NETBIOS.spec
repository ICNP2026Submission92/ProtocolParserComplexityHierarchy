NETBIOS = Header Payload

Header = MessageType Flags Length

Payload = ? case *MessageType
          | 0 NameQueryRequest
          | 1 NameQueryResponse
          | 2 NameRegistrationRequest
          | 3 NameRegistrationResponse
          | 4 NameReleaseRequest
          | 5 NameReleaseResponse
          | 6 Datagram
          | 7 SessionMessage
          | 8 SessionRequest
          | 9 SessionPositiveResponse
          | 10 SessionNegativeResponse
          | 11 SessionRetargetResponse
          ?

NameQueryRequest = CalledName CallingName QuestionType QuestionClass
NameQueryResponse = CalledName CallingName ResponseFlags TTL ResourceRecordsCount ResourceRecords
NameRegistrationRequest = NameFlags NameAddressType Name
NameRegistrationResponse = ResultCode
NameReleaseRequest = NameFlags NameAddressType Name
NameReleaseResponse = ResultCode

Datagram = SourceName DestinationName Data
SessionMessage = Data
SessionRequest = CalledName CallingName
SessionPositiveResponse = SessionID
SessionNegativeResponse = ErrorCode
SessionRetargetResponse = NewAddress

% Fields
Set(0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B) : MessageType
Fix(8)/uint  : Flags NameFlags NameAddressType QuestionType QuestionClass ResultCode ErrorCode ResponseFlags
Fix(16)/uint : Length TTL ResourceRecordsCount SessionID
Len(*Length)/ascii : CalledName CallingName Name Data ResourceRecords NewAddress SourceName DestinationName