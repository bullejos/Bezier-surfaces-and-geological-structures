
from functions import *
DATADIR='data/' # Directory with the data
CSV='data/csv/'

# C1

ControlC1_3=pd.read_csv(DATADIR+'control/C1_3_v1.csv')

bsC1_3=bezier(ControlC1_3.loc[:19],5)
tC1_3=traza2([bsC1_3],verde_c,'C1_3','C1',False)

bsC1_3c=bezier(ControlC1_3.loc[15:],5)
tC1_3c=traza2([bsC1_3c],verde_c,'C1_3c','C1',False)

Control1_C1_31=pd.read_csv(DATADIR+'control/Control1_C1_31_v10.csv')

Control15_31=pd.read_csv(DATADIR+'control/control15_C1_31.csv')
Control15_32=pd.read_csv(DATADIR+'control/control15_C1_32_v3.csv')

Control2_C1_31=pd.read_csv(DATADIR+'control/Control2_C1_31_v10.csv')
Control2_C1_32=pd.read_csv(DATADIR+'control/Control2_C1_32_v12.csv')

Control3_C1_31=pd.read_csv(DATADIR+'control/Control3_C1_31_v10.csv')
Control3_C1_32=pd.read_csv(DATADIR+'control/Control3_C1_32_v10.csv')

Control4_C1_31=pd.read_csv(DATADIR+'control/Control4_C1_31_v10.csv')
Control4_C1_32=pd.read_csv(DATADIR+'control/Control4_C1_32_v10.csv')

Control5_C1_31=pd.read_csv(DATADIR+'control/Control5_C1_31_v10.csv')
Control5_C1_32=pd.read_csv(DATADIR+'control/Control5_C1_32_v10.csv')

Control6_C1_31=pd.read_csv(DATADIR+'control/Control6_C1_31_v10.csv')
Control6_C1_32=pd.read_csv(DATADIR+'control/Control6_C1_32_v10.csv')


C1_31c=pd.concat([Control15_31,Control2_C1_31, Control3_C1_31, Control4_C1_31,Control5_C1_31,Control6_C1_31], axis=0)

C1_32c=pd.concat([Control15_32,Control2_C1_32, Control3_C1_32, Control4_C1_32,Control5_C1_32,Control6_C1_32], axis=0)

bsC1_31c=bezier(C1_31c,4)
tC1_31c=traza2([bsC1_31c],verde_c,'C1_31c','C1',False)

bsC1_32c=bezier(C1_32c,4)
tC1_32c=traza2([bsC1_32c],verde_c,'C1_32c','C1',False)

acopleC1_31=acople2(ControlC1_3.loc[15:],C1_31c,5,4)
tacopleC1_31=traza2([acopleC1_31],verde_c,'C1_31ca','C1',False)

acopleC1_312=acople2(C1_31c,C1_32c,4,4)
tacopleC1_312=traza2([acopleC1_312],verde_c,'C1_312ca','C1',False)

cunaC13=pd.read_csv(DATADIR+'control/cunaC13.csv')
bscunaC13=bezier(cunaC13,8)
tcunaC13=traza2([bscunaC13],verde_c,'cunaC13','C1',False)

tC13=tC1_3+tC1_3c+tC1_31c+tacopleC1_31+tC1_32c+tacopleC1_312+tcunaC13

# C2

Control0_C2_3=pd.read_csv(DATADIR+'control/Control0_C2_3_v10.csv')
Control1_C2_3=pd.read_csv(DATADIR+'control/Control1_C2_3_v10.csv')
Control15_C2_3=pd.read_csv(DATADIR+'control/Control15_C2_3.csv')
Control2_C2_3=pd.read_csv(DATADIR+'control/Control2_C2_3_v10.csv')
Control25_C2_3=pd.read_csv(DATADIR+'control/Control25_C2_3.csv')
Control3_C2_3=pd.read_csv(DATADIR+'control/Control3_C2_3_v10.csv')
Control4_C2_3=pd.read_csv(DATADIR+'control/Control4_C2_3_v10.csv')
Control5_C2_3=pd.read_csv(DATADIR+'control/Control5_C2_3_v10.csv')
Control6_C2_3=pd.read_csv(DATADIR+'control/Control6_C2_3_v10.csv')

C2_3=pd.concat([Control0_C2_3,Control1_C2_3,Control15_C2_3,Control2_C2_3], axis=0)
bsC2_3=bezier(C2_3,4)
tC2_3=traza2([bsC2_3],violeta,'C2_3','Pal',False)

C2_3c=pd.concat([Control2_C2_3,Control25_C2_3,Control3_C2_3, 
                Control4_C2_3,Control5_C2_3,Control6_C2_3], axis=0)

