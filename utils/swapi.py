import requests

from utils.logger import Logger


class Swapi:
    """Methods for working with SWAPI"""

    BASE_URL = "https://swapi.info/api"

    @staticmethod
    def get_character(character_id):
        """Get character information"""

        url = f"{Swapi.BASE_URL}/people/{character_id}"

        Logger.add_request(url, "GET")

        response = requests.get(url)

        Logger.add_response(response)

        # Check that the request was successful
        assert response.status_code == 200

        return response.json()

    @staticmethod
    def get_film(film_url):
        """Get film information"""

        Logger.add_request(film_url, "GET")

        response = requests.get(film_url)

        Logger.add_response(response)

        # Check that the request was successful
        assert response.status_code == 200

        return response.json()

    @staticmethod
    def get_character_by_url(character_url):
        """Get character information by URL"""

        Logger.add_request(character_url, "GET")

        response = requests.get(character_url)

        Logger.add_response(response)

        # Check that the request was successful
        assert response.status_code == 200

        return response.json()