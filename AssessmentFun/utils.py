# utils.py
import json
import os
import random
import textwrap
import time
from dataclasses import dataclass
from typing import Callable, List, Optional

# -----------------------------------------------------------------------------
# Flow-control exceptions used by assessment.py
# -----------------------------------------------------------------------------
class QuitToMenu(Exception):
    """Raised when the player chooses to quit back to the main menu."""
    pass

class SkipQuestion(Exception):
    """Raised when the player chooses to skip the current question."""
    pass

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------
@dataclass
class GameConfig:
    delay: float = 0.006                 # typing delay for slow()
    color: bool = False                  # (reserved) color output on/off
    taunts: bool = True                  # enable taunts/story beats
    shuffle_mc: bool = True              # shuffle multiple-choice answers
    reveal_answer: bool = True           # reveal correct answer after solving
    blank_line_between_questions: bool = True
    seed: Optional[int] = None           # RNG seed for deterministic runs
    debug: bool = False                  # extra traces on errors

CONFIG = GameConfig()

# -----------------------------------------------------------------------------
# Output helpers
# -----------------------------------------------------------------------------
def slow(text: str, delay: Optional[float] = None):
    """Print text slowly for dramatic effect."""
    d = CONFIG.delay if delay is None else delay
    for ch in str(text):
        print(ch, end='', flush=True)
        time.sleep(max(0.0, d))
    print()

def banner(text: str):
    text = str(text)
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def holo(title: str = "Holo‑msg"):
    slow(textwrap.dedent(f"""
       .---------------------------.
      /  /=====================\  \\
     |  |  {title:^19} |  |
      \\  \\=====================/  / 
       '---------------------------'
    """).rstrip("\n"))

def press_enter(prompt: str = "(Press Enter to continue) "):
    input(prompt)

def shell(prompt: str = "player@game:~$ ") -> str:
    """Simulates a shell prompt for user input."""
    return input(prompt).strip()

# -----------------------------------------------------------------------------
# Flavor text
# -----------------------------------------------------------------------------
ROOT_TAUNTS = [
    "\nROOT: 'You think you can out-type me? We'll see.'",
    "\nROOT: 'Hint? Go ahead. I’ll just count it against you…'",
    "\nROOT: 'You’re persistent… I almost admire it.'",
    "\nROOT: 'Ha! That was too easy. Ready for the next one?'",
    "\nROOT: 'Every mistake feeds my power… don’t slip.'",
    "\nROOT: 'Impressive. But you’re not out yet.'",
]

SYSTEM_EVENTS = [
    "\n[Warning: File permissions wobbling… Root is watching.]",
    "\n[Time dilates. A process spikes—something’s scanning your commands.]",
    "\nA cold digital wind howls. Somewhere, a cron job fails silently.",
    "\n[The terminal glitches. A phantom process whispers: Don’t trust the obvious answer.]",
    "\n[Kernel panic? Not yet. But the clock is ticking.]",
    "\n[Shadowy processes flicker in the task list…]",
]

def random_story_event():
    """Interleave taunts/events if enabled."""
    if not CONFIG.taunts:
        return
    if random.random() < 0.6:
        slow(random.choice(ROOT_TAUNTS))
    else:
        slow(random.choice(SYSTEM_EVENTS))

# -----------------------------------------------------------------------------
# Internal input normalizer
# -----------------------------------------------------------------------------
def _normalize_control(inp: Optional[str], on_hint: Optional[Callable[[], None]] = None):
    """
    Recognize hint/skip/quit tokens. On 'hint' returns 'HINT'.
    On 'skip' raises SkipQuestion. On 'quit' raises QuitToMenu.
    """
    t = (inp or "").strip().lower()

    if t in {"hint", "h", "?", "help"}:
        if on_hint:
            on_hint()
        return "HINT"

    if t in {"skip", "s", "next"}:
        raise SkipQuestion()

    if t in {"quit", "q", "exit", "menu"}:
        raise QuitToMenu()

    return None

