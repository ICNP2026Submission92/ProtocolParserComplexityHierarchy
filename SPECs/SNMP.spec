SNMP = PDUType Payload

Payload = ? case *PDUType
          | 0 GetRequest
          | 1 GetNextRequest
          | 2 SetRequest
          | 3 GetResponse
          | 4 Trap
          | 5 GetBulkRequest
          | 6 InformRequest
          | 7 Report
          ?

GetRequest = RequestID ErrorStatus ErrorIndex VariableBindings
SetRequest = RequestID ErrorStatus ErrorIndex VariableBindings
GetNextRequest = RequestID ErrorStatus ErrorIndex VariableBindings
GetResponse = RequestID ErrorStatus ErrorIndex VariableBindings
Trap = Enterprise SpecificTrap TimeStamp VariableBindings
GetBulkRequest = RequestID NonRepeaters MaxRepetitions VariableBindings
InformRequest = RequestID ErrorStatus ErrorIndex VariableBindings
Report = RequestID ErrorStatus ErrorIndex VariableBindings

VariableBindings = ObjectIdentifier Value

Value = ? case *ObjectIdentifier
                  | 1 Gauge
                  | 2 TimeTicks
                  | 3 IpAddress
                  | 4 Integer
                  ?

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08) : PDUType
Set(0x01,0x02,0x03,0x04) : ObjectIdentifier
Fix(8)/uint : RequestID ErrorStatus ErrorIndex NonRepeaters MaxRepetitions SpecificTrap Enterprise
Fix(32)/uint : TimeStamp
Fix(32)/uint : Integer
Del(8,0x00)/ascii : Value
Fix(32)/ip4 : IpAddress
Fix(32)/uint : Gauge
Fix(32)/uint : TimeTicks