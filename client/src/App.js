import React, { useState } from 'react';
import './App.css'; // Import external stylesheet

function App() {
  // State variables
  const [game, setGame] = useState(null);
  const [gameData, setGameData] = useState({
    playerChoice: '',
    computerChoice: '',
    result: '',
  });
  const startGame = (selectedGame) => setGame(selectedGame);
  const goBack = () => {
    setGame(null);
    setGameData({ playerChoice: '', computerChoice: '', result: '' });
  };
  const [computerLastChoice, setComputerLastChoice] = useState('');

  // Fetch function
  const makeMove = async (choice) => {
    try {
      const response = await fetch(`http://localhost:5001/play`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_type: game, choice, computerLastChoice }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setGameData({
        playerChoice: data.player_choice || 'Error',
        computerChoice: data.computer_choice || 'Error',
        result: data.result || 'Error',
      });
    } catch (error) {
      console.error('Fetch error:', error);
      setGameData({ playerChoice: 'Error', computerChoice: 'Error', result: 'Error' });
    }
  };

  // Render buttons
  const renderButtons = (choices) =>
    choices.map((choice) => (
      <button
        key={choice}
        onClick={() => makeMove(choice)}
        className="game-button"
      >
        {choice.charAt(0).toUpperCase() + choice.slice(1)}
      </button>
    ));

  const renderGameChoices = () => {
    const choices = game === 'rps' ? ['rock', 'paper', 'scissors'] : ['rock', 'paper', 'scissors', 'lizard', 'spock'];
    return renderButtons(choices);
  };

  // Checkbox for CPU setting
  const handleCheckbox = (event) => {
    // console.log(event.target.checked);
    setComputerLastChoice(event.target.checked);
  }
  console.log(computerLastChoice);



  
  return (
    <div className="container">
      {game === null ? (
        <div>
          <h1>Welcome to the Game</h1>
          <div className="game-buttons">
            <button onClick={() => startGame('rps')} className="game-button">
              Rock, Paper, Scissors
            </button>
            <button onClick={() => startGame('rpsls')} className="game-button">
              Rock, Paper, Scissors, Lizard, Spock
            </button>
          </div>
          <div className='checkbox_container'>
            <input type="checkbox" id="checkbox" checked={computerLastChoice} onChange={handleCheckbox}  />
            <label htmlFor='checkbox'>Use player last choice for CPU</label>
          </div>

        </div>
      ) : (
        <div>
          <header>
            <button onClick={goBack} className="back-btn">
              Back
            </button>
          </header>
          <main id="play">
            <h1>{game === 'rps' ? 'Rock, Paper, Scissors' : 'Rock, Paper, Scissors, Lizard, Spock'}</h1>
            <div className="game-buttons">{renderGameChoices()}</div>
            <div id="result">
              <p>You chose: {gameData.playerChoice}</p>
              <p>Computer chose: {gameData.computerChoice}</p>
              <p>Result: {gameData.result}</p>
            </div>
          </main>
        </div>
      )}
    </div>
  );
}

export default App;
