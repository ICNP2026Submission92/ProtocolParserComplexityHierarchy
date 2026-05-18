CVS = Command Payload

Payload = ? case *Command
          | 1 Root
          | 2 ValidResponses
          | 3 UseUnchanged
          | 4 Argument
          | 5 Request
          | 6 Response
          ?

Root = RepositoryPath
ValidResponses = ResponseType
UseUnchanged = Flag
Argument = Key Value
Request = FileName
Response = FileName

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06)/uint : Command
Del(16,0x0a0d)/ascii : RepositoryPath ResponseType Flag Key Value ModuleName FileName Revision ErrorMessage
Bit : ConflictFlags