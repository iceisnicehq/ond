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
            "5) гидравлический уклон i = λ*(1/d)*(υ^2/2g)",
            "6) Напор и давление на отметке H(x) и P(x)"
            ]
for i in formulas: 
    print(i)
choice = input("Choose equation: ")
while (choice.lower()!="no"):
    match choice:
        case "1": 
            print("υ=(4*Q)/(π*d^2)")
            q = float(input("Q = "))/3600
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
            v = (input("υ = "))
            d = float(input("d = "))*0.001
            nu = eval(input("ν = "))
            print("Re = ", float(v)*float(d)/(float(nu)))
        case "4":
            print ("ε=Δ/d")
            delta = input("Δ = ")
            d = input("d = ")
            print("ε= ", float(delta)/float(d))
        case "5":
            print("i = λ*(1/d)*(υ^2/2g)")
            hy_lambda = float(input("λ = "))
            d = float(input("d = "))*0.001
            v = float(input("ν = "))
            g = 9.8
            print("i = ", hy_lambda*(1/d)*(float(v)**2/(2*g)))
        case "6":
            rho = float(input("Плотность: "))
            quantity = int(input("Количество отметок: "))
            arr_x = [0, ]
            arr_x.append(float(input("x_конечный = ")))
            arr_z = []
            for i in range(quantity):
                # arr_x.append(float(input(f"x_{i+1} [km] = ")))
                arr_z.append(float(input(f"z_{i+1} [m]= ")))
            print("Напор и давление на отметке H(x) и P(x)")
            length  = arr_x[len(arr_x)-1]*1000
            z_0 = arr_z[0] #float(input("Начальная отметка Z_0 в м: "))
            p_0 = float(input("Давление на Z_0 в МПа: "))*10**6
            z_k = arr_z[len(arr_z)-1] #float(input("Конечная отметка Z_к в м: "))
            p_k = float(input("Давление на Z_к в МПа: "))*10**6
            h_0 = z_0+p_0/(rho*9.8)
            h_k = z_k+p_k/(rho*9.8)
            print(f"H_0 is {h_0}")
            k = 1000*(arr_x[len(arr_x)-1]-arr_x[0])/(quantity-1)
            i = (h_0-h_k)*k/length
            arr_h = [h_0]
            for j in range(quantity-2):
                h = arr_h[j]-i
                arr_h.append(h)
                print(f"H_{j+1} = {h}")
            arr_h.append(h_k)
            print(f"H_к is {h_k}")
            for i in range(1, quantity-1):
                print(f"p_{i} = ", float(round(rho*9.8*(arr_h[i]-arr_z[i])*10**-6, 1)))
            # print("H_н = υ^2/2g + υ*x + H0")


    choice = input("Choose equation or type \"no\": ")
