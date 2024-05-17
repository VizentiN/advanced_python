def my_gen():
    n = 1
    print(f'Primeiro print, n e igual a {n}')
    yield n

    n+= 1
    print('Segundo print, n e igual a {n}')
    yield n

    n+= 1
    print('Terceiro print, n e igual a {n}')
    yield n