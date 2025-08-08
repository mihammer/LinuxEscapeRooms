from utils import slow, banner, press_enter, run_quiz_from_json, random_story_event
import textwrap, random

EXTRA_TAUNTS = [
    "\nROOT: 'walinuxagent? More like walinux-maybe.'",
    "\nROOT: 'Extensions deployed. Confidence… not so much.'",
    "\nROOT: 'Logs in /var/log/azure are judging you.'",
    "\nROOT: 'LIS drivers loaded? So are my tricks.'",
]

def root_taunt():
    if random.random() < 0.6:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("CLOUD COMMAND: AZURE AGENT OPS")
    slow(textwrap.dedent("""
        [A digital storm brews over your Azure dashboard. Alarms flash: waagent out of sync!]
        ROOT: "Stability or chaos—pick one."
    """))
    press_enter("(Press Enter to accept your Azure Ops mission...) ")

def challenge_quiz():
    run_quiz_from_json("questions/module4.json", after_hook=root_taunt)

def challenge_outro():
    banner("AZURE AGENT OPS: CLOUD RESTORED")
    slow("ROOT: 'The cloud shifts. I will too.'")
