def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(total):
    return total["admin"]["total_cash"]

def add_or_remove_cash(total, num):
    total["admin"]["total_cash"] += num

    # total["admin"]["total_cash"] = total["admin"]["total_cash"] + num
    # += adds the right operand to the left operand - assigns the result to the left operand
    
def add_or_remove_cash(total, num):
    total["admin"]["total_cash"] += num
    