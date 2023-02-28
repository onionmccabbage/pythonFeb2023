# a service to access https://swapi.co/api
import requests

class SwapiService:
    def __init__(self):
        pass
    @staticmethod # callable on the Class i.e. SwapiService.getSwapi()
    def getSwapi(category='people', id=1): # no need for self this time (since its a static method)
        url = f"https://swapi.dev/api/{category}/{id}"
        print(url)
        response = requests.get(url)
        return response.text

if __name__ == "__main__":
    SwapiService().__init__()