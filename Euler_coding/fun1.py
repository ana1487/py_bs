import random

def generate_compliment():
    adjectives = ["amazing", "brilliant", "outstanding", "legendary", "spectacular", "incredible", "stupendous"]
    qualities = ["sense of humor", "intelligence", "coding skills", "good vibes", "kind heart", "creativity"]
    animals = ["puppy", "koala", "dolphin", "unicorn", "phoenix"]

    # Generate a random compliment
    compliment = (
        f"You have the {random.choice(adjectives)} {random.choice(qualities)} of a {random.choice(animals)}!"
    )
    return compliment

def main():
    print("Welcome to the Compliment Generator! Press Enter to receive a compliment.")
    while True:
        input("Press Enter to feel awesome (or type 'exit' to quit): ")
        print(generate_compliment())
        if input("Would you like another compliment? (yes/no): ").strip().lower() == "no":
            print("Have a great day! Stay awesome!")
            break

if __name__ == "__main__":
    main()
