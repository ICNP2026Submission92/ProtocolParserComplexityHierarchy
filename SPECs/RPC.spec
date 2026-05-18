RPC = MessageType Length Payload

Payload = ? case *MessageType
          | 0 CALL
          | 1 REPLY
          ?

CALL = RpcVersion Program ProgramVersion Procedure Credentials VerifierType Verifier ArgType Argument
REPLY = RpcVersion Accepted ReplyBody

Verifier = ? case *VerifierType
           | 0 VerifierNull
           | 1 VerifierSys
           | 2 VerifierShort
           | 3 VerifierDh
           | 4 VerifierKerb
           ?

Argument = ? case *ArgType
           | 0 ArgNull
           | 1 ArgInt
           | 2 ArgString
           | 3 ArgOpaque
           ?

% Fields
Set(0x00,0x01) : MessageType
Set(0x00,0x01,0x02,0x03,0x04) : VerifierType
Set(0x00,0x01,0x02,0x03) : ArgType


Bit : VerifierNull ArgNull Accepted
Fix(8)/uint : Length VerifierSys VerifierShort VerifierDh VerifierKerb ArgInt
Fix(32)/uint : RpcVersion Program ProgramVersion Procedure AuthType ReplyStat AcceptStat RejectStat
Del(8,0x00) : Credentials Verifier ArgString ArgOpaque ReplyBody