% Field Logic
CSI = DiscoveryMessage ConfigurationAssignment ImageAssignment DownloadProcess Activation

DiscoveryMessage = ClientID DirectorIP
ConfigurationAssignment = ConfigFileName ConfigFileSize
ImageAssignment = ImageFileName ImageFileSize
DownloadProcess = TFTPServerIP DownloadStatus
Activation = RebootFlag

% Fields
Fix(32)/ascii : ClientID
Fix(32)/ip4 : DirectorIP TFTPServerIP
Fix(64)/ascii : ConfigFileName ImageFileName
Fix(32)/uint : ConfigFileSize ImageFileSize
Fix(8)/uint : DownloadStatus
Bit : RebootFlag
