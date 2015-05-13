#-*- coding: UTF-8 -*-
#!/home/andrea
#importo moduli
import sys
 
#scrittura di presentazione file
 
pres = '''Benvenuto Utente in ProjectSchool
Questo è il pannello principale;
da qui poi controlare i tuoi voti e gestire
la tua situazione scolastica'''

mod = '''Premio INVIO per riavviare\nPremi 0 per uscire\nPremi 2 per aggiungere voti
Premi 3 per rimuovere un voto\n-->digita: '''
 
#definisco funzioni
 
#acquisisce databse dei voti
def acquisisci_percorso_file():
    percorso_file = way.readlines()[0].rstrip().split(',')
    return percorso_file[1]
 
#configura la lista delle materie
def configura_mat():
    with open('materie.txt', 'r') as conf:
        lista_mat = conf.readlines()[0].rstrip().split(',')[0:-1]
    return lista_mat
 
#creo comprenshion dizionario per i nomi della materie
def materie():
    materie = {ch:v for ch,v in enumerate(configura_mat(), 1)}
    return materie
 
#stampa materie   
def stampa_materie(mat):
    for cont,materia in enumerate(mat,1):
        print(cont,' ---> ',materia)
 
#media dei voti
def media(numeri):
    totale = 0
    for numero in numeri:
        numero = float(numero)
        totale = totale + numero
    if totale == 0:
        raise ZeroDivisionError('Non hai voti')
    return round(totale / len(numeri), 2)
 
#stampa a video i voti
def stampa_voti_modalità(voti):
    for voto in voti:
        voto = float(voto)
        print(voto, end=' ')
 
#trova la posizione di un elemento
def trova_x_in_lista(lista, x):
    for c, el in enumerate(lista):
        if el == x:
            return c 
 
#menu che stampa i voti della materia scelta
def print_marks(modalità, n):
   mat = file_voti.readlines()[n-1].rstrip().split(",")[1::]
   print("Ecco i voti di",materie()[n],"-->")
   if mat == []:
       print('non hai voti')
       return 
   stampa_voti_modalità(mat)
   file_voti.close()
   if modalità == 'main':
       print('\n')
       print("la tua media in",materie()[n], "-->")
       print(media(mat))
 
#funzione per aggiungere su un file un voto in una materia
def aggiungi_voto(n,voto,security,m_voti):
    linee_mat = leggi_voti_materie(m_voti)
    mat_voto = leggi_voti_materia(m_voti, n)
    mat_voto = ','.join(leggi_voti_materia('voti.txt', n)) + ',' + voto + '\n'
    linee_mat[n-1] = mat_voto
    if security == 'si':
        with open(m_voti, 'w') as mem_mat:
            for riga in linee_mat:
                mem_mat.write(riga)
        print('un voto/i aggiunto')
    else:
        print('nessun voto/i aggiunto')

#rimozione su file di testo di un voto di una materia
def rimuovi_voto(n,voto, m_voti):
    linee_voti = leggi_voti_materie(m_voti)
    mat_del_voto = leggi_voti_materia(m_voti, n)
    if mat_del_voto[trova_x_in_lista(mat_del_voto, voto_da_levare)] in mat_del_voto:
        del mat_del_voto[trova_x_in_lista(mat_del_voto, voto_da_levare)]
        mat_del_voto = ','.join(mat_del_voto) + '\n'
        linee_voti = leggi_voti_materie('voti.txt')
        linee_voti[n-1] = mat_del_voto
        with open(m_voti, 'w') as file_voti:
            for riga in linee_voti:
                file_voti.write(riga)

#menu delle modalità selezionate dopo il menu principale
def menu_modalità(modalità):
    print('\n')
    if modalità == '3':
        print('Rimuovi voto/i')
    elif modalità == '2':
        print('Aggiungi voto/i')
    return stampa_materie(configura_mat())
 
#acquisisce i voti di una determinata materia
def leggi_voti_materia(nome_file_voti, materia):  
    with open(nome_file_voti, 'r') as file_voti:  
        linea_voti =file_voti.readlines()[materia - 1].rstrip().split(',')    
    return linea_voti  
 
#acquisisce tutti i voti di tutte le materie
def leggi_voti_materie(nome_file_voti):
    with open(nome_file_voti, 'r') as file_voti:
        voti = file_voti.readlines()
    return voti
 
#acquisisco file
with open('memo.txt', 'r') as way:
    m_voti = acquisisci_percorso_file()

#inizializzazione
 
print(pres)
 
#main
 
while 1:
    print('Main Page','\n',"-Queste sono le tue materie:")
    stampa_materie(configura_mat()) 
    n = input("Seleziona la materia per vedere i voti: ")
    try:
        n = int(n)
        with open('voti.txt', 'r') as file_voti:
            print_marks('main', n)        
    except:
        print(sys.exc_info())
    print('')
    uscita = input(mod)
    if uscita == "0" :
        sys.exit()
    elif uscita=="2" :
        menu_modalità(uscita)
        n = int(input("seleziona una materia per aggiungere un voto/i: "))
        try:
            if configura_mat()[n-1] in configura_mat():
                voto = input("digita il tuo voto/i: ")
                security = input('sei sicuro di voler aggiungere questo voto/i: ')
                aggiungi_voto(n,voto,security,m_voti)
                print('')
        except IndexError :
            print('Materia non valida')
        except:
            print(sys.exc_info())
    elif uscita == '3':
        menu_modalità(uscita)
        n = input('seleziona una materia per rimuovere un voto: ')
        n = int(n)
        try:
            if configura_mat()[n-1] in configura_mat():
                with open('voti.txt', 'r') as file_voti:
                    print_marks('', n)
                print('')
                voto_da_levare = input('digita il voto da levare: ')
                rimuovi_voto(n, voto_da_levare, m_voti)
               	print('un voto rimosso')
		print('')
        except IndexError:
            print('La materia immessa non esiste!')
        except:
            print(sys.exc_info())
            print('nessun voto rimosso')
            print('')
            
