
 
def maximo(num, num2):
  maior = 0
  if num > num2:
    maior = num
  else:
    maior = num2

  return f' O maior número entre {num1} e {num2} é {maior}' 


num1 = int(input("Digite um número: "))
num2 = int(input('Digite o segundo numero:'))


print(maximo(num1, num2))


def multiplo(num1, num2):
  if num1 % num2 == 0:
    return f'{num1}  é multiplo de {num2}  = {True}'
  else:
    return f'{num1} não é multiplo {num2}'
  
num1 = int(input("Digite um número: "))
num2 = int(input('Digite o segundo numero:'))

print(multiplo(num1, num2))




def área(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {larg} x {comp} é de {a} m².")


print("Controle de Terrenos")
print("-=" * 30)
l = float(input("Largura (m): "))
c = float(input("COMPRIMENTO (m):"))
área(l, c)