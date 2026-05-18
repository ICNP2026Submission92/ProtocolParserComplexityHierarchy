SMB2 = Header Payload BlobOffset BlobLength SecurityBlob
Header = ProtocolId HeaderLength CreditCharge NTStatus Command CreditsGranted Flags ChainOffset MessageID ProcessID TreeID SessionID
Flags = R2 ReplayOperation DFSOperation R25 Priority Signing Chained AsyncCommand Response

Payload = ? case *Command 
        | 0 NegotiateProtocol
        | 1 SessionSetup
        ?

NegotiateProtocol = StructureSize SecurityMode Dialect R8 ServerGUID Capabilities MaxTransactionSize MaxReadSize MaxWriteSize CurrentTime BootTime
StructureSize = FixPartLength DynamicPart
SecurityMode = R6 SigningRequired SigningEnabled
Capabilities = R24 Notifications Encryption Directory PersistentHandles MultiChannel LargeMTU Leasing DFS
SecurityBlob = OID SimpleProtectedNegotiation
SimpleProtectedNegotiation = MechTypes HintName

SessionSetup = StructureSize SessionFlags
SessionFlags = R13 Guest Null Encrypt

% Fields
Bit : ReplayOperation DFSOperation Signing Chained AsyncCommand Response Guest Null Encrypt DynamicPart SigningRequired SigningEnabled Notifications Encryption Directory PersistentHandles MultiChannel LargeMTU Leasing DFS
Fix(3) : Priority
Fix(15)/uint/LE : FixPartLength
Fix(16)/uint/LE : HeaderLength CreditCharge Command CreditsGranted Dialect
Fix(8) : ProtocolId NTStatus ChainOffset ProcessID TreeID Capabilities MaxTransactionSize MaxReadSize MaxWriteSize BlobOffset BlobLength
Fix(6) : ServerGUID SessionID CurrentTime BootTime
Fix(64)/uint/LE : MessageID
Fix(8)/uint : OID MechTypes HintName