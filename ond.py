import math
gr= ["λ", "Δ", "δ", "ε", "μ", "ν", "π", "ρ" "υ"]
formulas = [
            "1) Скорость υ=(4*Q)/(π*d^2)", 
            "2) Вязкость ν=μ/ρ",
            "3) Число Рейнольдса Re=(υ*d/ν)",
            "4) ε=Δ/d"
            "5) λ..."]
for i in formulas: 
    print(i)
choice = input("Choose equation: ")
while (choice.lower()!="no"):
    match choice:
        case "1": 
            print("υ=(4*Q)/(π*d^2)")
            q = input("Q = ")
            d = input("d = ")
            print("υ = ", 4*float(q)/(math.pi*float(d)**2))
        case "2":
            print("ν=μ/ρ")
            mu = input("μ = ")
            rho = input("ρ = ")
            print("ν = ", float(mu)/float(rho))
        case "3":
            print("Re=(υ*d/ν)")
            v = input("υ = ")
            d = input("d = ")
            nu = input("ν = ")
            print("Re = ", float(v)*float(d)/(float(nu)))
        case "4":
            print ("ε=Δ/d")
            delta = input("Δ = ")
            d = input("d = ")
            print("ε= ", float(delta)/float(d))
    choice = input("Choose equation or type \"no\": ")
