# Topography data

## superficie topo

from functions import *

# import pandas as pd
DATADIR='data/' # Directory with the data
CSV='data/csv/'


topo=pd.read_csv(CSV+'zona.csv')

topo1=topo[['X','Y','SAMPLE_1']].to_numpy()
topox=[x[0] for x in topo1]
topoy=[x[1] for x in topo1]
topoelv=[x[2] for x in topo1]

topo_gr=[topox,topoy,topoelv]

cotasxy=[min(topox),max(topox),min(topoy),max(topoy)]


# Sections Planes

P0=[630312.260878774, 4213164.354736202]
P2=[631727.2235457341, 4211098.154021688]
P1=[632080.5579142272, 4214387.312460086]
P3=[633495.5205811873, 4212321.111745572]

d=distance(P0,P1)

r1=para_line(P0,P1)
r2=para_line(P2,P3)

points_t = np.concatenate([np.arange(0, d, d/12),[d]])

Qs=[r1(x) for x in points_t]
QQs=[r2(x) for x in points_t]


Plano0=[Qs[0]+[400],QQs[0]+[400],Qs[0]+[200]]
P0_dat=plano_3d(Plano0[0],Plano0[1],0,'Cross sections','planos',True)
Plano1=[Qs[2]+[400],QQs[2]+[400],Qs[2]+[200]]
P1_dat=plano_3d(Plano1[0],Plano1[1],0,'Plano1','planos',False)
Plano2=[Qs[4]+[400],QQs[4]+[400],Qs[4]+[200]]
P2_dat=plano_3d(Plano2[0],Plano2[1],0,'Plano2','planos',False)
Plano3=[Qs[6]+[400],QQs[6]+[400],Qs[6]+[200]]
P3_dat=plano_3d(Plano3[0],Plano3[1],0,'Plano3','planos',False)
Plano4=[Qs[8]+[400],QQs[8]+[400],Qs[8]+[200]]
P4_dat=plano_3d(Plano4[0],Plano4[1],0,'Plano4','planos',False)
Plano5=[Qs[10]+[400],QQs[10]+[400],Qs[10]+[200]]
P5_dat=plano_3d(Plano5[0],Plano5[1],0,'Plano5','planos',False)
Plano6=[Qs[12]+[400],QQs[12]+[400],Qs[12]+[200]]
P6_dat=plano_3d(Plano6[0],Plano6[1],0,'Plano6','planos',False)
Planos=[P0_dat,P1_dat,P2_dat,P3_dat,P4_dat,P5_dat,P6_dat]

data_planos=Planos

# Tracks in surface

#conformity
co1=pd.read_csv(DATADIR+'conformity/co1.csv')
xco1=[co1['X'][i] for i in range(0,len(co1['X']),8)]
yco1=[co1['Y'][i] for i in range(0,len(co1['X']),8)]
zco1=[co1['SAMPLE_1'][i]+15 for i in range(0,len(co1['X']),8)]

co2=pd.read_csv(DATADIR+'conformity/co2.csv')
xco2=[co2['X'][i] for i in range(0,len(co2['X']),8)]
yco2=[co2['Y'][i] for i in range(0,len(co2['X']),8)]
zco2=[co2['SAMPLE_1'][i]+15 for i in range(0,40,8)]+[
      co2['SAMPLE_1'][i]+35 for i in range(40,90,8)]+[
      co2['SAMPLE_1'][i]+15 for i in range(90,len(co2['X']),8)]


co3=pd.read_csv(DATADIR+'conformity/co3.csv')
xco3=[co3['X'][i] for i in range(0,len(co3['X']),8)]
yco3=[co3['Y'][i] for i in range(0,len(co3['X']),8)]
zco3=[co3['SAMPLE_1'][i]+10 for i in range(5,10,8)]+[
     co3['SAMPLE_1'][i]+30 for i in range(10,76,8)]+[
     co3['SAMPLE_1'][i]+15 for i in range(76,160,8)]+[
     co3['SAMPLE_1'][i]+27 for i in range(160,220,8)]+[
     co3['SAMPLE_1'][i]+15 for i in range(220,len(co3['X'])-8,8)]

co4=pd.read_csv(DATADIR+'conformity/co4.csv')
xco4=[co4['X'][i] for i in range(0,len(co4['X']),8)]
yco4=[co4['Y'][i] for i in range(0,len(co4['X']),8)]
zco4=[co4['SAMPLE_1'][i]+15 for i in range(0,len(co4['X']),8)]

