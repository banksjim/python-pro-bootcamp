from shared_modules.system_modules import clear_terminal
from silent_auction_banner import banner

# main() program logic module
def main():

    # clear the terminal screen
    clear_terminal()

    # initialize module variables
    additional_bidders:  str = "n"
    auction_winner_name: str = ""
    auction_winning_bid: float = 0.00
    bid_amount:          float = 0.00
    bidder_name:         str = ""
    bidding_complete:    bool = False
    
    auction_dictionary = {}

    # mainline statements
    
    # display program banner and welcome
    print(banner) 
    print("Welcome to the secret auction program.\n")
    
    # collect all auction bids
    while not bidding_complete:
        bidder_name = input("What is your name?: ")
        bid_amount = float(input("Bid amount?: $"))
        
        # add bidder and amount to the auction dictionary
        auction_dictionary[bidder_name] = bid_amount
        
        # ask if there are any other bidders
        additional_bidders = input("\nAre there other bidders (Y/N)?: ").lower()
        
        if (additional_bidders == 'y') or (additional_bidders == 'yes'):
            clear_terminal()
            bidding_complete = False
        else:
            bidding_complete = True
    
    # determine who made the highest bid
    for dict_bidder_name, dict_bid_amount in auction_dictionary.items():
        if dict_bid_amount > auction_winning_bid:
            auction_winner_name = dict_bidder_name
            auction_winning_bid = dict_bid_amount
    
    # clear the terminal and print the auction winner
    clear_terminal()
    print(f"The auction winner is {auction_winner_name} "
          f"with a bid of ${auction_winning_bid:.2f}.\n")
    
    return None

if __name__ == '__main__':
    main()
