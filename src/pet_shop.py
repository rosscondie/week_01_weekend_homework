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

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]
    
def increase_pets_sold(pets, num):
    pets["admin"]["pets_sold"] += num

def get_stock_count(stock):
    return len(stock["pets"])

def get_pets_by_breed(pet_shop, breed):
    found_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed
    
def find_pet_by_name(pet_shop, pet_name):
    found_name = None
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            found_name = pet
    return found_name

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)