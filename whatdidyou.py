import re


fping  = open('ping.txt', 'r')
fls = open('ls.txt', 'r')
fdd = open('dd.txt', 'r')
pingHist = re.split('\s' , fping.read()  )
lsHist = re.split('\s' , fls.read()  )
ddHist = re.split('\s' , fdd.read()  )


fping.close()
fls.close()
fdd.close()


print(pingHist)

pingPatron= re.compile('[op]+[uio]*[bnm]*[fgh]*')

lsPatron = re.compile('[kl]+[asd]*')
ddPatron = re.compile('[sdf]+')

ipPatron = re.compile('^(?:(?:25[0-5]|2[0-4][0-9]|'
          '[01]?[0-9][0-9]?)\.){3}'
          '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

entrada = ''
while entrada != 'z' and entrada != 'Z':
    entrada = input(">>")

    if pingPatron.match(entrada) is not None:
        if entrada in pingHist:
            print('Comando ping ejecutado exitosamente')    
            #Codigo del comando   
        else:
            #si es si codigo del comando
            temp = input('quisiste decir ping ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('ping.txt' , 'a')
                f.write(' '+entrada)
                f.close()
                pingHist.append(entrada)

    elif ddPatron.match(entrada) is not None:    
        if entrada in ddHist:
            print('Comando dd ejecutado exitosamente')    
            #Codigo del comando   
        else:
            #si es si codigo del comando
            temp = input('quisiste decir dd ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('dd.txt' , 'a')
                f.write(' '+entrada)
                f.close()
                ddHist.append(entrada)


    elif lsPatron.match(entrada) is not None:    
        if entrada in lsHist:
            print('Comando ls ejecutado exitosamente')    
            #Codigo del comando   
        else:
            #si es si codigo del comando
            temp = input('quisiste decir ls ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('ls.txt' , 'a')
                f.write(' '+entrada)
                f.close()
                lsHist.append(entrada)

    else:
        print('No se reconoce el comando')    


   