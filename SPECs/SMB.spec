SMB = Header TransRequest
Header = Command ErrorClass R8 ErrorCode Flags Flags2 ProcessIDHigh R64 TreeID ProcessID UserID MultiplexID
Flags = RequestResponse Notify Oplocks CanonicalizedPathnames CaseSensitivity ReceiveBuggerPosted LockAndRead
Flags2 = UnicodeStrings ErrorCodeType ExecuteOnlyReads Dfs ExtendedSecurityNegotiation ReparsePath R3 LongNamesUsed SecuritySignaturesRequired ExtendedAttributes LongNamesAllowed

TransRequest = WordCount TotalParameterCount TotalDataCount MaxParameterCount MaxDataCount MaxSetupCount R8 TransFlags Timeout R16 ParameterCount ParameterOffset DataCount DataOffset SetupCount Setup R8 ByteCount TransactionName
TransFlags = R14 OneWayTransaction DisconnectTID

% Fields
Bit : RequestResponse Notify Oplocks CanonicalizedPathnames CaseSensitivity ReceiveBuggerPosted LockAndRead UnicodeStrings ErrorCodeType ExecuteOnlyReads Dfs ExtendedSecurityNegotiation ReparsePath LongNamesUsed SecuritySignaturesRequired ExtendedAttributes LongNamesAllowed OneWayTransaction DisconnectTID
Fix(8)/uint : WordCount MaxSetupCount SetupCount
Fix(16) : Command ErrorClass ParameterCount ParameterOffset DataCount DataOffset
Fix(16)/uint : ProcessIDHigh TreeID ProcessID UserID MultiplexID TotalParameterCount TotalDataCount MaxParameterCount MaxDataCount ByteCount
Fix(32) : ErrorCode Timeout
Del(8,0x00)/ascii : TransactionName
Len(*SetupCount) : Setup
