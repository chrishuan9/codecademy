def hotel_cost(nights):
    return nights * 140

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
	amount_due = add_monthly_interest(balance - payment)
	print "You still owe: {}".format(amount_due)
	return amount_due
	

	
def main():
#my code here
    bill = hotel_cost(5)
    new_balance = make_payment(bill/2,bill)
    print "We still owe: {}".format(new_balance) 
    new_balance = make_payment(100,new_balance)
    print "We still owe: {}".format(new_balance)  

if __name__ == "__main__":
    main()
