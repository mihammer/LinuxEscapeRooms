from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'Repositories shifting… like your answers.'",
    "\nROOT: 'rpm -qa? Query all your doubts while you’re at it.'",
    "\nROOT: 'Kernel twitchy? Same.'",
    "\nROOT: 'Update or perish. Your call.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("PACKAGE PREDICAMENT: THE UPDATE APOCALYPSE")
    slow(textwrap.dedent("""
        [Sirens blare. Packages are stale, dependencies angry.]
        ROOT: "One wrong move may nuke your OS."
    """))
    press_enter("(Press Enter to begin the Package Predicament...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module3.json", after_hook=root_taunt)

def challenge_outro():
    banner("PACKAGE PREDICAMENT SURVIVED")
    slow("ROOT: 'Patch today, panic tomorrow.'")
