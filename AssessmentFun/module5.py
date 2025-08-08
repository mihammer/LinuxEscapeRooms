from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'Are your packets lost, or just your confidence?'",
    "\nROOT: 'You sure that’s not just DNS? Classic.'",
    "\nROOT: 'If this takes 30s, I’m changing your default gateway.'",
    "\nROOT: 'Careful, one wrong rule and I’ll drop your vibe chain.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("NETWORK: THE ROOT OF ALL PROBLEMS")
    slow(textwrap.dedent("""
        [Links flap. ARP caches whisper. Someone typed iptables -F…]
        ROOT: "Route wisely. Or don’t."
    """))
    press_enter("(Press Enter to begin your network trial...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module5.json", after_hook=root_taunt)

def challenge_outro():
    banner("NETWORK CHALLENGE: CONNECTION RESTORED")
    slow("ROOT: 'You got through my firewall of confusion… this time.'")
