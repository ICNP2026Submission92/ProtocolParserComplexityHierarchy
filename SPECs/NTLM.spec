NTLM = MessageType Length Payload

Payload = ? case *MessageType
          | 1 NegotiateMessage
          | 2 ChallengeMessage
          | 3 AuthenticateMessage
          | 4 SessionSetupMessage
          ?

NegotiateMessage = Flags WorkstationLen WorkstationMaxLen WorkstationBufferOffset

ChallengeMessage = TargetNameLen TargetNameMaxLen TargetNameBufferOffset ChallengeFlags TargetInfoLen TargetInfoMaxLen TargetInfoBufferOffset

AuthenticateMessage = LmChallengeResponseLen LmChallengeResponseMaxLen LmChallengeResponseBufferOffset NtChallengeResponseLen NtChallengeResponseMaxLen NtChallengeResponseBufferOffset UserNameLen UserNameMaxLen UserNameBufferOffset WorkstationLen WorkstationMaxLen WorkstationBufferOffset SessionKeyLen SessionKeyMaxLen SessionKeyBufferOffset

SessionSetupMessage = SessionFlags SessionKeyLen SessionKeyMaxLen SessionKeyBufferOffset

% Fields
Set(0x01,0x02,0x03,0x04) : MessageType
Fix(8)/uint : MessageType Length Flags SessionFlags UserNameBufferOffset WorkstationMaxLen WorkstationBufferOffset TargetNameLen TargetNameMaxLen TargetNameBufferOffset LmChallengeResponseBufferOffset NtChallengeResponseLen NtChallengeResponseMaxLen NtChallengeResponseBufferOffset UserNameLen UserNameMaxLen WorkstationMaxLen SessionKeyLen SessionKeyMaxLen SessionKeyBufferOffset ChallengeFlags TargetInfoLen TargetInfoMaxLen TargetInfoBufferOffset LmChallengeResponseLen LmChallengeResponseMaxLen
Len(*Length) : DomainName Workstation TargetName TargetInfo LmChallengeResponse NtChallengeResponse UserName SessionKey WorkstationLen
