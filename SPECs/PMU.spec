PMU = Header Payload Checksum
Header = SynchronizationWord Framesize PMUIdNumber SOCTimeStamp TimeQualityFlags FractionOfSecond PhasorData
SynchronizationWord = R9 FrameType Version
TimeQualityFlags = R1 LeapSecondDirection LeapSecondOccurred LeapSecondPending QualityIndicatorCode

Payload = ? case *FrameType 
        | 0 DataFrame
        | 3 ConfigurationFrame 
        | 4 CommandFrame
        ?

DataFrame = StationMeasurement
StationMeasurement = Flags FrequencyDeviation RateOfChange
Flags = DataError TimeSynchronized DataSorting TriggerDetected ConfigurationChanged DataModifiedIndicator PMUTimeQuality UnlockedTime TriggerReason
ConfigurationFrame = ResolutionOfFractionalSecond NumberOfPMUBlocks Station RateOfTransmission
CommandFrame = Command
Station = DataSourceID DataFormat NumPhasors NumAnalogValues NumDigitalStatusWords PhasorName^*NumPhasors PhasorConversionFactors NominalLineFrequency ConfigurationChangeCount
DataFormat = R12 FreqFormat AnalogValues PhasorFormat PhasorNotation

% Fields
Bit : FreqFormat AnalogValues PhasorFormat PhasorNotation LeapSecondDirection LeapSecondOccurred LeapSecondPending TimeSynchronized DataSorting TriggerDetected ConfigurationChanged DataModifiedIndicator UnlockedTime
Set(0) : R4
Fix(2) : DataError
Fix(3) : PMUTimeQuality
Set(000,011,100) : FrameType
Fix(4) : Version QualityIndicatorCode TriggerReason PhasorConversionFactors NominalLineFrequency
Fix(16) : Checksum Command ResolutionOfFractionalSecond NumberOfPMUBlocks DataSourceID RateOfTransmission
Fix(16)/uint : NumPhasors FrequencyDeviation RateOfChange NumAnalogValues NumDigitalStatusWords Framesize PMUIdNumber FractionOfSecond ConfigurationChangeCount
Fix(32)/unix : SOCTimeStamp
Len(*Framesize) : PhasorData
Fix(64)/ascii : PhasorName
