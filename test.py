
import requests

API_KEY="eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjBjNDkyNjY1ZjFkZDQ3MzU5OTNiZGRiNGEwMTk2ZDZjIiwiaCI6Im11cm11cjY0In0="

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}


start_city = input("Unesite grad polaska: ")
end_city = input("Unesite grad dolaska: ")

if start_city == "" or end_city == "":
    print("Morate uneti oba grada")
    exit()



def get_coords_by_name(city):

    params = {
        "text": city
    }

    response = requests.get("https://api.openrouteservice.org/geocode/search", params=params, headers=headers)
    data = response.json()

    return data['features']


def get_distance_by_coords(coords_start, coords_end):
    body = {
        "locations": [
            coords_start,
            coords_end
        ],
        "metrics": ['distance']
    }

    response = requests.post("https://api.openrouteservice.org/v2/matrix/driving-car", json=body, headers=headers)
    data = response.json()

    return data['distances']


def choose_city_from_list(city_list):
    print("*" * 10)
    print("Please choose your city")

    seen = set()
    unique_places = []

    for place in city_list:

        key = f"{place['properties']['name']}|{place['properties']['country']}"

        if key in seen:
            continue

        seen.add(key)
        unique_places.append(place)

    for index, place in enumerate(unique_places):
        print(f"{index+1}. {place['properties']['name']} {place['properties']['country']}")

    choice = int(input("Unesite redni broj grada: "))

    if choice < 1 or choice > len(unique_places):
        print("invalid choice")
        exit()

    print("*" * 10)

    return unique_places[choice - 1]['geometry']['coordinates']

def get_selected_city(city_name):

    city_features = get_coords_by_name(city_name)

    if len(city_features) > 1:
        return choose_city_from_list(city_features)

    return city_features[0]['geometry']['coordinates']


from_city_coords = get_selected_city(start_city)
end_city_coords = get_selected_city(end_city)

distance = get_distance_by_coords(from_city_coords, end_city_coords)

print("-" * 50)
print(f"FROM: {start_city}")
print(f"TO: {end_city}")
print(f"Distance: {distance[0][1] / 1000:.2f}")
print("-" * 50)