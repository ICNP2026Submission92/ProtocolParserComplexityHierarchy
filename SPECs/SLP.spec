SLP = PDUType Payload

Payload = ? case *PDUType
          | 1 ServiceRequest
          | 2 ServiceReply
          | 3 AttributeRequest
          | 4 AttributeReply
          | 5 ServiceRegistration
          | 6 ServiceDeregistration
          | 7 ServiceAcknowledgment
          | 8 Error
          ?

ServiceRequest = FunctionCode ScopeList ServiceType
ServiceReply = FunctionCode ErrorCode ServiceURLList
AttributeRequest = FunctionCode ServiceURL AttributeTypeList
AttributeReply = FunctionCode ErrorCode AttributeList
ServiceRegistration = FunctionCode ServiceURL AttributeList
ServiceDeregistration = FunctionCode ServiceURL
ServiceAcknowledgment = FunctionCode
Error = FunctionCode ErrorCode

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08) : PDUType FunctionCode
Fix(16)/uint : ErrorCode AttributeList ServiceURLList
Del(8,0x00)/ascii : ScopeList ServiceType ServiceURL AttributeTypeList AttributeType ValueList Value