InferredProtocolB = Type1 | Type2 ;
Type1 = '1' Fix(1) ;
Type2 = '0' Type3 ;
Type3 = '0' Fix(2) Fix(1) | '1' Fix(1) Fix(2) ;