co5=pd.read_csv(DATADIR+'conformity/co5.csv')
xco5=[co5['X'][i] for i in range(0,len(co5['X']),8)]
yco5=[co5['Y'][i] for i in range(0,len(co5['X']),8)]
zco5=[co5['SAMPLE_1'][i]+15 for i in range(0,len(co5['X']),8)]

co6=pd.read_csv(DATADIR+'conformity/co6.csv')
xco6=[co6['X'][i] for i in range(0,len(co6['X'])-380,8)]+[co6['X'][i] for i in range(len(co6['X'])-300,len(co6['X']),8)]
yco6=[co6['Y'][i] for i in range(0,len(co6['X'])-380,8)]+[co6['Y'][i] for i in range(len(co6['X'])-300,len(co6['X']),8)]
zco6=[co6['SAMPLE_1'][i]+15 for i in range(0,len(co6['X'])-380,8)]+[co6['SAMPLE_1'][i]+15 for i in range(len(co6['X'])-300,len(co6['X']),8)]

co_data=[go.Scatter3d(mode='markers',
              x=xco1,y=yco1,z=zco1,
              name='Conformity',
              legendgroup='trc',
              showlegend=True,
              marker=dict(
              color='black',
              size=2)),

              go.Scatter3d(mode='markers',
              x=xco2,y=yco2,z=zco2,
              name='Conformity',
              legendgroup='trc',
              showlegend=False,
              marker=dict(
              color='black',
              size=2)),
              go.Scatter3d(mode='markers',
              x=xco3,y=yco3,z=zco3,
              name='Conformity',
              legendgroup='trc',
              showlegend=False,
              marker=dict(
              color='black',
              size=2)),
              go.Scatter3d(mode='markers',
              x=xco4,y=yco4,z=zco4,
              name='Conformity',
              legendgroup='trc',
              showlegend=False,
              marker=dict(
              color='black',
              size=2)),
              go.Scatter3d(mode='markers',
              x=xco5,y=yco5,z=zco5,
              name='Conformity',
              legendgroup='trc',
              showlegend=False,
              marker=dict(
              color='black',
              size=2)),
              go.Scatter3d(mode='markers',
              x=xco6,y=yco6,z=zco6,
              name='Conformity',
              legendgroup='trc',
              showlegend=False,
              marker=dict(
              color='black',
              size=2))
]

#unconformity

uco1=contact_tr(DATADIR+'unconformity/uco1.csv',0)+['uco1']
uco2=contact_tr(DATADIR+'unconformity/uco2.csv',0)+['uco2']
uco3=contact_tr(DATADIR+'unconformity/uco3.csv',0)+['uco3']
uco4=contact_tr(DATADIR+'unconformity/uco4.csv',0)+['uco4']
uco5=contact_tr(DATADIR+'unconformity/uco5.csv',0)+['uco5']

techo_p11=contact_tr(DATADIR+'unconformity/t_paleo_11.csv',0)+['techos/techo_pal_n1']
techo_p12=contact_tr(DATADIR+'unconformity/t_paleo_12.csv',0)+['techos/techo_pal_n2']
techo_p13=contact_tr(DATADIR+'unconformity/t_paleo_13.csv',0)+['techos/techo_pal_n3']
techosp=[uco1,uco2,uco3,uco4,uco5]

tp1=[techo_p11,techo_p12,techo_p13]

tp1_dat=[contact_dat(x[0],x[1],x[2],12,"lines",x[3],'black','techosp',False,None) for x in tp1]

# white lies for  dash line
ucow_data=[contact_dat(x[0],x[1],x[2],15,"lines",x[3],'orange','techosp',False,'longdash') for x in techosp]

uco_data=[contact_dat(x[0],x[1],x[2],10,"lines",x[3],'black','techosp',False,None) for x in techosp[1:]]+[
    contact_dat(techosp[0][0],techosp[0][1],techosp[0][2],15,"lines",'Unconformity','black','techosp',True,None)
]+tp1_dat+ucow_data

