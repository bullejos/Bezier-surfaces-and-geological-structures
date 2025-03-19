# data analysis library
import pandas as pd

# math libraries
import numpy as np
from numpy.linalg import norm

import sympy
from sympy import *
t = Symbol('t')

from scipy.interpolate import interp2d
from scipy.interpolate import griddata
import math

from Bezier import Bezier


import shapely.geometry as geometry
from shapely.geometry import Polygon
from shapely.geometry import Point
from scipy.spatial import ConvexHull


# plotting libraries
import plotly.offline as go_offline
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker


# Ours custom fuctions

# color scales

gist_earth= [[0.0,'#b5e2ff'],#  '#2271b3'],
 [0.02, '#102977'],
 [0.05, '#215e7b'],
 [0.09, '#31827a'],
 [0.1, '#3e915a'],
 [0.3, '#5da04b'],
 [0.5, '#8dab56'],
 [0.7, '#b7b55e'],
 [0.8, '#c3a46e'],
 [0.9, '#e1bfaf'],
 [1.0, '#fdfafa']]

amarillo= [
 [0.0, '#F5CA61'],
[1.0, '#F4D166']]

azul=[
    [0, '#3352FF'],
    [1,'#5233FF']]

#naranja= [[0.0,'#ffe0b2'],#  '#2271b3'],
# [0.3, '#ffcc80'],
# [0.6, '#ffb74d'],
# [1.0, '#ffa726']]

naranja= [[0, 'orange'],
                    [0.5, 'orange'],
                    [1, 'orange']]

#[[0.0,'#ffe0b2'],#  '#2271b3'],
# [0.3, '#ffe0b2'],
# [0.6,'#ffe0b2'],
# [1.0, '#ffe0b2']]

#pink= [[0.0,'#f4c2c2'],#  '#2271b3'],
 #[0.3, '#ffc0cb'],
 #[0.6, '#ff91a4'],
 #[1.0, '#e4717a']]

pink= [[0.0,'#f4c2c2'],#  '#2271b3'],
 [0.3,'#f4c2c2'],
 [0.6, '#f4c2c2'],
 [1.0, '#f4c2c2']]

verde= [[0.0,'#a7ce4f'],#  '#2271b3'],
 [0.3, '#b5d66b'],
 [0.6, '#c3dd87'],
 [1.0, '#d1e5a3']]

verde_c= [[0.0,'#59c464'],#  '#2271b3'],
 [0.3, '#73cd7d'],
 [0.6, '#8ed695'],
 [1.0, '#a8e0ae']]

#marron= [[0.0,'#b17c54'],#  '#2271b3'],
 #[0.3, '#c69b7c'],
 #[0.6, '#dbbba6'],
 #[1.0, '#eeddd2']]

cyan= [[0.0,'#1a98a6'],
 [0.3, '#1dadc0'],
 [0.6, '#1fbdd2'],
 [1.0, '#33c7d8']]

violeta=[[0.0,'#b8a8ca'],
         [0.5,'#cfbde3'],
         [1,'#e7d3fd']
         ]

# read a csv file and split the data modifying the elevation with elevation_gain
def contact_tr(csv,elevation_gain):
    tr=pd.read_csv(csv)
    tr1=tr[['X','Y','SAMPLE_1']].to_numpy()
    tx=[x[0] for x in tr1]
    ty=[x[1] for x in tr1]
    telv=[x[2]+elevation_gain for x in tr1]
    return [tx,ty,telv]

def contact2_tr(csv,elevation_gain):
    tr=pd.read_csv(csv)
    tr1=tr[['UTM_X','UTM_Y','elevation']].to_numpy()
    tx=[x[0] for x in tr1]
    ty=[x[1] for x in tr1]
    telv=[x[2]+elevation_gain for x in tr1]
    t=[np.sqrt(tx[i]**2+ty[i]**2) for i in range(len(tx))]
    return [tx,ty,telv,t]

def contact3_tr(csv,elevation_gain):
    tr=pd.read_csv(csv)
    tr1=tr[['UTM_X','UTM_Y','elevation','color']].to_numpy()
    tx=[x[0] for x in tr1]
    ty=[x[1] for x in tr1]
    k=tr['color'].to_numpy()
    telv=[x[2]+elevation_gain for x in tr1]
    t=[np.sqrt(tx[i]**2+ty[i]**2) for i in range(len(tx))]
    return [tx,ty,telv,t,k]

