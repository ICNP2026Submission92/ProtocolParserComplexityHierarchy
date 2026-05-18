% Field Logic
IKE = MessageHeader Payload

MessageHeader = InitiatorSPI ResponderSPI NextPayload Reserved Length

Payload = ? case *NextPayload
        | 1 SecurityAssociation
        | 2 Proposal
        | 3 Transform
        | 4 KeyExchange
        | 5 Identification
        | 6 CertificateRequest
        | 7 Certificate
        | 8 CertificateStatus
        | 9 Hash
        | 10 Signature
        | 11 Nonce
        | 12 Notification
        | 13 Delete
        | 14 VendorID
        | 15 TrafficSelector
        | 16 Encrypted
        ?

% Fields
Fix(32)/uint : InitiatorSPI ResponderSPI
Fix(8)/uint : Reserved
Set(0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10)/uint : NextPayload
Fix(16)/uint : Length
EOF : SecurityAssociation Proposal Transform KeyExchange Identification CertificateRequest Certificate CertificateStatus Hash Signature Nonce Notification Delete VendorID TrafficSelector Encrypted