# utils.py
import textwrap
import time
import random

def slow(text, delay=0.006):
    """Print text slowly for dramatic effect (like a typing animation)."""
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def holo(title="Holo-msg"):
    slow(
        "+---------------------------+\n"
        "|      {0:^19}      |\n"
        "+---------------------------+\n".format(title)
    )

def shell(prompt="player@game:~$ "):
    return input(prompt).strip()

ROOT_TAUNTS = [
    "\nROOT: 'You think you can out-type me? We'll see.'\n",
    "\nROOT: 'Hint? Go ahead. I'll just count it against you...'\n",
    "\nROOT: 'You're persistent... I almost admire it.'\n",
    "\nROOT: 'Ha! That was too easy. I hope you're ready for the next one.'\n",
    "\nROOT: 'Every mistake feeds my power... don't slip.'\n",
    "\nROOT: 'Impressive. But you're not out yet.'\n"
]

SYSTEM_EVENTS = [
    "\n[System warning: File permissions corrupting... Root is watching.]\n",
    "\n[Time dilates. A process spikes--something's scanning your commands.]\n",
    "\nA cold digital wind howls. Somewhere, a cron job fails silently.\n",
    "\n[The terminal glitches. A phantom process whispers: Don't trust the obvious answer.]\n",
    "\n[Kernel panic? Not yet. But the clock is ticking.]\n",
    "\n[Shadowy processes flicker in the task list...]\n"
]

def random_story_event():
    if random.random() < 0.6:
        slow(random.choice(ROOT_TAUNTS))
    else:
        slow(random.choice(SYSTEM_EVENTS))

def ask_multiple_choice(prompt, options, correct_index, explanation, qnum=0, hint=None):
    asked_hint = False
    while True:
        slow(textwrap.dedent(prompt))
        for idx, opt in enumerate(options):
            slow(f"  {chr(65 + idx)}. {opt}")

        slow("Type 'hint' for a clue or 'skip' to move on.")
        user_input = shell("Choose [A/B/C/D] or type 'hint'/'skip': ").strip().upper()

        if user_input == "HINT" and hint:
            slow(f"\n💡 Hint: {hint}\n")
            asked_hint = True
            continue

        if user_input == "SKIP":
            slow("\n⏩ Question skipped.\n")
            banner("Next Challenge")
            break

        if user_input in "ABCD"[:len(options)]:
            if ord(user_input) - 65 == correct_index:
                slow("Correct!")
                slow(explanation)
                slow("\n")
                banner("Next Challenge")
                if qnum in [1, 3, 5, 7]:
                    random_story_event()
                break
            else:
                slow("Not quite. Try again.\n")
                if random.random() < 0.25:
                    slow(random.choice(ROOT_TAUNTS))
        else:
            slow("Please enter a valid option letter, 'hint', or 'skip'.\n")


