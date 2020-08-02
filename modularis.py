import itertools
import argparse

parser = argparse.ArgumentParser(description="see README.md")
parser.parse_args()

def getMenu():

    print('                      _         _               _      ')
    print('    /\/\    ___    __| | _   _ | |  __ _  _ __ (_) ___ ')
    print('   /    \  / _ \  / _` || | | || | / _` || \'__|| |/ __|')
    print('  / /\/\ \| (_) || (_| || |_| || || (_| || |   | |\__ \\')
    print('  \/    \/ \___/  \__,_| \__,_||_| \__,_||_|   |_||___/')

    print(' __      __                 _   _   _        _        ___                                   _               ')
    print(' \ \    / /  ___   _ _   __| | | | (_)  ___ | |_     / __|  ___   _ _    ___   _ _   __ _  | |_   ___   _ _ ')
    print('  \ \/\/ /  / _ \ | \'_| / _` | | | | | (_-< |  _|   | (_ | / -_) | \' \  / -_) | \'_| / _` | |  _| / _ \ | \'_|')
    print('   \_/\_/   \___/ |_|   \__,_| |_| |_| /__/  \__|    \___| \___| |_||_| \___| |_|   \__,_|  \__| \___/ |_|  ')

    print('\n')

def recursiveFunction(custom, pos4, aux, n, file):

    if (n >= len(pos4)):
        return

    for i in itertools.product(custom[n], repeat=1):

        aux[pos4[n]] = i
        aux[pos4[n]] = aux[pos4[n]][0]
        recursiveFunction(custom, pos4, aux, n+1, file)

        file.write(''.join(aux)+'\n')


def getModules():
    
    print('Generational modules:\n')

    print('1- Mr. Robot')
    print('2- Dates')
    print('3- Password format')
    print('4- Informational')
    print('5- Incremental')

    a = input('\nEnter the modules sequence (e.g. 12345): ')
    
    return a

def testModule(file):
    file.write('teste\n')
    file.write('teste2?\n')

def firstModule(file):

    print('1- Mr. Robot Module\n')

    string = input('Enter keywords or alpha-numeric sequences separated by \';\': ')

    print('\nGenerating...')

    words = (string.split(';'))

    reversedwords = []

    for i in words:
        reversedword = i[::-1]
        reversedwords.append(reversedword)

    words.extend(reversedwords)

    words.extend(['123', '321'])

    for i in range(len(words)): #[joao, maria, fern, carro] #vai concatenar ate 3 palavras
        file.write(words[i]+'\n')
        #file.write(words[i]+'123'+'\n')
    
        for j in range(len(words)):
            file.write(words[i]+words[j]+'\n')
            #file.write(words[i]+words[j]+'123'+'\n')

            for c in range(len(words)):
                file.write(words[i]+words[j]+words[c]+'\n')

    print('Finished.')

def secondModule(file):

    print('2- Dates Module\n')

    string1 = input('Enter the year range of the dates to be generated (e.g. 1980/2015): ')
    string2 = input('Enter the date field divider (ENTER for no divisors): ')
    string3 = input('American (month/day/year) or British (day/month/year) model? (A/b): ')
    string4 = input('Autocomplete fields with \'0\'? (e.g 01/06/2001)(y/N): ')

    print('\nGenerating...')

    ano1, ano2 = (string1.split('/'))
    ano1, ano2 = int(ano1), int(ano2)

    if (string3 == 'b'):
        if (string4 == 'y'):
            for i in range((ano2-ano1)+1):
                ano = ano1+i
                ano = str(ano)
                for j in range(12):
                    mes = j+1
                    mes = str(mes)
                    if (int(mes) < 10):
                        mes = '0' + mes

                    for c in range(31):
                        dia = c+1
                        dia = str(dia)

                        if (int(dia) < 10):
                            dia = '0'+dia

                        file.write(str(dia)+string2+str(mes)+string2+str(ano)+'\n')
        else: #string4 = 'n'
            for i in range((ano2-ano1)+1):
                ano = ano1+i
                ano = str(ano)
                for j in range(12):
                    mes = j+1
                    mes = str(mes)

                    for c in range(31):
                        dia = c+1
                        dia = str(dia)

                        file.write(str(dia)+string2+str(mes)+string2+str(ano)+'\n')

    else: #american model
        if (string4 == 'y'):
            for i in range((ano2-ano1)+1):
                ano = ano1+i
                ano = str(ano)
                for j in range(12):
                    mes = j+1
                    mes = str(mes)
                    if (int(mes) < 10):
                        mes = '0' + mes

                    for c in range(31):
                        dia = c+1
                        dia = str(dia)

                        if (int(dia) < 10):
                            dia = '0'+dia

                        file.write(str(mes)+string2+str(dia)+string2+str(ano)+'\n')
        else: #string4 = 'n'
            for i in range((ano2-ano1)+1):
                ano = ano1+i
                ano = str(ano)
                for j in range(12):
                    mes = j+1
                    mes = str(mes)

                    for c in range(31):
                        dia = c+1
                        dia = str(dia)

                        file.write(str(mes)+string2+str(dia)+string2+str(ano)+'\n')

    print('Finished.')

