#Conf for ProjectSchool  
#!/home/andrea
percorso_file = {1 : 'materie.txt', 2 : 'voti.txt'}
conf = open(percorso_file[1], 'w')  
voti = open(percorso_file[2],'w')  
memo = open('memo.txt', 'w')  
memo.write(percorso_file[1] + ',')  
memo.write(percorso_file[2])  
memo.close()  
print('Benvenuto Utente')
print('')
print('Stai configurando ProjectSchool per i tuoi usi')
mat_1 = int(input('Quante materie hai: ')) + 1  
for mat in range(1, mat_1):  
    i = input('Digita il nome della materia: ') + ','
    var = '0' + '\n' 
    conf.write(i)  
    voti.write(var)  
conf.close()  
voti.close()  
