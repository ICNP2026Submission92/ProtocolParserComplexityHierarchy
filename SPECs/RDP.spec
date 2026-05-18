RDP = PDUType Payload

Payload = ? case *PDUType
          | 1 ConnectionRequest
          | 2 ConnectionConfirm
          | 3 DataPDU
          | 4 ControlPDU
          | 5 SynchronizePDU
          | 6 ControlPDU
          | 7 DataPDU
          | 8 SynchronizePDU
          ?

ConnectionRequest = ClientVersion ClientFlags
ConnectionConfirm = ServerVersion ServerFlags
DataPDU = SequenceNumber DataLength Data
ControlPDU = SequenceNumber ControlType ControlData
SynchronizePDU = SequenceNumber

% Fields
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08)/uint : PDUType
Fix(16)/uint : SequenceNumber
Fix(32)/uint : ClientVersion ServerVersion DataLength
Fix(8)/uint  : ClientFlags ServerFlags ControlType
Len(*DataLength) : Data
EOF : ControlData