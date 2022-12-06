def factorial(n):
    if n == 0:
        return 1
    else:
        old = factorial(n-1)
        result = n * old
        return result


def permutation(n,r):
    result = factorial(n) / factorial(n-r)
    return result

permutation(5,2)
