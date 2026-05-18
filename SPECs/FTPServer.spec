% STATE -> 1

FTP = ? caset *STATE 
        | 1 Request 2
        | 2 Response 1 
        ?

Request = Command
Response = Code Argument

% Fields
Del(16,\x0d0a)/ascii : Command Argument
Fix(24)/ascii : Code