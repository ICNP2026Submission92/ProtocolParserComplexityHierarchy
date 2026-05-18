SMTP = ? caset *STATE
     | 1 Response 2
     | 2 CommandLine 2
     | 3 Response 4
     | 4 Username 5
     | 5 Response 6
     | 6 Password 1
     ?

Response = Code Parameters

CommandLine = Command Parameters

Command = ? set STATE
        | "AUTH" 3
        | 1 ?

%Fields
Fix(32)/ascii : Code
Del(8,0x20)/ascii : Command
Rep(Parameter) : Parameters
Del(16,0x0d0a)/ascii : Parameter Username Password