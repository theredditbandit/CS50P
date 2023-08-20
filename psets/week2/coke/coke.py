
def main():
    amt_due = 50 # Amount that's due
    moneygiven = 0 # sum of the total value of coins inserted
    while amt_due > 0:
        print("Amount Due:", amt_due)
        money_in = int(input("Insert Coin: "))
        if money_in == 5 or money_in == 10 or money_in == 25:
            amt_due -= money_in
            moneygiven += money_in
    print("Change Owed:", abs(50-moneygiven))


main()