def thirdModule(file):

    print('3- Password format Module\n')

    lowercase_char = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    comum_symbols = '!@#$%&*()-=+_'
    custom = []

    print('@ will insert lower case characters')
    print(', will insert upper case characters')
    print('% will insert numbers')
    print('^ will insert symbols')
    print('[*charset*] will insert your charset\n')

    string1 = input('Enter the password format (e.g pass[123]@,^): ') 

    print('\nGenerating...')

    pos = []
    pos1 = []
    pos2 = []
    pos3 = []
    pos4 = []
    aux = list()

    #dentro de colchetes
    #inside '[]'
    dentro = 0

    for i in range(len(string1)):
        
        if (dentro != 1):
            if (string1[i] != ']'):
                aux.append([string1[i]])
                #print(aux, i)
                aux[-1] = aux[-1][0]

        if (string1[i] == '['):

            for k in range(i+1,len(string1)):
            
                if string1[k] == ']':

                    custom.append(string1[i+1:k])
                    break
            dentro = 1
            continue
        elif (string1[i] == ']'):
            dentro = 0    
        
                
    for i in range(len(aux)):
        if aux[i] == '[':
            pos4.append(i)
        elif (aux[i] == '%'):
            pos.append(i)
        elif (aux[i] == '@'):
            pos1.append(i)    
        elif (aux[i] == ','):
            pos2.append(i)
        elif (aux[i] == '^'):
            pos3.append(i)  

    #print('CUSTOM: ',custom)

    #print('POS 4 =  '+str(pos4))   

    #print(aux)

    #print('POS: ',pos,pos1,pos2,pos3,pos4)

    for j in itertools.product(numbers, repeat=len(pos)):
        seq = ''.join(j)
        for i in range(len(pos)):
            aux[pos[i]] = seq[i]

        for c in itertools.product(lowercase_char, repeat=len(pos1)):
            seq1 = ''.join(c)
            for b in range(len(pos1)):
                aux[pos1[b]] = seq1[b]

            for d in itertools.product(uppercase_char, repeat=len(pos2)):
                seq2 = ''.join(d)
                for f in range(len(pos2)):
                    aux[pos2[f]] = seq2[f]

                for k in itertools.product(comum_symbols, repeat=len(pos3)):
                    seq3 = ''.join(k)
                    for l in range(len(pos3)):
                        aux[pos3[l]] = seq3[l]

                    if (len(pos4) > 0):
                        recursiveFunction(custom, pos4, aux, 0, file)
                    else:
                        file.write(''.join(aux)+'\n')

    print('Finished.')   

