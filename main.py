# main.py - An interactive, generative, text-based adventure RPG

import random

# Generative story mechanics
class StoryGenerator:
    def __init__(self):
        self.events = [
            "a mysterious fog envelops the area, obscuring your vision.",
            "you hear rustling in the bushes nearby. Someone or something is watching you.",
            "a glowing artifact catches your eye. It hums with otherworldly energy.",
            "an old traveler approaches you with a riddle and a promise of reward if you answer correctly.",
            "you stumble upon the remnants of an ancient battle, weapons and shields scattered on the ground.",
            "a distant howl sends a chill down your spine as you tread carefully through the terrain."
        ]
        self.explore_counter = 0

    def generate_event(self):
        self.explore_counter += 1
        event = random.choice(self.events)
        return f"On your exploration #{self.explore_counter}, {event}"

def game_start():
    print("Welcome to the Text Adventure RPG!")
    print("You find yourself in a mysterious land filled with adventure and danger.")
    print("Your choices will determine your fate. Choose wisely!")

def main():
    story = StoryGenerator()

    game_start()
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Rest")
        print("3. Check Stats")
        print("4. Quit")
        
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print("\nYou venture into the unknown...")
            print(story.generate_event())
        elif choice == "2":
            print("\nYou set up camp and rest for the night. Nothing unusual happens.")
        elif choice == "3":
            print("\nCharacter Stats:")
            print(f"Exploration Count: {story.explore_counter}")
        elif choice == "4":
            print("\nThank you for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()