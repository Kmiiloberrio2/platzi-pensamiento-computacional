def factorial(n):
    """Calcula el factorialde n.

    :param int n: cualquier entero
    :type n: int
    :return: factorial de n
    :rtype: int
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))

print(factorial(n))

