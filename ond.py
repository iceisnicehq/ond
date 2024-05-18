import math
#   YES
#       IM
#           A
#               PROGRAMER
gr= ["λ", "Δ", "δ", "ε", "μ", "ν", "π", "ρ" "υ"]
formulas = [
            "1) Скорость υ=(4*Q)/(π*d^2)", 
            "2) Вязкость ν=μ/ρ",
            "3) Число Рейнольдса Re=(υ*d/ν)",
            "4) ε=Δ/d",
            "5) гидравлический уклон i = λ*(1/d)*(υ^2/2g)"]
for i in formulas: 
    print(i)
choice = input("Choose equation: ")
while (choice.lower()!="no"):
    match choice:
        case "1": 
            print("υ=(4*Q)/(π*d^2)")
            q = float(input("Q = "))/360
            # q = q/360
            d = float(input("d = "))*0.001
            # d = d*0.001
            print("υ = ", 4*float(q)/(math.pi*float(d)**2))
        case "2":
            print("ν=μ/ρ")
            mu = input("μ = ")
            rho = input("ρ = ")
            print("ν = ", float(mu)/float(rho))
        case "3":
            print("Re=(υ*d/ν)")
            v = input("υ = ")
            d = float(input("d = "))*0.001
            nu = input("ν = ")
            print("Re = ", float(v)*float(d)/(float(nu)))
        case "4":
            print ("ε=Δ/d")
            delta = input("Δ = ")
            d = float(input("d = "))*0.001
            print("ε= ", float(delta)/float(d))
        case "5":
            print("i = λ*(1/d)*(υ^2/2g)")
            hy_lambda = float(input("λ = "))
            d = float(input("d = "))*0.001
            nu = input("ν = ")
            g = 9.8
            print("i = ", hy_lambda*(1/d)*(float(nu)**2/(2*g)))


    choice = input("Choose equation or type \"no\": ")
