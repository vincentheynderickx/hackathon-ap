import numpy as np
import matplotlib.pyplot as plt

def energie(d,P):
    g=10
    rho=1.3
    if P==3.5:
        A=4.56
        Cx=0.46*10**(-3)
        k1=2.15*10**(-3)
    if P==5.2:
        A=4.86
        Cx=0.53*10**(-3)
        k1=2.50*10**(-3)
    if P==18:
        A=7.17
        Cx=0.69*10**(-3)
        k1=3.25*10**(-3)
    if P==44:
        A=9.34
        Cx=0.79*10**(-3)
        k1=3.75*10**(-3)
    if d>=20:
        vmoy=(20*7+11*(d-20))/d
        accelmoy=5*2.2/(d/vmoy)
        print(accelmoy)
        return vmoy*((1/2)*rho*vmoy**2*Cx*A+P*g*k1+P*accelmoy)*(d/vmoy)

    if d<20:
        vmax=(11*d)/20
        print(vmax)
        vmoy=vmax/2
        accelmoy=vmax/(d/(vmoy))
        print(accelmoy)
        return vmoy*((1/2)*rho*vmoy**2*Cx*A+P*g*k1+P*accelmoy)*(d/vmoy)


"""print(energie(25,3.5))
print(energie(21,3.5))
print(energie(20,3.5))
print(energie(19.5,3.5))
print(energie(18,3.5))

liste_d=np.linspace(0,1000,100)
liste_energie=[energie(d,3.5) for d in liste_d]
plt.plot(liste_d,liste_energie)
plt.show()"""