# data for plotting
def contact_dat(x,y,elv,h,mode,nam,color,gr,t,ls):
    z=[x+h for x in elv]
    return go.Scatter3d(x=x, y=y, z=z,
            mode =mode,
            name=nam,
            legendgroup=gr,
            showlegend=t,
            line=dict(color=color,
                      dash=ls,
                      width=7)
                        )

def contact_dat2(x,y,elv,h,mode,nam,color,gr,t,ls,w):
    z=[x+h for x in elv]
    return go.Scatter3d(x=x, y=y, z=z,
            mode =mode,
            name=nam,
            legendgroup=gr,
            showlegend=t,
            line=dict(color=color,
                      dash=ls,
                      width=w)
                        )


def cabalga1(cab,col,nombre,op,grupo,t,dela):
    xx=cab[0]
    yy=cab[1]
    zz=cab[2]
    return go.Mesh3d(x=xx,y=yy,z=zz, 
                     delaunayaxis=dela,
                     name=nombre,
                     opacity=op,
                     color =col,
                     legendgroup=grupo,
                     showlegend=t 
                    )

def falla(fallaup,falladwn,color,nombre,op,grupo,dela,t):
    fn=[[[fallaup[0][i],fallaup[0][i+1],falladwn[0][i],falladwn[0][i+1]],
        [fallaup[1][i],fallaup[1][i+1],falladwn[1][i],falladwn[1][i+1]],
        [fallaup[2][i],fallaup[2][i+1],falladwn[2][i],falladwn[2][i+1]]] for i in range(len(fallaup[0])-1)
       ]
    fn2=[cabalga1(fn[i],color,nombre,1,grupo,False,dela) for i in range(len(fn)-1)]
    fn2.append(cabalga1(fn[-1],color,nombre,1,grupo,t,dela))
    return fn2

def traza(lista,color,nombre,grupo):
    t=[]
    for i in range(len(lista)):
        bx,by,bz=lista[i]
        t.append(go.Surface(x=bx,y=by,z=bz,
                      colorscale=color,
                      opacity = 1,name=nombre+str(i),
                      legendgroup=grupo+'str(i)',
                      showlegend=True,showscale=False))
    return t

def traza2(lista,color,nombre,grupo,true_valor):
    bx0,by0,bz0=lista[0]
    
    t=[go.Surface(x=bx0,y=by0,z=bz0,
                      colorscale=color,
                      opacity = 1,name=nombre,
                      legendgroup=grupo,
                      showlegend=true_valor,
                      showscale=False)]
    for i in range(1,len(lista)):
        bx,by,bz=lista[i]
        t.append(go.Surface(x=bx,y=by,z=bz,
                      colorscale=color,
                      opacity = 1,name=nombre,
                      legendgroup=grupo,
                       showlegend=False,
                       showscale=False))
    return t

# Geometric function

def distance(A,B):   #the distance between two point of the plane
    return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)


def para_line(p1,p2):   #parametric equation of a line in the plane
    d=distance(p1,p2)
    P1=np.array(p1)
    P2=np.array(p2)
    v = (P2 - P1)/d
    g = lambda t: [P1[0]+v[0]*t,P1[1]+v[1]*t]
    return g

def get_intersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return [x/z, y/z]



def distancia(A, B, P):
    #Comprobamos que el punto no corresponda a los extremos del segmento.
    if all(A==P) or all(B==P):
        return 0

    #Calculamos el angulo entre AB y AP, si es mayor de 90 grados retornamos la distancia enre A y P
    elif np.arccos(np.dot((P-A)/norm(P-A), (B-A)/norm(B-A))) > np.pi/2:
        return norm(P-A)

    #Calculamos el angulo entre AB y BP, si es mayor de 90 grados retornamos la distancia enre B y P.
    elif np.arccos(np.dot((P-B)/norm(P-B), (A-B)/norm(A-B))) > np.pi/2:
        return norm(P-B)

    #Como ambos angulos son menores o iguales a 90º sabemos que podemos hacer una proyección ortogonal del punto.
    return norm(np.cross(B-A, A-P))/norm(B-A)

