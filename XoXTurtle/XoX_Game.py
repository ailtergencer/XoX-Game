import turtle
import random
import playsound

turtle.title("XoX GAME")
turtle.setup(500,500)
screen = turtle.Screen()
kalem = turtle.Turtle()
kalem.hideturtle()
kalem.speed(0)

x_hucreleri = []
o_hucreleri = []
bos_hucreler = [str(i) for i in range(1, 10)]
oyun_bitti = False

def tablo():
    kalem.clear()
    kalem.penup()
    kalem.goto(-50,150)
    kalem.pendown()
    kalem.goto(-50,-150)

    kalem.penup()
    kalem.goto(50,150)
    kalem.pendown()
    kalem.goto(50,-150)

    kalem.penup()
    kalem.goto(-150,50)
    kalem.pendown()
    kalem.goto(150,50)

    kalem.penup()
    kalem.goto(-150,-50)
    kalem.pendown()
    kalem.goto(150,-50)

def x_olusturma(x , y):
    kalem.penup()
    kalem.goto(x-20 , y+20 )
    kalem.pendown()
    kalem.goto(x+20 , y-20)
    
    kalem.penup()
    kalem.goto(x+20 , y+20)
    kalem.pendown()
    kalem.goto(x-20 , y-20)

def o_ciz(x, y):
    kalem.penup()
    kalem.goto(x, y-20)
    kalem.pendown()
    kalem.circle(20)

def o_olusturma():
    if bos_hucreler:
        konum_o = random.choice(bos_hucreler)
        bos_hucreler.remove(konum_o)
        o_hucreleri.append(konum_o)
        if konum_o == "1":
            o_ciz(-100, 100)
        elif konum_o == "2":
            o_ciz(0, 100)
        elif konum_o == "3":
            o_ciz(100, 100)
        elif konum_o == "4":
            o_ciz(-100, 0)
        elif konum_o == "5":
            o_ciz(0, 0)
        elif konum_o == "6":
            o_ciz(100, 0)
        elif konum_o == "7":
            o_ciz(-100, -100)
        elif konum_o == "8":
            o_ciz(0, -100)
        elif konum_o == "9":
            o_ciz(100, -100)

def x_kontrol(x, y):
    global oyun_bitti
    if oyun_bitti:
        return

    if -150 <= x <= -50 and 50 <= y <= 150 and "1" in bos_hucreler:
        x_olusturma(-100, 100)
        x_hucreleri.append("1")
        bos_hucreler.remove("1")

    elif -50 <= x <= 50 and 50 <= y <= 150 and "2" in bos_hucreler:
        x_olusturma(0, 100)
        x_hucreleri.append("2")
        bos_hucreler.remove("2")
    
    elif 50 <= x <= 150 and 50 <= y <= 150 and "3" in bos_hucreler:
        x_olusturma(100, 100)
        x_hucreleri.append("3")
        bos_hucreler.remove("3")
    
    elif -150 <= x <= -50 and -50 <= y <= 50 and "4" in bos_hucreler:
        x_olusturma(-100, 0)
        x_hucreleri.append("4")
        bos_hucreler.remove("4")
    
    elif -50 <= x <= 50 and -50 <= y <= 50 and "5" in bos_hucreler:
        x_olusturma(0, 0)
        x_hucreleri.append("5")
        bos_hucreler.remove("5")
    
    elif 50 <= x <= 150 and -50 <= y <= 50 and "6" in bos_hucreler:
        x_olusturma(100, 0)
        x_hucreleri.append("6")
        bos_hucreler.remove("6")
    
    elif -150 <= x <= -50 and -150 <= y <= -50 and "7" in bos_hucreler:
        x_olusturma(-100, -100)
        x_hucreleri.append("7")
        bos_hucreler.remove("7")
    
    elif -50 <= x <= 50 and -150 <= y <= -50 and "8" in bos_hucreler:
        x_olusturma(0, -100)
        x_hucreleri.append("8")
        bos_hucreler.remove("8")
    
    elif 50 <= x <= 150 and -150 <= y <= -50 and "9" in bos_hucreler:
        x_olusturma(100, -100)
        x_hucreleri.append("9")
        bos_hucreler.remove("9")
    
    else:
        return  
    
    kazanan()

    if not oyun_bitti:
        o_olusturma()
        kazanan()

def kazanan():
    global oyun_bitti
    kazanma_kombinasyonlari = [
        ["1","2","3"], ["4","5","6"], ["7","8","9"],  # Yatay
        ["1","4","7"], ["2","5","8"], ["3","6","9"],  # Dikey
        ["1","5","9"], ["3","5","7"]                  # Çapraz
    ]
    
    for kombinasyon in kazanma_kombinasyonlari:
        if all(h in x_hucreleri for h in kombinasyon):
            kalem.penup()
            kalem.goto(-200, 200)
            kalem.pendown()
            kalem.write("X Kazandi!", font=("Arial", 16, "normal"))
            playsound.playsound("win_sound.mp3")
            oyun_bitti = True
            return
        if all(h in o_hucreleri for h in kombinasyon):
            kalem.penup()
            kalem.goto(-200, 200)
            kalem.pendown()
            kalem.write("O Kazandi!", font=("Arial", 16, "normal"))
            playsound.playsound("win_sound.mp3")
            oyun_bitti = True
            return

    if not bos_hucreler and not oyun_bitti:
        kalem.penup()
        kalem.goto(-200, 200)
        kalem.pendown()
        kalem.write("Berabere!", font=("Arial", 16, "normal"))
        oyun_bitti = True

def reset_oyun():
    global x_hucreleri, o_hucreleri, bos_hucreler, oyun_bitti
    x_hucreleri = []
    o_hucreleri = []
    bos_hucreler = [str(i) for i in range(1, 10)]
    oyun_bitti = False
    tablo()

def oyunu_kapat():
    screen.bye()

def oyun_devam_kontrol():
    screen.listen()
    screen.onkey(reset_oyun, "w")
    screen.onkey(oyunu_kapat, "q")

tablo()
screen.onscreenclick(x_kontrol)
oyun_devam_kontrol()
kalem.penup()
turtle.done()
