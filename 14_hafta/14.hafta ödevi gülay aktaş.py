print("Hello, World!")

if 5 > 2 :
    print("Five is greater than two!") # en az bir boşluk bırakmamız gerekiyor yoksa hata verir.

  #  if 5 > 2 :
  # print("Five is greater than two!") bu şekilde hata veirir.

#Değişkenler
    x = 5
    y = "Hello, World!"

    # bu bir yorum satırıdır.
    # birden fazla yorum satırı da yapabiliriz.

    """
    yorumlarımızı burda istediğimiz kadar 
    # karakteri  kullanmadan da yapabiliriz.
    çok satırlı dizeler için kullanılır.

    ''' 
    bu şekilde de yapabiliriz...

    '''

    """
x = 5 # x  int türünde 
y = "john" # y string türünde 
print(x)
print(y)


x = 4 # int 
x = "Sally" # string
print (x)

# veri tipini belirleme 
x = str(3)
y = int(3)
z = float(3) 

    # type() fonksiyon ile bir değişkenin veri tipini alabilirsiniz.
    #komut satırında class int ve class str yazıcaktır bu şekilde 
    # veri türlerini bilebiliriz.

x = 5 
y = "john" 
print(type(x))
print(type(y))

# değişkenlere tek veya çift tırnak kullanılabilir.
#ve bu şekilde değişkene dize atayabiliriz.
x = "GÜLAY"
x = 'GÜLAY'
print(x)

# değişken isimleri büyük/küçük harf duyarlıdır.
a = 4
A = "Sally"
print(a)
print(A)

# yasal değişken adları:

myvar = "john"
my_var = "john"
_my_var = "john"
myVar = "john"
MYVAR = "john"
myvar2 = "john"

"""geçersiz değişken adları:
 
 2myvar ="john"
 my-var = "john"
 my var = "john"

 """
 # DEVE KILIFI 
 # ilki hariç her kelime büyük harfle başlar.
myVariableName = "john"

# PASCAL VAKASI
#her kelime büyük harfle başlar
MyVariableName = "john"

#YILAN KILIFI
# her kelime bir alt çizgi karakteri ile ayrılır
my_variable_name = "john"


# bir satırda birden çok değişkene değer atamanıza izin verir
x, y, z = "Orange","Banana", "Cherry"
print(x)
print(y)
print(z)

# ve aynı değeri bir satırda birden çok değişkene atayabilirsiniz
x = y = z = "orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# hem metin hem değişken birleştirmek için + karakteri kullanılır
x = "harika"
print("python " + x)

# + Karakteri başka bir değişkene 
# bir değişken eklemek için de kullanabilirsiniz
x = "python is "
y = "awesome"
z = x + y
print(z)

# Sayılar için + karakter
#  matematiksel bir operatör olarak çalışır

x = 5 
y = 10
print(x + y)

"""
x = 5
y = "john"
print(x + y)
 bir dizgeyi ve bir sayıyı birleştirmeye çalışırsanz hata verir.

"""

#! Bir fonksiyonun dışında oluşturulan değişkenler
# ( yukarıdaki örneklerin  hepsi) global değişkenler olarak bilinir.

x = "Harika"

def myfunc():

  print("python " + x)

myfunc()

# bir fonksiyon içinde aynı isimde bir değişken oluşturursanız,
#  bu değişken yerel olur ! ve sadece fonksiyon içinde kullanılabilir

#aynı ada sahip global değişken, oldugu gibi ,global ve orjinal değerde kalacaktır.

x = "Harika"
def myfunc():
    x = "fantastik"

    print("python " + x)

myfunc()

print("python " + x)

#globalAnahtar kelimeyi kullanırsanız, değişken genel kapsama aittir:
def myfunc():

    global x 
    x = "bilimkurgu"
myfunc()

print("python " + x)    

# Bir fonksiyon içindeki global bir değişkenin 
# değerini değiştirmek için,
#  globalanahtar kelimeyi kullanarak değişkene bakın
x = "harika"

