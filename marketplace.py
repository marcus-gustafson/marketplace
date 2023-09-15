
users = {}
command = ""
activeUser = None
class User:
    def __init__(self, username, password, balance = 0):
        self.username = username
        self.password = password
        self.balance = balance
        self.active_listings = []
    def createUser(username, password, balance = 0):
        newUser = User(username, password, balance)
        users[newUser.username] = newUser
    def create_listing(self, item, price):
        self.active_listings.append(Listing(item, price))

class Item:
    def __init__(self, item_name, quality):
        self.item_name = item_name
        self.quality = quality

class Listing:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def print_listing(self):
        print(f'Selling a(n) {self.item.item_name}')
        print(f'Quality: {self.item.quality}')
        print(f'Price: {self.price}')

def sign_up():
    validName = False
    username = input('What would you like your username to be?')
    while validName != True:
        if username not in users.keys():
            validName == True
            break
        else:
            username = input('Sorry, that username is already taken. Please enter a new username.')
    password = input('What would you like your password to be?')
    User.createUser(username, password)

def log_in():
    username = input('Username:')
    while username not in users.keys():
        username = input('Username incorrect. Please try again.')
    password = input('Password')
    while password != users[username].password:
        password = input('Incorrect password. Please try again.')
    global activeUser
    activeUser = username
    print(f'Hello {username}!')

def create_listing():
    if activeUser == None:
        print('Please log in before creating a lisitng.')
        return
    item_name = input('What is the name of the item you want to list?')
    item_quality = input('What is the condition of the item?')
    price = input('What is the price you would like to sell the item for?')
    users[activeUser].create_listing(Item(item_name, item_quality), price)

def print_listings():
    for user in users.values():
        for listing in user.active_listings:
            print(user.username)
            listing.print_listing()
            print()

def buy_listing():
    seller = input("Who do you want to buy from?")
    i = 1
    for listing in users[seller].active_listings:
        print(i)
        listing.print_listing()
        i += 1
    listingNum = int(input("What is the number of the item you wish to purchase?"))
    listing = users[seller].active_listings[listingNum - 1]
    if listing.price > users[activeUser].balance:
        print('Sorry you do not have enough funds.')
    else:
        users[seller].active_listings.remove(listing)
        print('Item purchased!')

def deposit_funds():
    users[activeUser].balance += int(input('How much money do you want to deposit?'))

while command != 'quit':
    command = input('Enter your command. Type "help" for a list of commands. Type "quit" to exit the program.')
    if command == "help":
        #todo add command list
        print("sign up\nlog in\nlog out\ncreate listing\nprint listings\nbuy listing\ndeposit funds\ntest\n")
    if command == "sign up":
        sign_up()
    if command == "log in":
        log_in()
    if command == "log out":
        activeUser = None
    if command == "create listing":
        create_listing()
    if command == "print listings":
        print_listings()
    if command == "buy listing":
        buy_listing()
    if command == "deposit funds":
        deposit_funds()
    # set up test users and listings
    if command == 'test':
        User.createUser('mark', '12345', 50)
        users['mark'].create_listing(Item('fish', 'excellent'), 5)

        User.createUser('john', 'secret', 0)
        users['john'].create_listing(Item('tv', 'refurbished'), 300)
        users['john'].create_listing(Item('couch', 'used'), 100)

        User.createUser('test', 1234, 0)
        activeUser = 'test'
    








    