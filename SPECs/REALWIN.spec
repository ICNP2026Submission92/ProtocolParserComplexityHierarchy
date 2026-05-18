REALWIN = MessageType Length Payload

Payload = ? case *MessageType
          | 1 FcConnectFcsLogin
          | 2 FcCtaglistFcsCaddtag
          | 3 FcCtaglistFcsCdeltag
          | 4 FcCtaglistFcsAddtagms
          | 5 FcRfuserFcsLogin
          | 6 FcBinfileFcsFile
          | 7 FcCgettagFcsGettelemetry
          | 8 FcCgettagFcsGetchanneltelemetry
          | 9 FcCgettagFcsSettelemetry
          | 10 FcCgettagFcsSetchanneltelemetry
          | 11 FcScriptFcsStartprog
          ?

FcConnectFcsLogin = Username Password
FcCtaglistFcsCaddtag = TagName TagValue
FcCtaglistFcsCdeltag = TagName
FcCtaglistFcsAddtagms = TagName TagValue
FcRfuserFcsLogin = Username Password
FcBinfileFcsFile = FileName FileData
FcCgettagFcsGettelemetry = TagName
FcCgettagFcsGetchanneltelemetry = ChannelName
FcCgettagFcsSettelemetry = TagName TagValue
FcCgettagFcsSetchanneltelemetry = ChannelName ChannelValue
FcScriptFcsStartprog = ProgramName Parameters

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b) : MessageType
Fix(8)/uint : Length
Del(8,0x00) : Payload Username Password TagName TagValue FileName FileData ChannelName ChannelValue ProgramName Parameters