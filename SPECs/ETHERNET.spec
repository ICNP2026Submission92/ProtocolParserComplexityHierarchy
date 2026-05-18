ETHERNET = Destination Source TPID Optional

Optional = ? case *TPID
          | 0 VLANTag
          | 1 None
          ?
                    
VLANTag = TCI Type Length

% Fields
Fix(48)/ether : Destination Source
Set(0000000000000000,0000000000000001) : TPID
Fix(16)/uint : Type Length TCI
EOF : None
