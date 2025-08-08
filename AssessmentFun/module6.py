from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'Is your disk full, or just your mind?'",
    "\nROOT: 'I swapped your swap. Enjoy the thrash.'",
    "\nROOT: 'UUID? More like U-R-stuck.'",
    "\nROOT: 'Mount failure? Try hope -a.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("STORAGE: ROOT OF ALL SPACE PROBLEMS")
    slow(textwrap.dedent("""
        [Inodes dwindle. Blocks groan. fstab stares back silently.]
        ROOT: "df -h won’t save you now."
    """))
    press_enter("(Press Enter to face the storage boss...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module6.json", after_hook=root_taunt)

def challenge_outro():
    banner("STORAGE BOSS: SPACE RECLAIMED")
    slow("ROOT: 'Mounted a defense? I never truly unmount.'")
