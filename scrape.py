import os
import urllib.parse
import requests
import datetime

# Base URL for Old School RuneScape high scores
base_url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player="

# Name of the directory containing the player data files
data_dir = "data"

# Get a list of all directories in the data directory
dirs = [name for name in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, name))]

# Get the current date in YYYY_MM_DD format
current_date = datetime.date.today().strftime('%Y_%m_%d')

# Loop through each directory and scrape the player data
for dirname in dirs:
    # Load the player data from the file
    with open(os.path.join(data_dir, dirname), 'r') as f:
        player_data = f.read().strip()

    # Encode the player data and append it to the base URL
    url = base_url + urllib.parse.quote(player_data)

    # Make a request to the URL and save the response to a file
    filename = os.path.join(data_dir, f"{dirname}_{current_date}.txt")
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
