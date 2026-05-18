TCP = Header

Header = SrcPort DstPort SeqNum AckNum DataOffset Flags Window Checksum UrgentPointer

Flags = NS CWR ECE URG ACK PSH RST SYN FIN

% Fields
Fix(16)/uint : SrcPort DstPort
Fix(32)/uint : SeqNum AckNum
Fix(4)/uint  : DataOffset
Bit          : NS CWR ECE URG ACK PSH RST SYN FIN
Fix(16)/uint : Window Checksum UrgentPointer