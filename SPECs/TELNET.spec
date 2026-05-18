TELNET = DataStream

DataStream = Byte CommandSequence            

CommandSequence = IAC Command Option

% Fields
Set(0xFF) : Byte
Fix(8)/uint : IAC Option
Del(8,00000000) : Command