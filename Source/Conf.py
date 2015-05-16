#Conf for ProjectSchool  
#!/home/andrea
percorso_file = {1 : 'materie.txt', 2 : 'voti.txt'}
with open('memo.txt', 'w') as memo:  
    memo.write(percorso_file[1] + ',')  
    memo.write(percorso_file[2])  
print('Benvenuto Utente')
print('')
print('Stai configurando ProjectSchool per i tuoi usi')
numero_materie = input('Quante materie hai: ')   
numero_materie = int(numero_materie) + 1
with open(percorso_file[1] , 'w') as conf:    
    for materie in range(numero_materie-1):  
        nome_materia = input('Digita il nome della materia: ') + ','
        conf.write(nome_materia)  
with open(percorso_file[2], 'w') as voti:
    for materie in range(numero_materie-1):
        voto_nullo = '0' + '\n'
        voti.write(voto_nullo)  



