SLPRecursive = TurnOn ManyBrightness Colour
ManyBrightness = Repeats Brightness^*Repeats
Colour = R G B

Fix(1) : TurnOn
Fix(3)/uint : Repeats
Del(8,00000000)/ascii : Brightness
Fix(8)/uint : R G B