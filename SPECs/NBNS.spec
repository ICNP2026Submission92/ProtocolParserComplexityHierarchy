NBNS = Header Payload
Header = TransactionID Flags NumQuestions NumAnswerRRs NumAuthorityRRs NumAdditionalRRs
Flags = Response Opcode Reserved TC RD R3 Broadcast R4
Payload = Questions AnswerRRs
Questions = Question^*NumQuestions
Question = Name
AnswerRRs = RR^*NumAnswerRRs
RR = Name

% Fields
Bit : Reserved TC RD Broadcast Response
Set(000) : R3
Set(0000) : R4
Fix(4) : Opcode
Fix(16) : Type Class
Fix(16)/uint : TransactionID NumQuestions NumAnswerRRs NumAuthorityRRs NumAdditionalRRs
Fix(32)/uint : TTL
Len(Fix(16),uint) : RData
Del(8,0x00)/halfascii : Name