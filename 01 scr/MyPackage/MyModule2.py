#
# ---- zweites Modul
#
def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)
