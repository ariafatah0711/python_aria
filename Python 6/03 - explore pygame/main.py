# pygame| game
import pygame

''' init '''
pygame.init()

# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# kordinat posisi
x = 250
y = 250
# lebar window adalah 500*500
# maka jika posisi object 250 250 ada di tengah
# jika 150 150 di tengah kiri

# ukuran 
panjang = 20
lebar = 20

speed = 5

while isRun:
    pygame.time.delay(10) # agar tidak terlalu cepat

    ''' user input, database input '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed() # ngambil semua yang diketikan

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0: # agar tidak melebihi ke kiri
        x -= speed # artinya kordinatnya dikurangi dari kordinat x
        # maka otomatis ke kiri

    # ambil ke kanan
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar: # window lebar dikurangi lebar agar tidak melebihi
        x += speed # artinya kordinatnya di tambah dengan speed 
        # otomatis ke kanan

    # ambil ke atas
    if keys[pygame.K_UP] and y > 0: # tidak boleh lebih dari kordinat y 0
        y -= speed 

    # ambil ke bawah
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed  
   
    '''game dynamic'''
    

    ''' update asset '''
    window.fill((255,255,255)) # ubah warna
    # pygame draw rect ditaruh ke window, diberi warna orange,
    # kordinat posisi variable x dan y, besar dan lebar adalah variable panjang dan lebar
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))

    ''' render ke display '''
    pygame.display.update() # render dulu

pygame.quit()