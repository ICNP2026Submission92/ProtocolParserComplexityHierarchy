S7Comm = Header Errors Parameter Data
Header = ProtocolId ROSCTR RedundancyIdentification ProtocolDataUnit ParameterLength DataLength

Errors = ErrorClass ErrorCode
Data = ? case *Parameter
        | 0 CPUServices
        | 4 ReadVar
        | 240 SetupCommunication
        ?

CPUServices = ItemCount VariableSpecification LengthOfAddress SyntaxID Type FunctionGroup Subfunction SequenceNumber DataUnitErrors CPUServicesData

DataUnitErrors = DataUnitReference LastDataUnit ErrorCode
CPUServicesData = ReturnCode TransportSize Length 

ReadSZLPayload = SZLId SZLIndex
SZLId = DiagnosticType NumberOfPartialListExtract NumberOfPartialList
S7TimeStamp = Reserved Year1 Year2 Month Day Hour Minute Second Milliseconds Weekday

SetupCommunication = Reserved MaxAmQCalling MaxAmQCalled PDULength

ReadVar = ItemCount ReadVarData
ReadVarData = ItemCount Item^*ItemCount
Substructure = LIDFlags Value

% Fields
Fix(2)/uint : Type
Fix(4) : DiagnosticType NumberOfPartialListExtract Weekday
Fix(6)/uint : FunctionGroup
Fix(8) : ProtocolId  ErrorClass ErrorCode VariableSpecification SyntaxID ReturnCode TransportSize NumberOfPartialList Reserved
Fix(8)/uint : ROSCTR ItemCount LengthOfAddress Subfunction SequenceNumber Length Parameter
Fix(8)/hexint :  Year1 Year2 Month Day Hour Minute Second
Fix(12)/hexint : Milliseconds
Fix(16) : RedundancyIdentification SZLIndex
Fix(16)/uint : ProtocolDataUnit  ParameterLength  DataLength MaxAmQCalling MaxAmQCalled PDULength DataUnitReference LastDataUnit Item