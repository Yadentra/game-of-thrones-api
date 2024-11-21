from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

# Example list with 70 characters (replace this with your actual list of 70 characters)
characters = [
    {"id": 1, "name": "Jon Snow"},
    {"id": 2, "name": "Daenerys Targaryen"},
    {"id": 3, "name": "Tyrion Lannister"},
    {"id": 4, "name": "Arya Stark"},
    {"id": 5, "name": "Cersei Lannister"},
    {"id": 6, "name": "Jaime Lannister"},
    {"id": 7, "name": "Sansa Stark"},
    {"id": 8, "name": "Robb Stark"},
    {"id": 9, "name": "Bran Stark"},
    {"id": 10, "name": "Jorah Mormont"},
    {"id": 11, "name": "Samwell Tarly"},
    {"id": 12, "name": "Petyr Baelish"},
    {"id": 13, "name": "Varys"},
    {"id": 14, "name": "The Hound (Sandor Clegane)"},
    {"id": 15, "name": "The Mountain (Gregor Clegane)"},
    {"id": 16, "name": "Brienne of Tarth"},
    {"id": 17, "name": "Stannis Baratheon"},
    {"id": 18, "name": "Melisandre"},
    {"id": 19, "name": "Tormund Giantsbane"},
    {"id": 20, "name": "Gendry"},
    {"id": 21, "name": "Davos Seaworth"},
    {"id": 22, "name": "Grey Worm"},
    {"id": 23, "name": "Missandei"},
    {"id": 24, "name": "Ramsay Bolton"},
    {"id": 25, "name": "Theon Greyjoy"},
    {"id": 26, "name": "Yara Greyjoy"},
    {"id": 27, "name": "Euron Greyjoy"},
    {"id": 28, "name": "Balon Greyjoy"},
    {"id": 29, "name": "Olenna Tyrell"},
    {"id": 30, "name": "Margaery Tyrell"},
    {"id": 31, "name": "Loras Tyrell"},
    {"id": 32, "name": "Tywin Lannister"},
    {"id": 33, "name": "Kevan Lannister"},
    {"id": 34, "name": "Lancel Lannister"},
    {"id": 35, "name": "Bronn"},
    {"id": 36, "name": "Daario Naharis"},
    {"id": 37, "name": "Jaqen H'ghar"},
    {"id": 38, "name": "Hodor"},
    {"id": 39, "name": "Benjen Stark"},
    {"id": 40, "name": "Rickon Stark"},
    {"id": 41, "name": "Oberyn Martell"},
    {"id": 42, "name": "Ellaria Sand"},
    {"id": 43, "name": "The Sand Snakes"},
    {"id": 44, "name": "Asha Greyjoy"},
    {"id": 45, "name": "Joffrey Baratheon"},
    {"id": 46, "name": "Myrcella Baratheon"},
    {"id": 47, "name": "Tommen Baratheon"},
    {"id": 48, "name": "Shae"},
    {"id": 49, "name": "Missandei"},
    {"id": 50, "name": "Drogon"},
    {"id": 51, "name": "Rhaegal"},
    {"id": 52, "name": "Viserion"},
    {"id": 53, "name": "Bendrix of the Ironborn"},
    {"id": 54, "name": "Quentyn Martell"},
    {"id": 55, "name": "Gilly"},
    {"id": 56, "name": "Tormund Giantsbane"},
    {"id": 57, "name": "Jon Snow (Aegon Targaryen)"},
    {"id": 58, "name": "Bran Stark (Greenseer)"},
    {"id": 59, "name": "Eddard Stark"},
    {"id": 60, "name": "Catelyn Stark"},
    {"id": 61, "name": "Rickard Stark"},
    {"id": 62, "name": "Benjen Stark"},
    {"id": 63, "name": "Robb Stark"},
    {"id": 64, "name": "Hodor (Wylis)"},
    {"id": 65, "name": "Gendry Waters"},
    {"id": 66, "name": "Bittersteel"},
    {"id": 67, "name": "House Targaryen Lords"},
    {"id": 68, "name": "House Baratheon Lords"},
    {"id": 69, "name": "House Lannister Lords"},
    {"id": 70, "name": "House Stark Lords"}
]

# Home route
@main_routes.route('/')
def home():
    return jsonify(message="Welcome to Game of Thrones API")

# Route for characters
@main_routes.route('/characters')
def get_characters():
    return jsonify(characters)

# Route for a specific character by ID
@main_routes.route('/characters/<int:id>')
def get_character(id):
    # Find the character by ID
    character = next((char for char in characters if char["id"] == id), None)
    if character:
        return jsonify(character)
    else:
        return jsonify({"message": "Character not found"}), 404