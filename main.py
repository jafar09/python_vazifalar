sonlar1 = input("birinchi son kiriting ")
sonlar2 = input("ikkinchi son kiriting ")
if sonlar1== sonlar2:
    print("Sonlar teng?")
else:
    print("Sonlar bir birga teng emas ?")


# son=10
# if son<0:
#     print(" Manfiy son  ")
# else:
#     print("Musbat son")

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     yosh=0
# elif yosh<=12:
#     yosh=5000
# elif yosh<=18:
#     yosh=8000
# else:
#     yosh=12000
# #     print(f"sizga kirish{yosh} so'm ")
# #
# #
# kun=input('Bugin kun nima?>>>')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugin dam olish kuni')
# else:
#     print('Bugin ish kuni')

#
# kun = input("Bugun kun nima?")
# harorat = float(input("Havo harorati qanday?"))
#
# if kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='shanba' or kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 0
# assorti = 1
#
# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi. ")
#     narh = narh+1000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh+2000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh+3000
#
# print(f"Jami {narh} so'm")


# in degani ichida degani: in aperatori bilan tanishib chiqamiz
# menu = ['osh', 'manti', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ["osh","somsa","manti","shashlik"]
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor.")
#         else:
#             print(f"Menuda {taom} taom yuq.")
# else:
#    print("Savatingiz bo'sh?")
#1-MISOL
# son = float(input("Juft son kiriting: "))
# if son%2:
#     print("Bu junt son emas.")
# else:
#     print("Rahmat!")
# 2-misol
# yosh = int(input("Yoshingiz nechida: "))
# if yosh<=4:
#     yosh=0
# elif yosh<=12:
#     yosh=5000
# elif yosh<=18:
#     yosh=8000
# elif yosh<=20:
#     yosh=18000
# # print(f"Muziyga kirish {yosh} so'm")
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")






#
# mahsulotlar = ['banan', 'olma', 'anor', 'behi', 'nok', 'shavtoli'
#     , 'sovun', 'soda', 'kapliya', 'gupka']
#
#
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulot qushing "))
#     bor_mahsulot = []
#     mavjud_emas = []
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulot.append(mahsulot)
#         else:
#             mavjud_emas.append(mahsulot)
#
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
#     else:
#         print("So'z suragan baracha mahsulotlar do'konimizda bor.")

# users = ['vali', 'ali', 'jahon', 'jafar', 'polvon']
# login = input("Yangi login tanlang: ")
#
# if login in users:
#     print("Login band, boshqa login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")
#

# son = int(input("Istalgan butun son kiriting: "))
#
# for n in range(2,11):
#     if not (son%2):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#     else:
#         print("Butun son kiriting")
#         break
#
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")