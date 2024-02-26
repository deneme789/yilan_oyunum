#imports
import turtle
import time
import random

score = 0
high_score = 0
delay = 0.1 #yılanın hareket hızını kontrol eden gecikme süresi.

#Ekran Ayarları
wn = turtle.Screen()
wn.title("YILAN OYUNU")
wn.bgcolor("lightgreen")
wn.setup(width=700, height=700)
wn.tracer(0) #ekran güncellemelerini kapatır, manuel güncellemeler için

#Oyun alanının ana hatlarını oluşturalım
pencil = turtle.Turtle()
pencil.speed(0)        # en hızlı
pencil.shape("circle") #önemsiz çünkü kalemi gizleyeceğiz
pencil.color("black")
pencil.penup()
pencil.hideturtle()
pencil.goto(310,310)
pencil.pendown()
pencil.goto(-310,310)
pencil.goto(-310,-310)
pencil.goto(310,-310)
pencil.goto(310,310)
pencil.penup()

#Yılanın kafasını oluşturalım
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"  #yılan başlangıçta hareket etmeyecek.

#Yılan yemi oluşturalım
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("purple")
food.penup()
food.goto(0,100)

#yılan vücudunu dinamik bir şekilde yönetmek ve oyun işleyişi sırasında
#yılanın büyümesini sağlamak için kullanılır.Başlangıçta boş bir listedir.
#daha sonra yem yedikçe artacak ve her bir segment listeye eklenecek.

segments = []

#skor tablosunu oluşturalım.
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score: 0  High Score: 0 ",align="center",font=("Courier",24,"normal"))

####Fonksiyonlar
#Skor tablosuu güncelleme fonk.

def update_score():
    pen.clear()
    pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

#Yılanın hareketlerini sınırını belirleme fonk.
def go_up():
    if head.direction != "down":    #aşağı bakmıyorsa
        head.direction = "up"       #yukarı çevirebiliriz
def go_down():
    if head.direction != "up":      #yukarı bakmıyorsa
        head.direction = "down"     #aşağı çevirebileriz
def go_left():
    if head.direction != "right":   #sağa bakmıyorsa
        head.direction = "left"     #sola çevirebiliriz
def go_right():
    if head.direction != "left":    #sola bakmıyorsa
        head.direction = "right"    #sağa çevirebiliriz


#Yılanın her bir segmentinin ve başının konumunu güncelleme fonk.
def move():
    for index in range(len(segments)-1, 0, -1):  #sondan başa doğru tüm segmentler
        x = segments[index-1].xcor()            #bir önceki segmenti takip edicekler.
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #segment 0'ı başa taşıyalım
    if len(segments)>0:  #vücut başı takip etsin
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    #yılanın aynı yönde hareket etmesini sağlayalım
    if head.direction == "up":
        head.sety(head.ycor()+10)
    if head.direction == "down":
        head.sety(head.ycor()-10)
    if head.direction == "left":
        head.setx(head.xcor()-10)
    if head.direction == "right":
        head.setx(head.xcor()+10)

#Çarpışma meydana geldiğinde oyuna ne yapacağını söyleyelim.

def collision():
    global score, delay
    time.sleep(0.5)     # çarpışma anında oyun durur.
    head.goto(0,0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000,1000)  #segmentleri ekrandan kaldırır.
        segment.hideturtle()

    segments.clear()
    score=0                   #skoru sıfırla 
    update_score()            #skoru güncelle
    delay=0.1                 #gecikmeyi sıfırladık yeniden başlama hızına eşit olacaktır.

#oyunun klavye hareketlerimizi dinlemesini sağlayalım

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left,  "Left")

#Oyun ekranının güncellenmesi

while True:
    wn.update()  #pencereyi günceller

    #sınır ile çarpışma olup olmadığına bakalım
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        collision()

    if head.distance(food)<20:   #yılan yemi yedi mi? yemedi mi?
        food.goto(random.randint(-290,290),random.randint(-290,290)) #rastgele yeni bir yem oluşturalım.

        new_segment = turtle.Turtle()   #yem yedikçe yeni gövde
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001   #yılanın yem yedikçe oyun hızı
        score +=10
        if score > high_score:
            high_score=score
        update_score()

    move()  #hareket için geçerli

    for segment in segments:          #yılanın kafası kendisine 10 birim yaklaştığında
        if segment.distance(head)<10: #kendisini yemiş sayılsın ve oyun sonlansın
            collision()

    time.sleep(delay)  #yılan hareketlerini takip edebilmek için

wn.mainloop()   #ekran herzaman açıkkalır ve kullanıcı girdilerini dinler.

    
            
        
        
    




















