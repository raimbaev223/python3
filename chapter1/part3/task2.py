t = int(input('input your temp (only numbers): '))
c_or_f = str(input('input celsius(c) or fahrenheit(f):'))
if c_or_f == 'C' or c_or_f == 'c':
    t = round(t * (9/5) + 32)
    print(f'Температура за бортом {t} °F')
elif c_or_f == 'F' or c_or_f == 'f':
    t = round((t - 32) * (5/9))
    print(f'Температура за бортом {t} °C')