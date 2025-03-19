DATADIR='data/' # Directory with the data
CSV='data/csv/'

from functions import *


## E1

ControlE1_1=pd.read_csv(DATADIR+'/control/E1_1.csv')

ControlE1_11=pd.read_csv(DATADIR+'/control/E1_11.csv')

ControlE1_cola=pd.read_csv(DATADIR+'/control/E1_cola.csv')

zz=split_list(ControlE1_cola["SAMPLE_1"].to_list(),3)
for i in range(len(zz)):
    zz[i][1]=zz[i][1]-50

zzz=sum(zz, [])

ControlE1_cola['Z']=zzz

bsE1=bezier(ControlE1_1,3)

bsE11=bezier(ControlE1_11,3)

acE1_11=acople(ControlE1_1,ControlE1_11,3)

tE1=traza2([bsE1],pink,'Eocene 2','Eoc2',True)

tE11=traza2([bsE11],pink,'E11','Eoc2',False)

taE11=traza2([acE1_11],pink,'aE11','Eoc2',False)

bsE1_cola=bezier(ControlE1_cola,3)
tE1_cola=traza2([bsE1_cola],pink,'aE1_cola','Eoc2',False)

taE11=traza2([acE1_11],pink,'aE11','Eoc2',False)

pgE1=pegue(ControlE1_1,ControlE1_cola,3)
tpgE11=traza2([pgE1],pink,'pE11','Eoc2',False)

tE=tE1+taE11+tE11+tpgE11+tE1_cola

## P1

ControlP1_1=pd.read_csv(DATADIR+'/control/P1_1.csv')
bsP1=bezier(ControlP1_1,3)
#tP1=traza([bsP1],naranja,'P1','P1')

ControlP1_11=pd.read_csv(DATADIR+'/control/P1_11.csv')
bsP11=bezier(ControlP1_11,3)
#tP11=traza([bsP11],naranja,'P11','P11')

acP1_11=acople(ControlP1_1,ControlP1_11,3)
#taP11=traza([acP1_11],naranja,'aP11','aP11')

ControlP1_cola=pd.read_csv(DATADIR+'/control/P1_cola.csv')
bsP1_cola=bezier(ControlP1_cola,3)
tP1_cola=traza([bsP1_cola],naranja,'/control/P1_cola','P1_cola')

pgP1=pegue(ControlP1_1,ControlP1_cola,3)
#tpgP11=traza([pgP1],naranja,'pP11','pP11')

ControlP11_cola=pd.read_csv(DATADIR+'/control/cP11_cola.csv')

pzz=split_list(ControlP11_cola["Z"].to_list(),3)
for i in range(len(pzz)):
    pzz[i][1]=pzz[i][1]-40
    pzz[i][2]=pzz[i][2]-20
pzzz=sum(pzz, [])

ControlP11_cola['Z']=pzzz

bsP11_cola=bezier(ControlP11_cola,3)
#tP11_cola=traza([bsP11_cola],naranja,'P11_cola','P11_cola')

#ControlP1_11_copia=pd.read_csv(new_DATADIR+'P1_11 copia.csv')
pgP11=pegue(ControlP1_11,ControlP11_cola,3)
tpgP111=traza([pgP11],naranja,'pP111','pP111')

parche=pd.read_csv(DATADIR+'/control/parche.csv')

bsparche=bezier(parche,2)
#tparche=traza([bsparche],naranja,'parche','parche')

tP1=traza2([bsP1],naranja,'Eocene 1','Eoc1',True)
tP11=traza2([bsP11],naranja,'P11','Eoc1',False)
taP11=traza2([acP1_11],naranja,'aP11','Eoc1',False)
tP1_cola=traza2([bsP1_cola],naranja,'P1_cola','Eoc1',False)
tpgP11=traza2([pgP1],naranja,'pP11','Eoc1',False)
tP11_cola=traza2([bsP11_cola],naranja,'P11_cola','Eoc1',False)
tpgP111=traza2([pgP11],naranja,'pP111','Eoc1',False)
tparche=traza2([bsparche],naranja,'parche','Eoc1',False)
tP=tP1+taP11+tP11+tpgP11+tP1_cola+tP11_cola+tpgP111+tparche

## Superficie bz para C1_1