def intercection(polygon,point1,point2):
    x=polygon[0]
    y=polygon[1]
    xy=[np.array((x[i],y[i])) for i in range(len(x))]
    n1=np.array(point1)
    n2=np.array(point2)
    d1=[distancia(n1,n2,xy[i]) for i in range(len(xy))]
    xyd=[(x[i],y[i],d1[i]) for i in range(len(x))]
    sxyd=sorted(xyd, key=lambda x: x[2])
    c0=get_intersect(point1,point2,sxyd[0][:-1],sxyd[1][:-1])
    return c0

def plane_y(p1,p2,p3,x,z):
    P1=np.array(p1)
    P2=np.array(p2)
    P3=np.array(p3)
    v1 = P3 - P1
    v2 = P2 - P1
    cp = np.cross(v1, v2)
    a, b, c = cp
    d = np.dot(cp, P3)
    if b!=0:
        return [True,(d - a * x - c * z) / b ] 
    else:
        return [False, a*x+c*z-d]
    

DATADIR='data/' # Directory with the data
def control_to_csv(xs,Control,name):
    Controlx=[x[0] for x in Control]
    Controly=[x[1] for x in Control]
    Controlele=[x[2] for x in Control]
    Controlt=[np.sqrt(x[0]**2+x[1]**2) for x in Control]
    Controltt=[max(xs[3])-x for x in Controlt]

    Controlpan=pd.DataFrame(Controlx,columns = ['X'])
    Controlpan['Y']=Controly
    Controlpan['Z']=Controlele
    Controlpan['t']=Controlt
    Controlpan['tt']=Controltt
    
    Controlpan.to_csv(DATADIR+'control/'+name)

def bezier_to_csv(xs,bz,name):
    bzt=bz[4]
    bztt=[max(xs[3])-x for x in bzt]
    bzpan=pd.DataFrame(bz[0],columns = ['UTM_X'])
    bzpan['UTM_Y']=bz[1]
    bzpan['elevation']=bz[2]
    bzpan['t']=bz[4]
    bzpan['tt']=bztt
    bzpan.to_csv(DATADIR+'cbz/'+name)

def plano_3d(A0,A1,deep,nombre,grupo,t):
    x=[A0[0],A0[0],A1[0],A1[0]]
    y=[A0[1],A0[1],A1[1],A1[1]]
    z=[max(A0[2],A1[2])+100,deep,max(A0[2],A1[2])+100,deep]
    return go.Mesh3d(x=x,y=y,z=z,
                     delaunayaxis='y',
                     name=nombre,
                     legendgroup=grupo,
                     showlegend=t,
                     opacity=0.30,
                     color ='#FFE900' )

def split_list(lst, chunk_size):
    chunks = []
    for i in range(0, len(lst), chunk_size):
        chunk = lst[i:i + chunk_size]
        chunks.append(chunk)
    return chunks


# La topo
def surface(grid,metodo): #metodo='linear', 'cubic' o 'nearest'

    tx=grid[0]
    ty=grid[1]
    tz=grid[2]

    X = np.linspace(min(tx), max(tx))
    Y = np.linspace(min(ty), max(ty))
    X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
    Z = griddata((tx,ty),tz,(X,Y), 
                 method=metodo)
    
    return [tx,ty,tz,X,Y,Z]

# Bezier functions curve

t_points = np.arange(0, 1, 0.01) # Creates an iterable list from 0 to 1.

def bz(Plano,puntos):
    xc=[x[0] for x in puntos]
    yc=[x[1] for x in puntos]
    zc=[x[2] for x in puntos]
    c_Bz=[[xc[i], zc[i]] for i in range(len(xc))]
    npc_Bz=np.array(c_Bz)
    c1_Bz= Bezier.Curve(t_points,npc_Bz) 
    x1=[x[0] for x in c1_Bz]
    z1=[x[1] for x in c1_Bz]
    y1=[plane_y(Plano[0],Plano[1],Plano[2],x1[i],z1[i])[1] for i in range(len(x1))]
    t1=[np.sqrt(x1[i]**2+y1[i]**2) for i in range(len(x1))]
    return [x1,y1,z1,npc_Bz,t1]  

# Bezier functions surface
# elegimos tamaño
uCELLS= 6
wCELLS= 5

def Ni(n, i):
        return math.factorial(n) / (math.factorial(i) * math.factorial(n - i))

def Mj(m, j):
        return math.factorial(m) / (math.factorial(j) * math.factorial(m - j))

