n = int(input('Insert number: '))
while n < 0 or n > 4000:
    n = int(input('Insert number 0 < a < 4000: '))    
r = ''
T = 1
while n > 0:
    d = n % 10
    if T == 1:
        if d < 4:
            r = d*'I' + r
        if d == 4:
            r = 'IV' + r
        if 4 < d < 9:
            r = 'V' + (d-5)*'I' + r
        if d == 9:
            r = 'IX' + r
    if T == 10:
        if d < 4:
            r = d*'X' + r
        if d == 4:
            r = 'XL' + r
        if 4 < d < 9:
            r = 'L' + (d-5)*'X' + r
        if d == 9:
            r = 'XC' + r    
    if T == 100:
        if d < 4:
            r = d*'C' + r
        if d == 4:
            r = 'CD' + r
        if 4 < d < 9:
            r = 'D' + (d-5)*'C' + r
        if d == 9:
            r = 'CM' + r
    if T == 1000:
        if d < 4:
            r = d*'M' + r
    T = T * 10
    n = n // 10
print(r)