# -----------------------------------------------------------------------------
# Multiple-choice question runner
# -----------------------------------------------------------------------------
def ask_multiple_choice(
    prompt: str,
    options: List[str],
    correct_index: int,
    explanation: str,
    *,
    qnum: int = 0,
    hint: Optional[str] = None
):
    """
    Ask a multiple-choice question with built-in hint/skip/quit handling.
    - Type 'hint' (or h/?) to view the hint (if provided)
    - Type 'skip' to raise SkipQuestion (caught by the caller)
    - Type 'quit' to raise QuitToMenu (bubble up to main menu)
    """
    # Prepare RNG for deterministic shuffling if configured
    rng = random.Random(CONFIG.seed) if CONFIG.seed is not None else random

    # Build (option, is_correct) list and shuffle if enabled
    pairs = [(opt, i == correct_index) for i, opt in enumerate(options)]
    if CONFIG.shuffle_mc:
        rng.shuffle(pairs)

    # Recompute display options and new correct index
    disp_options = [p[0] for p in pairs]
    new_correct_index = next(i for i, p in enumerate(pairs) if p[1])

    # Question loop
    while True:
        if CONFIG.blank_line_between_questions:
            print()

        slow(textwrap.dedent(str(prompt)).rstrip("\n"))
        for idx, opt in enumerate(disp_options):
            slow(f"  {chr(65 + idx)}. {opt}")

        if hint:
            slow("Type 'hint' for a clue, 'skip' to move on, or 'quit' for menu.")
        else:
            slow("Type 'skip' to move on, or 'quit' for menu.")

        # Read answer or control word
        raw = shell("Choose [A/B/C/...] or type a command: ")

        # Handle control inputs (hint/skip/quit)
        res = _normalize_control(raw, on_hint=(lambda: slow(f"\n💡 Hint: {hint}\n")) if hint else None)
        if res == "HINT":
            # after hint, loop to re-ask
            continue

        # Validate letter choice
        ans = (raw or "").strip().upper()
        valid_letters = [chr(65 + i) for i in range(len(disp_options))]

        if ans not in valid_letters:
            slow("Please enter a valid option letter (A, B, …), or type 'hint', 'skip', or 'quit'.")
            continue

        if (ord(ans) - 65) == new_correct_index:
            slow("\n✅  Correct!")
            if CONFIG.reveal_answer:
                slow(str(explanation).rstrip("\n"))
            # small beat between questions
            if CONFIG.blank_line_between_questions:
                print()
            # sprinkle flavor after some questions
            if CONFIG.taunts and qnum in {1, 3, 5, 7}:
                random_story_event()
            return  # done
        else:
            slow("\n❌  Not quite. Try again.")
            if CONFIG.taunts and random.random() < 0.25:
                random_story_event()

# -----------------------------------------------------------------------------
# JSON-driven quiz runner used by module*.py
# -----------------------------------------------------------------------------
def _load_json(path: str):
    # Resolve relative to the working dir; caller typically passes "questions/moduleX.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_quiz_from_json(path: str, after_hook: Optional[Callable[[], None]] = None):
    """
    Drives a MCQ quiz from a JSON file with fields:
      - title (str), version (int), questions (list of objects)
    Each question object supports:
      prompt, options[list], correct_index[int], explanation, (optional) hint, (optional) qnum[int], (optional) after[str]
    Special controls:
      - 'skip' raises SkipQuestion (caught here and continues)
      - 'quit' raises QuitToMenu (re-raised to bubble up to menu)
    """
    data = _load_json(path)
    title = data.get("title") or os.path.basename(path)
    if title:
        banner(str(title))

    qs = data.get("questions", [])
    for q in qs:
        try:
            ask_multiple_choice(
                prompt=q["prompt"],
                options=q["options"],
                correct_index=int(q["correct_index"]),
                explanation=q.get("explanation", ""),
                qnum=int(q.get("qnum", 0)),
                hint=q.get("hint")
            )
            # Optional per-question hook or JSON "after": "taunt"
            if after_hook:
                after_hook()
            elif q.get("after") == "taunt":
                random_story_event()

        except SkipQuestion:
            slow("⏭️  Skipped.\n")
            continue
        except QuitToMenu:
            # Bubble up so assessment.py can return to main menu
            raise

# -----------------------------------------------------------------------------
# Convenience for modules that want a single place to call quit/skip if needed
# -----------------------------------------------------------------------------
def quit_to_menu():
    raise QuitToMenu()

def skip_question():
    raise SkipQuestion()
