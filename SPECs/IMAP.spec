% Field Logic
IMAP = Command Response

Command = Tag CommandName Argument
Response = Tag Status ResponseCode Message

Argument =  Date Time 
Date = Day Month Year
Time = Hour Minute Second

% Fields
Fix(8)/uint : Tag CommandName Status Month Day Hour Minute Second SequenceNumber UIDNumber
Del(8,0x00)/ascii : Arguments ResponseCode Message Atom QuotedString Literal Flag MailboxName Text MailboxElement SearchKey MessageSet
Fix(16)/uint : Year
