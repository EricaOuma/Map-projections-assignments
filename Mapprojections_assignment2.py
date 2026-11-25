from math import*

a= float(input("Enter a: "))
Az= float(input("Enter Az: "))
phi = float(input("Enter phi: "))
phi0 = float(input("Enter phi0: "))
lambdaa = float(input("Enter lambda: "))
lambda0 = float(input("Enter lambda0: "))

def forward(a,phi,phi0,lambdaa,lambda0,Az,f=1/293.465,):
   lambdaa = radians(lambdaa)
   lambda0 = radians(lambda0)
   es = 2*f - f**2
   N= a/sqrt(1-es*(sin(phi)**2)) 
   T = (tan(phi))**2
   A = (lambdaa - lambda0) * cos(phi)
   C= es*(cos(phi))**2/(1-es)
   M= a*(phi*(1-es/4-3*es**2/64-5*e**3/256)-sin(2*phi)*(3*es/8+3*es**2/32+45*es**3/1024)+sin(4*phi)*(15*es**2/256+45*es**3/1024)-sin(6*phi)*(35*es**3/3072))
   M0= a*(phi0*(1-es/4-3*es**2/64-5*e**3/256)-sin(2*phi0)*(3*es/8+3*es**2/32+45*es**3/1024)+sin(4*phi0)*(15*es**2/256+45*es**3/1024)-sin(6*phi0)*(35*es**3/3072))
   x= N*(A-T*A**3/6-(8-T+8*C)*T*A**5/120)
   y= M-M0+N*tan(phi)*(A**2/2+(5-T+6*C)*A**4/24)
   s=1+x**2*(cos(Az))**2*(1-es*(sin(phi))**2/2*a**2*(1-es))

   return f"x: {x} \n y: {y} \n s: {s}"
print(forward(a,Az,phi, phi0, lambdaa, lambda0))

   




