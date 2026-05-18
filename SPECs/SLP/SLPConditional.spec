SLPConditional = Header Payload
Header = MsgType PktLength
Payload = ? case *MsgType 
        | 0 TurnOn 
        | 1 Brightness
        | 2 Colour ?
Colour = R G B

Fix(1) : TurnOn
Set(00,01,10) : MsgType
Fix(3)/uint : Brightness
Fix(6)/uint : PktLength
Fix(8)/uint : R G B