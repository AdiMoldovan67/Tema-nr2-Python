#problema 1
def my_funct(*arg,**kwargs):
       i=0
       s=0
       while type(arg[i])==int or type(arg[i])==float:
             s=s+arg[i]
             i+=1
       print('suma numerelor intregi sau zecimale este',s)



my_funct(1,5,-3,'abc',[12,56,'cad'])



# problema 2 - prametru care se introduc este n

n=100
def suma_numere(n):
    if n <= 0:
        return 0
    else:
        return n + suma_numere(n - 1)


print('suma numerelor este:', suma_numere(n))

if n%2==0:
    def suma_numere_pare(n):
        if n<=0:
            return 0
        else:
            return n+suma_numere_pare(n-2)


    print('suma numerelor pare este:',suma_numere_pare(n))
    print('suma numer impare este',suma_numere(n)-suma_numere_pare(n))


else:
    def suma_numere_impare(n):
        if n<=0:
            return 0
        else:
            return n+suma_numere_impare(n-2)

    print('suma numer pare este', suma_numere(n) - suma_numere_impare(n))
    print('suma numerelor impare este:',suma_numere_impare(n))
n=10

#problema 3-- prametru se introduce de la consola

while True:
   user=input('introduceti numarul')
   try:
       user=int(user)
       print(user)
   except ValueError:
       print(0)
   break

