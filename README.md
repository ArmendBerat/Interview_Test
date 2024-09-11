# Rock Paper Scissors

A simple web-based Rock, Paper, Scissors game with an optional variation to include Lizard and Spock. This project allows players to play against the computer, and also has a feature where the computer can reuse the player's last move.

## Features

### Game 1: Basic text based implementation 

- Text based version of the games Rock, Paper, Scissors game or an extended version with Lizard and Spock.

### Game 2: React Application with a working backend implementation

- Play the classic Rock, Paper, Scissors game or an extended version with Lizard and Spock.
- Players can choose their moves via buttons.
- A checkbox option allows the computer to reuse the player's last move in the next round.
- Results are displayed after each round (e.g., player’s choice, computer’s choice, and the outcome of the game).

## Technologies Used

- **Frontend**: React.js
- **Styling**: CSS
- **Backend**: Flask Python
- **Testing**: Jest and React Testing Library

## Getting Started

### Prerequisites

Ensure you have the following installed:

- **Node.js** (>= v14.x.x)
- **npm** (Node Package Manager)
- **Python** (>= 3.x) with **Flask** installed for the backend
- **Flask-cors** 

### Application 1

1. Navigate to the `Rock_Paper_Scissors` directory:
   ```bash
   python basic-Version.py

### Application 2

#### 
1. Navigate to the `flask-server` directory:
   ```bash
   cd flask-server

2. Start the flask server:
   ```bash
   python server.py

3. Open a new terminal and navigate to the `client` directory:
   ```bash
   cd client

4. Install the dependencies:
   ```bash
   npm install

5. Start the React component:
   ```bash
   npm start

6. If the website doesn't load automatically try:
    http://localhost:3000/

## Tests

### Testing the backend 
####
1. Navigate to the `flask-server` directory:
   ```bash
   cd flask-server

2. Install the dependencies:
  ```bash
   pip install -r requirements.txt

3. Start the flask server tests:
   ```bash
   python server_test.py

### Testing the frontend 
####
1. Open a new terminal and navigate to the `client` directory:
   ```bash
   cd client

2. Start the React component:
   ```bash
   npm test




