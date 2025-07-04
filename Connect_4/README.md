# Connect 4 AI Game

This is a fully playable Connect 4 game with a command-line interface and an unbeatable AI opponent powered by the minimax algorithm with alpha-beta pruning.
This project hurned and grounded me on object-oriented programming, lists , time complexity and so much more. I can't wait to share in detail.


## FEATURES:
- Complete Connect 4 game engine
- The Connect4 class manages board state, move application, win detection, and heuristic scoring.
- Player classes interact with the game instance passed into them. They do not inherit from the game but use its methods directly. This classes included:
  - Human input
  - Random computer
  - Unbeatable AI using minimax

- The unbeatable AI uses minimax with alpha-beta pruning. At terminal states, it scores based on:
- Win: 1000 × number of empty spaces
- Loss: -1000 × number of empty spaces
- Draw: 0
- At depth limit: heuristic evaluation based on line patterns, for non-terminal game states. The Heuristic evaluation considers rows, columns, and diagonals, scoring based on the number of aligned AI or opponent pieces in a four-cell window.


## METHODOLOGIES ADOPTED
This project is built using a loosely coupled architecture that separates game logic from player behavior
- This promotes composition over inheritance, allowing players and logic to evolve independently.
- The approach follows key design principles such as:
  - Dependency injection
  - Interface-oriented design
  - Loose coupling
 

## WHAT YOU CAN LEARN
While building this project, I gained hands-on experience in:
- List-based algorithm design and list comprehensions
- Pattern recognition using numbers and board indexing
- Object-oriented programming, including method delegation and instance-based state handling
- Recursive algorithms, especially through minimax with alpha-beta pruning
- Designing modular, maintainable code suitable for real-world applications

## FUTURE ADD-ONS
This game engine can be wrapped in a Django web application with modern UI and interactive gameplay, by:

- Creating Django views and routes for move handling
- Rendering the board dynamically using HTML/CSS and JavaScript
- Exposing the backend logic via APIs or AJAX endpoints

How to Run

Run `game_connect_4.py` to start a round-robin match between AI and random player:
```bash
python game_connect_4.py
