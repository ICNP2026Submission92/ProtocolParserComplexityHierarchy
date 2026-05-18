DNS = Header Payload
Header = TransactionID Flags NumQuestions NumAnswerRRs NumAuthorityRRs NumAdditionalRRs
Flags = QR Opcode AA TC RD RA Zero RCode
Payload = Questions AnswerRRs
Questions = Question^*NumQuestions
AnswerRRs = RR^*NumAnswerRRs

% Fields
Bit : QR AA TC RD RA
Set(000) : Zero
Set(0000,0001,0010) : Opcode
Set(0000,0001,0010,0011,0100,0101) : RCode
Fix(16)/uint : TransactionID
Set(0x00,0x01) : NumQuestions NumAnswerRRs NumAuthorityRRs NumAdditionalRRs
Del(8,00000000)/ascii : Question RR