# thrusts
cierva=contact_tr(DATADIR+'fallas y cbm/Thrust_front_la_Cierva_rev.csv',0)+['thr_front_cierva']+['cbm1']
castillo=contact_tr(DATADIR+'fallas y cbm/castillo.csv',0)+['thr_castillo']+['cbm2']
thrusts=[castillo,cierva]
tracks_thruts_data=[contact_dat(x[0],x[1],x[2],10,"lines",'Thrusts','blue','cbm',True,
                    None) for x in [thrusts[0]]]+[contact_dat(x[0],x[1],x[2],10,
                    "lines",x[3],'blue','cbm',False,None) for x in thrusts[1:]]

# Faults tracks

falla_castillo_mula=contact_tr(DATADIR+'fallas y cbm/Falla Castillo Mula.csv',0)+['Falla Castillo Mula']+["fc1"]
falla_castillo2=contact_tr(DATADIR+'fallas y cbm/Falla_castillo 2_rev.csv',0)+['falla_castillo2']+["fc2"]
falla_lomo1=contact_tr(DATADIR+'fallas y cbm/falla_lomo1xy.csv',0)+['falla_lomo1']+["fl1"]
falla_lomo2=contact_tr(DATADIR+'fallas y cbm/falla_lomo2xy.csv',0)+['falla_lomo2']+["fl2"]

fallas=[falla_castillo_mula,falla_castillo2,falla_lomo1,falla_lomo2]
tracks_fallas_data=[contact_dat(x[0],x[1],x[2],20,"lines",'Faults','black','fallas',True,      
                    None) for x in [fallas[0]]]+[contact_dat(x[0],x[1],x[2],20,"lines",
                    x[3],'black','fallas',False,None) for x in fallas]



# Faults

flomo1up=contact2_tr(DATADIR+'fallas y cbm/falla_lomo1.csv',0)
flomo2up=contact2_tr(DATADIR+'fallas y cbm/falla_lomo2.csv',0)

flomo1dwn=[list(np.array(flomo1up[0])+70),
           list(np.array(flomo1up[1])-70),
           [0,0,0,0,0]]

flomo1_dat=falla(flomo1up,flomo1dwn,'#404040','Faults',1,'fallas','y',True)

flomo2dwn=[list(np.array(flomo2up[0])+70),
           list(np.array(flomo2up[1])-70),
           [250 for i in range(len(flomo2up[0]))]]
flomo2_dat=falla(flomo2up,flomo2dwn,'#404040','falla lomo2',1,'fallas','y',False)

fcastillo1up=contact2_tr(DATADIR+'fallas y cbm/Falla Castillo Mula UTM.csv',0)
fcastillo2up=contact2_tr(DATADIR+'fallas y cbm/Falla_castillo 2_rev UTM.csv',0)

fcastillo1dwn=[list(np.array(fcastillo1up[0])+100),
           list(np.array(fcastillo1up[1])+100),
          [220 for i in range(len(fcastillo1up[0]))]]

fcastillo1_dat=falla(fcastillo1up,fcastillo1dwn,'#404040','falla castillo Mula',1,'fallas','y',False)

fcastillo2upp=[list(np.array(fcastillo2up[0])),
           list(np.array(fcastillo2up[1])),
           fcastillo2up[2]]

fcastillo2dwn=[list(np.array(fcastillo2up[0])+130),
           list(np.array(fcastillo2up[1])-130),
           [0 for i in range(len(fcastillo2up[0]))]]

fcastillo2_dat=falla(fcastillo2upp,fcastillo2dwn,'#404040','falla castillo2',1,'fallas','y',False)

data_fallas=flomo1_dat+flomo2_dat+fcastillo1_dat+fcastillo2_dat

# Cabalgamientos cbm

Control_cbm0=pd.read_csv(DATADIR+'control/cbm/Control_cbm0.csv')
Control_cbm01=pd.read_csv(DATADIR+'control/cbm/Control_cbm01.csv')
Control_cbm1=pd.read_csv(DATADIR+'control/cbm/Control_cbm1.csv')
Control_cbm11=pd.read_csv(DATADIR+'control/cbm/Control_cbm11.csv')
Control_cbm2=pd.read_csv(DATADIR+'control/cbm/Control_cbm2.csv')
Control_cbm21=pd.read_csv(DATADIR+'control/cbm/Control_cbm21.csv')
Control_cbm3=pd.read_csv(DATADIR+'control/cbm/Control_cbm3.csv')
Control_cbm31=pd.read_csv(DATADIR+'control/cbm/Control_cbm31.csv')
Control_cbm4=pd.read_csv(DATADIR+'control/cbm/Control_cbm4.csv')
Control_cbm41=pd.read_csv(DATADIR+'control/cbm/Control_cbm41.csv')
Control_cbm5=pd.read_csv(DATADIR+'control/cbm/Control_cbm5.csv')
Control_cbm51=pd.read_csv(DATADIR+'control/cbm/Control_cbm51.csv')
Control_cbm6=pd.read_csv(DATADIR+'control/cbm/Control_cbm6.csv')
Control_cbm61=pd.read_csv(DATADIR+'control/cbm/Control_cbm61.csv')