def myfunc():

  global x
  x = "bilimkurgu"

myfunc()

print("Python " + x)

# python da üç sayısal tür vardır 
#int , float, complex

x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# int 
x = 7
y = 356562225978966
z = -19

print(type(x))
print(type(y))
print(type(z))

#float
x = 3.14
y = 1.0
z = -12.99

print(type(x))
print(type(y))
print(type(z))

x = 5e5
y = 12E77
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex
u = 3+5j
o = 5j
k = -5j

print(type(u))
print(type(o))
print(type(k))

x = 6    # int
y = 3.8  # float
z = 8j   # complex

#int den float' a çeviriyoruz
a = float(x)

#floattan int' a çeviriyoruz
b = int(y)

# int den complex' e çeviriyoruz
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#rastgele sayı 

import random
print(random.randrange(1, 20))

#int
x = int(1)           
y = int(2.8) 
z = int("3") 

print(x)
print(y)
print(z)

#float
x = float(1) 
y = float(2.8)   
z = float("3")   
w = float("4.2") 

print(x)
print(y)
print(z)

#string
x = str("s1") 
y = str(2)    
z = str(3.0)

print(x)
print(y)
print(z)

# 7. sıradaki karakteri alır.indis sıfır(0) dan başlar.

a = "Merhaba, Dünya!"
print(a[7])

#"Kiraz" kelimesindeki harfler arasında dolaşır
for x in "Kiraz":
  print(x)

#len()İşlevi, bir dizenin uzunluğunu döndürür
a = "Merhaba, Python!"
print(len(a))
#Aşağıdaki metinde "espiri" ifadesinin olup olmadığını kontrol eder
txt = "Kod, espiri gibidir. Açıklamak zorundaysanız kötüdür!"
print("espiri" in txt)
#Yalnızca "kötüdür!" varsa yazdırın:
txt = "Kod, espiri gibidir. Açıklamak zorundaysanız kötüdür!"
if "kötüdür!" in txt:
  print("Ewet, 'kötüdür!' mevcut.")
#Aşağıdaki metinde "pahalı" ifadesinin OLMADIĞINI kontrol eder
txt = "Hayattaki en güzel şeyler bedavadır!"
print("pahalı" not in txt)

txt = "Hayattaki en güzel şeyler bedavadır!"
if "pahalı" not in txt:
 print("Hayır, 'pahalı' mevcut değildir.")

b = "Hello, World!"
print(b[2:5])
#İlk karakterin indeksi 0'dır.

b = "Merhaba, Dünya!"
print(b[:5])

# 2.karakterden itibaren hepsini yazdır demektir
b = "Merhaba, Dünya!"
print(b[2:])

#geriye doğru say:)
b = "Merhaba, Dünya!"
print(b[-5:-2])

#büyük harfe çevirir..
b = "Merhaba, Dünya!"
print(b.upper())

#küçük harfe çevirir...
b = "MERHABA, DÜNYA!"
print(b.lower())

# başında veya sonunda herhangi bir boşluk varsa kaldırır.
b = "    Merhaba Ben GÜLAY!    "
print(b.strip())

# başka bir dizeyle dize yerine geçer
b = "Merhaba Ben GÜLAY!"
print(b.replace("B", "G"))

#belirtilen ayırıcı arasındaki metin 
# liste öğeleri haline gelen bir listesini döndürür.
a = "Hello, World!"
print(a.split(",")) 

#değişken birleştirme
a = "Hello"
b = "World"
c = a + b
print(c)
#yukardakine bu şekilde çift tırnak bırakarak boşluk bırakabiliriz.
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#sayı ve metin birleştirmeyi bu şekilde yapabiliriz. 
age = 22
txt = "Merhaba benim adım GÜLAY,ve ben  {} yaşındayım."
print(txt.format(age))

