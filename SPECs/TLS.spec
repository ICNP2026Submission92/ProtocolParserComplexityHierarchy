TLS = Record HandshakeType Handshake

Record = ContentType Version Length Fragment

Fragment = ? case *ContentType
           | 20 ChangeCipherSpec
           | 21 Alert
           | 22 Handshake
           | 23 ApplicationData
           ?

Handshake = ? case *HandshakeType
            | 1 ClientHello
            | 2 ServerHello
            ?

Alert = Level Description
ChangeCipherSpec = Message
ApplicationData = Data

ClientHello = Version Random SessionID CipherSuite Extensions
ServerHello = Version Random SessionID CipherSuite Extensions

% Fields
Set(0x14,0x15,0x06,0x17) : ContentType
Set(0x01,0x02) : HandshakeType
Fix(8)/uint : Level Description CompressionMethod ServerHelloDone CertificateVerify Finished Certificate ServerKeyExchange CertificateRequest ClientKeyExchange
Fix(16)/uint : Version Length CipherSuite Random SessionID
Len(*Length) : Data Message CipherSuites
EOF : Extensions