from functions import *
DATADIR='data/' # Directory with the data
CSV='data/csv/'

# C1

Control0_C1_31=pd.read_csv(DATADIR+'control/Control0_C1_31_v10.csv')
Control0_C1_32=pd.read_csv(DATADIR+'control/Control0_C1_32_v10.csv')

Control1_C1_31=pd.read_csv(DATADIR+'control/Control1_C1_31_v14.csv')
Control1_C1_32=pd.read_csv(DATADIR+'control/Control1_C1_32_v10.csv')
Control15_C1_312=pd.read_csv(DATADIR+'control/Control15_C1_321_v14.csv')
Control14_C1_312=pd.read_csv(DATADIR+'control/Control14_C1_31_v1.csv')
Control13_C1_312=pd.read_csv(DATADIR+'control/Control13_C1_31_v1.csv')

Control2_C1_31=pd.read_csv(DATADIR+'control/Control2_C1_31_v13.csv')
Control2_C1_32=pd.read_csv(DATADIR+'control/Control2_C1_32_v13.csv')

Control3_C1_312=pd.read_csv(DATADIR+'control/Control3_C1_312_v12.csv')

C1_31_s4=pd.concat([Control0_C1_31,Control0_C1_32,
                    Control1_C1_31,Control1_C1_32,
                    Control13_C1_312,
                    Control14_C1_312,
                    Control15_C1_312,
                    Control2_C1_31,
                    Control2_C1_32,
                    Control3_C1_312], axis=0)

bsC1_312_s4=bezier(C1_31_s4,8)
tC1_312_s4=traza2([bsC1_312_s4],verde_c,'C1_312','C1',False)

tC13_s4=tC1_312_s4#+tC1_32_c

# C2

Control0_C2_31=pd.read_csv(DATADIR+'control/Control0_C2_31_v10.csv')
Control0_C2_32=pd.read_csv(DATADIR+'control/Control0_C2_32_v10.csv')


Control1_C2_31=pd.read_csv(DATADIR+'control/Control1_C2_31_v10.csv')
Control1_C2_32=pd.read_csv(DATADIR+'control/Control1_C2_32_v10.csv')
Control15_C2_312=pd.read_csv(DATADIR+'control/Control15_C2_312_v13.csv')


Control2_C2_31=pd.read_csv(DATADIR+'control/Control2_C2_31_v13.csv')
Control2_C2_32=pd.read_csv(DATADIR+'control/Control2_C2_32_v10.csv')

Control3_C2_312=pd.read_csv(DATADIR+'control/Control3_C2_312_v12.csv')

C2_3_s4=pd.concat([Control0_C2_31,Control0_C2_32,
                   Control1_C2_31,Control1_C2_32,
                   Control15_C2_312,
                   Control2_C2_31,Control2_C2_32,
                  Control3_C2_312], axis=0)
bsC2_3_s4=bezier(C2_3_s4,7)
tC2_3_s4=traza2([bsC2_3_s4],violeta,'C2_3_s4','Pal',False)

# P

Control0_P_31=pd.read_csv(DATADIR+'control/Control0_P_31_v21.csv')
Control0_P_32=pd.read_csv(DATADIR+'control/Control0_P_32_v10.csv')


Control1_P_31=pd.read_csv(DATADIR+'control/Control1_P_31_v10.csv')
Control1_P_32=pd.read_csv(DATADIR+'control/Control1_P_32_v10.csv')


Control0_P_31

Control2_P_31=pd.read_csv(DATADIR+'control/Control2_P_31_v13.csv')
Control2_P_32=pd.read_csv(DATADIR+'control/Control2_P_32_v10.csv')

Control3_P_312=pd.read_csv(DATADIR+'control/Control3_P_312_v12.csv')

P_3_s4=pd.concat([Control0_P_31,Control0_P_32,
                Control1_P_31,Control1_P_32,
                Control2_P_31,Control2_P_32,
                  Control3_P_312
                ], axis=0)
bsP_3_s4=bezier(P_3_s4,7)
tP_3_s4=traza2([bsP_3_s4],naranja,'P_3_s4','Eoc1',False)

# E1

Control0_E1_31=pd.read_csv(DATADIR+'control/Control0_E1_31_v13.csv')
Control0_E1_32=pd.read_csv(DATADIR+'control/Control0_E1_32_v10.csv')


Control1_E1_31=pd.read_csv(DATADIR+'control/Control1_E1_31_v13.csv')
Control1_E1_32=pd.read_csv(DATADIR+'control/Control1_E1_32_v10.csv')
Control15_E1_312=pd.read_csv(DATADIR+'control/Control15_E1_312_v13.csv')



Control2_E1_31=pd.read_csv(DATADIR+'control/Control2_E1_31_v12.csv')
Control2_E1_32=pd.read_csv(DATADIR+'control/Control2_E1_32_v10.csv')

Control3_E1_312=pd.read_csv(DATADIR+'control/Control3_E1_312_v12.csv')

E1_3_s4=pd.concat([Control0_E1_31,Control0_E1_32,
                   Control1_E1_31,Control1_E1_32,
                   Control15_E1_312,#Control2_E1_32,
                   Control3_E1_312
                 ], axis=0)
bsE1_3_s4=bezier(E1_3_s4,7)
tE1_3_s4=traza2([bsE1_3_s4],pink,'E1_3_s4','Eoc2',False)
