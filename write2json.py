#writing to json

import json

my_data = {
    'wins': 5,
    'losses': 4,
    'ties': 3,
    'games': 12,
}

with open('gamestats.json', 'w') as json_file:
    json.dump(my_data, json_file)