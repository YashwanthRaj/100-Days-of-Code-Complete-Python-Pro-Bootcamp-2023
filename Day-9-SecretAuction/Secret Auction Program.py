from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)


auction_database = {}

def input_names(name,bid):
    auction_database[name]  = bid
    
flag = True
temp_max = 0
user = ""

while flag:
    name_user = input("Enter your name: ")
    users_bid = int(input("Enter your bid: $"))
    input_names(name_user, users_bid)
    
    ask = input("Do you want to continue, yes/no: ").lower()
    if ask == 'no':
        flag = False
    else:
        clear()
        
        
for name_of_user in auction_database:
    if auction_database[name_of_user] > temp_max:
        temp_max = auction_database[name_of_user]
        user = name_of_user
    
print(f"The person with the highest bid is {user} with bid value ${temp_max} !!")
