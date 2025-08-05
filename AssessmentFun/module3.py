from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap

def challenge_intro():
    banner("PACKAGE PREDICAMENT: THE UPDATE APOCALYPSE")
    slow(textwrap.dedent("""
        [Warning sirens blare! The datacenter is flickering, packages everywhere are out of date!]
        ROOT: "Welcome to Update Nightmares, where every wrong command might nuke your OS. 
        The package manager is... unstable. Repositories are shifting. The kernel is... twitchy.
        If you can survive this, you can survive *anything*. Good luck, sysadmin. You'll need it."
    """))
    input("\n(Press Enter to begin the Package Predicament...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="What's the correct syntax to check the distribution version?",
        options=[
            "cat /etc/*release",
            "uname",
            "modinfo",
            "os --version"
        ],
        correct_index=0,
        explanation="✅ `cat /etc/*release` gives you the distribution version.",
        qnum=1
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to list the currently running kernel version?",
        options=[
            "cat /etc/*release",
            "uname -r",
            "grep -i default /boot/grub/grub.conf",
            "First kernel in grub configuration file"
        ],
        correct_index=1,
        explanation="✅ `uname -r` shows the currently running kernel version.",
        qnum=2
    )

    ask_multiple_choice(
        prompt="What is a repository?",
        options=[
            "An inventory which tracks the installed packages.",
            "A collection of packages from which the system can retrieve and install updates/upgrades.",
            "A dedicated storage drive where software can be preserved.",
            "Virtual storage from which the OS can be upgraded to next major version."
        ],
        correct_index=1,
        explanation="✅ A repository is a collection of packages you can install or update from.",
        qnum=3
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to query if a package is installed on RHEL/CentOS/OEL?",
        options=[
            "rpm -ivh <package_name>",
            "yum <package_name>",
            "apt list –a <package_name>",
            "rpm -qa <package_name>"
        ],
        correct_index=3,
        explanation="✅ `rpm -qa <package_name>` queries installed packages on RHEL/CentOS/OEL.",
        qnum=4
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to install all applicable updates on Ubuntu?",
        options=[
            "apt-get upgrade",
            "yum update",
            "zypper up",
            "apt-get update"
        ],
        correct_index=0,
        explanation="✅ `apt-get upgrade` installs all applicable updates (after `apt-get update`).",
        qnum=5
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to remove an installed package on SUSE?",
        options=[
            "rpm -d <package_name>",
            "yum remove <package_name>",
            "zypper remove <package_name>",
            "zypper se <package_name>"
        ],
        correct_index=2,
        explanation="✅ `zypper remove <package_name>` removes a package on SUSE.",
        qnum=6
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to perform an OS upgrade on CentOS?",
        options=[
            "yum update",
            "zyyper up",
            "apt-get update",
            "apt-get upgrade"
        ],
        correct_index=0,
        explanation="✅ `yum update` performs an OS upgrade on CentOS.",
        qnum=7
    )

    ask_multiple_choice(
        prompt="A kernel panic issue is encountered after an OS update. What is the best approach to quickly recover from that issue?",
        options=[
            "Delete the kernel which is causing the kernel panic issue.",
            "Quickly reinstall the kernel using console and boot the VM.",
            "Boot the VM from previous working kernel with the help of the console.",
            "Delete the impacted VM and create new VM."
        ],
        correct_index=2,
        explanation="✅ Boot from a previous working kernel using the console—don't panic, just reboot smart!",
        qnum=8
    )

def challenge_outro():
    banner("PACKAGE PREDICAMENT SURVIVED")
    slow("ROOT: 'You made it through the update apocalypse. But remember... the next patch could be your last.'")
