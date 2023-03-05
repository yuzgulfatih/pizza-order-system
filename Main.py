from Pizza import *
from Sauce import *
import csv
import datetime

def menu() :
    with open("Menu.txt" , "r") as menu:
        print(menu.read())

def main():
    menu()
    pizza_choice = int(input("Bir Pizza Tabanı Seçiniz: "))
    sauce_choice = int(input("Sosunuzu Seçiniz: "))
    pizza = None
    if pizza_choice == 1 : 
        pizza = ClassicPizza()
    elif pizza_choice == 2 :
        pizza = Margherita()
    elif pizza_choice == 3 :
        pizza = TurkPizza()
    elif pizza_choice == 4 :
        pizza = DominosPizza()
    else : 
        "Hatalı Seçim"

    sauce = None
    if sauce_choice == 11 :
        sauce = Olives(pizza)
    elif sauce_choice == 12 :
        sauce = Mushrooms(pizza)
    elif sauce_choice == 13 : 
        sauce == GoatCheese(pizza)
    elif sauce_choice == 14 :
        sauce = Meat(pizza)
    elif sauce_choice == 15 :
        sauce = Onions(pizza)
    elif sauce_choice == 16 :
        sauce = Corn(pizza)    
    else : 
        "Hatalı Seçim"

        
    print("Pizza seçiminiz: " , sauce.get_description())
    print("Ödenecek tutar: " , sauce.get_cost())
    full_name = input("Adınızı Soyadınızı Giriniz: ")
    ccno= input("Kredi Kartı Numarınızı Giriniz: ")
    date = datetime.datetime.now()
    users_info = open("müsteri.txt", "a")
    users_info.write("{}- {} - {} \n".format(full_name , ccno , date))
 




if __name__ == "__main__":
    main()