import math


def c_binomial(n: int, k: int) -> int:
    n1 = math.factorial(n)
    k1 = math.factorial(k)
    denominador1 = math.factorial(n-k)
    denominador2 = k1 * denominador1
    return n1 // denominador2


if __name__ == "__main__":

    valor_n = int(input("Insira o valor de N: "))
    valor_K = int(input("Insira o valor de K: "))
    resultado = c_binomial(valor_n, valor_K)
    print(resultado)
