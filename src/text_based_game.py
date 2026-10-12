# Codi Rudd
# IT-140 Project Two: Text-Based Game

def show_instructions():
    """Print the game title, objective, and available commands."""
    print("--------------------------------------")
    print("Welcome to the Castle Text Adventure Game!")
    print("Collect all 6 items to win, or face the villain unprepared.")
    print("--------------------------------------")
    print("Move commands: go north, go south, go east, go west")
    print("Add to Inventory: get [item name]")
    print("Exit game: exit")
    print("--------------------------------------")

def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and visible items."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    
    # Check if there is an item in the current room and display it
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        # Only show the item if it hasn't been picked up yet
        if item not in inventory:
            print(f"You see a {item}")
    print("-" * 38)

def main():
    # A dictionary linking a room to other rooms and an item for each room
    rooms = {
        'Great Hall': {
            'south': 'Bedroom', 
            'north': 'Dungeon', 
            'east': 'Kitchen', 
            'west': 'Library'
        },
        'Bedroom': {
            'north': 'Great Hall', 
            'east': 'Cellar', 
            'item': 'Armor'
        },
        'Cellar': {
            'west': 'Bedroom', 
            'item': 'Helmet'
        },
        'Dungeon': {
            'south': 'Great Hall', 
            'item': 'Sword'
        },
        'Library': {
            'east': 'Great Hall', 
            'item': 'Shield'
        },
        'Kitchen': {
            'west': 'Great Hall', 
            'east': 'Gallery', 
            'item': 'Potion'
        },
        'Gallery': {
            'west': 'Kitchen', 
            'item': 'Key'
        },
        'Throne Room': {
            'west': 'Dungeon', 
            'item': 'Dragon'  # Villain room
        }
    }

    # Initialize game variables
    current_room = 'Great Hall'
    inventory = []
    total_items = 6  # Total number of collectible items in the game

    # Show instructions at the start of the game
    show_instructions()

    # Main gameplay loop
    while True:
        # Display player status and current room item
        show_status(current_room, inventory, rooms)

        # Prompt user for input
        command = input("Enter your move: ").strip()

        # Handle exit condition
        if command.lower() == 'exit':
            print("Thanks for playing!")
            break

        # Standardize input by splitting into parts
        parts = command.split()
        
        if len(parts) == 0:
            print("Invalid input. Please enter a valid command.")
            continue

        action = parts[0].lower()

        # Handle movement commands
        if action == 'go':
            if len(parts) > 1:
                direction = parts[1].lower()
                # Check if direction exists in the current room's links
                found_direction = None
                for key in rooms[current_room]:
                    if key.lower() == direction:
                        found_direction = key
                        break

                if found_direction:
                    current_room = rooms[current_room][found_direction]
                    
                    # Check if the player entered the villain room
                    if "item" in rooms[current_room] and rooms[current_room]["item"] == "Dragon":
                        if len(inventory) == total_items:
                            print("\nCongratulations! You have collected all items and defeated the dragon!")
                        else:
                            print("\nNOM NOM...GAME OVER! You faced the dragon without all the required items.")
                        print("Thanks for playing the game. Hope you enjoyed it.")
                        break
                else:
                    print("You can't go that way!")
            else:
                print("Specify a direction to go (e.g., 'go north').")

        # Handle item pickup commands
        elif action == 'get':
            if len(parts) > 1:
                # Reconstruct item name in case it has multiple words
                item_name = " ".join(parts[1:]).title()
                
                # Check if room has an item and if it matches the requested item
                if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == item_name.lower():
                    actual_item = rooms[current_room]["item"]
                    if actual_item not in inventory:
                        inventory.append(actual_item)
                        print(f"You picked up the {actual_item}!")
                    else:
                        print("You already have this item.")
                else:
                    print(f"Can't get {item_name}!")
            else:
                print("Specify an item to get (e.g., 'get Sword').")
        else:
            print("Invalid command! Use 'go [direction]' or 'get [item]'.")

# Run the main function
if __name__ == "__main__":
    main()
