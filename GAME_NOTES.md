# Running the original Pygame game

The game was created for Python 3.11 with Pygame. From the `snake-game` directory, install the dependency and run the script **with `game` as the working directory**, because the original code loads art and audio with relative paths:

```bash
python -m pip install -r requirements.txt
cd game
python main.py
```

Choose Easy, Medium, or Hard from the Start menu. Player 1 uses the arrow keys and Player 2 uses W, A, S, and D. Collect apples to grow and increase your displayed score. The medium level adds a poison apple; the hard level also displays a golden apple. After a game over, press Enter to play again or Escape to return to level selection.

This is a desktop Pygame application. The files in `game/` are the final project with minimal portability and privacy fixes: student ID numbers were removed, asset names were normalized, and Python 3 exception raising was corrected. The original third-party display font was replaced by Pygame's built-in font because its embedded terms do not clearly permit redistribution.
