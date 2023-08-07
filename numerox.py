from multide import *

numero = int(input("Digite um numero e receba um resultado: "))

conferir = multide(numero)

if conferir == 1:
    print("fizzbuzz")
if conferir == 2:
    print("fizz")
if conferir == 3:
    print("buzz")
if conferir == 4:
    print("miss")