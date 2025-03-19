from functions import *
DATADIR='data/' # Directory with the data
CSV='data/csv/'
# C1_2

Control0_C1_2=pd.read_csv(DATADIR+'control/Control0_C1_2_v10.csv')
Control0_C1_21=pd.read_csv(DATADIR+'control/Control0_C1_21_v10.csv')
Control0_C1_22=pd.read_csv(DATADIR+'control/Control0_C1_22_v10.csv')
Control1_C1_2=pd.read_csv(DATADIR+'control/Control1_C1_2_v10.csv')
Control1_C1_21=pd.read_csv(DATADIR+'control/Control1_C1_21_v10.csv')
Control1_C1_22=pd.read_csv(DATADIR+'control/Control1_C1_22_v10.csv')
Control2_C1_2=pd.read_csv(DATADIR+'control/Control2_C1_2_v10.csv')
Control2_C1_21=pd.read_csv(DATADIR+'control/Control2_C1_21_v10.csv')
Control2_C1_22=pd.read_csv(DATADIR+'control/Control2_C1_22_v10.csv')
Control3_C1_2=pd.read_csv(DATADIR+'control/Control3_C1_2_v10.csv')
Control3_C1_21=pd.read_csv(DATADIR+'control/Control3_C1_21_v10.csv')
Control3_C1_22=pd.read_csv(DATADIR+'control/Control3_C1_22_v10.csv')
Control4_C1_2=pd.read_csv(DATADIR+'control/Control4_C1_2_v10.csv')
Control4_C1_21=pd.read_csv(DATADIR+'control/Control4_C1_21_v10.csv')
Control4_C1_22=pd.read_csv(DATADIR+'control/Control4_C1_22_v10.csv')
Control5_C1_2=pd.read_csv(DATADIR+'control/Control5_C1_2_v10.csv')
Control5_C1_21=pd.read_csv(DATADIR+'control/Control5_C1_21_v10.csv')
Control5_C1_22=pd.read_csv(DATADIR+'control/Control5_C1_22_v10.csv')
Control6_C1_2=pd.read_csv(DATADIR+'control/Control6_C1_2_v10.csv')
Control6_C1_21=pd.read_csv(DATADIR+'control/Control6_C1_21_v10.csv')
Control6_C1_22=pd.read_csv(DATADIR+'control/Control6_C1_22_v10.csv')

lC1_2=[Control0_C1_2,
Control0_C1_21,
Control0_C1_22,
Control1_C1_2,
Control1_C1_21,
Control1_C1_22,
Control2_C1_2,
Control2_C1_21,
Control2_C1_22,
Control3_C1_2,
Control3_C1_21,
Control3_C1_22,
Control4_C1_2,
Control4_C1_21,
Control4_C1_22,
Control5_C1_2,
Control5_C1_21,
Control5_C1_22,
Control6_C1_2,
Control6_C1_21,
Control6_C1_22]

lC12=[lC1_2[i] for i in range(0,len(lC1_2),3)]
lC1201=[lC1_2[i] for i in [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19]]
lC121=[lC1_2[i] for i in range(1,len(lC1_2),3)]
lC12102=[lC1_2[i] for i in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]]
lC122=[lC1_2[i] for i in range(2,len(lC1_2),3)]

tC12=traza2([bs(lC12),bs2(lC1201),bs(lC121),bs2(lC12102),bs(lC122)],verde_c,'C12','C1',False)

l2=[i for i in range(0,len(lC1_2),3)]
l21=[i for i in range(1,len(lC1_2),3)]
l22=[i for i in range(2,len(lC1_2),3)]


# C2_2

Control0_C2_2=pd.read_csv(DATADIR+'control/Control0_C2_2_v10.csv')
Control0_C2_21=pd.read_csv(DATADIR+'control/Control0_C2_21_v2.csv') 
Control0_C2_22=pd.read_csv(DATADIR+'control/Control0_C2_22_v2.csv')

Control1_C2_2=pd.read_csv(DATADIR+'control/Control1_C2_2_v10.csv')
Control1_C2_21=pd.read_csv(DATADIR+'control/Control1_C2_21_v10.csv')
Control1_C2_22=pd.read_csv(DATADIR+'control/Control1_C2_22_v10.csv')

