import random


def spin_row():
    symbol = ["🌸", "🍒", "🪙" ,"🔔" ,"⭐"]

    return [random.choice(symbol) for _ in range(3)]



def print_row(row):
    print("*******************")
    print("  |  ".join(row))
    print("*******************\n")

def get_payment(row , bet ):
    if row[0] == row[1] == row[2]:
        if row[0]== '🌸':
            return bet * 2 
        elif row[0] == "🍒":
            return bet * 3
        elif row[0] == '🪙':
            return bet * 4 
        elif row[0] == "🔔" :
            return bet * 5 
        elif row[0] == '⭐':
            return bet * 10
        return 0
    return 0

def main():
    n = int(input("enter amount :"))
    balance = n

    print("**********************")

    print("letsss go gamblingggggg") 
    print("symbol:🌸 🍒 🪙 🔔 ⭐")

    print("*********************")


    while balance > 0 : 
        print("current balance :", "$", balance)

        bet = input("enter your bet :") 
         
        if  not bet.isdigit():
            print("please enter a vaild number")
            continue 

        bet = int(bet) 

        if bet > balance:
            print("ye garreb ki ####@##") 
            continue 

        if bet <= 0 :
            print("bet must be greater than 0")
            continue
        
        balance -= bet 

        row =  spin_row()
        print("spinning.. \n")
        print_row(row) 
        

        payout = get_payment(row, bet)

        if payout  >  0:
            print("you won $", payout)
        else :
            print("you lost") 

        balance += payout
        


if __name__ == "__main__":
    main()