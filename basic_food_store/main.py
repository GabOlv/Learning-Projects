import os
import json
import time

class Menu():
    def __init__(self, foods): ## Ver como instanciar nos parametros
        self.oper = Operation(self)
        self.food = foods
        self.show_foods()
        self.menu_choice(foods)
              
    def show_foods(self):
        return (', '.join(map(str, (self.food for self.food in foods))))

    def menu_choice(self, foods):
        while True:
            if not self.oper.cart:
                pass
            else:
                print(f'Foods Selected: {self.oper.cart} | Price: {sum(self.oper.cart)}')
            print('Foods on Catalogue:\n-',self.show_foods())
            choice = input('Select an option\n1- Add to cart\n2- Checkout\n3- Clear Cart\n4- Exit\nResult: ')
            match choice:
                case '1':
                    continue_menu = self.oper.cart_operation(foods)
                case '2':
                    continue_menu = self.oper.food_checkout()
                case '3':
                    continue_menu = self.oper.clear_operation()
                case '4':
                    print("Exited")
                    break
            if not continue_menu:
                break
class Operation():
    def __init__(self, choice):
        self.cart = []
        self.total_value = []
        self.menu = choice
    
    def select_foods_from_menu(self, foods):
        return [(key, value) for key, value in foods.items()]

    def get_food_price(self,food_names, food_prices, buy_food):
        index = food_names.index(buy_food)
        return food_prices[index]
        
    def cart_operation(self, foods):
        while True:
            buy_food = input("Select the food you want: ").capitalize()
            catalogue_list = self.select_foods_from_menu(foods)
            food_names, food_prices = [food[0] for food in catalogue_list], [value[1] for value in catalogue_list]
            if buy_food in food_names:
                self.cart.append(self.get_food_price(food_names, food_prices, buy_food))
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
            else:
                print(f'The selected food {buy_food} is not avaliable in the cart ;(')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
                
    def food_checkout(self):
        if not self.cart:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cart is empty!!")
            return True
        else:
            total_value = sum(self.cart)
            choice_checkout = input(f'Cart:{self.cart} and the total value is: {total_value} $\n Are you sure? (Y/N)').upper()
            if choice_checkout == 'Y':
                print(f"You have Purchased the foods")
                return False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
                
    def clear_operation(self):
        self.cart.clear()
        os.system('cls' if os.name == 'nt' else 'clear')
        return True

def get_file_path(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(script_dir, filename)
    return main_path

def load_file():
    file_path = get_file_path(filename='menu.json')
    with open(file_path, 'r', encoding='utf-8') as json_data:
        dic = json.load(json_data)
        json_data.close()
    return dic
    
if __name__ == '__main__':
        foods = load_file()
        menu = Menu(foods)