listado=[Control_cbm0,
Control_cbm01,
Control_cbm1,
Control_cbm11,
Control_cbm2,
Control_cbm21,
Control_cbm3,
Control_cbm31,
Control_cbm4,
Control_cbm41,
Control_cbm5,
Control_cbm51,
Control_cbm6,
Control_cbm61]

listado0=[listado[i] for i in range(0,len(listado),2)]
listado1=[listado[i] for i in range(1,len(listado),2)]

b_cbm0x,b_cbm0y,b_cbm0z=bs(listado0)

b_cbm1x,b_cbm1y,b_cbm1z=bs(listado1)

tcbm=traza2([bs(listado0),bs(listado1)],azul,'Thrusts','cbm',True)


# Colored surface

# Superficie

H1=['hulls/h1_1.csv','hulls/h1_2.csv',
   'hulls/h1_3.csv','hulls/h1_4.csv',
   'hulls/h1_5.csv','hulls/h1_6.csv',
   'hulls/h1_7.csv','hulls/h1_8.csv']


H1_dat=[hul_dat4(DATADIR+H1[0],'Superficie','pink','Eoc2',False)]+[
    hul_dat4(DATADIR+x,'E2'+x,'pink','Eoc2',False) for x in H1[1:]]

H2=['hulls/h2_1.csv','hulls/h2_2.csv',
   'hulls/h2_3.csv','hulls/h2_4.csv',
   'hulls/h2_5.csv','hulls/h2_6.csv',
   'hulls/h2_7.csv','hulls/h2_8.csv',
   'hulls/h2_9.csv','hulls/h2_10.csv',
   'hulls/h2_11.csv','hulls/h2_111.csv',
   'hulls/h2_12.csv','hulls/h2_13.csv',
   'hulls/h2_14.csv']



H2_dat=[hul_dat4(DATADIR+H2[0],'Eocene 1','orange','Eoc1',False)]+[
    hul_dat4(DATADIR+x,'E1'+x,'orange','Eoc1',False) for x in H2[1:]]


H3=['hulls/h3_1.csv','hulls/h3_2.csv',
   'hulls/h3_3.csv','hulls/h3_4.csv']

H3_dat=[hul_dat4(DATADIR+H3[0],'Paleocene in surface','#b8a8ca','Pal',False)]+[
    hul_dat4(DATADIR+x,'sup','#b8a8ca','Pal',False) for x in H3[1:]]

H4=['hulls/h4_1.csv','hulls/h4_2.csv','hulls/h4_3.csv']

H4_dat=[hul_dat4(DATADIR+H4[0],'Paleoceno','#b8a8ca','Pal',False)]+[
    hul_dat4(DATADIR+x,'sup','#b8a8ca','Pal',False) for x in H4[1:]]


H5=['hulls/h5_1.csv','hulls/h5_2.csv']

H5_dat=[hul_dat4(DATADIR+H5[0],'E1','orange','Eoc1',False)]+[
    hul_dat4(DATADIR+x,'sup','orange','Eoc1',False) for x in H5[1:]]


H6=['hulls/h6_1.csv','hulls/h6_2.csv',
   'hulls/h6_3.csv','hulls/h6_4.csv',
   'hulls/h6_5.csv','hulls/h6_6.csv',
   'hulls/h6_7.csv','hulls/h6_8.csv',
   'hulls/h6_9.csv','hulls/h6_10.csv']

H6_dat=[hul_dat4(DATADIR+H6[0],'E2','pink','Eoc2',False)]+[
    hul_dat4(DATADIR+x,'E2'+x,'pink','Eoc2',False) for x in H6[1:]]


H7=['hulls/h7_1.csv','hulls/h7_2.csv',
    #'hulls/h7_3.csv',
    'hulls/h7_33.csv',
    'hulls/h7_34.csv',
    'hulls/h7_35.csv',
    'hulls/h7_36.csv',
    'hulls/h7_37.csv',
    'hulls/h7_38.csv',
    'hulls/h7_39.csv',
    'hulls/h7_310.csv',
    'hulls/h7_311.csv',
   'hulls/h7_4.csv']

