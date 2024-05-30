# import math
print("hi")
tkr = 194
pkr = 4.9
val = []
for i in range(2): 
    print(i)
    t = float(input())+273
    p = float(input())
    z = 1 - 0.4273*(float(p/pkr))*(float(t/tkr))**-3.668
    rho = p/(z*t)
    val.append(rho)
ans = val[0]/val[1]
print(f"ans =  {ans}")

# d = float(input("d [mm] = "))*0.001
# q = float(input("Q [m3/h] = "))/3600
# delta = float(input("Δ  [mm] = "))*0.001
# # l = float(input("L [km] = "))*1000
# v = round(4*float(q)/(math.pi*float(d)**2), 3)
# mu = float(input("μ [sPz]= "))*10**-3
# rho = float(input("ρ [kg/m3]= "))
# nu = round(float(mu)/float(rho), 10)
# print("υ=(4*Q)/(π*d^2) = ", v, " m/s")
# e = round(float(delta)/float(d), 6)
# print("ε = ", e)
# re = round(float(v)*float(d)/(float(nu)), 2)
# print("Re=(υ*d/ν) = ", re)
# print("ν= μ/ρ = ", nu, "m2/s")
# hy_lambda = ""
# if 0 < re < 2380:
#     print(f"Re is between 0 and 2380")
#     hy_lambda = float(64/re)
# elif 2380 < re < 10**4:
#     print(f"Re is between 2380 and 10,000")
#     gamma = 1-(math.e)**(-0.002*(re-2320))
#     hy_lambda = float((64/re)*(1 - gamma) + (0.3164/(re**0.25))*gamma)
# elif 10**4 < re < 10/e:
#     print(f"10/ε = {10/e}")
#     print(f"Re is between 10,000 and 10/e")
#     hy_lambda = float(0.3164/(re**0.25))
# elif 10/e < re < 500/e:
#     print(f"10/ε = {10/e}")
#     print(f"500/ε = {500/e}")
#     print(f"Re is between 10/e and 500/e")
#     hy_lambda = float(0.11*((e+68/re)**0.25))
# elif re > 500/e:
#     print(f"Re is greater than 500/e")
#     hy_lambda = float(0.11*e**0.25)
# else:
#     print(f"Re is not in any of the specified intervals")
# hy_lambda = round(hy_lambda, 6)
# print("λ = ", hy_lambda)
