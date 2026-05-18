ARP = HardwareType ProtocolType HardwareSize ProtocolSize Opcode SenderMACAddress SenderIPAddress TargetMACAddress TargetIPAddress

% Fields
Set(00000110,00001000) : HardwareSize 
Set(00000100,00010000) : ProtocolSize 
Fix(16)/uint : HardwareType ProtocolType Opcode
Len(*ProtocolSize) : SenderIPAddress TargetIPAddress
Len(*HardwareSize) : SenderMACAddress TargetMACAddress