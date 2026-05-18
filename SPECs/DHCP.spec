DHCP = MessageType HardwareType HardwareAddressLength Hops TransactionID SecondsElapsed BootpFlags ClientIPAddress YourClientIPAddress NextServerIPAddress RelayAgentIPAddress ClientMACAddress ClientHardwareAddressPadding MagicCookie ServerHostName BootFileName DHCPOptions Padding
BootpFlags = BroadcastFlag ReservedFlags

% Fields
Bit  : BroadcastFlag ServerDDNS Encoding ServerOverrides Server
Fix(8)/uint  : Hops NumOptions Option
Fix(16)/uint : SecondsElapsed
Fix(32)      : TransactionID
Fix(32)/ip4  : ClientIPAddress YourClientIPAddress NextServerIPAddress RelayAgentIPAddress
Len(*HardwareAddressLength) : ClientMACAddress
Fix(80)      : ClientHardwareAddressPadding
Fix(512)     : ServerHostName             
Fix(1024)    : BootFileName  
Fix(32)      : MagicCookie
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,0x10,0x11,0x12) : MessageType
Set(0x01) : HardwareType
Set(0x06) : HardwareAddressLength
Set(0x0000) : ReservedFlags
Fix(8)/uint : OptionCode OptionLength
Del(8,0xff) : DHCPOptions
EOF : Padding
