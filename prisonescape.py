import textwrap, time, sys

# ---------------------------------------------------------------------------
#  Utility helpers
# ---------------------------------------------------------------------------

def slow(text, delay=0.008):  # Fast scroll for CLI game
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def shell(prompt="inmate@cell-console:~$ "):
    return input(prompt).strip()

def give_key(inventory, name):
    inventory.append(name)
    slow(f"\n🔑  You pocket the **{name}**, its cold metal promising freedom…")

# ---------------------------------------------------------------------------
#  Generic challenge wrapper (with hint support)
# ---------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, inventory, key_name=None, reveal_answer=True, hint=None):
    attempts = 0
    while True:
        cmd = shell(question)
        cmd_lc = cmd.lower()

        if cmd_lc in {c.lower() for c in correct_cmds} or any(cmd_lc.startswith(c.lower()) for c in correct_cmds):
            slow("\n✅  Correct—but the guard’s footsteps echo closer.")
            slow(explanation)
            if key_name:
                give_key(inventory, key_name)
            break

        if cmd_lc == "hint" and hint:
            slow(f"💡 Hint: {hint}")
            continue

        attempts += 1
        if attempts == 3:
            slow("❌  Three failed attempts! The lights flicker—type `skip` to move on, `hint` for a clue, or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  You back away, heart pounding. No key this time, but the cell door stays ajar… for now.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Still wrong. Steel clanks in the corridor. (Try `hint` or `skip`.)")
        else:
            slow("❌  Wrong! The bars tremble. Try again or type `hint`.")

# ---------------------------------------------------------------------------
#  Intro & ambience
# ---------------------------------------------------------------------------

def intro():
    banner("ESCAPE FROM BLOCK 7")
    slow(textwrap.dedent("""
        You’ve been framed and locked away in Block 7’s high-security wing.
        The corridor beyond your cell is patrolled by armed guards,
        and the alarms could blare at any mistake.

        To escape, you must crack each console’s Linux puzzle—
        earning keys to unlock the final gate.

        • Solve each command to survive and gather keys.
        • Type 'hint' if you dare; 'skip' after 3 fails sacrifices the key.
        • Guards patrol slowly… but they never rest.
    """))
    input("\n(Press Enter to begin plotting your breakout…) ")

# ---------------------------------------------------------------------------
#  Scene helpers
# ---------------------------------------------------------------------------

def show_box(label="Lockbox"):
    slow(r"""
      ______________________
     / ____________________ \
    | |                    | |
    | |    {0:^14}    | |
    | |____________________| |
     \______________________/""".format(label))

# ---------------------------------------------------------------------------
#  Challenges
# ---------------------------------------------------------------------------

def challenge_pwd(inventory):
    banner("Challenge 1 – Cell Identification")
    show_box("Cell Panel")
    slow("A scratchy voice hidden in the panel: 'Tell me where you stand. Which command shows your location?'")
    ask_shell("cell> ", {"pwd"},
              "`pwd` reveals your current directory—your digital cell number.",
              inventory, key_name="Rusty Key",
              hint="Print Working Directory.")

def challenge_ls(inventory):
    banner("Challenge 2 – Hidden Compartments")
    show_box("Floor Grate")
    slow("You spot a hidden grate. The panel whispers: 'Reveal every file—even the ones they hide.'")
    ask_shell("grate> ", {"ls -a"},
              "`ls -a` lists all files, even those with a leading dot.",
              inventory, key_name="Steel Shank",
              hint="List all files, including dotfiles.")

def challenge_ps(inventory):
    banner("Challenge 3 – Guard Roster")
    show_box("Roster Board")
    slow("A faded note reads: 'Who’s on duty now? List every running process.'")
    ask_shell("roster> ", {"ps"},
              "`ps` shows all current processes—mapping the guards’ shifts.",
              inventory, key_name="Iron Shank",
              hint="Process Status: two letters.")

def challenge_kernel(inventory):
    banner("Challenge 4 – Security Firmware")
    show_box("Mainframe")
    slow("The central terminal growls: 'Show me the core version they can’t patch.'")
    ask_shell("firmware> ", {"uname -r", "uname -a"},
              "`uname -r` reveals the running kernel version.",
              inventory, key_name="Circuit Key",
              hint="Starts with `uname`.")

def challenge_sshd(inventory):
    banner("Challenge 5 – Watchtower Link")
    show_box("Watchtower")
    slow("Radio crackles: 'Is the remote watchtower link alive? Check the SSH daemon.'")
    ask_shell("watchtower> ", {
        "systemctl status sshd", "service sshd status",
        "ps -ef | grep sshd", "pgrep sshd"
    },
    "You confirm `sshd` is active—guards might intercept orders here.",
    inventory, key_name="Obsidian Shard",
    hint="Check service status or process list.")

def challenge_tail(inventory):
    banner("Challenge 6 – Surveillance Logs")
    show_box("Log Terminal")
    slow("A flicker shows: 'Only the last ten entries of /var/log/auth.log reveal the guard codes.'")
    ask_shell("log> ",
              {"tail -n 10 /var/log/auth.log", "tail /var/log/auth.log -n 10", "tail /var/log/auth.log"},
              "`tail` fetches the final lines—those guard codes you need.",
              inventory, key_name="Copper Shard",
              hint="Use `tail` to view the end of a file.")

def challenge_lslt(inventory):
    banner("Challenge 7 – Evidence Locker")
    show_box("Locker")
    slow("'Find the file they tampered with last—sort by modification time.'")
    ask_shell("locker> ", {"ls -lt", "ls -t"},
              "`ls -lt` lists files sorted newest first.",
              inventory, key_name="Marble Fragment",
              hint="List files by time with `ls` flags.")

def challenge_who(inventory):
    banner("Challenge 8 – Visitor Log")
    show_box("Logbook")
    slow("'Who just signed in? Identify logged-in users and where they came from.'")
    ask_shell("logbook> ", {"who", "w"},
              "`who` shows current users and their terminals.",
              inventory, key_name="Jade Fragment",
              hint="Think simple: ask 'who' is online.")

def challenge_cat(inventory):
    banner("Challenge 9 – The Warden’s Note")
    show_box("Warden File")
    slow("On a desk lies `warden_note.txt`: 'Read me before they catch you.'")
    ask_shell("warden> ", {"cat warden_note.txt", "less warden_note.txt", "nano warden_note.txt"},
              "You read the warden’s note—clues to the final escape.",
              inventory, key_name="Golden Lockpick",
              hint="Use `cat`, `less`, or an editor.")

# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale(inventory):
    banner("THE FINAL GATE")
    slow(f"You approach the heavy gate and insert {len(inventory)} implements…")
    time.sleep(1)
    for k in inventory:
        slow(f"  • {k}")
        time.sleep(0.3)

    if len(inventory) >= 7:
        slow("\n🎉 With a gavel-like clang, the gate swings open. You slip into the night—free at last!")
    else:
        slow("\nSome locks remain… The alarm buzzer blares as guards approach.\nGAME OVER – They recapture you.")
        
# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    inventory = []
    intro()
    challenge_pwd(inventory)
    challenge_ls(inventory)
    challenge_ps(inventory)
    challenge_kernel(inventory)
    challenge_sshd(inventory)
    challenge_tail(inventory)
    challenge_lslt(inventory)
    challenge_who(inventory)
    challenge_cat(inventory)
    finale(inventory)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  The lights snap off. You’re dragged back into your cell.")