bsC2_3c=bezier(C2_3c,4)
tC2_3c=traza2([bsC2_3c],violeta,'C2_3c','Pal',False)

Control0_C2_31=pd.read_csv(DATADIR+'control/Control0_C2_31_v10.csv')
Control1_C2_31=pd.read_csv(DATADIR+'control/Control1_C2_31_v11.csv')
Control15_C2_31=pd.read_csv(DATADIR+'control/control15_C2_31_v13.csv')
Control17_C2_31=pd.read_csv(DATADIR+'control/control17_C2_31.csv')
Control2_C2_31=pd.read_csv(DATADIR+'control/Control2_C2_31_v11.csv')
Control25_C2_31=pd.read_csv(DATADIR+'control/control25_C2_31.csv')
Control25_C2_31a=pd.read_csv(DATADIR+'control/control25_C2_31a.csv')
Control3_C2_31=pd.read_csv(DATADIR+'control/Control3_C2_31_v10.csv')
Control4_C2_31=pd.read_csv(DATADIR+'control/Control4_C2_31_v10.csv')
Control5_C2_31=pd.read_csv(DATADIR+'control/Control5_C2_31_v10.csv')
Control6_C2_31=pd.read_csv(DATADIR+'control/Control6_C2_31_v10.csv')

Control2_C2_32=pd.read_csv(DATADIR+'control/Control2_C2_32_a.csv')
Control25_C2_32=pd.read_csv(DATADIR+'control/control25_C2_32_v2.csv')
Control3_C2_32=pd.read_csv(DATADIR+'control/Control3_C2_32_v10.csv')
Control4_C2_32=pd.read_csv(DATADIR+'control/Control4_C2_32_v10.csv')
Control5_C2_32=pd.read_csv(DATADIR+'control/Control5_C2_32_v10.csv')
Control6_C2_32=pd.read_csv(DATADIR+'control/Control6_C2_32_v10.csv')

Control2_C2_312=pd.concat([Control2_C2_31,Control2_C2_32], axis=0)
Control25_C2_312=pd.concat([Control25_C2_31a,Control2_C2_32], axis=0)
Control3_C2_312=pd.concat([Control3_C2_31,Control3_C2_32], axis=0)
Control4_C2_312=pd.concat([Control4_C2_31,Control4_C2_32], axis=0)
Control5_C2_312=pd.concat([Control5_C2_31,Control5_C2_32], axis=0)
Control6_C2_312=pd.concat([Control6_C2_31,Control6_C2_32], axis=0)

C2_312c=pd.concat([Control2_C2_312,Control25_C2_312,Control3_C2_312, 
                Control4_C2_312,Control5_C2_312,Control6_C2_312], axis=0)

bsC2_312c=bezier(C2_312c,7)
tC2_312c=traza2([bsC2_312c],violeta,'C2_312c','Pal',False)

acopleC2_31c=acople2(C2_3c,C2_312c,4,7)
tacopleC2_31c=traza2([acopleC2_31c],violeta,'C2_31ca','Pal',False)

C2_31=pd.concat([Control15_C2_31,Control17_C2_31,Control25_C2_31],axis=0)
bsC2_31=bezier(C2_31,3)
tC2_31=traza2([bsC2_31],violeta,'C2_31','Pal',False)

tC23=tC2_3+tC2_3c+tC2_31+tC2_312c+tacopleC2_31c

# P

Control0_P_3=pd.read_csv(DATADIR+'control/Control0_P_3_v10.csv')

Control0_P_31=pd.read_csv(DATADIR+'control/Control0_P_31_v21.csv')
Control05_P_31=pd.read_csv(DATADIR+'control/Control05_P_31_v22.csv')

Control1_P_3=pd.read_csv(DATADIR+'control/Control1_P_3_v10.csv')

Control15_P_31=pd.read_csv(DATADIR+'control/Control15_P_31_v22.csv')
Control17_P_31=pd.read_csv(DATADIR+'control/Control17_P_31_v21.csv')
Control18_P_31=pd.read_csv(DATADIR+'control/Control18_P_31_v21.csv')

Control2_P_3=pd.read_csv(DATADIR+'control/Control2_P_3_v10.csv')
Control25_P_3=pd.read_csv(DATADIR+'control/Control25_P_3_v2.csv')

Control2_P_31=pd.read_csv(DATADIR+'control/Control2_P_31_v20.csv')
Control25_P_31=pd.read_csv(DATADIR+'control/Control25_P_31_v2.csv')
Control26_P_31=pd.read_csv(DATADIR+'control/Control26_P_31.csv')

