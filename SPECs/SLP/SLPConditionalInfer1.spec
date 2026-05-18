SLPConditionalInfer1 = F1 Payload
Payload = ? case *F1 
        | 9 F2 
        | 73 F3
        | 160 Colour ?
Colour = R G B

Set(00001001,10100000,01001001) : F1
Set(1) : F2
Set(001,100) : F3
Fix(8)/uint : R G B