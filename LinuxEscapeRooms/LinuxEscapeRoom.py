import importlib
import os

# List of all modules and their friendly names
MODULES = [
    ("Space Shell Escape", "spaceshellescape"),
    ("Prison Escape", "prisonescape"),
    ("Submarine Escape", "submarineescape"),
    ("Grain Silo Escape", "grainsiloescape"),
    ("ssh: contact lost!", "sshcontactlost"),
    (" ", " "),
    ("Quit", None)
]

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*36)
    print("ROOT'S REVENGE: CHALLENGE MENU")
    print("="*36)
    for idx, (title, _) in enumerate(MODULES, 1):
        print(f"{idx}. {title}")
    while True:
        choice = input("\nSelect a challenge [1-7]: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(MODULES):
                print(f"\nYou chose: {MODULES[idx][0]}\n")
                return MODULES[idx][1]
        print("Invalid choice. Please enter a number 1-7.")

def main():
    while True:
        module_name = main_menu()
        if module_name is None:
            print("\nThanks for playing! May your logs always be clean.")
            break
        try:
            challenge_module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            print(f"Error: Could not find module '{module_name}'. Make sure the module file is present.")
            continue
        except Exception as e:
            print(f"Error importing '{module_name}': {e}")
            continue

        if hasattr(challenge_module, "challenge_intro"):
            challenge_module.challenge_intro()
        if hasattr(challenge_module, "challenge_quiz"):
            challenge_module.challenge_quiz()
        if hasattr(challenge_module, "challenge_outro"):
            challenge_module.challenge_outro()

        again = input("\nWould you like to try another challenge? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing! May your logs always be clean.")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame aborted. May the logs guide you next time.")
