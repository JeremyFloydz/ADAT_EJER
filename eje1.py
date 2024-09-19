# Escribe un programa que imprima solo
#  las palabras que tienen más de 10 letras
if __name__=='__main__':
    p= ('m')
    while p != ('fin'):
        p = input ('escribe una palabra: ')
        if len(p)>=10:
            print(p)