# Asteroids

A classic Asteroids game clone built with Python and Pygame.

## Description

This project is a simple implementation of the Asteroids arcade game. Players control a spaceship, navigation through an asteroid field, destroying asteroids while avoiding collisions.

## Requirements

- Python >= 3.13
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- pygame

## Installation

1. Clone the repository.
2. Install dependencies using `uv`:

   ```bash
   uv sync
   ```

   Alternatively, you can install the dependencies manually:

   ```bash
   pip install pygame
   ```

## Usage

To start the game, run:

```bash
uv run main.py
```

Or if you are running it directly with python:

```bash
python3 main.py
```

## Controls

- **W**: Move Forward
- **S**: Move Backward
- **A**: Rotate Left
- **D**: Rotate Right
- **SPACE**: Shoot
- **Close Window**: Quit Game

## Project Structure

- `main.py`: The main entry point of the game. Handles the game loop and rendering.
- `player.py`: Defines the `Player` class, handling movement and shooting logic.
- `asteroid.py`: Defines the `Asteroid` class and its splitting behavior.
- `shot.py`: Defines the `Shot` class for projectiles.
- `asteroidfield.py`: Manages the spawning of asteroids.
- `constants.py`: Contains game configuration constants (screen size, speeds, etc.).
- `logger.py`: Handles game state and event logging to JSONL files.
- `circleshape.py`: Base class for circular game objects.
