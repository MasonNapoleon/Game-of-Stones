# 🪨 Game of Stones 🪨
**A game where whoever takes the last stone wins!**

## About this game:
- You can only take 1 - 3 stones each turn
- The computer is smart and knows how to win
- Pick to go first or second
```
if num_stones %4 != 0:
        computers_stones_removed += num_stones %4
    else:
        computers_stones_removed += random.randint(1, 3)
    num_stones -= computers_stones_removed
```
## Overview
The Game of Stones is based on the game Nim, also known as The Substraction Game, where two players take turns removing 1, 2, or 3 objects from a pile. It's a very simple game, with the earliest known evidence of this game being in 16th century China. However, many don't know that if played well enough, there will always be a winner.

## How to win
The logic to always win is taking away enough stones to make the remaining number of stones a multiple of 4. The mathematical logic for this is dividing by the highest amount you can take plus 1, and taking the remainder.\
Other variations of this game may include taking more than 3 stones, but the logic is still the same. If you can take up to 4 stones, take away stones to make the remaining a multiple of 5. If you can take 5, take away enough to make it a multiple of 6.
```
The computer removed 3 stones.

The computer took the last stone and now there are 0 stones remaining. The computer beat you! NOOOOOOOOOO :(
```
---
---
### 👨‍💻 Independently developed by Mason Napoleon 👨‍💻
---
---
