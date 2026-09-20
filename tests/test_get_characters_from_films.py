from utils.swapi import Swapi


class TestCharacterFilms:
    """Get characters who appeared in the same films as the selected character"""

    def test_get_characters_from_films(self):
        """Get characters from all films of the selected character and save them to a file"""

        # Character configuration
        character_id = 4
        target_character_name = "Darth Vader"
        file_name = "vader_characters.txt"

        print(f"Character ID: {character_id}")
        print(f"Character name: {target_character_name}")

        # Get character information
        character = Swapi.get_character(character_id)
        print(f"Data for {target_character_name} was retrieved successfully")

        # Get the list of films in which the character appeared
        film_urls = character.get("films")
        print(f"Number of films for {target_character_name}: {len(film_urls)}")

        # Use a set to avoid duplicate character names
        characters = set()

        # Get characters from each film
        for film_url in film_urls:
            print(f"Getting film data: {film_url}")

            film = Swapi.get_film(film_url)
            film_title = film.get("title")
            print(f"Film: {film_title}")

            # Get character URLs from the film
            character_urls = film.get("characters")
            print(f"Number of characters in the film: {len(character_urls)}")

            # Get the name of each character
            for character_url in character_urls:
                character = Swapi.get_character_by_url(character_url)
                character_name = character.get("name")

                # Add the name to the set
                characters.add(character_name)

        # Save character names to a file
        with open(file_name, "w", encoding="utf-8") as file:
            for character_name in sorted(characters):
                file.write(character_name + "\n")

        print(f"Total unique characters: {len(characters)}")
        print(f"All characters were saved to {file_name}")