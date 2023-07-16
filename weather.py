import requests
def result(city):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
    if city:
        querystring = {"q": city, "days":"7"}

    headers = {
        "X-RapidAPI-Key": "9d5a0cd825msh80de5048fcbf454p183725jsnf012abc8f146",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()



# print(result('Samarkand'))

# print(f'location: {result()["location"]["name"]}, {result()["location"]["country"]}')
# print(f'location: {result()["current"]["last_updated"]}, Now: {result()["current"]["temp_c"]}, feels like: {result()["current"]["feelslike_c"]}')