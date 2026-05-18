SLPConditionalInfer2 = F1 Payload
Payload = ? case *F1 
        | 9 F2 
        | 73 F3
        | 160 Colour ?
Colour = R G B

Set(00001001,10100000,01001001) : F1
Del(1,1) : F2
Fix(3) : F3
Fix(8)/uint : R G B