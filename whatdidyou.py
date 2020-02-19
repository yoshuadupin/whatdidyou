import re
import os
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers


def makePing(hostname):
    #Codigo del comando
    response = os.system("ping " + hostname)

fping  = open('ping.txt', 'r')
fls = open('ls.txt', 'r')
fvi = open('vi.txt', 'r')
pingHist = re.split('\s' , fping.read()  )
lsHist = re.split('\s' , fls.read()  )
viHist = re.split('\s' , fvi.read()  )


fping.close()
fls.close()
fvi.close()


pingPatron= re.compile('[op]+[uio]*[bnm]*[fgh]*')
lsPatron = re.compile('[kl]+[asd]*|[asd]+[kl]*')
viPatron = re.compile('[cvb]+[uio]*')


entrada = ''
while entrada != 'z' and entrada != 'Z':
    entrada = input(">>")
    args = re.split('\s' ,entrada)
    if pingPatron.match(args[0]) is not None:
        if args[0] in pingHist or args[0] == 'ping':
            if len(args)>=2:
                makePing(args[1]) 
            else:
                makePing("google.com")   
            continue
        else:
            #si es si codigo del comando
            temp = input('quisiste decir ping ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('ping.txt' , 'a')
                f.write(' '+args[0])
                f.close()
                pingHist.append(args[0])
                if len(args)>=2:
                    makePing(args[1]) 
                else:
                    makePing("google.com")
                continue
                    
    if lsPatron.match(entrada) is not None:    
        if entrada in lsHist or entrada == 'ls':
            #Codigo del comando  
            # 
            files = os.listdir('.')
            for name in files:
                print(name) 
            continue
        else:
            #si es si codigo del comando
            temp = input('quisiste decir ls ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('ls.txt' , 'a')
                f.write(' '+entrada)
                f.close()
                lsHist.append(entrada)
                files = os.listdir('.')
                for name in files:
                    print(name) 
                continue
    if viPatron.match(entrada) is not None:    
        if entrada in viHist or entrada == 'vi':
            f = open('goose'+(str(randint(0,99)%3))+'.txt' , 'r')
            print(f.read())
            f.close() 
            continue   
        else:
            #si es si codigo del comando
            temp = input('quisiste decir vi ? S/N ')
            if temp == 'S' or temp == 's':
                f = open('vi.txt' , 'a')
                f.write(' '+entrada)
                f.close()
                viHist.append(entrada)
                f = open('goose'+(str(randint(0,99)%3))+'.txt' , 'r')
                print(f.read())
                f.close()
                continue



    else:
        print('No se reconoce el comando')    


   