def fourthModule(file):

    print('4- Informational Module\n')

    chrs_numerics = '1234567890'

    print('\nIn this module you must provide as much information about the target')
    print('If you don\'t have an answer to some of the questions, press ENTER to proceed to the next question')
    print('Separate multiple responses with ";" and without space (e.g. mary;john;mike)\n')

    nomes = input('Enter name(s) connected to the target (the name of the target, of relatives ...):')
    sobrenomes = input('Enter last name(s):')
    animais = input('Target pets name(s) (e.g. dog;flipper;cat;lulu): ')
    times = input('Enter the name of team(s) (e.g. yankees):')
    datas = input('Enter target-related date(s) (vary formats for the same date) (e.g. 24112007;11/24/2007): ')
    numeros = input('Enter number(s) linked to the target (e.g. year of birth, residence number ...): ')
    hobbies = input('Enter hobbie(s) (e.g. skateboard;surf;painting;lol): ')
    documentos = input('Enter document(s) number(s): ')
    telefones = input('Enter phone number(s)/cell phone(s): ')
    placas = input('Enter vehicle(s) license plate(s) (e.g. 284FH8;FOR1094): ')
    servico = input('Enter words that define the target service (e.g. wifi;facebook;twitter;lol): ')
    emails = input('Enter the part before the "@" of email(s) associated with the target (e.g johnsnow02): ')
    palavras = input('Enter a few more keywords and/or alpha-numeric strings associated with the target: ')

    print('\nGenerating...')

    palavraschave = list(nomes.split(";")
    +sobrenomes.split(";")
    +animais.split(";")
    +times.split(";")
    +hobbies.split(";")
    +servico.split(";")
    +emails.split(";")
    +palavras.split(";"))

    palavrasinvertidas = []
    numerosinvertidos = []

    for string in palavraschave:
        if (string != ''):
            string = string[::-1]
            palavrasinvertidas.append(string)

    palavraschave.extend(palavrasinvertidas)
    
    numeroschave = list(datas.split(";")
    +numeros.split(";")
    +telefones.split(";")
    +placas.split(";"))

    for numero in numeroschave:
        if (numero != ''):
            numero = numero[::-1]
            numerosinvertidos.append(numero)

    numeroschave.extend(numerosinvertidos)

    #incremental
    for p in palavraschave:
        if (p == ''):
            continue

        for n in numeroschave:
            if (n == ''):
                continue

            file.write(p+n+'\n')
            file.write(n+p+'\n')    

        file.write(p+'\n')

        for j in itertools.product(chrs_numerics, repeat=1):
            inc = ''.join(j)
            file.write(p+inc+'\n')
            file.write(inc+p+'\n')    
        for j in itertools.product(chrs_numerics, repeat=2):
            inc = ''.join(j)
            file.write(p+inc+'\n')
            file.write(inc+p+'\n')    
        for j in itertools.product(chrs_numerics, repeat=3):
            inc = ''.join(j)
            file.write(p+inc+'\n')
            file.write(inc+p+'\n')
        for j in itertools.product(chrs_numerics, repeat=4):
            inc = ''.join(j)
            file.write(p+inc+'\n')
            file.write(inc+p+'\n')
        for j in itertools.product(chrs_numerics, repeat=5):
            inc = ''.join(j)
            file.write(p+inc+'\n')
            file.write(inc+p+'\n')
    
    print('Finished.')            
        
def fifthModule(file):

    print('5- Incremental Module\n')

    #Credits -> Goblin wordlist generator

    use_nouse = str(input("\nDo you want to enter personal data? [y/N]: "))
    
    if use_nouse == 'y':

        print('Just enter relevant information, the less variety of characters, the more accurate the Incremental will be.')

        first_name = str(input("\nFist Name: "))
        last_name = str(input("\nLast Name: "))
        hobbie = str(input("\nHobbie: "))
        servico = str(input("\nService: "))
        someword = str(input("\nA guess word: "))
        chrs = first_name + last_name + hobbie + servico + someword
    else:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        pass

    chrs_up = chrs.upper()
    chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
    chrs_numerics = '1234567890'

    intervalo = input('Enter the length range of the passwords that will be generated (e.g. 5/8): ')
    
    menor = int((intervalo.split('/'))[0])
    maior = int((intervalo.split('/'))[1])

    if (input('Use uppercase characters? (y/N): ') == 'y'):
        chrs = ''.join([chrs, chrs_up])
        
    if (input('Use numeric characters? (y/N): ') == 'y'):
        chrs = ''.join([chrs, chrs_numerics])

    if (input('Use symbols? (y/N): ') == 'y'):
        chrs = ''.join([chrs, chrs_specials])

    print('\nGenerating...')

    for i in range(menor, maior+1):
        for j in itertools.product(chrs, repeat=i):
            word = ''.join(j)
            #print(word)
            file.write(word+'\n')

    print('Finished.')

if __name__ == "__main__":

    file = open("wordlist.txt", "w+")

    getMenu()

    modules = getModules()    

    for i in modules:
        
        i = int(i);

        print('\n---------------------------------------------------------------------------')

        #if i == 0:
        #    testModule(file)
        
        if i == 1:
            firstModule(file)
        elif i == 2:
            secondModule(file)
        elif i == 3:
            thirdModule(file)
        elif i == 4:
            fourthModule(file)
        elif i == 5:
            fifthModule(file)
       
    file.close()        
