from math import *

a = float(input("Enter a: "))
phi = float(input("Enter phi: "))
phi0 = float(input("Enter phi0: "))
lambdaa = float(input("Enter lambda: "))
lambda0 = float(input("Enter lambda0: "))


def forward(a, phi, phi0,  lambd, lambda0, k0=0.9996, f=1/298.25722):
    e0 = 500_000
    es = 2*f - f**2
    lambd = radians(lambd)
    lambda0 = radians(lambda0)
    phi = radians(phi)
    T = (tan(phi))**2
    eps = es/(1-es)
    C = eps * (cos(phi))**2
    A = (lambd - lambda0) * cos(phi)
    N = a/sqrt(1-es*(sin(phi))**2)
    M = a*(phi*(1-es/4-3*es**2/64-5*es**3/256) - sin(2*phi)*(3*es/8 + 3*es**2/32 + 45*es**3/1024) - sin(4*phi)*(15*es**2/256 + 45*es**3/1024) - sin(6*phi)*(35*es**3/3072))
    M0 = a*(phi0*(1-es/4-3*es**2/64-5*es**3/256) - sin(2*phi0)*(3*es/8 + 3*es**2/32 + 45*es**3/1024) - sin(4*phi0)*(15*es**2/256 + 45*es**3/1024) - sin(6*phi0)*(35*es**3/3072))
    x = e0 + k0 * N*(A + (1-T+C)*A**3/6 + (5-18*T+ T**2+72*C-58*eps)*A**5/120)
    y = k0 * (M-M0+N*tan(phi)*(A**2/2 + (5-T+9*C+4*C**2)*A**4/24) + (61-58*T+T**2 +600*C-330*eps)*A**6/720)
    k = k0*(1+(1+C)*A**2/2 + (5-4*T+42*C+13*C**2-28*eps)*A**4/24 + (61-148*T+16*T**2)*A**6/720)
    return f"x: {x} \n y: {y} \n k: {k}"

print(forward(a, phi, phi0, lambdaa, lambda0))
