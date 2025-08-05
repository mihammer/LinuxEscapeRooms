# utils.py
import textwrap
import time
import random

def ask_shell(question, correct_cmds, explanation, hint="", reveal_answer=True):
    attempts = 0
    while True:
        cmd = input(question).strip()
        cmd_lc = cmd.lower()

        if cmd_lc == "hint":
            print(f" Hint: {hint}")
            continue

        if cmd_lc in correct_cmds or any(cmd_lc.startswith(c) for c in correct_cmds):
            print("\n  Correct!")
            print(explanation)
            break

        attempts += 1
        if attempts == 3:
            print("  Strike three! Type `skip` to move on, or `hint` for a clue.")
        elif attempts > 3:
            if cmd_lc == "skip":
                print("  Skipped.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    print(f"  The answer was: `{correct_sample}`")
                break
            else:
                print("  Wrong again. (Try `hint` or `skip`.)")
        else:
            print("  That’s not it. Try again or type `hint`.")

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

def ask_multiple_choice(prompt, options, correct_index, explanation, qnum=0):
    while True:
        slow(textwrap.dedent(prompt))
        for idx, opt in enumerate(options):
            slow(f"  {chr(65 + idx)}. {opt}")

        choice = shell("Choose [A/B/C/D]: ").upper()

        if choice in "ABCD"[:len(options)]:
            if ord(choice) - 65 == correct_index:
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
            slow("Please enter a valid option letter.\n")
