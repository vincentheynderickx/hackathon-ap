import numpy as np
import matplotlib.pyplot as plt

def energie(d):
    m = 5000
    P = 100*745.7 #on utilise 100 chevaux en moyenne
    E = P*(9/4 * d**2 * m/(2*P))**(1/3) #obtenue à partir de E=Pt et v=sqrt(2Pt/m)
    return E

"""d=np.linspace(0,1000,10000)
plt.plot(d,energie(d))
plt.show()"""