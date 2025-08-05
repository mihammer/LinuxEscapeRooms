from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap
import random

# Bonus custom Root taunts just for this module!
EXTRA_TAUNTS = [
    "\nROOT: 'Are your packets lost, or just your confidence?'",
    "\nROOT: 'You sure that's not just a DNS issue? Classic rookie move.'",
    "\nROOT: 'If this takes you more than 30 seconds, I’m changing your default gateway.'",
    "\nROOT: 'Network down? Don't blame me... (Actually, do.)'",
    "\nROOT: 'Feeling isolated? Good. That's how a misconfigured firewall feels.'",
    "\nROOT: 'Careful, one wrong command and I’ll reroute your traffic to /dev/null!'"
]

def root_taunt():
    if random.random() < 0.5:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("NETWORK: THE ROOT OF ALL PROBLEMS")
    slow(textwrap.dedent("""
        [Static crackles. All routes lead to... nowhere?]
        ROOT: "You’re in my domain now! I swapped your default gateway, spiked your MTU, and tossed a few bad DNS entries your way.
        Let’s see if you can find your way back online—or will you be lost in the ether forever?"
    """))
    input("\n(Press Enter if your connection is still alive...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="Which file contains the interface details in Red Hat?",
        options=[
            "/etc/sysconfig/network",
            "/etc/network/interfaces",
            "/etc/sysconfig/network-scripts/ifcfg-eth(n)",
            "/etc/hosts"
        ],
        correct_index=2,
        explanation="✅ /etc/sysconfig/network-scripts/ifcfg-eth(n) holds interface configs in Red Hat.",
        qnum=1
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Where should you check DNS resolution configuration?",
        options=[
            "/etc/hostname",
            "/etc/hosts.allow",
            "/etc/hosts.deny",
            "/etc/resolv.conf"
        ],
        correct_index=3,
        explanation="✅ /etc/resolv.conf shows DNS configuration.",
        qnum=2
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Which command is used to determine if the port is listening or not?",
        options=[
            "ifconfig",
            "ip addr",
            "route -n",
            "ss -ntulp"
        ],
        correct_index=3,
        explanation="✅ ss -ntulp lists listening ports and services.",
        qnum=3
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Which two commands and options may be used to determine the MTU size of the interface?",
        options=[
            "ipconfig and ip addr",
            "ip addr show and route -n",
            "netstat and ip addr show",
            "ifconfig and ip addr show"
        ],
        correct_index=3,
        explanation="✅ ifconfig and ip addr show display MTU info.",
        qnum=4
    )
    root_taunt()

    ask_multiple_choice(
        prompt="What's the correct syntax to obtain route information?",
        options=[
            "ip route show",
            "route -r",
            "route -rn",
            "ifconfig -r"
        ],
        correct_index=0,
        explanation="✅ ip route show is the modern way to see routing.",
        qnum=5
    )
    root_taunt()

    ask_multiple_choice(
        prompt="What's the correct syntax to show iptables rules?",
        options=[
            "iptables -L",
            "iptables -l",
            "iptables -F",
            "iptables -rules"
        ],
        correct_index=0,
        explanation="✅ iptables -L lists current firewall rules.",
        qnum=6
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Which command is used to collect the network traces when working on a connectivity issue?",
        options=[
            "tcpdump",
            "selinux",
            "netcat",
            "netsh"
        ],
        correct_index=0,
        explanation="✅ tcpdump is the go-to tool for packet traces.",
        qnum=7
    )
    root_taunt()

    ask_multiple_choice(
        prompt="What are the different modes of selinux?",
        options=[
            "enforcing, permissive and disabled",
            "active, normal and deactivate",
            "enabled, permissive and disabled",
            "allow, deny, reject"
        ],
        correct_index=0,
        explanation="✅ The three SELinux modes: enforcing, permissive, and disabled.",
        qnum=8
    )
    root_taunt()

def challenge_outro():
    banner("NETWORK CHALLENGE: CONNECTION RESTORED")
    slow("ROOT: 'Not bad. You got through my firewall of confusion. But next time... I’m pulling the plug.'")
