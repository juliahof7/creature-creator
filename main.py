# main.py

from creature import create_hybrid_creature
from graphics import show_graphic

def main():
    print("Welcome to the Creature Creator!")
    creature1 = input("Enter the name of the first creature: ").strip()
    creature2 = input("Enter the name of the second creature: ").strip()

    hybrid = create_hybrid_creature(creature1, creature2)

    print("\nYour new creature has been created!")
    print(f"Name: {hybrid['name']}")
    print(f"Weight: {hybrid['weight']} lbs")
    print(f"Diet: {hybrid['diet']}")

    show_graphic(hybrid['name'])

if __name__ == "__main__":
    main()
    
# This code is a simple creature creation program that combines two creature names, generates random stats, and displays the result in a GUI.
# It uses the `creature.py` module to handle the logic of creating hybrid names and generating stats, and the `graphics.py` module to create a GUI for displaying the results.