#sınırsız sayıda argüman alır ve ilgili ver tutuculara yerleştirilir
Ürünmiktari =3
ÜrünNumarasi=567
Ürünfiyati=49.95
rapor ="{} dolara ürün miktarı {} olan {} numaralı üründen istiyorum! "
print(rapor.format(Ürünfiyati, Ürünmiktari, ÜrünNumarasi ))

#doğru yerleştirildiğinden emin olmaz için dizin numaraları kullanabilirsiniz.
Ürünmiktari =3
ÜrünNumarasi=567
Ürünfiyati=49.95
rapor ="{0} dolara ürün miktarı {1} olan {2} numaralı üründen istiyorum! "
print(rapor.format(Ürünfiyati, Ürünmiktari, ÜrünNumarasi ))

#çift tırnak içinde çift tırnak kullandığımızda hata  verir ama 
#bu sorunu çözmek için kaçış karakterini kullanın \" 
txt = "Kod, espiri gibidir. \"Açıklamak\" zorundaysanız kötüdür!"
print(txt)

#Bu örnek bir karakteri siler(geri al)
txt = "Hello \bWorld!"
print(txt) 

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

# alt satıra geçme özelliği vardir
txt = "Hello\nWorld!"
print(txt) 

# alt satıra geçme özelliği vardir
txt = "Hello\rWorld!"
print(txt)

#boşluk bırakır 
txt = "Hello\tWorld!"
print(txt) 

#bir ters eğik çizgi ve ardından üç tam sayı, sekizlik bir değerle sonuçlanır
txt = "\110\145\154\154\157"
print(txt) 

# bir ters eğik çizgi ve ardından bir 'x' ve bir onaltılık sayı,
#bir onaltılık değeri temsil eder
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
# true ve false cevaplarını yazıcaktır ekrana 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Koşulun True veya olup olmadığına bağlı 
# olarak bir mesaj yazdırın False
a = 200
b = 33
if b > a:
  print("b a 'dan büyüktür")
else:
  print("b a 'dan büyük değildir")

#Bir dizeyi ve bir sayıyı değerlendirir
print(bool("Hello"))
print(bool(15))

