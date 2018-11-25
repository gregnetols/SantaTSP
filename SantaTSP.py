import pandas as pd


df_cities = pd.read_csv("cities_test.csv")
list_cities = df_cities.values.tolist()
list_cities = [ [int(city[0]), float(city[1]), float(city[2])] for city in list_cities]
print(len(list_cities))

def build_prime_dict(integers):
    # create dictionary of which cities are prime for quick lookup
    primes = {}
    for a in integers:
        if all( a % i for i in xrange(2, a)): # a is prime if for all integers i between 2 and a the a/i is not 0
            primes[a] = 1
        else:
            primes[a] = 0
    return primes

def build_location_dict(cities):
    # Builds a dictionary of city x, y coordinates indexed by city number
    city_locations = {}
    for city in cities:
        city_locations[city[0]] = {'x':city[1], 'y':city[2]}
    return city_locations

def distance_euc(city_a_idx, city_b_idx):
    #computes euclidean distance between two cities
    ax, ay = city_location[city_a_idx].values()
    bx, by = city_location[city_b_idx].values()
    return ((bx - ax)**2 + (by - ay)**2)**(0.5)

def score_path(path):
    step_number = 1
    score = 0
    for idx, city_a in enumerate(path):
        city_b = path[idx+1]

        modifier = 1.0
        if step_number % 10 == 0 and not prime_cities[city_a]:
            modifier = 1.1

        score = score + distance_euc(city_a, city_b) * modifier

        if city_b == 0:
            return score


prime_cities = build_prime_dict([city[0] for city in list_cities])
print("primes found")
city_location = build_location_dict(list_cities)
print(city_location[0])
test_distance = distance_euc(0,1)
print(test_distance)


test_path = [city[0] for city in list_cities] + [0]
print(test_path)

test_score = score_path(test_path)
print(test_score)




