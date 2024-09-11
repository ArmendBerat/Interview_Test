from flask import Flask, request, jsonify, session
from flask_cors import CORS
import random
import secrets


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

secret_key = secrets.token_hex(32)
print(secret_key)

app.secret_key = secret_key


# Define the possible choices for both games
CHOICES = {
    'rps': ['rock', 'paper', 'scissors'],
    'rpsls': ['rock', 'paper', 'scissors', 'lizard', 'spock']
}

# Define the win conditions for both games
WIN_CONDITIONS = {
    'rps': {
        'rock': ['scissors'],
        'paper': ['rock'],
        'scissors': ['paper']
    },
    'rpsls': {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissors']
    }
}

# Define the route of the play endpoint
@app.route('/play', methods=['POST'])
def play():
    data = request.json
    game_type = data.get('game_type')
    player_choice = data.get('choice')
    computer_settings = data.get('computer_randomiser')
    
    if game_type not in CHOICES:
        return jsonify({'error': 'Invalid game type'}), 400
    
    if player_choice not in CHOICES[game_type]:
        return jsonify({'error': 'Invalid choice'}), 400
    
    if computer_settings == 'false':
        computer_choice = random.choice(CHOICES[game_type])
    else:
        computer_choice = session.get('previous_choice', random.choice(CHOICES[game_type]))
    
    # computer_choice = random.choice(CHOICES[game_type])

    session['previous_choice'] = player_choice

    
    # Determine the outcome
    result = determine_winner(game_type, player_choice, computer_choice)
    
    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result
    })

# Define the function to determine the winner
def determine_winner(game_type, player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif computer_choice in WIN_CONDITIONS[game_type][player_choice]:
        return 'win'
    else:
        return 'lose'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
