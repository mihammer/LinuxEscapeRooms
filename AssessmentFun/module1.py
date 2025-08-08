from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'Welcome to my terminal. Try not to trip over /bin.'",
    "\nROOT: 'GRUB got you? Chew carefully.'",
    "\nROOT: 'Permissions look… *permissive*. Bold.'",
    "\nROOT: 'More v’s, more truth. Or more pain.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("LINUX ESCAPE ROOM: ROOT'S REVENGE")
    slow(textwrap.dedent("""
        [Screen flickers... Cursor blinks.]
        ROOT: "Welcome back, old friend. Think you can escape *my* terminal?"
    """))
    press_enter("(Press Enter to begin your escape...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module1.json", after_hook=root_taunt)

def challenge_outro():
    banner("ESCAPE ROOM: SUCCESS")
    slow("ROOT: 'Impressive. But the logs never forget.'")
