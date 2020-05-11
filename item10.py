def decorador(func):
    def function_wrapper(x):
        print("Olá! Estou decorando a funcao " + func.__name__)
        res = func(x)
        print(res)
        print("Seu resultado agora está realcado :) \n")
    return function_wrapper


@decorador
def dobro(n):
    return 2 * n

@decorador
def triplo(n):
    return 3 * n

dobro(2)
triplo(2)