Control26_P_32=pd.read_csv(DATADIR+'control/Control26_P_32.csv')
Control27_P_32=pd.read_csv(DATADIR+'control/Control27_P_32.csv')
Control28_P_32=pd.read_csv(DATADIR+'control/Control28_P_32_v2.csv')

Control3_P_3=pd.read_csv(DATADIR+'control/Control3_P_3_v10.csv')

Control3_P_31=pd.read_csv(DATADIR+'control/Control3_P_31_v10.csv')

Control3_P_32=pd.read_csv(DATADIR+'control/Control3_P_32_v11.csv')
Control35_P_32=pd.read_csv(DATADIR+'control/Control35_P_32_v3.csv')

Control4_P_3=pd.read_csv(DATADIR+'control/Control4_P_3_v10.csv')
Control45_P_3=pd.read_csv(DATADIR+'control/Control45_P_3.csv')
Control47_P_3=pd.read_csv(DATADIR+'control/Control47_P_3.csv')

Control4_P_31=pd.read_csv(DATADIR+'control/Control4_P_31.csv')
Control45_P_31=pd.read_csv(DATADIR+'control/Control45_P_31.csv')

Control4_P_32=pd.read_csv(DATADIR+'control/Control4_P_32_v10.csv')
Control45_P_32=pd.read_csv(DATADIR+'control/Control45_P_32.csv')
Control47_P_32=pd.read_csv(DATADIR+'control/Control47_P_32.csv')

Control5_P_3=pd.read_csv(DATADIR+'control/Control5_P_3_v10.csv')
Control55_P_3=pd.read_csv(DATADIR+'control/Control55_P_3.csv')

Control5_P_32=pd.read_csv(DATADIR+'control/Control5_P_32_v10.csv')
Control55_P_32=pd.read_csv(DATADIR+'control/Control55_P_32.csv')

Control6_P_3=pd.read_csv(DATADIR+'control/Control6_P_3_v10.csv')
Control6_P_32=pd.read_csv(DATADIR+'control/Control6_P_32_v10.csv')

# Frente

P_3f=pd.concat([Control0_P_3,Control1_P_3,Control2_P_3,Control25_P_3
                ], axis=0)
bsP_3f=bezier(P_3f,4)
tP_3f=traza2([bsP_3f],naranja,'P_3','Eoc1',False)

P_31f=pd.concat([Control0_P_31,Control05_P_31,
                 Control15_P_31,Control17_P_31,Control18_P_31,
                 Control2_P_31,Control25_P_31
                ], axis=0)
bsP_31f=bezier(P_31f,3)
tP_31f=traza2([bsP_31f],naranja,'P_31f','Eoc1',False)

P_32f=pd.concat([Control26_P_32,Control27_P_32,Control28_P_32,
                 Control3_P_32,Control35_P_32], axis=0)
bsP_32f=bezier(P_32f,4)
tP_32f=traza2([bsP_32f],naranja,'P_32f','Eoc1',False)

# medio

Control255_P_3=pd.read_csv(DATADIR+'control/Control255_P_3.csv')
Control29_P_3=pd.read_csv(DATADIR+'control/Control29_P_3.csv')

Control255_P_32=pd.read_csv(DATADIR+'control/Control255_P_32.csv')
Control29_P_32=pd.read_csv(DATADIR+'control/Control29_P_32.csv')

Control3_P_3_31=pd.concat([Control3_P_3,
          # Control3_P_31[2:],
           Control3_P_32], axis=0)

P_3m=pd.concat([Control255_P_3,Control29_P_3,Control3_P_3,
                Control4_P_3,Control45_P_3], axis=0)
bsP_3m=bezier(P_3m,4)
tP_3m=traza2([bsP_3m],naranja,'P_3m','Eoc1',False)

P_31m=pd.concat([Control26_P_31,Control3_P_31,
                 Control4_P_31,Control45_P_31], axis=0)
bsP_31m=bezier(P_31m,3)
tP_31m=traza2([bsP_31m],naranja,'P_31m','Eoc1',False)

P_32m=pd.concat([#Control255_P_32,
                 Control35_P_32,
                 Control4_P_32,Control45_P_32], axis=0)
bsP_32m=bezier(P_32m,4)
tP_32m=traza2([bsP_32m],naranja,'P_32m','Eoc1',False)

acopleP_31m=acople2(P_3m[:-4],P_31m,4,3)
tacopleP_31m=traza2([acopleP_31m],naranja,'P_31ma','Eoc1',False)

acopleP_312m=acople2(P_31m,P_32m,3,3)
tacopleP_312m=traza2([acopleP_312m],naranja,'P_312ma','Eoc1',False)

# cola

P_3c=pd.concat([Control45_P_3,Control47_P_3,
                Control5_P_3,Control55_P_3,
                Control6_P_3], axis=0)
