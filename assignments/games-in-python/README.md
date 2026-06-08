# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Implement the Hangman word-guessing game in Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️	Game Core: Word Selection and Progress Display

#### Description
Create functions to choose a secret word and display the player's current progress (e.g., `_ a _ _ _`).

#### Requirements
Completed program should:

- Randomly select a word from a predefined list.
- Provide a function `display_progress(secret, guesses)` that returns the masked word showing guessed letters and underscores for missing letters.

Example:

```python
secret = 'python'
guesses = {'p', 'o'}
print(display_progress(secret, guesses))  # p _ _ _ o _
```

### 🛠️	Gameplay Loop and Input Handling

#### Description
Implement the main gameplay loop that accepts letter guesses, updates state, and ends the game on win or loss.

#### Requirements
Completed program should:

- Accept single-letter guesses from the user and validate input.
- Track and display remaining incorrect attempts (e.g., 6 starting attempts).
- End the game when the word is fully guessed or attempts are exhausted, showing a clear win/lose message.
- Avoid crashing on invalid input (numbers, multiple letters, empty input).

Example usage:

```python
play_game()
# Output: prompts for guesses, shows progress, and prints final win/lose message
```
