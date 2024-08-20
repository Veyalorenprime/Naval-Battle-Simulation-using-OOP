#  Naval Battle Simulation

This is a Python-based naval battle simulation project that allows users to create and control various types of naval vessels, including aircraft, submarines, surface ships, and missile launchers. The simulation is designed to be a turn-based game where players can strategically maneuver their vessels and engage in combat with opposing forces.

## Features

- **Vessel Types**: The simulation supports the following vessel types:
  - Aircraft
  - Submarines
  - Frigates
  - Destroyers
  - Cruisers
  - Surface Missile Launchers
  - Air Missile Launchers
  - Torpedos Launchers
- **Vessel Attributes**: Each vessel has various attributes, such as speed, armor, weapon systems, and more.
- **Combat Mechanics**: The simulation includes combat mechanics that determine the outcome of engagements between vessels based on their attributes and positioning.
- **Game Controller**: The game can be controlled through a command-line interface or a pygame-based graphical user interface.
- **Game DAO**: The game data access object (DAO) allows for the persistence and retrieval of game data, such as player information and battle history.
- **Game Service**: The game service layer handles the core game logic, including vessel management, combat resolution, and game state management.

## Prerequisites

- Python 3.x
- pygame (for the graphical user interface)

## Installation

1. Clone the repository:
git clone https://github.com/Veyalorenprime/TP-3-4.git

2. Change to the project directory:
```bash
cd TP-3-4

3. Install the required dependencies:
```bash
pip install -r requirements.txt

## Usage

To run the game, execute the following command:
```bash
python main.py

This will launch the game and allow you to interact with the simulation through the command-line interface or the pygame-based graphical user interface.





