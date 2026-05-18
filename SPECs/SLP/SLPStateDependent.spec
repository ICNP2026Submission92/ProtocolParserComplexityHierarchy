% State -> 1

SLPStateDependent = Header Payload ;
Header = PktLength  TurnOn ;
Payload = ? case *State 
        | 1 = ManyBrightness % State -> 2
        | 2 = Colour ? ; % State -> 1
ManyBrightness =  Repeats Brightness^*Repeats ;
Colour = R G B ;

Repeats = Brightness = Fix(3)/uint ;
PktLength = Fix(6)/uint ;
TurnOn = Fix(1) ;
R = G = B = Fix(8)/uint ;