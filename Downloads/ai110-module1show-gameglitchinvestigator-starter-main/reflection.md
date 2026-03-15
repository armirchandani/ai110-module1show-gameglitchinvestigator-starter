# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Honestly, the game was a mess when I first opened it. The attempt counter was wrong right away. Players only got 7 tries instead of 8, which doesn't sound like a big deal until you're one guess away from winning and the game cuts you off early. The hints were completely missing too, so there was no "go higher" or "go lower" feedback at all, just silence after every guess. And the New Game button? Clicking it did basically nothing. The old game state just sat there, which made it impossible to actually start fresh.

## 2. How did you use AI as a teammate?

I worked with Claude throughout the project. The most useful moment was when I couldn't figure out why the New Game button wasn't doing anything. Claude pointed out that I wasn't actually resetting the session state variables, just the ones I thought mattered. Once I re-initialized the right keys, the button worked. I tested it by clicking through a few new games and watching the score and attempts actually go back to zero. That said, Claude wasn't always right. At one point it gave me a hint fix that was way too vague. It was comparing ranges instead of the actual guess against the secret number. I only caught it because I played through the game manually and the hints still felt off.

## 3. Debugging and testing your fixes

My rule was simple: I didn't mark something fixed until I saw it work in the actual running app, not just in the code. For the attempt counter, I sat there and played a full game, counting each guess out loud until the game over screen hit, and it hit at 8, which was the first time it felt right. Claude helped me think about edge cases I probably would have skipped, like what happens when someone guesses exactly 1 or exactly 100. Those boundary tests ended up catching a couple of small issues I hadn't noticed before.

## 4. What did you learn about Streamlit and state?

Streamlit basically has no memory. Every time you click something or type something, the whole script reruns from scratch, and anything you stored in a regular variable just disappears. That's what session state is for. It's the one place where information actually sticks between those reruns. The way I'd explain it to a friend: picture your app forgetting everything the moment you blink, and session state is the sticky note it keeps on its desk so it doesn't lose track of what's happening.

## 5. Looking ahead: your developer habits

The habit I'm keeping is testing edge cases every single time, not just the obvious happy path. It felt tedious at first but it caught real bugs that I would have shipped otherwise. Next time I use AI on a coding project, I'm going to slow down and actually run each suggestion before moving on. I got burned a couple times by trusting the code looked right without checking if it actually worked. More than anything, this project made me realize that AI generated code needs a human in the loop. It can get you 80% of the way there, but that last 20% still requires someone who actually understands what the app is supposed to do.