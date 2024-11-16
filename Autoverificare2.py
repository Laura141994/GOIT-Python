#Ex. 1
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message:
    if i==search:
        result+=1
print(result)

#Ex. 2
num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(num):
        sum+=i+1
    num = int(input("Enter integer (0 for output): "))
print (sum)

#Ex. 3
def greeting():
 print('Hello world!')

 #Ex. 4
 username=str(input("Introdu numele invitatului"))
def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"

#Ex. 5
base_rate = 40
price_per_km = 10
total_trip = 0
def calculate_trip_price(distance_km):
    global total_trip  # Declarăm că folosim variabila globală total_trip
    total_trip += 1  # Incrementăm contorul pentru fiecare apel al funcției
    
    # Calculăm costul total
    total_cost = base_rate + (price_per_km * distance_km)
    return total_cost

# Exemple de utilizare
print("Costul călătoriei pentru 10 km:", calculate_trip_price(10))
print("Numărul total de călătorii efectuate:", total_trip)

print("Costul călătoriei pentru 5 km:", calculate_trip_price(5))
print("Numărul total de călătorii efectuate:", total_trip)

#Ex. 6
def get_fullname(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

# Calling the function
print(get_fullname("Carmen", "Enache"))
print(get_fullname("Carmen", "Enache", "Mihaela"))

#Ex. 7
def amount_payment(payment):
    sum = 0  # Inițializăm suma datoriilor la 0
    for value in payment:
        if value >= 0:
            sum += value
        else:
            print("Valoare negativă:", value)
    return sum

# Exemplu de utilizare
indicatori = [100, -50, 200, -75, 0, 150]
print("Suma totală a datoriilor este:", amount_payment(indicatori))
    
#Ex. 8
def prepare_data(data):
    # Verificăm dacă lista are cel puțin 3 elemente pentru a putea elimina valorile extreme
    if len(data) < 3:
        print("Lista trebuie să aibă cel puțin 3 elemente pentru a elimina valorile extreme.")
        return []
    
    # Identificăm cea mai mică și cea mai mare valoare
    min_value = min(data)
    max_value = max(data)
    
    # Construim o listă care exclude toate aparițiile valorilor minime și maxime
    filtered_data = [value for value in data if value != min_value and value != max_value]
    
    # Sortăm lista rezultată
    filtered_data.sort()
    
    return filtered_data

# Exemplu de utilizare
valori = [10, 5, 3, 8, 15, 7]
rezultat = prepare_data(valori)
print("Lista modificată este:", rezultat)

#Ex. 9
def lookup_key(data, value):
    # Creăm o listă cu toate cheile care au valoarea specificată
    keys = [key for key, val in data.items() if val == value]
    return keys
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30
}
rezultat = lookup_key(data, 10)
print("Cheile care corespund valorii 10 sunt:", rezultat)

#Ex. 10
def split_list(grades):
    # Dacă lista este goală, returnăm două liste goale
    if not grades:
        return [], []
    
    # Calculăm media
    average = sum(grades) / len(grades)
    
    # Împărțim notele în funcție de medie
    below_or_equal_average = [grade for grade in grades if grade <= average]
    above_average = [grade for grade in grades if grade > average]
    
    return below_or_equal_average, above_average

# Exemplu de utilizare
notate = [85, 70, 90, 60, 75, 80]
rezultat = split_list(notate)
print("Note sub sau egale cu media:", rezultat[0])
print("Note peste medie:", rezultat[1])
        
