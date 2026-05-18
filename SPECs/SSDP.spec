SSDP = MessageType StartLine Header CRLF

Header = Name Value

StartLine = ? case *MessageType
            | 1 RequestLine
            | 2 StatusLine
            ?

RequestLine = Method URI Version
StatusLine = Version StatusCode ReasonPhrase

% Fields
Set(0x01,0x02) : MessageType
Del(8,0x20)/ascii : Method URI Version Name Value ReasonPhrase
Fix(16)/uint : StatusCode
Set(0x0d0a) : CRLF
