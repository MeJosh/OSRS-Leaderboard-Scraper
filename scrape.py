import os
import urllib.parse
import requests
import datetime

# Base URL for Old School RuneScape high scores
base_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

# Name of the directory containing the player data files
data_dir = "data"

# Get a list of all directories inside the data_dir directory
characters = [name for name in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, name))]

# Get the current date in YYYY_MM_DD format
current_date = datetime.date.today().strftime('%Y_%m_%d')

# Loop through each file and scrape the player data
for character in characters:
    # Encode the player data and append it to the base URL
    url = base_url + urllib.parse.quote(character)

    # Make a request to the URL and save the response to a file
    output_filename = f"{character}_{current_date}.txt"
    output_path = os.path.join(data_dir, character, output_filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully scraped data for {character}")
    else:
        print(f"Failed to scrape data for {character}. Status code: {response.status_code}")
