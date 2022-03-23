
import snaps
import random
import time


#(iloscRzutow) = 2
#sumaRzutow = 0
#for i in range(iloscRzutow):
    #rzut = random.randint(1, 6)
    #sumaRzutow = sumaRzutow + rzut

    #print(rzut)
#print(sumaRzutow)
















#kostka2 = random.randint(1,6)
#kostka1 = random.randint(1,6)
#print(kostka1)
#time.sleep(1)
#print(kostka2)
#time.sleep(1)
#print("wylosowałeś: ", (kostka1) + (kostka2))
#time.sleep(1)




#rzut = int(input("ile razy rzucić kostką?: "))


#for i in range(rzut):
 #   print(random.randint(1,6))

#print("gotuj jajka przez 5 minut")
#time.sleep(270)
#print("Prawie ugotowane, przygotuj łyżeczkę")







timer = random.randint(1,3)


print(f'Stój przez: {timer} sekund!')
time.sleep(timer)
snaps.play_sound('multimedia\ding.wav')
print('Czas minął!!!')