Control2_C2_2=pd.read_csv(DATADIR+'control/Control2_C2_2_v10.csv')
Control2_C2_21=pd.read_csv(DATADIR+'control/Control2_C2_21_v10.csv')
Control2_C2_22=pd.read_csv(DATADIR+'control/Control2_C2_22_v10.csv')

Control3_C2_2=pd.read_csv(DATADIR+'control/Control3_C2_2_v10.csv')
Control3_C2_21=pd.read_csv(DATADIR+'control/Control3_C2_21_v10.csv')
Control3_C2_22=pd.read_csv(DATADIR+'control/Control3_C2_22_v10.csv')

Control4_C2_2=pd.read_csv(DATADIR+'control/Control4_C2_2_v10.csv')
Control4_C2_21=pd.read_csv(DATADIR+'control/Control4_C2_21_v10.csv')
Control4_C2_22=pd.read_csv(DATADIR+'control/Control4_C2_22_v10.csv')

Control5_C2_2=pd.read_csv(DATADIR+'control/Control5_C2_2_v10.csv')
Control5_C2_21=pd.read_csv(DATADIR+'control/Control5_C2_21_v10.csv')
Control5_C2_22=pd.read_csv(DATADIR+'control/Control5_C2_22_v10.csv')

Control6_C2_2=pd.read_csv(DATADIR+'control/Control6_C2_2_v10.csv')
Control6_C2_21=pd.read_csv(DATADIR+'control/Control6_C2_21_v10.csv')
Control6_C2_22=pd.read_csv(DATADIR+'control/Control6_C2_22_v10.csv')

lC2_2=[
    Control0_C2_2,
    Control0_C2_21,
    Control0_C2_22,
    Control1_C2_2,
    Control1_C2_21,
    Control1_C2_22,
    Control2_C2_2,
    Control2_C2_21,
    Control2_C2_22,
    Control3_C2_2,
    Control3_C2_21,
    Control3_C2_22,
    Control4_C2_2,
    Control4_C2_21,
    Control4_C2_22,
    Control5_C2_2,
    Control5_C2_21,
    Control5_C2_22,
    Control6_C2_2,
    Control6_C2_21,
    Control6_C2_22
]
lC22=[lC2_2[i] for i in [0,3,6,9,12,15,18]]
lC2201=[lC2_2[i] for i in [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19]]
lC221=[lC2_2[i] for i in [1,4,7,10,13,16,19]]
lC22102=[lC2_2[i] for i in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]]
lC222=[lC2_2[i] for i in [2,5,8,11,14,17,20]]

tC22=traza2([bs(lC22),bs2(lC2201),bs(lC221),bs2(lC22102),bs(lC222)],violeta,'C22','Pal',False)


# P_2

Control0_P_2=pd.read_csv(DATADIR+'control/Control0_P_2_v10.csv')
Control0_P_21=pd.read_csv(DATADIR+'control/Control0_P_21_v10.csv')
Control0_P_22=pd.read_csv(DATADIR+'control/Control0_P_22_v10.csv')

Control1_P_2=pd.read_csv(DATADIR+'control/Control1_P_2_v10.csv')
Control1_P_21=pd.read_csv(DATADIR+'control/Control1_P_21_v10.csv')
Control1_P_22=pd.read_csv(DATADIR+'control/Control1_P_22_v10.csv')

Control2_P_2=pd.read_csv(DATADIR+'control/Control2_P_2_v10.csv')
Control2_P_21=pd.read_csv(DATADIR+'control/Control2_P_21_v10.csv')
Control2_P_22=pd.read_csv(DATADIR+'control/Control2_P_22_v10.csv')

Control3_P_2=pd.read_csv(DATADIR+'control/Control3_P_2_v10.csv')
Control3_P_21=pd.read_csv(DATADIR+'control/Control3_P_21_v10.csv')
Control3_P_22=pd.read_csv(DATADIR+'control/Control3_P_22_v10.csv')

