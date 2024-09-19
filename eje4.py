# Escribe un programa que devuelva True cuando una palabra no contenga
# ‘a’ y false en caso contrario

if __name__ == '__main__':
    p = input('Escribe una palabra2')
    if p.find('a') == -1:
        print('true')
    else:
        print('false')


