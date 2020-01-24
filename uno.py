def s_calc_decor(func):
    def wrap(v0,v1,t):
        a=func(v0,v1,t)
        print ('s= '+str(v0*t+(a*t*t/2)))
    return wrap


@s_calc_decor
def a_calc(v0,v1,t):
    print('a= '+str(v1-v0/t))
    return (v1-v0)/t

def main():
    try:
        a_calc(int(input('v0 ')),int(input('v1 ')),int(input('t ')))
    except ValueError:
        print("Пачиму не число")
    except ZeroDivisionError:
        print("Пачиму время ноль")

if __name__ == '__main__':
    main()
