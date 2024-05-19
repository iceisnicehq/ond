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
            "6) Напор и давление на отметке H(x) и P(x)",
            "7) ДЗ 2 задача 1",
            "8) ДЗ 2 задача 2",
            "9) ДЗ 2 задача 3"
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
        case "7":
            d = float(input("d [mm] = "))*0.001
            l = float(input("L [km] = "))*1000
            q = float(input("Q [m3/h] = "))/3600
            delta = float(input("Δ  [mm] = "))*0.001
            v_b = float(input("ν_b [sSt] = "))*10**-6
            v_d = float(input("ν_d [sSt] = "))*10**-6
            v = round(4*float(q)/(math.pi*float(d)**2), 3)
            print("υ=(4*Q)/(π*d^2) = ", v, " m/s")
            e = round(float(delta)/float(d), 6)
            print("ε = ", e)
            re_b = round(float(v)*float(d)/(float(v_b)), 2)
            print("Re_b=(υ*d/ν) = ", re_b)
            re_d = round(float(v)*float(d)/(float(v_d)), 2)
            print("Re_d=(υ*d/ν) = ", re_d)
            fuel = [re_b, re_d]
            arr_lambda = []
            for re in fuel:
                hy_lambda = ""
                post = ""
                r = ""
                if re == re_b:
                    post = "λ_b = "
                    r  = "b"
                else:
                    post = "λ_d = "
                    r = "d"
                if 0 < re < 2380:
                    print(f"Re_{r} is between 0 and 2380")
                    hy_lambda = float(64/re)
                elif 2380 < re < 10**4:
                    print(f"Re_{r} is between 2380 and 10,000")
                    gamma = 1-(math.e)**(-0.002*(re-2320))
                    hy_lambda = float((64/re)*(1 - gamma) + (0.3164/(re**0.25))*gamma)
                elif 10**4 < re < 10/e:
                    print(f"Re_{r} is between 10,000 and 10/e")
                    hy_lambda = float(0.3164/(re**0.25))
                elif 10/e < re < 500/e:
                    print(f"Re_{r} is between 10/e and 500/e")
                    hy_lambda = float(0.11*((e+68/re)**0.25))
                elif re > 500/e:
                    print(f"Re_{r} is greater than 500/e")
                    hy_lambda = float(0.11*e**0.25)
                else:
                    print(f"Re_{r} is not in any of the specified intervals")
                print(post, round(hy_lambda, 6))
                arr_lambda.append(round(float(hy_lambda), 6))
            print("--- Объём смеси ---")
            vol = round((math.pi*(d**2)*l*0.25), 3)
            print("Volume = ", vol , " m3")
            print(f"V_c = 1000*({arr_lambda[0]}**1.8+{arr_lambda[1]}**1.8)*(({d}/{l})**0.43)*{vol}")
            V_c = round(1000*(arr_lambda[0]**1.8+arr_lambda[1]**1.8)*((d/l)**0.43)*vol, 3)
            print("V_c = ", V_c, " m3")
        case "8":
            d = float(input("d [mm] = "))*0.001
            q = float(input("Q [m3/h] = "))/3600
            delta = float(input("Δ  [mm] = "))*0.001
            l = float(input("L [km] = "))*1000
            v = round(4*float(q)/(math.pi*float(d)**2), 3)
            mu = float(input("μ [sPz]= "))*10**-3
            rho = float(input("ρ [kg/m3]= "))
            nu = round(float(mu)/float(rho), 10)
            print("υ=(4*Q)/(π*d^2) = ", v, " m/s")
            e = round(float(delta)/float(d), 6)
            print("ε = ", e)
            re = round(float(v)*float(d)/(float(nu)), 2)
            print("Re=(υ*d/ν) = ", re)
            print("ν= μ/ρ = ", nu, "m2/s")
            hy_lambda = ""
            if 0 < re < 2380:
                print(f"Re is between 0 and 2380")
                hy_lambda = float(64/re)
            elif 2380 < re < 10**4:
                print(f"Re is between 2380 and 10,000")
                gamma = 1-(math.e)**(-0.002*(re-2320))
                hy_lambda = float((64/re)*(1 - gamma) + (0.3164/(re**0.25))*gamma)
            elif 10**4 < re < 10/e:
                print(f"Re is between 10,000 and 10/e")
                hy_lambda = float(0.3164/(re**0.25))
            elif 10/e < re < 500/e:
                print(f"Re is between 10/e and 500/e")
                hy_lambda = float(0.11*((e+68/re)**0.25))
            elif re > 500/e:
                print(f"Re is greater than 500/e")
                hy_lambda = float(0.11*e**0.25)
            else:
                print(f"Re is not in any of the specified intervals")
            hy_lambda = round(hy_lambda, 6)
            print("λ = ", hy_lambda)
            i = round(hy_lambda*(1/d)*(float(v)**2/(2*9.8)), 6)
            print("i = λ*(1/d)*(υ^2/2g) = ", i, " [m/m]")
            d_h = i*l
            print("ΔH = i*L = ", d_h, " m")
        case "9":
            d = float(input("d [mm] = "))*0.001
            delta = float(input("Δ  [mm] = "))*0.001
            q_1 = float(input("Q_1 [m3/h] = "))/3600
            q_2 = float(input("Q_2 [m3/h] = "))/3600
            v_b = float(input("ν_b [sSt] = "))*10**-6
            v_d = float(input("ν_d [sSt] = "))*10**-6
            e = round(float(delta)/float(d), 6)
            print("ε = ", e)
            fuel = [q_1, q_2]
            # arr_v = []
            # arr_re = []
            arr_vc = []
            for q in fuel:
                if q == q_1:
                    i = 1
                else:
                    i = 2
                print(f"_________________СЛУЧАЙ {i}________________")
                arr_lambda = []
                hy_lambda = ""
                post = ""
                r = ""
                v = round(4*float(q)/(math.pi*float(d)**2), 3)
                print(f"υ_{i}=(4*Q)/(π*d^2) = ", v, " m/s")

                for j in range(2):
                    if j == 0:
                        nu = v_b
                        r  = "b"
                        post = "λ_b = "
                    else:
                        nu = v_d
                        r  = "d"
                        post = "λ_d = "
                    re = round(float(v)*float(d)/(float(nu)), 2)
                    print(f"Re_{r}=(υ*d/ν) = ", re)
                    if 0 < re < 2380:
                        print(f"Re_{r} is between 0 and 2380")
                        hy_lambda = float(64/re)
                    elif 2380 < re < 10**4:
                        print(f"Re_{r} is between 2380 and 10,000")
                        gamma = 1-(math.e)**(-0.002*(re-2320))
                        hy_lambda = float((64/re)*(1 - gamma) + (0.3164/(re**0.25))*gamma)
                    elif 10**4 < re < 10/e:
                        print(f"Re_{r} is between 10,000 and 10/e")
                        hy_lambda = float(0.3164/(re**0.25))
                    elif 10/e < re < 500/e:
                        print(f"Re_{r} is between 10/e and 500/e")
                        hy_lambda = float(0.11*((e+68/re)**0.25))
                    elif re > 500/e:
                        print(f"Re_{r} is greater than 500/e")
                        hy_lambda = float(0.11*e**0.25)
                    else:
                        print(f"Re_{r} is not in any of the specified intervals")
                    print(post, round(hy_lambda, 6))
                    arr_lambda.append(round(float(hy_lambda), 6))
                print(f"        --- Объём смеси_{i} ---")
                print(f"V_c{i} = 1000*({arr_lambda[0]}**1.8+{arr_lambda[1]}**1.8)*((d/l)**0.43)*V")
                V_c = round(1000*(arr_lambda[0]**1.8+arr_lambda[1]**1.8), 3)
                arr_vc.append(V_c)
                print(f"V_c_{i} = ", V_c, " *((d/l)**0.43)*V   m3")
                print(f"__________________________________________")
            change = arr_vc[1]/arr_vc[0]
            print(f" ___    Изменение в {change} раз ___")
            print(f" ___ИЛИ Изменение в {change**-1} раз ___")

    choice = input("Choose equation or type \"no\": ")
