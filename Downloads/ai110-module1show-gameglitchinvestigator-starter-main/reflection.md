# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game was a mess from the moment I ran it. Right away I noticed players were only getting 7 guesses instead of 8, which meant someone could be one move away from winning and just get cut off. No explanation, no warning, just game over. The hints were completely gone too. Every guess went into a void with zero feedback, no go higher, no go lower, nothing. And the New Game button was basically decorative. Clicking it left everything from the last game sitting there, old score, old attempts, all of it. The only way to actually start clean was to refresh the whole page yourself.

## 2. How did you use AI as a teammate?

I used both Claude and Copilot while working through this. The most useful thing Copilot did was explain why the New Game button wasn't working. I passed it the file with #file:app.py and it spotted that the session state variables were never actually being reinitialized when the button was clicked. That was the whole problem. I verified it by clicking New Game several times in a row and watching the score and attempt count reset properly each time. But Copilot wasn't always right. When I asked it to fix the hints, its first suggestion was comparing guess ranges instead of directly checking the guess against the secret number. The hints were still wrong after that fix. I only caught it because I sat down and played through the game manually until the feedback stopped matching what I was guessing.

## 3. Debugging and testing your fixes

I had one rule: I didn't call something fixed until I saw it work in the actual running app. Code looking right on screen wasn't enough. For the attempt counter I played a full game and counted every single guess out loud until the game over screen showed up at exactly 8. For the hints I asked Copilot to generate pytest cases in test/test_game_logic.py and ran them with python3 -m pytest to confirm they passed. Copilot also nudged me to test boundary values like guessing 1 or 100, which felt unnecessary at first but ended up surfacing a small edge case I definitely would have missed otherwise.

## 4. What did you learn about Streamlit and state?

Streamlit reruns your whole script from scratch every single time someone interacts with the app. Click a button, type a number, anything at all, and Python starts over from the top. Regular variables don't survive that. They just reset. Session state is what keeps things alive between those reruns, scores, attempt counts, the secret number, all of it lives there. The way I'd explain it to someone who has never touched Streamlit: your app forgets everything the moment you interact with it, and session state is the one notebook it actually holds onto.

## 5. Looking ahead: your developer habits

Testing edge cases every single time is the habit I'm keeping. It slowed me down at first and felt like overkill, but it caught real bugs that would have made it into the final version. Going forward I also want to actually run every AI suggestion before accepting it instead of just reading through the code and assuming it's correct. That's where I got burned a few times on this project. More broadly, this changed how I see AI generated code. It moves fast and gets you most of the way there, but it doesn't know your full context and that gap is exactly where things go wrong. Someone still has to be paying attention.