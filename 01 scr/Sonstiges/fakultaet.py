# Beispiel: Fakultät berechnen - iterativ
def iterative_fakultaet(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result