Control4_P_2=pd.read_csv(DATADIR+'control/Control4_P_2_v10.csv')
Control4_P_21=pd.read_csv(DATADIR+'control/Control4_P_21_v10.csv')
Control4_P_22=pd.read_csv(DATADIR+'control/Control4_P_22_v10.csv')

Control5_P_2=pd.read_csv(DATADIR+'control/Control5_P_2_v10.csv')
Control5_P_21=pd.read_csv(DATADIR+'control/Control5_P_21_v10.csv')
Control5_P_22=pd.read_csv(DATADIR+'control/Control5_P_22_v10.csv')

Control6_P_2=pd.read_csv(DATADIR+'control/Control6_P_2_v10.csv')
Control6_P_21=pd.read_csv(DATADIR+'control/Control6_P_21_v10.csv')
Control6_P_22=pd.read_csv(DATADIR+'control/Control6_P_22_v10.csv')

lP_2=[
    Control0_P_2,
    Control0_P_21,
    Control0_P_22,
    Control1_P_2,
    Control1_P_21,
    Control1_P_22,
    Control2_P_2,
    Control2_P_21,
    Control2_P_22,
    Control3_P_2,
    Control3_P_21,
    Control3_P_22,
    Control4_P_2,
    Control4_P_21,
    Control4_P_22,
    Control5_P_2,
    Control5_P_21,
    Control5_P_22,
    Control6_P_2,
    Control6_P_21,
    Control6_P_22
]
lP2=[lP_2[i] for i in range(0,len(lP_2),3)]
lP201=[lP_2[i] for i in [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19]]
lP21=[lP_2[i] for i in range(1,len(lP_2),3)]
lP2102=[lP_2[i] for i in [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20]]
lP22=[lP_2[i] for i in range(2,len(lP_2),3)]

tP2=traza2([bs(lP2),
            bs2(lP201),
            bs(lP21),
            bs2(lP2102),
            bs(lP22)],naranja,'P_2','Eoc1',False)


## E1

ControlE1_2_f=pd.read_csv(DATADIR+'/control/E1_2_f.csv')

zzf=split_list(ControlE1_2_f["Z"].to_list(),3)
for i in range(len(zzf)):
    zzf[i][1]=zzf[i][1]-30
    
zzzf=sum(zzf, [])
ControlE1_2_f['Z']=zzzf

bsE1_2_f=bezier(ControlE1_2_f,3)
tE1_2_f=traza2([bsE1_2_f],pink,'E1_2','Eoc2',False)

bsE1_2_ff=bezier(ControlE1_2_f.loc[0:8],3)
tE1_2_ff=traza2([bsE1_2_ff],pink,'E1_2ff','Eoc2',False)

bsE1_2_fff=bezier(ControlE1_2_f.loc[9:],3)
tE1_2_fff=traza2([bsE1_2_fff],pink,'E1_2','Eoc2',False)

ControlE1_2_m=pd.read_csv(DATADIR+'/control/E1_2_m.csv')

zzm=split_list(ControlE1_2_m["Z"].to_list(),3)
for i in range(len(zzm)):
    zzm[i][1]=zzm[i][1]-30
    
zzzm=sum(zzm, [])
ControlE1_2_m['Z']=zzzm

bsE1_2_m=bezier(ControlE1_2_m,3)
tE1_2_m=traza2([bsE1_2_m],pink,'E1_2m','Eoc2',False)

pgE1fm=pegue(ControlE1_2_f.loc[0:8],ControlE1_2_f.loc[9:],3)
tpgE1ff=traza2([pgE1fm],pink,'pE1_2ff','Eoc2',False)

pgE1fm=pegue(ControlE1_2_f,ControlE1_2_m,3)
tpgE1fm=traza2([pgE1fm],pink,'pE1_2fm','Eoc2',False)

ControlE1_2_cola=pd.read_csv(DATADIR+'/control/E1_2_cola.csv')

zzc=split_list(ControlE1_2_cola["SAMPLE_1"].to_list(),3)
for i in range(len(zzc)):
    zzc[i][1]=zzc[i][1]-30
    
zzzc=sum(zzc, [])
ControlE1_2_cola['Z']=zzzc