def J(n,i,u):
        return np.matrix(Ni(n, i)*(u**i)*(1-u)**(n - i))

def k(m,j,w):
        return np.matrix(Mj(m,j)*(w**j)*(1-w)**(m-j))


def bezierSurface(x,y,z,uCELLS,wCELLS):
    uPTS= np.size(x,0)
    wPTS= np.size(x,1)
    n=uPTS -1
    m=wPTS -1

    u = np.linspace (0, 1, uCELLS)
    w = np.linspace (0, 1, wCELLS)

    b=[]
    d=[]

    xBezier=np.zeros((uCELLS,wCELLS))
    yBezier=np.zeros((uCELLS,wCELLS))
    zBezier=np.zeros((uCELLS,wCELLS))

    for i in range(0,uPTS):
        for j in range(0,wPTS):
            b.append(J(n,i,u))
            d.append(k(m,j,w))
        
            Jt=J(n,i,u).transpose()
        
            xBezier=Jt*k(m,j,w)*x[i,j]+xBezier
            yBezier=Jt*k(m,j,w)*y[i,j]+yBezier
            zBezier=Jt*k(m,j,w)*z[i,j]+zBezier
    return xBezier,yBezier,zBezier

def bs(lista):
    x=[]
    y=[]
    z=[]
    for l in lista:
        ll=l[['X','Y','Z','t','tt']].to_numpy()
        lx=[x[0] for x in ll]
        ly=[x[1] for x in ll]
        lz=[x[2] for x in ll]
        x.append(lx)
        y.append(ly)
        z.append(lz)
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 

def bs2(lista):
    xlast=[]
    ylast=[]
    zlast=[]
    xfirst=[]
    yfirst=[]
    zfirst=[]
    for l in lista:
        ll=l[['X','Y','Z','t','tt']].to_numpy()
        lx=[x[0] for x in ll]
        ly=[x[1] for x in ll]
        lz=[x[2] for x in ll]
        xfirst.append(lx[0])
        yfirst.append(ly[0])
        zfirst.append(lz[0])
        xlast.append(lx[-1])
        ylast.append(ly[-1])
        zlast.append(lz[-1])
    x=np.array([[xlast[i],xfirst[i+1]] for i in range(0,len(xfirst),2)])  
    y=np.array([[ylast[i],yfirst[i+1]] for i in range(0,len(yfirst),2)]) 
    z=np.array([[zlast[i],zfirst[i+1]] for i in range(0,len(zfirst),2)]) 
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 

# antes bs = bezier ahora

def bezier(data,r):
    x=split_list(data["X"].to_list(),r)
    y=split_list(data["Y"].to_list(),r)
    z=split_list(data["Z"].to_list(),r)
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 
def acople(data1,data2,r):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),r)
    y2=split_list(data2["Y"].to_list(),r)
    z2=split_list(data2["Z"].to_list(),r)
    x1l=[x[-1] for x in x1]
    x2f=[x[0] for x in x2]
    x=[[x1l[i],x2f[i]] for i in range(len(x1l))]
    y1l=[x[-1] for x in y1]
    y2f=[x[0] for x in y2]
    y=[[y1l[i],y2f[i]] for i in range(len(y1l))]
    z1l=[x[-1] for x in z1]
    z2f=[x[0] for x in z2]
    z=[[z1l[i],z2f[i]] for i in range(len(z1l))]
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 


def acople2(data1,data2,r,s):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),s)
    y2=split_list(data2["Y"].to_list(),s)
    z2=split_list(data2["Z"].to_list(),s)
    x1l=[x[-1] for x in x1]
    x2f=[x[0] for x in x2]
    x=[[x1l[i],x2f[i]] for i in range(len(x1l))]
    y1l=[x[-1] for x in y1]
    y2f=[x[0] for x in y2]
    y=[[y1l[i],y2f[i]] for i in range(len(y1l))]
    z1l=[x[-1] for x in z1]
    z2f=[x[0] for x in z2]
    z=[[z1l[i],z2f[i]] for i in range(len(z1l))]
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 



def pegue(data1,data2,r):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),r)
    y2=split_list(data2["Y"].to_list(),r)
    z2=split_list(data2["Z"].to_list(),r)
    x=[x1[-1],x2[0]]
    y=[y1[-1],y2[0]]
    z=[z1[-1],z2[0]]
    return bezierSurface(np.array(x),np.array(y),np.array(z),uCELLS,wCELLS) 