bsP_3c=bezier(P_3c,4)
tP_3c=traza2([bsP_3c],naranja,'P_3c','Eoc1',False)

P_32c=pd.concat([Control45_P_32,Control47_P_32,
                 Control5_P_32,Control55_P_32,
                 Control6_P_32], axis=0)
bsP_32c=bezier(P_32c,4)
tP_32c=traza2([bsP_32c],naranja,'P_32c','Eoc1',False)

tP3=tP_3f+tP_31f+tP_32f+tP_3m +tP_31m+tP_32m+tacopleP_312m+tP_3c+tP_32c+tacopleP_31m

# E1

Control05_E1_3=pd.read_csv(DATADIR+'control/Control05_E1_3_v2.csv')
Control06_E1_3=pd.read_csv(DATADIR+'control/Control06_E1_3.csv')

Control1_E1_3=pd.read_csv(DATADIR+'control/Control1_E1_3.csv')
Control13_E1_3=pd.read_csv(DATADIR+'control/Control13_E1_3_v2.csv')

Control2_E1_3=pd.read_csv(DATADIR+'control/Control2_E1_3_v10.csv')
Control22_E1_3=pd.read_csv(DATADIR+'control/Control22_E1_3.csv')
Control23_E1_3=pd.read_csv(DATADIR+'control/Control23_E1_3.csv')
Control24_E1_3=pd.read_csv(DATADIR+'control/Control24_E1_3_v2.csv')

Control25_E1_3=pd.read_csv(DATADIR+'control/Control25_E1_3.csv')
Control26_E1_3=pd.read_csv(DATADIR+'control/Control26_E1_3.csv')

Control3_E1_3=pd.read_csv(DATADIR+'control/Control3_E1_3_v11.csv')
Control35_E1_3=pd.read_csv(DATADIR+'control/Control35_E1_3.csv')
Control4_E1_3=pd.read_csv(DATADIR+'control/Control4_E1_3_v10.csv')
Control45_E1_3=pd.read_csv(DATADIR+'control/Control45_E1_3.csv')
Control5_E1_3=pd.read_csv(DATADIR+'control/Control5_E1_3_v10.csv')
Control6_E1_3=pd.read_csv(DATADIR+'control/Control6_E1_3_v10.csv')

E1_3f=pd.concat([Control05_E1_3,Control06_E1_3,
                 Control1_E1_3,Control13_E1_3,
                 ], axis=0)
bsE1_3f=bezier(E1_3f,3)
tE1_3f=traza2([bsE1_3f],pink,'E1_3','Eoc2',False)

E1_3m=pd.concat([Control13_E1_3,
                 Control2_E1_3,Control22_E1_3,Control23_E1_3,Control24_E1_3], axis=0)
bsE1_3m=bezier(E1_3m,3)
tE1_3m=traza2([bsE1_3m],pink,'E1_3m','Eoc2',False)

E1_3c=pd.concat([Control25_E1_3,Control26_E1_3,
                 Control3_E1_3,Control35_E1_3,
                 Control4_E1_3,Control45_E1_3,
                 Control5_E1_3,Control6_E1_3], axis=0)
bsE1_3c=bezier(E1_3c,3)
tE1_3c=traza2([bsE1_3c],pink,'E1_3c','Eoc2',False)

Control2_E1_32=pd.read_csv(DATADIR+'control/Control2_E1_32_v11.csv')
Control3_E1_32m=pd.read_csv(DATADIR+'control/Control3_E1_32_v10.csv')

Control3_E1_32=pd.read_csv(DATADIR+'control/Control3_E1_32_v11.csv')
Control35_E1_32=pd.read_csv(DATADIR+'control/Control35_E1_32.csv')

Control4_E1_32=pd.read_csv(DATADIR+'control/Control4_E1_32_v10.csv')
Control5_E1_32=pd.read_csv(DATADIR+'control/Control5_E1_32_v10.csv')
Control6_E1_32=pd.read_csv(DATADIR+'control/Control6_E1_32_v10.csv')

E1_32m=pd.concat([Control2_E1_32,
                  Control3_E1_32m,Control3_E1_32
                  ], axis=0)
bsE1_32m=bezier(E1_32m,3)
tE1_32m=traza2([bsE1_32m],pink,'E1_32m','Eoc2',False)

E1_32c=pd.concat([Control3_E1_32,Control35_E1_32,
                  Control4_E1_32,
                 Control5_E1_32,
                  Control6_E1_32], axis=0)
bsE1_32c=bezier(E1_32c,3)
tE1_32c=traza2([bsE1_32c],pink,'E1_32c','Eoc2',False)

tE13=tE1_3f+tE1_3m+tE1_3c+tE1_32m+tE1_32c