RTSP = Header Payload

Header = ClientAddress ServerAddress SequenceNumber MessageType

Payload = ? case *MessageType
| 0 OPTIONSRequest
| 1 OPTIONSResponse
| 2 DESCRIBERequest
| 3 DESCRIBEResponse
| 4 SETUPRequest
| 5 SETUPResponse
| 6 PLAYRequest
| 7 PLAYResponse
| 8 PAUSEREquest
| 9 PAUSEResponse
| 10 TEARDOWNRequest
| 11 TEARDOWNResponse
| 12 ANNOUNCERequest
| 13 ANNOUNCEResponse
| 14 RECORDRequest
| 15 RECORDResponse
| 16 GETPARAMETERRequest
| 17 GETPARAMETERResponse
| 18 SETPARAMETERRequest
| 19 SETPARAMETERResponse
?

OPTIONSRequest = CSeq
OPTIONSResponse = CSeq PublicHeader

DESCRIBERequest = CSeq Accept
DESCRIBEResponse = CSeq ContentLength ContentType EntityBody

SETUPRequest = CSeq Transport
SETUPResponse = CSeq SessionID Transport

PLAYRequest = CSeq SessionID Range
PLAYResponse = CSeq RTPInfo

PAUSEREquest = CSeq SessionID
PAUSEResponse = CSeq

TEARDOWNRequest = CSeq SessionID
TEARDOWNResponse = CSeq

ANNOUNCERequest = CSeq ContentLength ContentType EntityBody
ANNOUNCEResponse = CSeq

RECORDRequest = CSeq SessionID ContentLength EntityBody
RECORDResponse = CSeq

GETPARAMETERRequest = CSeq ParameterCount ParameterIDs
GETPARAMETERResponse = CSeq ParameterCount Parameters

SETPARAMETERRequest = CSeq ContentLength ContentType EntityBody
SETPARAMETERResponse = CSeq StatusCode

ParameterIDs = ParameterID^*ParameterCount
Parameters = Parameter^*ParameterCount
Parameter = ParameterID ParameterLength ParameterValue

% Fields

Fix(32)/uint : SequenceNumber CSeq ContentLength ParameterCount ParameterID ParameterLength MessageType StatusCode
Del(8,0x00)/ascii : Method RequestURI RTSPVersion HeaderValue EntityBody ParameterValue PublicHeader Accept Transport SessionID Range RTPInfo ContentType
Fix(32) : ClientAddress ServerAddress