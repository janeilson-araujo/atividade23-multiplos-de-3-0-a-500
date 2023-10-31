# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
print("os numeros multiplos de 3 de 0 a 500 são:")
for numeros in range(0, 501, 3):
    print(numeros)
else :
    soma = sum(range(0, 501, 3))
    print(f"a soma de todos eles é:{soma}")