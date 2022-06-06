import numpy as np
from scipy.integrate import odeint

class Dstate:
    def __init__(self, Cd):
        self.Cd = Cd

    def __call__(self, X, t):
        # Parametri fissi
        rho = 1.25 # Densita' dell'aria
        A = 2.5 * 1.2 # Superficie della seziojne
        m = 1539 # Massa dell'auto
        F = 10000 # Forza di accelerazione
        
        # Spacchetto lo stato
        x, v = X
        # Calcolo la forza di trascinamento
        Ft = -0.5 * rho * A * self.Cd * v * np.abs(v)
        # Calcolo le derivate
        dx = v
        dv = 1/m * (F + Ft)
        return np.array([dx, dv])


def simulate(Cd):
    x0 = [0, 0]
    t = np.linspace(0, 60, 60000)
    f = Dstate(Cd)
    X = odeint(f, x0, t)
    return X, t
    
    
    
    
    