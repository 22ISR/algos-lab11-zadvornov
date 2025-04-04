import requests
import json


# response = requests.get("http://www.omdbapi.com/?apikey=505480d7&s=Joker")
# if response.status_code == 200:
#     print(response.json())  # {'name': 'michael', 'age': 40, 'count': 12345}


# json_data = '{"name": "Alice", "age": 25}'
# data = json.loads(json_data)  # Преобразование строки JSON в словарь
# print(data["name"])  # Alice

while True:
    command = input("Enter command (or 'exit' to quit): ")
    if command.lower() == "exit":
        print("Goodbye!")
        break
    base_url = "http://www.omdbapi.com/"
    API_KEY = "505480d7"
    full_url = f"{base_url}?apikey={API_KEY}&s={command}"

    response = requests.get(full_url)
    data = response.json()
    
    if data["Response"] == "True":
        for movie in data["Search"]:
            print(f"Название: {movie['Title']}, Год: {movie['Year']}, Тип: {movie['Type']}")
    else:
        print("No movies found.")

    # response = requests.get(full_url)
    # # data_json = response.json()
    # #data_dumps = json.dumps(response.json())
    # data = json.loads(data_dumps)
    # # print(data)
    # for movie in data:
    # print(f"Название: {data['Title']}, Год: {data['Year']}, Тип: {data['Type']}")
        

# print(data["Title"])
    # if response.status_code == 404:
    #     print("Error: Not Found")
    # elif response.status_code == 200:
    #     print("Success:", response.json())



# response = requests.get("http://www.omdbapi.com/data")
# if response.status_code == 404:
#     print("Error: Not Found")
# elif response.status_code == 200:
#     print("Success:", response.json())


# movies = [
#     {"Title": "Inception", "Year": "2010"},
#     {"Title": "The Matrix", "Year": "1999"},
# ]

# for movie in movies:
#     print(f"🎬 {movie['Title']} ({movie['Year']})")