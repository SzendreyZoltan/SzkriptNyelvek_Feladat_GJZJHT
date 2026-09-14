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
