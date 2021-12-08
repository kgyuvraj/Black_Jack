import random
def insert_card():
    user.append(random.choice(deck))

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
dealer = []
user.append(random.choice(deck))
user.append(random.choice(deck))
dealer.append(random.choice(deck))
dealer.append(random.choice(deck))
print(f"user's card: {user}")
print(f"dealer's card : {dealer[0]}")
user_sum = 0
dealer_sum = 0
for cards in range(0, len(user)):
    user_sum += user[cards]
print(f"user score: {user_sum}")
for cards in range(0, len(dealer)):
    dealer_sum += dealer[cards]
print(f"dealer score: {dealer_sum}")
if user_sum==21:
    print("user win!!")
elif dealer_sum==21:
    print("you lose!!")
elif user_sum>21:
    if '11' in user:
        position=user.index('11')
        if user_sum >21:
            user[position]=1
            if user_sum>21:
                print("you lose!")
        else:
            user[position]=11
        elif user_sum<21:
        else:
            choice=input("want another card?").lower()
            if choice=='y':
                insert_card()

elif user_sum<21:
    choice=input("want another card?")
    if choice=='y':
        insert_card()
print(user)