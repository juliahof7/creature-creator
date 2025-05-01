# main.py

# import functions as other files
from creature import create_hybrid_creature
from graphics import show_graphic

def main():
    print("Welcome to the Creature Creator!")

    # get the user input for 2 creatures
    creature1 = input("Enter the name of the first creature: ").strip()
    creature2 = input("Enter the name of the second creature: ").strip()

    if not creature1 or not creature2:
        print("Both creature names are required!")
        return
    # generate the hybrid creature with a random name and stats
    hybrid = create_hybrid_creature(creature1, creature2)

    # display the creature info in the terminal    
    print("\nYour new creature has been created!")
    print(f"Name: {hybrid['name']}")
    print(f"Weight: {hybrid['weight']} lbs")
    print(f"Diet: {hybrid['diet']}")

    # show confirmation graphic using tkinter
    show_graphic(hybrid['name'])

if __name__ == "__main__":
    main()