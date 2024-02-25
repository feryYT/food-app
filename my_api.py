import requests

def search_recipes(query, number=5):
    api_key = "38b54c269d9041698014936f36456bdf"

    
    url = f"https://api.spoonacular.com/recipes/search?query={query}&number={number}&apiKey={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        for recipe in data['results']:
            print(f"Название: {recipe['title']}")
            print(f"ID: {recipe['id']}")
            if 'spoonacularScore' in recipe:
                print(f"Рейтинг: {recipe['spoonacularScore']}")
            else:
                print("Рейтинг: Неизвестно")
            print(f"Время приготовления: {recipe['readyInMinutes']} мин.")
            print()

    else:
        print("Ошибка при выполнении запроса.")


#search_recipes("beef")
