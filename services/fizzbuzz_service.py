# Algoritmo FizzBuzz


# Inicio
def generate_fizzbuzz(fizz_value, buzz_value, stop_value):
    results = []
    #     Para Numero ← 1 Hasta StopValue Hacer
    for n in range(1, stop_value + 1):
        #         Si Numero es divisible por FizzValue y BuzzValue Entonces
        #             Mostrar "FizzBuzz"
        if n % fizz_value == 0 and n % buzz_value == 0:
            results.append("FizzBuzz")
        #         Sino Si Numero es divisible por FizzValue Entonces
        #             Mostrar "Fizz"
        elif n % fizz_value == 0:
            results.append("Fizz")
        #         Sino Si Numero es divisible por BuzzValue Entonces
        #             Mostrar "Buzz"
        elif n % buzz_value == 0:
            results.append("Buzz")
        #         Sino
        #             Mostrar Numero
        else:
            results.append(n)
        #         Fin Si
    return results


#     Fin Para

# Fin
