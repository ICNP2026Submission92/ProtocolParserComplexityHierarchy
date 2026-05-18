SDP = Version Origin SessionName SessionInformation URI Email Phone Connection Media

Media = MediaType Port Protocol Format
Format = PayloadType EncodingName ClockRate Channels

% Fields
Fix(8)/ascii : Version
Del(8,0x0a)/ascii : Origin SessionName SessionInformation URI Email Phone Connection MediaType Protocol EncodingName
Fix(16)/uint : Port ClockRate Channels
Fix(8)/uint : PayloadType