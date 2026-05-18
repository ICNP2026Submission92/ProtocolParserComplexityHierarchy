WINBOX = Header Payload

Header = Length CRC Flags

Payload = ? case *Flags
          | 1 Login
          | 2 Command
          | 3 Reply
          | 4 Notification
          ?

Login = Username Password
Command = CommandID CommandData
Reply = ReplyID ReplyData
Notification = NotificationID NotificationData

% Fields
Set(0x01,0x02,0x03,0x04) : Flags
Fix(32)/uint : Length CRC
Fix(8)/uint : Flags CommandID ReplyID NotificationID
Del(8,0x00)/ascii : Username Password
Len(*Length) : CommandData ReplyData NotificationData