H7_dat=[hul_dat4(DATADIR+H7[0],'E7','orange','Eoc1',False)]+[
    hul_dat4(DATADIR+x,'E1'+x,'orange','Eoc1',False) for x in H7[1:]]


H8=['hulls/h8_1.csv']
H8_dat=[hul_dat4(DATADIR+H8[0],'Paleoceno','#b8a8ca','Pal',False)]  

H9=['hulls/h9_1.csv','hulls/h9_2.csv',
   'hulls/h9_3.csv','hulls/h9_4.csv']

H9_dat=[hul_dat4(DATADIR+H9[0],'Cretásico','#a8e0ae','C1',False)]+[
    hul_dat4(DATADIR+x,'Cretásico'+x,'#a8e0ae','C1',False) for x in H9[1:]]


H10=['hulls/h10_1.csv','hulls/h10_2.csv',
   'hulls/h10_3.csv','hulls/h10_4.csv']

H10_dat=[hul_dat4(DATADIR+H10[0],'Paleoceno','#b8a8ca','Pal',False)]+[
    hul_dat4(DATADIR+x,'Paleoceno'+x,'#b8a8ca','Pal',False) for x in H10[1:]]


H11=['hulls/h11_1.csv','hulls/h11_2.csv',
    'hulls/h11_3.csv','hulls/h11_4.csv',
    'hulls/h11_5.csv']

H11_dat=[hul_dat4(DATADIR+H11[0],'Eoceno','orange','Eoc1',False)]+[
    hul_dat4(DATADIR+x,'Eoceno'+x,'orange','Eoc1',False) for x in H11[1:]]


H12=['hulls/h12_1.csv','hulls/h12_2.csv',
     'hulls/h12_3.csv','hulls/h12_4.csv',
     'hulls/h12_5.csv']

H12_dat=[hul_dat4(DATADIR+H12[0],'E2','pink','Eoc2',False)]+[
    hul_dat4(DATADIR+x,'E2'+x,'pink','Eoc2',False) for x in H12[1:]]


H13=['hulls/h13_1.csv','hulls/h13_2.csv',
     'hulls/h13_3.csv','hulls/h13_4.csv',
     'hulls/h13_5.csv',
     'hulls/h13_61.csv',
     'hulls/h13_62.csv',
     'hulls/h13_63.csv',
     'hulls/h13_64.csv',
     'hulls/h13_65.csv',
     'hulls/h13_66.csv',
     'hulls/h13_67.csv',
     'hulls/h13_68.csv',
     'hulls/h13_69.csv',
     'hulls/h20.csv','hulls/h21.csv','hulls/h23.csv','hulls/h24.csv']

H13_dat=[hul_dat4(DATADIR+H13[0],'Eoceno','orange','Eoc1',False)]+[
    hul_dat4(DATADIR+x,'Eoceno'+x,'orange','Eoc1',False) for x in H13[1:]]


H14=['hulls/h14_1.csv','hulls/h14_2.csv',
   'hulls/h14_3.csv']

H14_dat=[hul_dat4(DATADIR+H14[0],'Paleoceno','#b8a8ca','Pal',False)]+[
    hul_dat4(DATADIR+x,'Paleoceno'+x,'#b8a8ca','Pal',False) for x in H14[1:]]


H15=['hulls/h15_1.csv','hulls/h15_2.csv',
   'hulls/h15_3.csv']

H15_dat=[hul_dat4(DATADIR+H15[0],'Cretásico','pink','Eoc2',False)]+[
    hul_dat4(DATADIR+x,'Cretásico'+x,'pink','Eoc2',False) for x in H15[1:]]

#H20=['hulls/h20.csv','hulls/h21.csv','hulls/h22_v2.csv']
#H20_dat=[hul_dat4(DATADIR+H20[0],'P20','orange','P en sup1',True)]+[
 #   hul_dat4(DATADIR+x,'P20'+x,'orange','P en sup'+x,True) for x in H20[1:]]


H=H1_dat+H2_dat+H3_dat+H4_dat+H5_dat+H6_dat+H7_dat+H8_dat+H9_dat+H10_dat+H11_dat+H12_dat+H13_dat+H14_dat+H15_dat#+H20_dat