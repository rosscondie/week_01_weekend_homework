#TEST 1
def get_pet_shop_name(petshop):
    return petshop["name"]

#TEST 2
def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

#TEST 3 & 4
def add_or_remove_cash(petshop, num):
    petshop["admin"]["total_cash"] += num

# total["admin"]["total_cash"] = total["admin"]["total_cash"] + num
# += adds the right operand to the left operand - assigns the result to the left operand
    
#TEST 5
def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]

#TEST 6    
def increase_pets_sold(petshop, num):
    petshop["admin"]["pets_sold"] += num

#TEST 7
def get_stock_count(petshop):
    return len(petshop["pets"])

#TEST 8 & 9
def get_pets_by_breed(petshop, breed):
    found_breed = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            found_breed.append(pet)
    return found_breed

#TEST 10 & 11   
def find_pet_by_name(petshop, pet_name):
    found_name = None
    for pet in petshop["pets"]:
        if pet["name"] == pet_name:
            found_name = pet
    return found_name

#TEST 12
def remove_pet_by_name(petshop, pet_name):
    for pet in petshop["pets"]:
        if pet["name"] == pet_name:
            petshop["pets"].remove(pet)

#TEST 13
def add_pet_to_stock(petshop, new_pet):
    petshop["pets"].append(new_pet)

#TEST 14
def get_customer_cash(customer):
    return customer["cash"]

#TEST 15
def remove_customer_cash(customer, customer_cash):
    customer["cash"] -= customer_cash

#TEST 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#TEST 17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)