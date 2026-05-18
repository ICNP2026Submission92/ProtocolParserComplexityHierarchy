EAPOL = Preamble Version Type Length Payload

% Fields
Fix(8)/uint : Preamble Version Type
Fix(16)/uint : Length
Len(*Length) : Payload
