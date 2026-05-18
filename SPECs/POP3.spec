POP3 = Command Payload

Payload = ? case *Command
          | 1431520594 USER
          | 1346458451 PASS
          | 1398030676 STAT
          | 1279873876 LIST
          | 1380275282 RETR
          | 1145392197 DELE
          | 1313820496 NOOP
          | 1381188948 RSET
          | 1414483968 TOP
          | 1430864972 UIDL
          | 1128353857 CAPA
          | 1364543828 QUIT
          ?

USER = Username
PASS = Password
STAT = Empty
LIST = Empty
RETR = MessageNumber
DELE = MessageNumber
NOOP = Empty
RSET = Empty
TOP = MessageNumber Lines
UIDL = Empty
CAPA = Empty
QUIT = Empty

% Fields
Set(0x55534552,0x50415353,0x53544154,0x4c495354,0x52455452,0x44454c45,0x4e4f4f50,0x52534554,0x544f5000,0x5549444c,0x43415041,0x51554954)/uint : Command
Fix(32)/uint : MessageNumber Lines
Del(8,0x00)/ascii : Username Password
EOF : Empty