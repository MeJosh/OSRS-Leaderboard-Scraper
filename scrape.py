import os
import urllib.parse
import requests
import datetime

# Base URL for Old School RuneScape high scores
base_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

# Name of the directory containing the player data files
data_dir = "data"

# Get a list of all files (not directories) in the data directory
files = [name for name in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, name))]

# Get the current date in YYYY_MM_DD format
current_date = datetime.date.today().strftime('%Y_%m_%d')

# Loop through each file and scrape the player data
for filename in files:
    # Load the player data from the file
    with open(os.path.join(data_dir, filename), 'r') as f:
        player_data = f.read().strip()

    # Encode the player data and append it to the base URL
    url = base_url + urllib.parse.quote(player_data)

    # Make a request to the URL and save the response to a file
    dirname = os.path.splitext(filename)[0]
    output_filename = f"{dirname}_{current_date}.txt"
    output_path = os.path.join(data_dir, output_filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully scraped data for {dirname}")
    else:
        print(f"Failed to scrape data for {dirname}. Status code: {response.status_code}")
