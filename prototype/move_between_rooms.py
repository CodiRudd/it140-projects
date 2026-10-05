"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room
current_room = 'Great Hall'

# Gameplay loop
while True:
    # 1. Display current status
    print(f"You are in the {current_room}")
    
    # 2. Prompt user for input
    command = input("Enter your move (e.g., 'go South' or 'exit'): ").strip()
    
    # Exit condition
    if command.lower() == 'exit':
        print("Thanks for playing!")
        break
    
    # Standardize input to extract direction (e.g., "go South" -> "south")
    parts = command.split()
    if len(parts) > 1 and parts[0].lower() == 'go':
        direction = parts[1].lower()
    else:
        direction = command.lower()
    
    # 3 & 4. Check if the direction is valid from the current room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
    else:
        print("You can't go that way!")
# TODO: Set the player's starting room for the simplified prototype.

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.
