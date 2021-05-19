hava_durumu = str(input("Lütfen bir seçim yapınız. --> [1]:Güneşli, [2]:Yağmurlu, [3]:Karlı, [4]: Çamurlu"))
if hava_durumu == "1":
    hava_durumu = "Güneşli"
elif hava_durumu == "2":
    hava_durumu = "Yağmurlu"
elif hava_durumu == "3":
    hava_durumu = "Karlı"
elif hava_durumu == "4":
    hava_durumu = "Çamurlu"
    
müzik_türü = str(input("Lütfen bir seçim yapınız. --> [1]:Rock, [2]:Arabesk, [3]:Pop, [4]:Blues, [5]:Caz"))
if müzik_türü == "1":
    müzik_türü = "Rock"
elif müzik_türü == "2":
    müzik_türü = "Arabesk"
elif müzik_türü == "3":
    müzik_türü = "Pop"
elif müzik_türü == "4":
    müzik_türü = "Blues"
elif müzik_türü == "5":
    müzik_türü = "Caz"
    
fiil = str(input("Lütfen bir seçim yapınız. --> [1]:Yürüyerek, [2]:Koşarak, [3]:Emekleyerek, [4]:Sekerek"))
if fiil == "1":
    fiil = "Yürüyerek"
elif fiil == "2":
    fiil = "Koşarak"
elif fiil == "3":
    fiil = "Emekleyerek"
elif fiil == "4":
    fiil = "Sekerek"
    
söz =  str(input("Lütfen bir seçim yapınız. --> [1]:Damlaya damlaya göl olur, [2]:Hadi be!!!, [3]:Yaşasın!!!"))
if söz == "1":
    söz = "Damlaya damlaya göl olur"
elif söz == "2":
    söz = "Hadi be!!!"
elif söz == "3":
    söz = "Yaşasın!!!"

print(hava_durumu + " bir günde, kulaklığında çalan " + müzik_türü + " ve kafasında dönüp dolaşan" +
      "düşünceler eşliğinde " + fiil + " otobüs durağına doğru ilerliyordu." +
      "Durağa henüz birkaç metre mesafe kalmışken," +
      "otobüsün hareket ettiğini gördü ve içinden " + söz + " dedi")
