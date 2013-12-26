import string

def hotel_cost(nights):
    return nights * 140
    
def plane_ride_cost(city):
    cityToCheck = string.lower(city)
    if cityToCheck == "charlotte":
        return 183
    elif cityToCheck == "tampa":
        return 220
    elif cityToCheck == "pittsburgh":
        return 222
    elif cityToCheck == "los angeles":
        return 475
        
def rental_car_cost(days):
    day_rate = 40
    three_day_discount = 20
    #discounts cannot be accumulated
    seven_day_discount = 50
    total_cost = 40 * days
    if days >= 7:
        total_cost = total_cost - seven_day_discount
    elif days >= 3:
        total_cost = total_cost - three_day_discount
    return total_cost


def main():
#my code here
    

if __name__ == "__main__":
    main()
