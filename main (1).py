salario = float(input("digite o salario atual: ").replace(',','.'))
a = float(input("digite valor do aumento").replace(',','.'))
e =  salario * (a/100)
r =  salario + e 
print("valor do novo salario: ",r)