# cutting Beziere surface

def bezierSinpol(x,y,z,uCELLS,wCELLS,points):
    pol=Polygon(points)
    bx,by,bz=bezierSurface(x,y,z,uCELLS,wCELLS)
    x0=bx.flatten().tolist()[0]
    y0=by.flatten().tolist()[0]
    z0=bz.flatten().tolist()[0]
    xx=[]
    yy=[]
    zz=[]
    for i in range(len(x0)):
        if pol.contains(Point(x0[i],y0[i])):
            xx=xx+[x0[i]]
            yy=yy+[y0[i]]
            zz=zz+[z0[i]]
    return xx,yy,zz



def bezierSnearpol(x,y,z,uCELLS,wCELLS,points,d):
    pol=Polygon(points)
    bx,by,bz=bezierSurface(x,y,z,uCELLS,wCELLS)
    x0=bx.flatten().tolist()[0]
    y0=by.flatten().tolist()[0]
    z0=bz.flatten().tolist()[0]
    xx=[]
    yy=[]
    zz=[]
    for i in range(len(x0)):
        if pol.distance(Point(x0[i],y0[i]))< d:
            xx=xx+[x0[i]]
            yy=yy+[y0[i]]
            zz=zz+[z0[i]]
    return xx,yy,zz
    

def bezierr(data,r,points):
    x=split_list(data["X"].to_list(),r)
    y=split_list(data["Y"].to_list(),r)
    z=split_list(data["Z"].to_list(),r)
    return bezierSinpol(np.array(x),np.array(y),np.array(z),100,100,points) 

def acopler(data1,data2,r,points):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),r)
    y2=split_list(data2["Y"].to_list(),r)
    z2=split_list(data2["Z"].to_list(),r)
    x1l=[x[-1] for x in x1]
    x2f=[x[0] for x in x2]
    x=[[x1l[i],x2f[i]] for i in range(len(x1l))]
    y1l=[x[-1] for x in y1]
    y2f=[x[0] for x in y2]
    y=[[y1l[i],y2f[i]] for i in range(len(y1l))]
    z1l=[x[-1] for x in z1]
    z2f=[x[0] for x in z2]
    z=[[z1l[i],z2f[i]] for i in range(len(z1l))]
    return bezierSinpol(np.array(x),np.array(y),np.array(z),100,100,points) 


def acople2r(data1,data2,r,s,points):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),s)
    y2=split_list(data2["Y"].to_list(),s)
    z2=split_list(data2["Z"].to_list(),s)
    x1l=[x[-1] for x in x1]
    x2f=[x[0] for x in x2]
    x=[[x1l[i],x2f[i]] for i in range(len(x1l))]
    y1l=[x[-1] for x in y1]
    y2f=[x[0] for x in y2]
    y=[[y1l[i],y2f[i]] for i in range(len(y1l))]
    z1l=[x[-1] for x in z1]
    z2f=[x[0] for x in z2]
    z=[[z1l[i],z2f[i]] for i in range(len(z1l))]
    return bezierSinpol(np.array(x),np.array(y),np.array(z),100,100,points) 



def peguer(data1,data2,r,puntos):
    x1=split_list(data1["X"].to_list(),r)
    y1=split_list(data1["Y"].to_list(),r)
    z1=split_list(data1["Z"].to_list(),r)
    x2=split_list(data2["X"].to_list(),r)
    y2=split_list(data2["Y"].to_list(),r)
    z2=split_list(data2["Z"].to_list(),r)
    x=[x1[-1],x2[0]]
    y=[y1[-1],y2[0]]
    z=[z1[-1],z2[0]]
    return bezierSinpol(np.array(x),np.array(y),np.array(z),100,100,puntos) 

def surface2(grid,n,metodo): #metodo='linear', 'cubic' o 'nearest' n=nº de puntos en el linespace

    tx=grid[0]
    ty=grid[1]
    tz=grid[2]

    X = np.linspace(min(tx), max(tx),n)
    Y = np.linspace(min(ty), max(ty),n)
    X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
    Z = griddata((tx,ty),tz,(X,Y), 
                 method=metodo)
    
    return [tx,ty,tz,X,Y,Z]