Control0_C1_1=pd.read_csv(DATADIR+'control/Control0_C1_1_v10.csv')
Control0_C1_11=pd.read_csv(DATADIR+'control/Control0_C1_11_v10.csv')
Control1_C1_1=pd.read_csv(DATADIR+'control/Control1_C1_1_v10.csv')
Control1_C1_11=pd.read_csv(DATADIR+'control/Control1_C1_11_v10.csv')
Control2_C1_1=pd.read_csv(DATADIR+'control/Control2_C1_1_v10.csv')
Control2_C1_11=pd.read_csv(DATADIR+'control/Control2_C1_11_v10.csv')
Control3_C1_1=pd.read_csv(DATADIR+'control/Control3_C1_1_v10.csv')
Control3_C1_11=pd.read_csv(DATADIR+'control/Control3_C1_11_v10.csv')
Control4_C1_1=pd.read_csv(DATADIR+'control/Control4_C1_1_v10.csv')
Control4_C1_11=pd.read_csv(DATADIR+'control/Control4_C1_11_v10.csv')
Control5_C1_1=pd.read_csv(DATADIR+'control/Control5_C1_1_v10.csv')
Control5_C1_11=pd.read_csv(DATADIR+'control/Control5_C1_11_v10.csv')
Control6_C1_1=pd.read_csv(DATADIR+'control/Control6_C1_1_v10.csv')
Control6_C1_11=pd.read_csv(DATADIR+'control/Control6_C1_11_v10.csv')

lC1=[Control0_C1_1,
Control0_C1_11,
Control1_C1_1,
Control1_C1_11,
Control2_C1_1,
Control2_C1_11,
Control3_C1_1,
Control3_C1_11,
Control4_C1_1,
Control4_C1_11,
Control5_C1_1,
Control5_C1_11,
Control6_C1_1,
Control6_C1_11]

lC11=[lC1[i] for i in range(0,len(lC1),2)]
lC111=[lC1[i] for i in range(1,len(lC1),2)]


tC11=traza2([bs(lC11),bs2(lC1),bs(lC111)],verde_c,'Cretaceous','C1',True)


# C2_1

Control0_C2_1=pd.read_csv(DATADIR+'control/Control0_C2_1_v10.csv')
Control0_C2_11=pd.read_csv(DATADIR+'control/Control0_C2_11_v10.csv')
Control1_C2_1=pd.read_csv(DATADIR+'control/Control1_C2_1_v10.csv')
Control1_C2_11=pd.read_csv(DATADIR+'control/Control1_C2_11_v10.csv')
Control2_C2_1=pd.read_csv(DATADIR+'control/Control2_C2_1_v10.csv')
Control2_C2_11=pd.read_csv(DATADIR+'control/Control2_C2_11_v10.csv')
Control3_C2_1=pd.read_csv(DATADIR+'control/Control3_C2_1_v10.csv')
Control3_C2_11=pd.read_csv(DATADIR+'control/Control3_C2_11_v10.csv')
Control4_C2_1=pd.read_csv(DATADIR+'control/Control4_C2_1_v10.csv')
Control4_C2_11=pd.read_csv(DATADIR+'control/Control4_C2_11_v10.csv')
Control5_C2_1=pd.read_csv(DATADIR+'control/Control5_C2_1_v10.csv')
Control5_C2_11=pd.read_csv(DATADIR+'control/Control5_C2_11_v10.csv')
Control6_C2_1=pd.read_csv(DATADIR+'control/Control6_C2_1_v10.csv')
Control6_C2_11=pd.read_csv(DATADIR+'control/Control6_C2_11_v10.csv')

lC2=[Control0_C2_1,
Control0_C2_11,
Control1_C2_1,
Control1_C2_11,
Control2_C2_1,
Control2_C2_11,
Control3_C2_1,
Control3_C2_11,
Control4_C2_1,
Control4_C2_11,
Control5_C2_1,
Control5_C2_11,
Control6_C2_1,
Control6_C2_11]

lC21=[lC2[i] for i in range(0,len(lC2),2)]
lC211=[lC2[i] for i in range(1,len(lC2),2)]


tC21=traza2([bs(lC21),bs2(lC2),bs(lC211)],violeta,'Paleocene','Pal',True)
