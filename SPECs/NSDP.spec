NSDP = Header Payload

Header = MACAddress IPAddress SequenceNumber MessageType

Payload = ? case *MessageType
          | 0 DiscoveryRequest
          | 1 DiscoveryResponse
          | 2 DeviceConfigurationRequest
          | 3 DeviceConfigurationResponse
          | 4 SetParameterRequest
          | 5 SetParameterResponse
          | 6 GetParameterRequest
          | 7 GetParameterResponse
          ?

DiscoveryRequest = DeviceType
DiscoveryResponse = DeviceType DeviceName FirmwareVersion IPAddress SubnetMask Gateway MACAddress
DeviceConfigurationRequest = DeviceType ParameterCount ParameterValue^*ParameterCount
DeviceConfigurationResponse = DeviceType ParameterCount ParameterValue^*ParameterCount
SetParameterRequest = DeviceType ParameterCount ParameterValue^*ParameterCount
SetParameterResponse = StatusCode
GetParameterRequest = DeviceType ParameterCount ParameterID^*ParameterCount
GetParameterResponse = DeviceType ParameterCount ParameterValue^*ParameterCount

% Fields
Set(0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07) : MessageType
Fix(16)/uint : ParameterCount
Fix(32)/uint : SequenceNumber StatusCode ParameterID ParameterLength
Del(8,0x00)/ascii : DeviceType DeviceName FirmwareVersion ParameterValue
Fix(32) : IPAddress SubnetMask Gateway
Fix(48)/ether : MACAddress