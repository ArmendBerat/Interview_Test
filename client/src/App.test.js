import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import App from './App';

// Test initial render (before starting the game)
test('renders welcome message and game buttons', () => {
  render(<App />);
  expect(screen.getByText('Welcome to the Game')).toBeInTheDocument();
  expect(screen.getByText('Rock, Paper, Scissors')).toBeInTheDocument();
  expect(screen.getByText('Rock, Paper, Scissors, Lizard, Spock')).toBeInTheDocument();
});

// Test starting Rock, Paper, Scissors game
test('starts Rock, Paper, Scissors game', () => {
  render(<App />);
  const rpsButton = screen.getByText('Rock, Paper, Scissors');
  fireEvent.click(rpsButton);

  expect(screen.getByText('Rock, Paper, Scissors')).toBeInTheDocument();
  expect(screen.getByText('You chose:')).toBeInTheDocument();
  expect(screen.getByText('Computer chose:')).toBeInTheDocument();
});

// Test starting Rock, Paper, Scissors, Lizard, Spock game
test('starts Rock, Paper, Scissors, Lizard, Spock game', () => {
  render(<App />);
  const rpslsButton = screen.getByText('Rock, Paper, Scissors, Lizard, Spock');
  fireEvent.click(rpslsButton);

  expect(screen.getByText('Rock, Paper, Scissors, Lizard, Spock')).toBeInTheDocument();
  expect(screen.getByText('You chose:')).toBeInTheDocument();
  expect(screen.getByText('Computer chose:')).toBeInTheDocument();
});

// Test going back to the main menu
test('goes back to the main menu', () => {
  render(<App />);
  fireEvent.click(screen.getByText('Rock, Paper, Scissors'));
  
  const backButton = screen.getByText('Back');
  fireEvent.click(backButton);

  expect(screen.getByText('Welcome to the Game')).toBeInTheDocument();
});

// Test checkbox toggle
test('checkbox toggle behavior', () => {
  render(<App />);
  const checkbox = screen.getByLabelText('Use player last choice for CPU');
  
  // Initially unchecked
  expect(checkbox.checked).toEqual(false);
  
  // Check the checkbox
  fireEvent.click(checkbox);
  expect(checkbox.checked).toEqual(true);
  
  // Uncheck the checkbox
  fireEvent.click(checkbox);
  expect(checkbox.checked).toEqual(false);
});

// Test making a move
test('makes a move and updates the result', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({
          player_choice: 'rock',
          computer_choice: 'scissors',
          result: 'win'
        }),
      })
    );
    
    render(<App />);
    fireEvent.click(screen.getByText('Rock, Paper, Scissors'));
    fireEvent.click(screen.getByText('Rock'));
  
    expect(await screen.findByText('You chose: rock')).toBeInTheDocument();
    expect(await screen.findByText('Computer chose: scissors')).toBeInTheDocument();
    expect(await screen.findByText('Result: win')).toBeInTheDocument();
  });

// Test making a move with the checkbox checked
test('makes a move with the checkbox checked and updates the result', async () => {
    // Mock the fetch response
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve({
            player_choice: 'rock',
            computer_choice: 'rock',
            result: 'draw',
          }),
      })
    );
  
    // Render the component
    render(<App />);
  
    // Check the checkbox to use player's last choice for the CPU
    fireEvent.click(screen.getByLabelText('Use player last choice for CPU'));
  
    // Start the game by selecting 'Rock, Paper, Scissors'
    fireEvent.click(screen.getByText('Rock, Paper, Scissors'));
  
    // Make the 'Rock' move
    fireEvent.click(screen.getByText('Rock'));
  
    // Verify the result is updated correctly
    expect(await screen.findByText('You chose: rock')).toBeInTheDocument();
    expect(await screen.findByText('Computer chose: rock')).toBeInTheDocument();
    expect(await screen.findByText('Result: draw')).toBeInTheDocument();
  });