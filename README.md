# Game Glitch Investigator

A Python number guessing game built with Streamlit, debugged as part of an AI-assisted coding project.

## Demo

The game generates a secret number between 1 and 100. The player has 8 attempts to guess it. After each guess the game gives a hint of go higher or go lower. The score decreases with each wrong guess. The New Game button resets everything and starts a fresh round.

## Bugs Fixed

- **Attempt limit**: The game only allowed 7 attempts instead of 8. Fixed the counter logic in logic_utils.py.
- **Missing hints**: The game showed no feedback after each guess. Fixed the hint logic to correctly return go higher or go lower based on the guess versus the secret number.
- **New Game button**: Clicking New Game did not reset the game. Fixed by reinitializing all session state variables on button click.

## Document Your Experience

### What I learned
Working through this project taught me that AI generated code needs careful human review. The bugs weren't obvious from reading the code, they only showed up when actually playing the game. I learned to test every fix manually in the live app and not just trust that the code looked right.

### How I used AI
I used Copilot and Claude to help identify bugs, generate fixes, and write pytest tests. AI was helpful for explaining why certain logic was broken, but it also gave me at least one incorrect suggestion that I had to catch and fix manually by playing through the game myself.

### How to run the project
1. Install dependencies: `python3 -m pip install -r requirements.txt`
2. Run the app: `python3 -m streamlit run app.py`
3. Run tests: `python3 -m pytest`
