from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'Tail it, fail it—either way I see it.'",
    "\nROOT: 'Case-insensitive? Your confidence isn’t.'",
    "\nROOT: 'Cron jobs don’t forget. Unlike you.'",
    "\nROOT: 'Sosreport? More like sos-regret.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("LINUX APPENDIX: LOGFILE MAYHEM")
    slow(textwrap.dedent("""
        [The air is thick with log rotation and mysterious errors.]
        ROOT: "Every mistake in /var/log echoes forever..."
    """))
    press_enter("(Press Enter to face the chaos...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module2.json", after_hook=root_taunt)

def challenge_outro():
    banner("APPENDIX DEFEATED")
    slow("ROOT: 'You tamed the logs—for now.'")
