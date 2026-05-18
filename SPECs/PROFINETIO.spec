PROFINETIO = FrameHeader FramePayload

FrameHeader = FrameType Version Length SourceMAC DestinationMAC

FramePayload = ? case *FrameType
               | 34930 RealTimeCyclicData      
               | 35010 Alarm                    
               | 35012 RecordDataRequest
               | 35016 DCPRequest
               | 35032 RealTimeCyclicData   
               | 35048 IsochronousRealTimeData 
               ?

RealTimeCyclicData = SequenceNumber StatusPayload InputData OutputData
Alarm = AlarmType SubType DeviceID PayloadLength Payload
RecordDataRequest = RecordType RecordDataLength RecordData
RecordDataResponse = RecordType RecordDataLength RecordData ResultCode
DCPRequest = ServiceType BlockID BlockData
DCPResponse = ServiceType BlockID BlockData ResultCode
IsochronousRealTimeData = SequenceNumber StatusPayload InputData OutputData

% Fields
Fix(16)/uint : FrameType Version Length SequenceNumber StatusPayload RecordType RecordDataLength ServiceType BlockID ResultCode AlarmType SubType DeviceID PayloadLength
Fix(48)/ether : SourceMAC DestinationMAC
Len(*Length)/ascii : InputData OutputData Payload RecordData BlockData