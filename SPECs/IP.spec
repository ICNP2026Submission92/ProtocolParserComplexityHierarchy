% Field Logic
IP = Header
Header = Version IHL DSCP ECN TotalLength Identification Flags FragmentOffset TTL Protocol HeaderChecksum SrcIP DstIP

% Fields
Set(0100) : Version
Fix(4)/uint : IHL
Fix(6)/uint : DSCP
Fix(2)/uint : ECN
Fix(16)/uint : TotalLength Identification
Fix(3)/uint : Flags
Fix(13)/uint : FragmentOffset
Fix(8)/uint : TTL Protocol
Fix(16)/uint : HeaderChecksum
Fix(32)/uint : SrcIP DstIP