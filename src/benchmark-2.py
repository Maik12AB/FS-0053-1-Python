import timeit

N = 2_000_000

def con_for():
    resultado = []

    for x in range(N):
        if x % 2 == 0:
            resultado.append(x)

    return resultado


def con_list_comprehension():
    return [x for x in range(N) if x % 2 == 0]


tiempo_for = timeit.timeit(con_for, number=10)
tiempo_list = timeit.timeit(con_list_comprehension, number=10)

print(f'For tradicional:        {tiempo_for:.4f} segundos')
print(f'List comprehension:     {tiempo_list:.4f} segundos')

if tiempo_list < tiempo_for:
    mejora = ((tiempo_for - tiempo_list) / tiempo_for) * 100
    print(f'List comprehension fue {mejora:.2f}% más rápida')
else:
    mejora = ((tiempo_list - tiempo_for) / tiempo_list) * 100
    print(f'For tradicional fue {mejora:.2f}% más rápido')
