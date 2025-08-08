# assessment.py
import importlib
import os

# Pull everything we actually use from utils
from utils import (
    CONFIG, banner, slow, shell, press_enter,
    QuitToMenu
)

# -----------------------------
# SETTINGS
# -----------------------------
def settings_menu():
    while True:
        banner("Settings")
        slow(f"Typing delay: {CONFIG.delay}")
        slow(f"Color: {'on' if CONFIG.color else 'off'}")
        slow(f"Taunts: {'on' if CONFIG.taunts else 'off'}")
        slow(f"Shuffle MC: {'on' if CONFIG.shuffle_mc else 'off'}")
        slow(f"Reveal answers: {'on' if CONFIG.reveal_answer else 'off'}")
        slow(f"Blank line spacing: {'on' if CONFIG.blank_line_between_questions else 'off'}")
        slow(f"Seed: {CONFIG.seed if CONFIG.seed is not None else '(none)'}")
        slow("\nCommands: delay <n>, color on/off, taunts on/off, shuffle on/off, "
             "reveal on/off, spacing on/off, seed <int>, back")

        cmd = shell("settings> ").strip().lower()
        if cmd == "back":
            break
        elif cmd.startswith("delay "):
            try:
                CONFIG.delay = max(0.0, float(cmd.split()[1]))
            except ValueError:
                slow("Invalid delay.")
        elif cmd in {"color on", "color off"}:
            CONFIG.color = cmd.endswith("on")
        elif cmd in {"taunts on", "taunts off"}:
            CONFIG.taunts = cmd.endswith("on")
        elif cmd in {"shuffle on", "shuffle off"}:
            CONFIG.shuffle_mc = cmd.endswith("on")
        elif cmd in {"reveal on", "reveal off"}:
            CONFIG.reveal_answer = cmd.endswith("on")
        elif cmd in {"spacing on", "spacing off"}:
            CONFIG.blank_line_between_questions = cmd.endswith("on")
        elif cmd.startswith("seed "):
            try:
                CONFIG.seed = int(cmd.split()[1])
            except ValueError:
                slow("Seed must be an integer (e.g., seed 42).")
        else:
            slow("Unknown command.")

# -----------------------------
# MODULE MENU
# -----------------------------
MODULES = [
    ("Module 1 Linux OS Fundamentals", "module1"),
    ("Module 2 Linux OS Fundamentals", "module2"),
    ("Module 3 Package Management", "module3"),
    ("Module 4 Linux On Azure", "module4"),
    ("Module 5 Network Concepts", "module5"),
    ("Module 6 Storage Concepts", "module6"),
    ("Settings", "__settings__"),
    ("Quit", None),
]

def main_menu(clear=True):
    if clear:
        os.system('cls' if os.name == 'nt' else 'clear')
    print("="*36)
    print("ROOT'S REVENGE: CHALLENGE MENU")
    print("="*36)
    for idx, (title, _) in enumerate(MODULES, 1):
        print(f"{idx}. {title}")
    while True:
        choice = input("\nSelect a challenge [1-8]: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(MODULES):
                print(f"\nYou chose: {MODULES[idx][0]}\n")
                return MODULES[idx][1]
        print("Invalid choice. Please enter a number 1-8.")

# -----------------------------
# MAIN
# -----------------------------
def main():
    # Welcome (pause so it isn't wiped by main_menu's clear)
    banner("WELCOME TO ROOT'S REVENGE – LINUX ESCAPE ROOM")
    slow("Test your Linux skills against ROOT’s devious challenges.\n")
    press_enter("(Press Enter to open the Challenge Menu) ")

    first_draw = True
    while True:
        module_name = main_menu(clear=not first_draw)  # don't clear the very first time we show it
        first_draw = False

        if module_name is None:
            print("\nThanks for playing! May your logs always be clean.")
            break

        if module_name == "__settings__":
            settings_menu()
            continue

        try:
            challenge_module = importlib.import_module(module_name)

            if hasattr(challenge_module, "challenge_intro"):
                challenge_module.challenge_intro()
            if hasattr(challenge_module, "challenge_quiz"):
                challenge_module.challenge_quiz()
            if hasattr(challenge_module, "challenge_outro"):
                challenge_module.challenge_outro()

        except QuitToMenu:
            slow("\n↩️  Back to main menu.\n")
            continue
        except Exception as ex:
            slow(f"\n⚠️  An error occurred in {module_name}: {ex}")
            if getattr(CONFIG, "debug", False):
                import traceback
                traceback.print_exc()
            press_enter("(Press Enter to return to the main menu) ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame aborted. May the logs guide you next time.")
