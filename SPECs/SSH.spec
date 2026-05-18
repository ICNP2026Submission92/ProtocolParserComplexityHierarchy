SSH = PacketLength MessageType Payload MAC PaddingLength Padding

Payload = ? case *MessageType
          | 20 KexInit
          | 21 NewKeys
          | 30 UserAuthRequest
          | 31 UserAuthFailure
          | 32 UserAuthSuccess
          | 50 ChannelOpen
          | 51 ChannelOpenConfirmation
          | 52 ChannelOpenFailure
          | 53 ChannelWindowAdjust
          | 54 ChannelData
          | 55 ChannelExtendedData
          | 60 ChannelEof
          | 61 ChannelClose
          | 62 ChannelRequest
          | 63 ChannelSuccess
          | 64 ChannelFailure
          ?

KexInit = Cookie KexAlgorithms ServerHostKeyAlgorithms EncryptionAlgorithms MacAlgorithms CompressionAlgorithms Languages FirstKexFollows R32
NewKeys = None
UserAuthRequest = Username ServiceName MethodName MethodDataLength MethodData
UserAuthFailure = AuthMethods PartialSuccess
UserAuthSuccess = None
ChannelOpen = ChannelType SenderChannel InitialWindowSize MaxPacketSize
ChannelOpenConfirmation = RecipientChannel SenderChannel InitialWindowSize MaxPacketSize
ChannelOpenFailure = RecipientChannel ReasonCode Description LanguageTag
ChannelWindowAdjust = RecipientChannel BytesToAdd
ChannelData = RecipientChannel Data
ChannelExtendedData = RecipientChannel DataTypeCode Data
ChannelEof = RecipientChannel
ChannelClose = RecipientChannel
ChannelRequest = RecipientChannel RequestType WantReply RequestData
ChannelSuccess = None
ChannelFailure = None

% Fields

Set(0x14,0x15,0x1e,0x1f,0x20,0x32,0x33,0x34,0x35,0x36,0x37,0x3c,0x3d,0x3e,0x3f,0x40) : MessageType
Bit : FirstKexFollows PartialSuccess WantReply
Fix(32)/uint : PacketLength NameListLength UsernameLength ServiceNameLength MethodNameLength MethodDataLength ChannelTypeLength DescriptionLength LanguageTagLength RequestTypeLength RequestDataLength SenderChannel RecipientChannel InitialWindowSize MaxPacketSize BytesToAdd ReasonCode DataTypeCode MAC
Fix(8)/uint : PaddingLength KexAlgorithms Cookie ServerHostKeyAlgorithms EncryptionAlgorithms MacAlgorithms CompressionAlgorithms Languages
Len(*PaddingLength) : Padding
Len(*MethodDataLength) : MethodData
Del(8,0x2c)/ascii : Name 
Del(8,0x00)/ascii : Username ServiceName MethodName ChannelType Description LanguageTag RequestType AuthMethods
EOF : None Data RequestData