import requests
url = "https://jsonplaceholder.typicode.com/todos"  # Пример открытого API

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for item in data:
        print(f"ID: {item['id']}, Title: {item['title']}")
else:
    print(f"Ошибка: {response.status_code}")
