from utils import slow, banner, ask_shell
import textwrap
import time

def show_box(label="Lockbox"):
    slow(r"""
      ______________________
     / ____________________ \
    | |                    | |
    | |    {0:^14}    | |
    | |____________________| |
     \______________________/""".format(label))

def challenge_intro():
    banner("ESCAPE FROM BLOCK 7")
    slow(textwrap.dedent("""
        You’ve been framed and locked away in Block 7’s high-security wing.
        The corridor beyond your cell is patrolled by armed guards,
        and the alarms could blare at any mistake.

        To escape, you must crack each console’s Linux puzzle—
        earning keys to unlock the final gate.

        • Solve each command to survive.
        • Type 'hint' if you dare; 'skip' after 3 fails.
        • Guards patrol slowly… but they never rest.
    """))
    input("\n(Press Enter to begin plotting your breakout…) ")

def challenge_quiz():
    # 1. pwd
    banner("Challenge 1 – Cell Identification")
    show_box("Cell Panel")
    slow("A scratchy voice hidden in the panel: 'Tell me where you stand. Which command shows your location?'")
    ask_shell("cell> ", {"pwd"},
        "`pwd` reveals your current directory—your digital cell number.",
        hint="Print Working Directory.")

    # 2. ls -a
    banner("Challenge 2 – Hidden Compartments")
    show_box("Floor Grate")
    slow("You spot a hidden grate. The panel whispers: 'Reveal every file—even the ones they hide.'")
    ask_shell("grate> ", {"ls -a"},
        "`ls -a` lists all files, even those with a leading dot.",
        hint="List all files, including dotfiles.")

    # 3. ps
    banner("Challenge 3 – Guard Roster")
    show_box("Roster Board")
    slow("A faded note reads: 'Who’s on duty now? List every running process.'")
    ask_shell("roster> ", {"ps"},
        "`ps` shows all current processes—mapping the guards’ shifts.",
        hint="Process Status: two letters.")

    # 4. uname -r / uname -a
    banner("Challenge 4 – Security Firmware")
    show_box("Mainframe")
    slow("The central terminal growls: 'Show me the core version they can’t patch.'")
    ask_shell("firmware> ", {"uname -r", "uname -a"},
        "`uname -r` reveals the running kernel version.",
        hint="Starts with `uname`.")

    # 5. sshd status
    banner("Challenge 5 – Watchtower Link")
    show_box("Watchtower")
    slow("Radio crackles: 'Is the remote watchtower link alive? Check the SSH daemon.'")
    ask_shell("watchtower> ", {
        "systemctl status sshd", "service sshd status", "ps -ef | grep sshd", "pgrep sshd"
    },
    "You confirm `sshd` is active—guards might intercept orders here.",
    hint="Check service status or process list.")

    # 6. tail -n 10 /var/log/auth.log
    banner("Challenge 6 – Surveillance Logs")
    show_box("Log Terminal")
    slow("A flicker shows: 'Only the last ten entries of /var/log/auth.log reveal the guard codes.'")
    ask_shell("log> ",
        {"tail -n 10 /var/log/auth.log", "tail /var/log/auth.log -n 10", "tail /var/log/auth.log"},
        "`tail` fetches the final lines—those guard codes you need.",
        hint="Use `tail` to view the end of a file.")

    # 7. ls -lt / ls -t
    banner("Challenge 7 – Evidence Locker")
    show_box("Locker")
    slow("'Find the file they tampered with last—sort by modification time.'")
    ask_shell("locker> ", {"ls -lt", "ls -t"},
        "`ls -lt` lists files sorted newest first.",
        hint="List files by time with `ls` flags.")

    # 8. who / w
    banner("Challenge 8 – Visitor Log")
    show_box("Logbook")
    slow("'Who just signed in? Identify logged-in users and where they came from.'")
    ask_shell("logbook> ", {"who", "w"},
        "`who` shows current users and their terminals.",
        hint="Think simple: ask 'who' is online.")

    # 9. cat warden_note.txt / less / nano
    banner("Challenge 9 – The Warden’s Note")
    show_box("Warden File")
    slow("On a desk lies `warden_note.txt`: 'Read me before they catch you.'")
    ask_shell("warden> ", {"cat warden_note.txt", "less warden_note.txt", "nano warden_note.txt"},
        "You read the warden’s note—clues to the final escape.",
        hint="Use `cat`, `less`, or an editor.")

    # Finale
    challenge_outro()

def challenge_outro():
    banner("THE FINAL GATE")
    slow("You approach the heavy gate, heart pounding. This is it—the last step between you and freedom.\n")
    time.sleep(1)
    slow("\n🎉 With a gavel-like clang, the gate swings open. You slip into the night—free at last! ...Or are you?")
