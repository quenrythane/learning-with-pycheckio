
for i in range(18):
    number = ("00" + str(i+1))[-3:]
    name = f'{number} - .py'
    open(name, 'a')
