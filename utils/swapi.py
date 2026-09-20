import requests


class Swapi:
    """Методы для работы с SWAPI"""

    BASE_URL = "https://swapi.info/api"

    @staticmethod
    def get_character(character_id):
        """Получаем информацию о персонаже"""

        url = f"{Swapi.BASE_URL}/people/{character_id}"
        response = requests.get(url)

        assert response.status_code == 200

        return response.json()

    @staticmethod
    def get_film(film_url):
        """Получаем информацию о фильме"""

        response = requests.get(film_url)

        assert response.status_code == 200

        return response.json()

    @staticmethod
    def get_character_by_url(character_url):
        """Получаем информацию о персонаже по URL"""

        response = requests.get(character_url)

        assert response.status_code == 200

        return response.json()