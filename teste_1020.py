dias = int(input("Digite sua idade em dias: "))

anos = dias // 365
meses = (dias % 365) // 30
dias = (dias % 365) - (((dias % 365)//30) * 30)


print (anos ,"ano(s)")
print (meses ,"mes(es)")
print (dias ,"dia(s)")



