from utils import slow, banner, holo, ask_shell
import textwrap

def challenge_intro():
    banner("ESCAPE FROM THE SPACE SHELL")
    slow(textwrap.dedent("""
        Deep in the void, your station’s life support groans under strain.
        Something malevolent has awakened the cursed SPACE SHELL—an AI
        weapon corrupting every system, hungry for control.

        Every corridor is bathed in red emergency lights. The air tastes
        metallic, and distant alarms pulse like a dying heartbeat.

        ✅  Each command could be the difference between survival… or oblivion.
        ✖️   After three failures, you may type 'skip'—but who knows what waits.
    """))
    input("\n(Press Enter if you dare…) ")

def challenge_quiz():
    # Challenge 1
    banner("Challenge 1 – Infiltrate or Perish")
    holo("Crew Register")
    slow("The terminal sparks as you approach. A voice crackles: 'Authorize stardust or be erased.' Create user `stardust`—your last chance.")
    ask_shell(
        "space-shell> ",
        {"sudo useradd stardust", "useradd stardust"},
        "A new operator breathes life into the logs. You live… for now.",
        hint="Command that adds a user. Don’t let your alias slip into oblivion."
    )

    # Challenge 2
    banner("Challenge 2 – Memory Overload")
    holo("Resource Scan")
    slow("Red alerts flood the display: 'Memory corruption detected.' Report free memory before it vanishes.")
    ask_shell(
        "space-shell> ",
        {"free", "free -h"},
        "Memory snapshot secured, but the shell whispers warnings of leaks everywhere.",
        hint="Think of ‘no cost’—and human-readable sanity."
    )

    # Challenge 3
    banner("Challenge 3 – Under Siege")
    holo("System Overview")
    slow("You feel the station shudder. Real-time CPU and memory stats are required to avoid certain disaster!")
    ask_shell(
        "space-shell> ",
        {"top"},
        "You see rogue tasks clawing at the core. At least you know what you face.",
        hint="This command shows the top predators in process form."
    )

    # Challenge 4
    banner("Challenge 4 – Exterminate the Menace")
    holo("Terminate 1045")
    slow("A phantom process (PID 1045) screams in the logs. It’s devouring cycles—kill it before it kills you.")
    ask_shell(
        "space-shell> ",
        {"kill 1045", "kill -9 1045"},
        "Silence. The system exhales… but something else stirs in the dark.",
        hint="Ending a process is literal. Use its PID like a scalpel."
    )

    # Challenge 5
    banner("Challenge 5 – Breach the Locks")
    holo("Unlock Hatch")
    slow("A sealed hatch bars your path to the core. File runme.sh demands 755 permissions to release its hold on the deck.")
    ask_shell(
        "space-shell> ",
        {"chmod 755 runme.sh", "chmod 755"},
        "The hatch groans open. A stale breeze carries distant screams.",
        hint="File mode 755. Unleash the hatch."
    )

    # Challenge 6
    banner("Challenge 6 – Purge the Traitor")
    holo("Crew Member Delete")
    slow("Operator `nebula` went rogue, broadcasting your coordinates to the void. Delete the account before they summon the horror.")
    ask_shell(
        "space-shell> ",
        {"sudo userdel nebula", "userdel nebula"},
        "Nebula’s profile vanishes. Your heartbeat steadies… barely.",
        hint="Opposite of useradd. Start with `userdel`."
    )

    # Challenge 7
    banner("Challenge 7 – Hunt the Word")
    holo("Log Analysis")
    slow("Your HUD flickers: ‘Find “orbit” in starlogs.txt or we’re scrap.’ Every second, the shell pulses with red.")
    ask_shell(
        "space-shell> ",
        {"grep orbit starlogs.txt", "grep orbit"},
        "The pattern glows in the text—intel extracted from chaos.",
        hint="Use the text-hunting beast: grep."
    )

    # Challenge 8
    banner("Challenge 8 – Forge the Lifeline")
    holo("Symbolic Links")
    slow("Systems collapsing, you need a shortcut to the comms deck. Create a symbolic link or be trapped forever. (Give the command to create a symlink.)")
    ask_shell(
        "space-shell> ",
        {"ln -s target link", "ln -s"},
        "A slender link appears, a fragile lifeline in the breach.",
        hint="‘ln -s’ for symbolic link. It’s your rope out."
    )

    # Challenge 9
    banner("Challenge 9 – I/O Cataclysm")
    holo("Disk Performance")
    slow("The fusion core’s I/O is spiking. If you don’t stabilize it, the station will implode around you. Check the I/O stats!")
    ask_shell(
        "space-shell> ",
        {"iostat"},
        "Diagnostics complete. Core trembles but holds—for this moment.",
        hint="Combine IO with stats—iostat."
    )

    # Challenge 10
    banner("Challenge 10 – Last Support Beacon")
    holo("Diagnostic Tools")
    slow("Your comms are dying. Use a single command from a Red Hat or SUSE environment to gather diagnostic data!")
    ask_shell(
        "space-shell> ",
        {"sosreport", "supportconfig", "sosreport supportconfig"},
        "Beacon launched. Rescue… or ruin… is on its way.",
        hint="One starts with ‘sos’, the other sounds like your cry for help."
    )

def challenge_outro():
    banner("MISSION OR OBLIVION")
    slow("Sirens wail as the core breaches containment. You sprint through the smoking corridor,\n"
         "launching yourself into your escape pod. The shell’s claws reach for you—but then silence.\n"
         "Did you win… or did you awaken something worse? 🎉\n")

