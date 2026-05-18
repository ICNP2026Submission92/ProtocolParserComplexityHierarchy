MSNRPC = MessageID ProtocolOp Length Payload

Payload = ? case *ProtocolOp
          | 0 NetrServerAuthenticate3
          | 1 NetrServerPasswordSet2
          | 2 NetrServerPasswordGet2
          | 3 NetrServerTrustPasswordsGet
          | 4 NetrServerTrustPasswordsSet
          | 5 NetrLogonSamLogon
          | 6 NetrLogonSamLogoff
          | 7 NetrLogonSamLogonWithFlags
          | 8 NetrGetDomainInfo
          | 9 NetrEnumerateTrustedDomains
          | 10 NetrQueryInformationPolicy
          | 11 NetrSetInformationPolicy
          ?

NetrServerAuthenticate3 = AccountName SecureChannelType ComputerName ClientCredential ServerCredential
NetrServerPasswordSet2 = AccountName SecureChannelType ComputerName EncryptedPassword
NetrServerPasswordGet2 = AccountName SecureChannelType ComputerName
NetrServerTrustPasswordsGet = AccountName
NetrServerTrustPasswordsSet = AccountName PasswordData
NetrLogonSamLogon = LogonRequest
NetrLogonSamLogoff = LogoffRequest
NetrLogonSamLogonWithFlags = LogonRequest Flags
NetrGetDomainInfo = DomainName InfoClass
NetrEnumerateTrustedDomains = DomainController
NetrQueryInformationPolicy = PolicyHandle InformationClass
NetrSetInformationPolicy = PolicyHandle InformationClass PolicyData

% Fields
Fix(32)/uint : MessageID Flags AccountName SecureChannelType ComputerName InfoClass PolicyHandle Flags Length InformationClass
Len(*Length) : ClientCredential ServerCredential EncryptedPassword PasswordData LogonRequest LogoffRequest DomainName PolicyData DomainController
Set(0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B) : ProtocolOp