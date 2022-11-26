def DtoN(num, base):
    if num >= base:
        yield from DtoN(num // base, base)
    yield num % base

num=0
base = 46
kana = list('あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん')

for i in range(2048):    
    digits = list(DtoN(num, base))
    if base <= num:
      print(kana[digits[0]]+kana[digits[1]]) 
    elif base > num:
      print('あ'+kana[digits[0]])  
    num=num+1
