import textwrap, time, sys

# =============================================================================
# ESCAPE ROOM GAME FRAMEWORK
# -----------------------------------------------------------------------------
# This framework lets you build a CLI-based escape game using a mix of:
#   • Command-style input (simulating a Linux shell)
#   • Multiple-choice questions (A/B/C/D format)
#
# 🔧 WHAT YOU CAN CUSTOMIZE
# -----------------------------------------------------------------------------
# 1. Intro & Outro Text
#    - Update `game_intro()` and `game_outro()` for your own story or theme.
#
# 2. Challenges
#    - Add as many challenges as you like inside `main()`.
#    - Use:
#       - `ask_shell()` for shell-style prompts
#       - `ask_multiple_choice()` for quiz-style questions
#
# 3. Holo Box Display
#    - Use `holo("Title")` inside any challenge to show a stylized message box.
#
# 4. Hints & Skipping
#    - `ask_shell()` supports 'hint' and 'skip' commands.
#    - `ask_multiple_choice()` does not (by design – can be extended).
#
# 5. Custom Inventory, Scoring, Keys
#    - You can add inventory tracking if needed (see `give_key()` in other variants).
#
# Happy hacking 🧠💻
# =============================================================================


# -----------------------------------------------------------------------------
# Utility functions for output styling
# -----------------------------------------------------------------------------

def slow(text, delay=0.006):
    """Print text slowly for dramatic effect (like a typing animation)."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    """Display a centered banner with horizontal bars above and below."""
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def holo(title="Holo‑msg"):
    """Display a stylized 'holo box' title."""
    slow(rf"""
       .---------------------------.
      /  /=====================\  \
     |  |  {title:^19} |  |
      \  \=====================/  / 
       '---------------------------'
    """)

def shell(prompt="player@game:~$ "):
    """Simulates a shell prompt for user input."""
    return input(prompt).strip()


# -----------------------------------------------------------------------------
# Shell-style challenge (command-based)
# -----------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, hint="", reveal_answer=True):
    """
    Ask a shell-style question.
    - correct_cmds: set of valid commands or command starts
    - explanation: message to show on correct input
    - hint: optional clue shown on 'hint'
    - reveal_answer: whether to show answer after 'skip'
    """
    attempts = 0
    while True:
        cmd = shell(question).lower()

        if cmd == "hint":
            slow(f"💡 Hint: {hint}")
            continue

        if cmd in correct_cmds or any(cmd.startswith(c.lower()) for c in correct_cmds):
            slow("\n✅  Correct!")
            slow(explanation)
            break

        attempts += 1
        if attempts == 3:
            slow("❌  Strike three! Type `skip` to move on, or `hint` for a clue.")
        elif attempts > 3:
            if cmd == "skip":
                slow("↩️  Skipped.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Nope. Try again, or type `hint` or `skip`.")
        else:
            slow("❌  Nope. Try again or type `hint`.")


# -----------------------------------------------------------------------------
# Multiple-choice question challenge
# -----------------------------------------------------------------------------

def ask_multiple_choice(prompt, options, correct_index, explanation):
    """
    Ask a multiple-choice question.
    - prompt: The question text
    - options: List of answer choices (A, B, C, D…)
    - correct_index: Index of the correct answer (0=A, 1=B, etc.)
    - explanation: Message shown when user selects correct answer
    """
    while True:
        slow(textwrap.dedent(prompt))
        for idx, opt in enumerate(options):
            slow(f"  {chr(65 + idx)}. {opt}")

        choice = shell("Choose [A/B/C/D]: ").upper()

        if choice in "ABCD"[:len(options)]:
            if ord(choice) - 65 == correct_index:
                slow("✅  Correct!")
                slow(explanation)
                break
            else:
                slow("❌  Not quite. Try again.")
        else:
            slow("❓  Please enter a valid option letter.")


# -----------------------------------------------------------------------------
# Game intro & outro
# -----------------------------------------------------------------------------

def game_intro():
    """Show intro text and instructions."""
    banner("ESCAPE ROOM INITIATED")
    slow(textwrap.dedent("""
        You’ve awakened in a sealed environment. Solve puzzles to escape.

        🧠 Use Linux-style commands or correct answers to proceed.
        💡 Type 'hint' during shell prompts if stuck.
        ↩️  Type 'skip' to move on after 3 failed attempts (shell only).
    """))
    input("\n(Press Enter to begin…) ")

def game_outro():
    """Show game completion message."""
    banner("ESCAPE COMPLETE")
    slow("All challenges cleared. You are free! 🏆")


# -----------------------------------------------------------------------------
# Sample challenge stubs – replace these with your real puzzles
# -----------------------------------------------------------------------------

def challenge_shell_input():
    """Example shell-based challenge."""
    banner("Challenge – Terminal Prompt")
    holo("Your Mission")
    slow("Use the correct shell command to proceed.")
    ask_shell(
        question="player@escape:~$ ",
        correct_cmds={"echo success", "echo 'success'"},
        explanation="✅ Command executed successfully.",
        hint="Try using a basic `echo` command."
    )

def challenge_multiple_choice():
    """Example multiple-choice challenge."""
    banner("Challenge – Multiple Choice")
    holo("Trivia")
    ask_multiple_choice(
        prompt="""
        What is the most commonly used port for HTTPS?
        """,
        options=["21", "22", "443", "80"],
        correct_index=2,  # "443"
        explanation="Correct! Port 443 is used for secure HTTPS connections."
    )


# -----------------------------------------------------------------------------
# Game main loop
# -----------------------------------------------------------------------------

def main():
    """Main game loop – run challenges in sequence here."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    game_intro()

    # Add as many custom challenges as you'd like
    challenge_shell_input()
    challenge_multiple_choice()

    game_outro()


# -----------------------------------------------------------------------------
# Run game
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Game aborted. Better luck next boot.")
