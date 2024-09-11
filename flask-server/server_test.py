import unittest
from unittest.mock import patch
import json
from server import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # This is run before each test. It sets up the test client.
        self.client = app.test_client()
        self.client.testing = True  # Set testing mode to True

    # Tests for the Rock-Paper-Scissors game
    def test_valid_rps_game(self):
        response = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "rps",
                "choice": "rock",
                "computer_randomiser": "false"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)  # Check if status code is OK
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('player_choice', data)
        self.assertIn('computer_choice', data)
        self.assertIn('result', data)
        self.assertIn(data['player_choice'], ['rock', 'paper', 'scissors'])
        self.assertIn(data['computer_choice'], ['rock', 'paper', 'scissors'])
        self.assertIn(data['result'], ['win', 'lose', 'draw'])

    # Tests for the invalid game type
    def test_invalid_game_type(self):
        response = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "invalid_game",
                "choice": "rock",
                "computer_randomiser": "false"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)  # Should return a 400 status code for invalid game
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid game type')

    # Tests for the invalid choice
    def test_invalid_choice(self):
        """Test for invalid choice in a valid game type"""
        response = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "rps",
                "choice": "invalid_choice",
                "computer_randomiser": "false"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)  # Should return a 400 status code for invalid choice
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid choice')

    # Tests for the computer remembering the last choice
    def test_computer_remembers_choice(self):
        # First round: Play rock, random CPU choice
        response1 = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "rps",
                "choice": "rock",
                "computer_randomiser": "false"
            }),
            content_type='application/json'
        )
        data1 = json.loads(response1.get_data(as_text=True))
        self.assertEqual(response1.status_code, 200)

        # Second round: Play rock again, computer should pick previous choice (rock)
        response2 = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "rps",
                "choice": "paper",
                "computer_randomiser": "true"
            }),
            content_type='application/json'
        )
        data2 = json.loads(response2.get_data(as_text=True))
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(data2['computer_choice'], 'rock')  # CPU should remember previous choice (rock)

    # Tests for the win condition
    def test_win_condition(self):
        with patch('random.choice', return_value='scissors'):  # Computer chooses scissors
            response = self.client.post(
                '/play',
                data=json.dumps({
                    "game_type": "rps",
                    "choice": "rock",
                    "computer_randomiser": "false"
                }),
                content_type='application/json'
            )
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['player_choice'], 'rock')
            self.assertEqual(data['computer_choice'], 'scissors')
            self.assertEqual(data['result'], 'win')

    # Tests for the lose condition
    def test_lose_condition(self):
        """Test lose condition for player"""
        with patch('random.choice', return_value='paper'):  # Computer chooses paper
            response = self.client.post(
                '/play',
                data=json.dumps({
                    "game_type": "rps",
                    "choice": "rock",
                    "computer_randomiser": "false"
                }),
                content_type='application/json'
            )
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['player_choice'], 'rock')
            self.assertEqual(data['computer_choice'], 'paper')
            self.assertEqual(data['result'], 'lose')

    # Tests for the draw condition
    def test_draw_condition(self):
        """Test draw condition when player and computer choose the same"""
        with patch('random.choice', return_value='rock'):  # Computer chooses paper
            response = self.client.post(
                '/play',
                data=json.dumps({
                    "game_type": "rps",
                    "choice": "rock",
                    "computer_randomiser": "false"
                }),
                content_type='application/json'
                )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['player_choice'], 'rock')
        self.assertEqual(data['computer_choice'], 'rock')  # Assuming rock is randomly chosen for both
        self.assertEqual(data['result'], 'draw')

    # Tests for the Rock-Paper-Scissors-Lizard-Spock game
    def test_rpsls_lizard_spock(self):
        """Test Lizard-Spock game interactions"""
        response = self.client.post(
            '/play',
            data=json.dumps({
                "game_type": "rpsls",
                "choice": "lizard",
                "computer_randomiser": "false"
            }),
            content_type='application/json'
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIn(data['player_choice'], ['rock', 'paper', 'scissors', 'lizard', 'spock'])
        self.assertIn(data['computer_choice'], ['rock', 'paper', 'scissors', 'lizard', 'spock'])
        self.assertIn(data['result'], ['win', 'lose', 'draw'])

            

if __name__ == '__main__':
    unittest.main()
