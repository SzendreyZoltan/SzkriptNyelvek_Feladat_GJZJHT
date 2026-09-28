# negyedik alkalom

def osszeadas(a,b):
    return (a + b) / s

# Főprogram
if __name__ == '__main__':
    x = 4
    y = 6
    s = 1
    print(osszeadas(x, y))

    sorozat = [1,5,9,6,8,7]
    for elem in sorozat:
        if elem == 5:
            continue
        print(elem)
        if elem == 5:
            break
    else:
        print('vége')
    print()

    for elem in range(1,6,2):
        print(elem)

    for elem in range('Jó reggelt!'):
        print(elem)

    # Hibás futás
    s = 1
    x = 58
    try:
        eredmeny = x / s
    except ZeroDivisionError:
        eredmeny = 0
        print('Hiba - nullával való osztás')
    except ValueError:
        eredmeny = 1
        print('Az egyik érték hibás')
    else:
        print(eredmeny)
    finally:
        print('Vége')