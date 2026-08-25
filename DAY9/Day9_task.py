"""THE SECRET AUCTION PROGRAM
    """
auction_list = {}
my_auction_list = []
name_dict = {}
name_list = []
bid_dict = {}
bid_list = []


def question():
    print("Welcome to the secret auction program")
    name = str(input("What is your name? : "))
    bid = int(input("What is your bid? : #"))
    name_list.append(name)
    bid_list.append(bid)
    name_dict["Name"] = name_list
    bid_dict["Bid"] = bid_list
    auction_list[name] = bid


bidder_status = "yes"

while bidder_status == "yes":
    # Clear Screen
    question()
    bidder_status = input("Are there any other bidders? Type yes or no ").lower()

my_auction_list += (name_dict, bid_dict)


print(auction_list)

# bid_list = [2.5, 5, 9.5, 3, 4]

highest_bid = 0
for bid_amount in bid_list:
    if highest_bid <= bid_amount:
        highest_bid = bid_amount
        position = bid_list.index(bid_amount)


# print(f"The winner is JAMES with a bid of {highest_bid}")
print(f"The winner is {name_list[position]} with a bid of {highest_bid}")