def surface2inpol(grid,n,metodo,point1,point2): #metodo='linear', 'cubic' o 'nearest' n=nº de puntos en el linespace
    # point1 es un csv point2 es una lista de puntos (x,y)
    p_pol1=point1[['X','Y']].to_numpy()
    pol1=Polygon(p_pol1)
    pol2=Polygon(point2)
    tx=list(grid['X'])
    ty=list(grid['Y'])
    tz=list(grid['SAMPLE_1'])
    for i in range(len(tz)):
        if not(pol1.contains(Point(tx[i],ty[i]))) or not(pol2.contains(Point(tx[i],ty[i]))):
          tz[i]=np.nan
    X = np.linspace(min(tx), max(tx),n)
    Y = np.linspace(min(ty), max(ty),n)
    X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
    Z = griddata((tx,ty),tz,(X,Y), 
                 method=metodo)
    return [tx,ty,tz,X,Y,Z]

def surface2nearpol(grid,n,metodo,point1,point2,d): #metodo='linear', 'cubic' o 'nearest' n=nº de puntos en el linespace
    # point1 es un csv point2 es una lista de puntos (x,y)
    p_pol1=point1[['X','Y']].to_numpy()
    pol1=Polygon(p_pol1)
    pol2=Polygon(point2)
    tx=list(grid['X'])
    ty=list(grid['Y'])
    tz=list(grid['SAMPLE_1'])
    for i in range(len(tz)):
        if pol1.distance(Point(tx[i],ty[i]))>d or not(pol2.contains(Point(tx[i],ty[i]))):
          tz[i]=np.nan
    X = np.linspace(min(tx), max(tx),n)
    Y = np.linspace(min(ty), max(ty),n)
    X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
    Z = griddata((tx,ty),tz,(X,Y),method=metodo)
    return [tx,ty,tz,X,Y,Z]

def surface2nearpol2(grid,n,metodo,point1,point2,d1,d2): #metodo='linear', 'cubic' o 'nearest' n=nº de puntos en el linespace
    # point1 es un csv point2 es una lista de puntos (x,y)
    p_pol1=point1[['X','Y']].to_numpy()
    pol1=Polygon(p_pol1)
    pol2=Polygon(point2)
    tx=list(grid['X'])
    ty=list(grid['Y'])
    tz=list(grid['SAMPLE_1'])
    for i in range(len(tz)):
        if pol1.distance(Point(tx[i],ty[i]))>d1 or pol2.distance(Point(tx[i],ty[i]))>d2:
          tz[i]=np.nan
    X = np.linspace(min(tx), max(tx),n)
    Y = np.linspace(min(ty), max(ty),n)
    X, Y = np.meshgrid(X, Y)  # 2D grid for interpolation
    Z = griddata((tx,ty),tz,(X,Y),method=metodo)
    return [tx,ty,tz,X,Y,Z]

  # Triangles

def triangulo(data,gr,d):
    x=split_list(data["X"].to_list(),3)
    y=split_list(data["Y"].to_list(),3)
    zz=data["SAMPLE_1"].to_list()
    zd=[zz[i]+d for i in range(len(zz))]
    z=split_list(zd,3)
    return [go.Mesh3d(x=x[i],y=y[i],z=z[i],
                        alphahull=5, opacity=1, color='black',
                        i = np.array([0]),
                        j = np.array([1]),
                        k = np.array([2]),
                        legendgroup=gr,
                        showlegend=False) for i in range(len(x))]




# Convex Hull functions

def hul_dat0(lista,nam,col,grupo,tr):
    H=ConvexHull(lista)
    PH=H.points
    vh=H.vertices
    sh=H.simplices 
    return go.Mesh3d(x=PH[:, 0],y=PH[:, 1], z=PH[:, 2], 
                        name=nam,
                        legendgroup=grupo,
                        showlegend=tr,
                        colorbar_title=nam,
                        color=col, 
                     #i=sh[:, 0], j=sh[:, 1], k=sh[:, 2],
                        opacity=1,
                        alphahull=5,
                        showscale=False)

def hul_dat4(csv,nam,col,grupo,tr):
    pan=pd.read_csv(csv)
    pan0=pan[['X','Y','SAMPLE_1']].to_numpy()
    return hul_dat0(pan0,nam,col,grupo,tr)
