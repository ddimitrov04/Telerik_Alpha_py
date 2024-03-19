class SantaHelper:
    def __init__(self):

        self.wishes = {}

    def add_wish(self, item_name, price, child_name):
        formatted_price = float(price)
        wish = (item_name, formatted_price)

        if child_name not in self.wishes:
            self.wishes[child_name]= []
        self.wishes[child_name].append(wish)
        print("Wish added")

    def delete_wishes(self, child_name):
        if child_name in self.wishes:
            delete_count = len(self.wishes[child_name])
            del self.wishes[child_name]
            print(f"{delete_count} Wishes deleted")
        else:
            print("No wishes found")

    def find_wishes_by_price_range(self, from_price, to_price):
        found = False
        wishes_list = []
        for child_name, wishes in self.wishes.items():
            for item_name, price in wishes:
                if from_price <= price <= to_price:
                    wishes_list.append((item_name, child_name, f"{price:.2f}"))
                    found = True

        wishes_list.sort()
        for wish in wishes_list:
            print(f"{{{wish[0]};{wish[1]};{wish[2]}}}")
        if not found:
            print("No Wishes found")

    def find_wishes_by_child(self, child_name):
        if child_name in self.wishes and self.wishes[child_name]:
            sorted_wishes = sorted(self.wishes[child_name], key = lambda x: x[0])
            for item_name, price in sorted_wishes:
                print(f"{{{item_name};{child_name};{price:.2f}}}")
        else:
            print("No Wishes found")

helper = SantaHelper()
n = int(input())

for _ in range(n):
    command_line = input()
    action, args_str = command_line.split(' ', 1)
    if action == "AddWish":
        item_name, price, child_name = args_str.split(';')
        helper.add_wish(item_name, price, child_name)
    elif action == "DeleteWishes":
        helper.delete_wishes(args_str)
    elif action == "FindWishesByPriceRange":
        from_price, to_price = args_str.split(';')
        helper.find_wishes_by_price_range(float(from_price), float(to_price))
    elif action == "FindWishesByChild":
        helper.find_wishes_by_child(args_str)
