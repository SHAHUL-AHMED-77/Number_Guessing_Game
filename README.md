
# Number Guessing Game

This is a simple Python-based Number Guessing Game where the player has to guess a randomly generated number within a specified range. The number of attempts is limited based on the range size, ensuring a challenging yet fair gameplay experience.

## How It Works

1. The player is prompted to enter a lower and an upper bound to define the range.
2. A random number is generated within this range.
3. The player is informed of the maximum number of attempts they have to guess the number.
4. The player then guesses the number, and the program provides feedback:
   - If the guess is too low, the program will prompt "Too Low, Try Again!"
   - If the guess is too high, the program will prompt "Too High, Try Again!"
   - If the guess is correct, the program will congratulate the player and end the game.
5. The game continues until the player guesses the number or runs out of attempts.

## How to Run

1. Clone this repository.
2. Navigate to the directory where the game file is located.
3. Run the game using the command:
   ```bash
   python number_guessing_game.py
   ```
4. Follow the on-screen prompts to play the game.

## Sample Output

```
Enter Lower Bound Number: 1
Enter Upper Bound Number: 100
You have 7 chances to guess the number.
Guess the Number: 50
Too Low, Try Again!
Guess the Number: 75
Too High, Try Again!
Guess the Number: 60
Too High, Try Again!
Guess the Number: 55
Too Low, Try Again!
Guess the Number: 57
Too High, Try Again!
Guess the Number: 56
Congratulations!!! You Guessed It Correctly in 6 tries.
```

## Customization

You can easily customize the game by adjusting the range or by modifying the number of attempts allowed. This can be done by changing the logic in the code.

## Dependencies

This game is implemented using Python's built-in libraries:
- `random` for generating random numbers
- `math` for calculating the number of chances

No additional libraries are required.

## License
 Not Licensed

