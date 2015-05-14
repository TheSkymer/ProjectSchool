#Conf for ProjectSchool  
#!/home/andrea
percorso_file = {1 : 'materie.txt', 2 : 'voti.txt'}
conf = open(percorso_file[1], 'w')
voti = open(percorso_file[2],'w')  
with open('memo.txt', 'w') as memo:  
    memo.write(percorso_file[1] + ',')  
    memo.write(percorso_file[2])  
print('Benvenuto Utente')
print('')
print('Stai configurando ProjectSchool per i tuoi usi')
numero_materie = input('Quante materie hai: ')   
numero_materie = int(numero_materie) + 1
for materie in range(1, numero_materie):  
    i = input('Digita il nome della materia: ') + ','
    var = '0' + '\n' 
    conf.write(i)  
    voti.write(var)  
conf.close()  
voti.close()  
