
# download ranodm library :-
import random
#-----------------------------------------------------------------------------------------------------------

# name gen :-
n = ["sophia","emma","jacob","mason","ava","emaily","noah","ethan","aidan","daniel","ella","liam","james","logan","lily","ryan","luke"]
__a = ["Smith"," Johnson ","Williams" ,"Brown", "Jones" ,"Garcia" ,"Miller" ,"Davis" ,"Rodriguez" ,"Martinez" ,"Hernandez" ,"Lopez" ,"Gonzalez" ,"Wilson" ,"Anderson" ,"Thomas" ,"Taylor" ,"Moore" ,"Jackson" ,"Martin" ,"Lee" ,"Perez" ,"Thompson" ,"White" ,"Harris" ,"Sanchez" ,"Clark" ,"Ramirez" ,"Lewis" ,"Robinson" ,"Walker" ,"Young" ,"Allen" ,"King" ,"Wright" ,"Scott" ,"Torres" ,"Nguyen" ,"Flores" ,"salim" ]
n1 = random.choice(n)
__a1 = random.choice(__a)
print("-"*50)
print("insta : 192.168.170 ----------------------------------")
print("-"*50)
name = f"name : {n1} {__a1}"
print(name)
#-----------------------------------------------------------------------------------------------------------

# email gen :-
e = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
m = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a = ["1","2","3","4","5","6","7","8","9"]
i = ["$","-","_","."]
l = ["@hotmail.com","@gmail.com"]
e1 = random.choice(e)
m2 = random.choice(m)
a3 = random.choice(a)
i4 = random.choice(i)
l5 = random.choice(l)
email = f"email : {e1}{m2}{a3}{i4}{l5}"
print(email)
#------------------------------------------------------------------------------------------------------------

# password gen :-
p = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
_a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s = ["1","2","3","4","5","6","7","8","9"]
_s = ["$","-","_","."]
w = ["1","2","3","4","5","6","7","8","9"]
o = ["1","2","3","4","5","6","7","8","9"]
r = ["1","2","3","4","5","6","7","8","9"]
d = ["1","2","3","4","5","6","7","8","9"]
_p = ["1","2","3","4","5","6","7","8","9"]
_as =  ["1","2","3","4","5","6","7","8","9"]
_as2 = ["1","2","3","4","5","6","7","8","9"]
_w = ["1","2","3","4","5","6","7","8","9"]
_o = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
_ww = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
p1 = random.choice(p)
_a2 = random.choice(_a)
s3 = random.choice(s)
_s4 = random.choice(_s)
w5 = random.choice(w)
o6 = random.choice(o)
r7 = random.choice(r)
d8 = random.choice(d)
_p9 = random.choice(_p)
_as10 = random.choice(_as)
_as11 = random.choice(_as2)
_w12 = random.choice(_w)
_o13 = random.choice(_o)
_ww14 = random.choice(_ww)
password = f"password : {p1}{_a2}{s3}{_s4}{w5}{o6}{r7}{d8}{_p9}{_as10}{_as11}{_w12}{_o13}{_ww14}"
print(password)
#----------------------------------------------------------------------------------------------------------

# country , city , zip code  :-
# country :-
c = ["united state","united kingdom","italy","spain"]
_c = random.choice(c)
print(f"country : {_c}")
# city :-
if _c == "united state" :
    ci = ["new york","chicago","houston","taxes","sandiego","florida"]
    _ci = random.choice(ci)
    print(f"city : {_ci}")
        #===================
    if _ci == "new york" :
        newyork = ["10022","10018","10013","10009","10005","10001","10023","10014","10016","10017"]
        _newyork = random.choice(newyork)
        print(f"zip code / post code : {_newyork}")
        #__________________
    elif _ci == "chicago" :
            chicago = ["60615","60611","60607","60176","60616","60613","6069","60614","60618","60606","60131"]
            _chicago = random.choice(chicago)
            print(f"zip code / post code : {_chicago}")
        #------------------
    elif _ci == "houston" :
                houston = ["77017","77021","77013","77009","77005","77001","77022","77016","77024","77008","77004"]
                Houston = random.choice(houston)
                print(f"zip code / post code : {Houston}")
        #--------------------
    elif _ci == "taxes" :
            taxes = ["75006","75011","75013","75016","75020","75021","75022","75023","75026","75051","7502"]
            _taxes = random.choice(taxes)
            print(f"zip code / post code : {_taxes}")
        #-------------------
    elif _ci == "sandiego" :
        sandiego = ["92105","92106","92107","92104","92092","91942","92027","92108","92093","92102","91932"]
        _sandiego = random.choice(sandiego)
        print(f"zip code / post code : {_sandiego}")
        #-------------------
    elif _ci == "florida" :
        florida = ["32003","32004","32006","32011","3026","32030","32033","32034","32041","32042","32043"]
        _florida = random.choice(florida)
        print(f"zip code / post code : {_florida}")
        #======================
