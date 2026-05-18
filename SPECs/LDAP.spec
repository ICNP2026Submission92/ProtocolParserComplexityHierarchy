LDAP = MessageID ProtocolOp ControlsCount Payload

ControlsCount = R8

Payload = ? case *ProtocolOp
          | 0 BindRequest
          | 1 BindResponse
          | 2 UnbindRequest
          | 3 SearchRequest
          | 4 SearchResultEntry
          | 5 SearchResultDone
          | 6 SearchResultReference
          | 7 ModifyRequest
          | 8 ModifyResponse
          | 9 AddRequest
          | 10 AddResponse
          | 11 DelRequest
          | 12 DelResponse
          | 13 ModifyDNRequest
          | 14 ModifyDNResponse
          | 15 CompareRequest
          | 16 CompareResponse
          | 17 AbandonRequest
          | 18 ExtendedRequest
          | 19 ExtendedResponse
          | 20 IntermediateResponse
          ?

BindRequest = Version Name Authentication
BindResponse = ResultCode MatchedDN DiagnosticMessage Referral
UnbindRequest = Empty

SearchRequest = BaseObject Scope DerefAliases SizeLimit TimeLimit TypesOnly Filter AttributesCount Attributes
SearchResultEntry = ObjectName PartialAttributesCount PartialAttributes
SearchResultDone = ResultCode MatchedDN DiagnosticMessage Referral
SearchResultReference = URIListCount URIList

ModifyRequest = Object ChangesCount Changes
ModifyResponse = ResultCode MatchedDN DiagnosticMessage Referral

AddRequest = Entry DistinguishedName AttributesCount Attributes
AddResponse = ResultCode MatchedDN DiagnosticMessage Referral

DelRequest = DistinguishedName
DelResponse = ResultCode MatchedDN DiagnosticMessage Referral

ModifyDNRequest = Entry DistinguishedName NewRDN DeleteOldRDN NewSuperior
ModifyDNResponse = ResultCode MatchedDN DiagnosticMessage Referral

CompareRequest = Entry AttributeValueAssertion
CompareResponse = ResultCode MatchedDN DiagnosticMessage Referral

AbandonRequest = AbandonMessageID

ExtendedRequest = RequestName RequestValue
ExtendedResponse = ResultCode MatchedDN DiagnosticMessage Referral ResponseName ResponseValue

IntermediateResponse = ResponseName ResponseValue

% Fields
Fix(32)/uint        : MessageID Version SizeLimit TimeLimit ResultCode ControlsCount AttributesCount PartialAttributesCount URIListCount ChangesCount AbandonMessageID
Fix(64)/uint : Name Authentication BaseObject Scope DerefAliases TypesOnly Filter Attributes ObjectName PartialAttributes Referral URIList Object Changes Entry DistinguishedName NewRDN DeleteOldRDN NewSuperior AttributeValueAssertion RequestName RequestValue ResponseName ResponseValue MatchedDN DiagnosticMessage
EOF : Empty
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,0x10,0x11,0x12,0x13,0x14) : ProtocolOp