bsE1_2_cola=bezier(ControlE1_2_cola,3)
tE1_2_cola=traza2([bsE1_2_cola],pink,'E1_2cola','Eoc2',False)

pgE1_2mc=pegue(ControlE1_2_m,ControlE1_2_cola,3)
tpgE1_2mc=traza2([pgE1_2mc],pink,'pE1_2mc','Eoc2',False)

ControlE1_21=pd.read_csv(DATADIR+'/control/E1_21_2.csv')

zz1=split_list(ControlE1_21["Z"].to_list(),3)
for i in range(3,len(zz1)-1):
    zz1[i][0]=zz1[i][0]-20
for i in range(len(zz1)):
    zz1[i][1]=zz1[i][1]-40
    
zzz1=sum(zz1, [])
ControlE1_21['Z']=zzz1

bsE1_21=bezier(ControlE1_21,3)
tE1_21=traza2([bsE1_21],pink,'E1_21','Eoc2',False)

acE1_21f=acople(ControlE1_2_f.loc[0:8],ControlE1_21.loc[0:8],3)
taE1_21f=traza2([acE1_21f],pink,'aE11f','Eoc2',False)

acE1_21ff=acople(ControlE1_2_f.loc[:8],ControlE1_21,3)
taE1_21ff=traza2([acE1_21ff],pink,'aE11ff','Eoc2',False)

cuña0=pd.read_csv(DATADIR+'/control/cuña010.csv')
bscuña0=bezier(cuña0,2)
tcuña0=traza2([bscuña0],pink,'cuña0','Eoc2',False)

cuña=pd.read_csv(DATADIR+'/control/cuña1.csv')
bscuña=bezier(cuña,3)
tcuña=traza2([bscuña],pink,'cuña','Eoc2',False)

cuña2=pd.read_csv(DATADIR+'/control/cuña2_4.csv')
bscuña2=bezier(cuña2,2)
tcuña2=traza2([bscuña2],pink,'cuña2','Eoc2',False)

ControlE1_22f=pd.read_csv(DATADIR+'/control/E1_2_22f2.csv')

zz2f=split_list(ControlE1_22f["SAMPLE_1"].to_list(),3)
for i in range(len(zz2f)):
    zz2f[i][1]=zz2f[i][1]-40
for i in range(len(zz2f)):
    zz2f[i][2]=zz2f[i][2]-30
    
zzz2f=sum(zz2f, [])
ControlE1_22f['Z']=zzz2f

bsE1_22f=bezier(ControlE1_22f,3)
tE1_22f=traza2([bsE1_22f],pink,'E1_22f','Eoc2',False)

ControlE1_22m=pd.read_csv(DATADIR+'/control/E1_2_22m.csv')

zz2m=split_list(ControlE1_22m["SAMPLE_1"].to_list(),3)
for i in range(len(zz2m)):
    zz2m[i][1]=zz2m[i][1]-40
for i in range(len(zz2f)):
    zz2m[i][2]=zz2m[i][2]-30
    
zzz2m=sum(zz2m, [])
ControlE1_22m['Z']=zzz2m

bsE1_22m=bezier(ControlE1_22m,3)
tE1_22m=traza2([bsE1_22m],pink,'E1_22m','Eoc2',False)

ControlE1_22c=pd.read_csv(DATADIR+'/control/E1_2_22c.csv')

zz2c=split_list(ControlE1_22c["SAMPLE_1"].to_list(),3)
for i in range(len(zz2c)):
    zz2c[i][1]=zz2c[i][1]-40
for i in range(len(zz2c)):
    zz2c[i][2]=zz2c[i][2]-30
    
zzz2c=sum(zz2c, [])
ControlE1_22c['Z']=zzz2c

bsE1_22c=bezier(ControlE1_22c,3)
tE1_22c=traza2([bsE1_22c],pink,'E1_22c','Eoc2',False)

tE1_2=tE1_2_ff+tE1_2_fff+tE1_2_m+tpgE1fm+tpgE1ff+tE1_2_cola+tpgE1_2mc+tE1_21+tcuña+tcuña0+tcuña2+tE1_22f+tE1_22m+tE1_22c