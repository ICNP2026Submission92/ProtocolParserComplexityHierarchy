KADM5 = MessageType Length Payload

Payload = ? case *MessageType
          | 1 CreatePrincipal
          | 2 ModifyPrincipal
          | 3 DeletePrincipal
          | 4 GetPrincipal
          | 5 ListPrincipals
          | 6 AddPolicy
          | 7 ModifyPolicy
          | 8 DeletePolicy
          | 9 GetPolicy
          | 10 ListPolicies
          ?

CreatePrincipal = PrincipalName PrincipalData
ModifyPrincipal = PrincipalName PrincipalData
DeletePrincipal = PrincipalName
GetPrincipal = PrincipalName
ListPrincipals = Filter
AddPolicy = PolicyName PolicyData
ModifyPolicy = PolicyName PolicyData
DeletePolicy = PolicyName
GetPolicy = PolicyName
ListPolicies = Filter

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A)/uint : MessageType 
Fix(16)/uint : Length
Len(*Length) : PrincipalName PolicyName Filter
EOF : PrincipalData PolicyData