#İki değişkeni değerlendirir
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""
True Boş dizeler dışında herhangi bir dizedir .
Herhangi bir sayı True, 0(sıfır) hariçtir .
True Boş olanlar hariç herhangi bir liste, demet, küme ve sözlük .
"""
"""
None false zero (sıfır değeri) boş diziler ,
boş parantez ,köşeli, süslü parantezler bunların değeri false dır.
"""
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#false
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Fonksiyonlar Boolean Döndürebilir
def myFunction() :
  return True

print(myFunction())

#EVET! Yazdır işlev True döndürürse,
#  aksi takdirde "NO!" yazdırın:
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  #EVET!" Yazdır işlev True döndürürse, 
  # aksi takdirde "NO!" yazdırın:
x = 500
print(isinstance(x, int))

#aritmetik operatörler
print(10 + 5)
print(10 - 5)
print(10 / 5)
print(10 * 5)

#Listeler köşeli parantezler kullanılarak oluşturulur:
thislist = ["elma", "muz", "kiraz"]
print(thislist)

#Listeler, yinelenen değerlere izin verir
#Listedeki öğelerin sayısını yazdırın
thislist = ["elma", "muz", "kiraz", "elma ", "kiraz"]
print(thislist)
print(len(thislist))

#Dize, int ve boolean veri türleri
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Dizeler, tam sayılar ve boole değerleri içeren bir liste
list1 = ["abc", 34, True, 40, "male"]

#Bir listenin veri türünü belirler
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#çift ​​yuvarlak parantezlere dikkat edin
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#İlk öğenin indeksi 0'dır.
#Listenin birinci öğesini yazdırın:
thislist = ["apple", "banana", "cherry"]
print(thislist[0])

thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

# Arama, dizin 2'de (dahil) başlar 
# ve dizin 5'te (dahil değildir) biter.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Bu örnek, öğeleri baştan sona döndürür, 
# ancak "kivi" dahil DEĞİLDİR:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#Bu örnek, "kiraz" dan sona kadar olan öğeleri döndürür:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#Bu örnek, "turuncu"dan (-4)'e kadar olan öğeleri döndürür, 
# ancak "mango" (-1) dahil DEĞİLDİR:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# listede elma olup olmadığını kontrol edeceğiz

thislist = ["elma", "muz", "kiraz"]
if "elma" in thislist:
  print("Evet 'elma' bu listede var")

#Belirli bir öğenin değerini değiştirmek için
#  dizin numarasına bakın
thislist = ["elma", "muz", "kiraz"]
thislist[1] = "Üzüm"
print(thislist)

#"Muz" ve "kiraz" değerlerini "üzüm" ve 
# "karpuz" değerleriyle değiştirin

thislist = ["elma", "muz", "kiraz", "portakal", "kiwi", "mango"]
thislist[1:3] = ["üzüm", "karpuz"]
print(thislist)

#İkinci değeri iki yeni değerle değiştirerek değiştirin 
thislist = ["elma", "muz", "kiraz"]
thislist[1:2] = ["üzüm", "karpuz"]
print(thislist)

#Üçüncü öğe olarak "karpuz" ekleyin:

thislist = ["elma", "muz", "kiraz"]
thislist.insert(2, "karpuz")
print(thislist)
#Yukarıdaki örneğin bir sonucu olarak, 
# liste artık 4 öğe içerecektir.

#append()Bir öğe eklemek için yöntemi kullanma
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Geçerli listeye başka bir 
# listeden öğeler eklemek için extend()yöntemi kullanın .
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove()Yöntem, belirtilen öğeyi kaldırır.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop()Yöntem, belirtilen indeks kaldırır.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Dizini belirtmezssek, pop yöntemi son öğeyi kaldırır.

#del Anahtar kelime de belirtilen indeksi kaldırır
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)

#tüm listeyi silmek için:
thislist = ["apple", "banana", "cherry"]
del thislist


#Liste hala duruyor, ancak içeriği yok.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Listedeki tüm öğeleri tek tek yazdırmak için for döngüsünü kullanıyoruz.
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Bir meyve listesinde , sadece adında 
# "a" harfi olan
#  meyveleri içeren yeni bir liste oluşturyoruz.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#Liste kavrama ile tüm bunları yalnızca bir 
# kod satırıyla yapabilirsiniz

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(30)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

#6'dan küçük olduğu sürece i'yi yazdırır
i = 1
while i < 6:
  print(i)
  i += 1


#3 olduğumda döngüden çıkın:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



#x"muz" olduğunda döngüden çıkın 
fruits = ["elma", "muz", "kiraz"]
for x in fruits:
  print(x)
  if x == "muz":
    break


#Muz yazdırmayın
fruits = ["elma", "muz", "kiraz"]
for x in fruits:
  if x == "muz":
    continue
  print(x)

#0'dan 5'e kadar olan tüm sayıları 
# yazdırır ve döngü bittiğinde bir mesaj yazar
for x in range(6):
  print(x)
else:
  print("Sonunda Bitti!")



#Bir işlevi çağırmak için işlev adını ve 
# ardından parantez kullanın:
def my_function():
  print("Hello from a function")

my_function()

#işlev  çağrıldığında, işlevin içinde tam adı yazdırmak
#  için kullanılan bir ad iletiyoruz
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




#Argümana 10 ekleyin a ve sonucu döndürür
x = lambda a : a + 10
print(x(5))

#a ile b yi çarp 5 ve 6 ya sırayla değerleri ata
x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


#araba adlarını içeren bir dizi oluşturduk
cars = ["Ford", "Volvo", "BMW"]
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
#Dizideki eleman sayısını cars döndür
x = len(cars)
#Dizideki her öğeyi yazdırır
for x in cars:
  print(x)

cars.append("Honda")# diziye bir eleman ekleme

cars.pop(1)#carsDizinin ikinci öğesini siler

cars.remove("BMW") # BMW değerine sahip öğeyi siiilin
print(cars)