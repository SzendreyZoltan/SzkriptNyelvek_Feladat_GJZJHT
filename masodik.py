# Ez a második labor
import harmadik

harmadik.lotto()

felhasznalo_neve = input('Kérem a nevet:')
felhasznalo_kora = int(20)
felhasznalo_kora *= 2
felhasznalo_kora += 4
metszet = felhasznalo_neve[:-5]
jegyek = [2,5,4,3]
jegyek += [5]
del jegyek[0]
halmaz = {'magyar' , 'angol' , 'orosz' , 3}
hallgato = {"nev": 'Zoltán', "kor":19}
print(hallgato["nev"])
print (halmaz)
print('Szia', felhasznalo_neve, '!', felhasznalo_kora , metszet, jegyek)

print('Jó', 'reggelt', 'DUE!',end='\n\n', sep='-')
print('Több soros\n'
      'kiírás\n'
      '!!!!')

print(f'Szia {felhasznalo_neve}! \n{jegyek}')
print(f'Kora: {felhasznalo_kora: .2f}')

print(felhasznalo_neve.rjust(30))
print(felhasznalo_neve.ljust(30, '.'))
print(felhasznalo_neve.rjust(30))
print(felhasznalo_neve.rjust(30))
