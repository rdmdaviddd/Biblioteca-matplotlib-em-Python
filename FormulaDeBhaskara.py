import math
# Resultados convertidos para inteiro
# Teste delta == 0 utilize a=1, b =-6, c=9
# Teste delta > 0 utilize a=1, b =12, c=-13
# Teste delta == 0 utilize a=1, b =-6, c=10
a = int (input ("Digite o valor de a \n"))
b = int (input ("Digite o valor de b \n"))
c = int (input ("Digite o valor de c \n"))
e = a,"*x²",b,"*x",c
print ("Expressão de 2º Grau =",e)
delta = ((b**2)- 4*a*c)
print("Delta=", delta)
if (delta == 0):
   x = (-b + math.sqrt(delta))/2*a
   x = int (x)
   print ("As raíz da equação é",x)
if   (delta > 0):
   print  ( "A expressao",e, "Possui dois resultados distintos reais.")
   x = (-b + math.sqrt(delta))/2*a
   x1 = (-b - math.sqrt(delta))/2*a
   x = int (x)
   x1 = int (x1)
   print ("As raízes da equação são",x, "e", x1)
if (delta < 0):
   print ("A expressao",e,"não possui resultados reais.")