if _c == "united kingdom" :
    _cit = ["london","manchester","durham","leeds","lincoln","oxford"]
    __cit = random.choice(_cit)
    print(f"city : {__cit}")
    #-----------------------
    if __cit == "london" :
        london = ["181747","181382","181368","18185","181388","181365","181445","181400","181436","181401","181300"]
        _london = random.choice(london)
        print(f"zip code / post code : {_london}")
        #---------------------
    elif __cit == "manchester" :
        manchester = ["03101","03102","03103","03104","03105","03106","03107","03108","03109","03110","03111"]
        _manchster = random.choice(manchester)
        print(f"zip code / post code : {_manchster}")
        #---------------------
    elif __cit == "durham" :
        durham =['27701', '27708', '27704', '27703', '27709', '27705', '27713', '27714', '27515', '27514', '27613', '27509']
        _durham = random.choice(durham)
        print(f"zip code / post code : {_durham}")
        #---------------------
    elif __cit == "leeds"  :
        leeds = ["35173","35094","35004"]
        _leeds = random.choice(leeds)
        print(f"zip code / post code : {_leeds}")
        #----------------------
    elif __cit == "lincoln" :
        lincoln = ["02865","02863","02838","02802"]
        _lincoln = random.choice(lincoln)
        print(f"zip code / post code : {_lincoln}")
        #----------------------
    elif __cit == "oxford" :
        oxford = ["38655","38675","01540"]
        _oxford = random.choice(oxford)
        print(f"zip code / post code : {_oxford}")
        #----------------------
if _c == "italy" :
    _city = ['rome', 'milan','genoa']
    __city = random.choice(_city)
    print(f"city : {__city}")
    #==========================
    if __city == "rome" :
        rome = ['00017', '00026', '00040', '00044', '00045', '00046', '00050', '00062', '00063', '00069', '00100', '00100','00118', '00119']
        _rome = random.choice(rome)
        print(f"zip code / post code : {_rome}")
        #--------------------
    elif __city == "milan" :
            milan =['20100', '20990', '20090', '20900', '20021', '20030']
            _milan = random.choice(milan)
            print(f"zip code / post code : {_milan}")
            #--------------------
    elif __city == "genoa" :
                genoa = ['16100', '16121', '16122', '16123', '16124', '16126', '16127', '16131']
                _genoa = random.choice(genoa)
                print(f"zip code / post code : {_genoa}")
                #======================
if _c == "spain":
                spain = ['madrid', 'barcelona', 'bilbao', 'seville']
                _spain = random.choice(spain)
                print(f"city : {_spain}")
                #-----------------------
                if _spain == "madrid" :
                    madrid = ['28864', '28130', '28630', '28100', '28108', '28219', '28920', '28921', '28925']
                    _madrid = random.choice(madrid)
                    print(f"zip code / post code : {_madrid}")
                    #--------------------
                elif _spain == "barcelona" :
                    barcelona =['08001', '08002', '08003', '08004', '08005', '08005', '08006', '08016']
                    _barcelona = random.choice(barcelona)
                    print(f"zip code / post code : {_barcelona}")
                    #---------------------
                elif _spain == "bilbao" :
                    bilbao =['48001', '48002', '48003', '48004', '48005', '48006', '48007', '48008', '48009']
                    _bilbao = random.choice(bilbao)
                    print(f"zip code / post code : {_bilbao}")
                    #---------------------
                elif _spain == "seville" :
                    seville = ['41001', '41002', '41003', '41005', '41006', '41007']
                    _seville = random.choice(seville)
                    print(f"zip code / post code : {_seville}")
#-------------------------------------- insta : 192.168.170 ------------------------------------
