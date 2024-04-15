path = ''
lib = []
with open('messaggi\\path.txt', 'r') as file:
    path = file.read()
with open(path, 'r') as file:
    contents = file.read()
indice = 0

#includi librerie
while indice < len(contents):
    indice= contents.find('#', indice)
    if indice== -1:
        break
    indice_inizio = indice + 1
    indice_fine = contents.find('#', indice_inizio)
    if indice_fine == -1:
        break
    lib.append(contents[indice_inizio:indice_fine])
    indice = indice_fine + 1
with open('cpp.cpp','w') as cppfile:
    for i in range(0,len(lib)):
        cppfile.write('#include <')
        cppfile.write(lib[i])
        cppfile.write('.h> \n')

#funzioni
