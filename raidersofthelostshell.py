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

def shell(prompt="player@escape-room:~$ "):
    return input(prompt).strip()

def give_key(inventory, name):
    inventory.append(name)
    slow(f"\n🔑  You received **{name}** and slip it into your pocket.")

# ---------------------------------------------------------------------------
#  Generic challenge wrapper
# ---------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, inventory, key_name=None):
    attempts = 0
    while True:
        cmd = shell(question)
        cmd_lc = cmd.lower()

        if cmd_lc in correct_cmds or any(cmd_lc.startswith(c) for c in correct_cmds):
            slow("\n✅  Correct!")
            slow(explanation)
            if key_name:
                give_key(inventory, key_name)
            break

        attempts += 1
        if attempts == 3:
            slow("❌  Strike three!  Type `skip` to move on or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  Skipped.  No key for this one, but the story marches on.")
                break
            else:
                slow("❌  Nope.  (Or type `skip`.)")
        else:
            slow("❌  Nope.  Try again.")

# ---------------------------------------------------------------------------
#  Intro & ambience
# ---------------------------------------------------------------------------

def intro():
    banner("RAIDERS OF THE LOST SHELL")
    slow(textwrap.dedent("""
        You are Todd Hammer, digital archaeologist. A secret login portal has transported you
        to the legendary Temple of Kernux. Your goal: retrieve the Lost Shell before the
        rival hacker cult, The Forked Process, beats you to it.

        ⚠️  The temple is filled with traps. Solve each Linux challenge to survive.
        You’ll receive keys that may unlock the final chamber...

        You may type 'help' at any time. Type 'skip' after 3 misses to continue (no key earned).
    """))
    input("\n(Press Enter to begin your quest...) ")

# ---------------------------------------------------------------------------
#  Scene helpers
# ---------------------------------------------------------------------------

def show_box(label="Mysterious"):
    slow(r"""
      ______________________
     / ____________________ \
    | |                    | |
    | |    {0:^14}    | |
    | |____________________| |
     \______________________/""".format(label))

# ---------------------------------------------------------------------------
#  Challenges adapted from Raiders plot
# ---------------------------------------------------------------------------

def challenge_pwd(inventory):
    banner("Challenge 1 – The Temple Gate")
    show_box("Gate")
    slow("A whisper from the stone: 'Name the command that reveals your current location.'")
    ask_shell("gate> ", {"pwd"}, "`pwd` prints your present working directory.", inventory, key_name="Bronze Key")

def challenge_ls(inventory):
    banner("Challenge 2 – The Trap Room")
    show_box("Traps")
    slow("Laser traps everywhere. 'Reveal all files — even those hidden from mortal eyes.'")
    ask_shell("traps> ", {"ls -a"}, "`ls -a` includes hidden files (those beginning with a dot).", inventory, key_name="Glass Key")

def challenge_ps(inventory):
    banner("Challenge 3 – The Forked Path")
    show_box("Fork")
    slow("Two tunnels. One safe. 'Find the command to list what's running…'")
    ask_shell("fork> ", {"ps"}, "`ps` lists currently running processes.", inventory, key_name="Iron Key")

def challenge_kernel(inventory):
    banner("Challenge 4 – Guardian of the Kernel")
    show_box("Kernel")
    slow("The guardian awakens: 'Reveal the version of the kernel you serve.'")
    ask_shell("kernel> ", {"uname -r", "uname -a"}, "`uname -r` shows kernel version.", inventory, key_name="Steel Key")

def challenge_sshd(inventory):
    banner("Challenge 5 – The SSH Pit")
    show_box("SSH")
    slow("You can’t SSH in. The box says: 'Is the SSH daemon even alive?'")
    ask_shell("ssh-pit> ", {
        "systemctl status sshd", "systemctl status ssh",
        "service ssh status", "service sshd status",
        "ps -ef | grep sshd", "pgrep sshd"
    }, "These commands verify if the SSH service is running.", inventory, key_name="Obsidian Key")

def challenge_tail(inventory):
    banner("Challenge 6 – The File of Doom")
    show_box("Logs")
    slow("A log file crackles: 'Only the final 10 lines of /var/log/syslog are safe to read.'")
    ask_shell("log> ", {"tail /var/log/syslog", "tail -n 10 /var/log/syslog", "tail -10 /var/log/syslog"}, "`tail` lets you read the last lines of a file.", inventory, key_name="Copper Key")

def challenge_lslt(inventory):
    banner("Challenge 7 – The Timekeeper’s Tomb")
    show_box("Tomb")
    slow("'Reveal the file most recently changed. Time is ticking.'")
    ask_shell("tomb> ", {"ls -lt", "ls -t"}, "`ls -lt` sorts files by modification time.", inventory, key_name="Marble Key")

def challenge_who(inventory):
    banner("Challenge 8 – Rival Encounter")
    show_box("Rival")
    slow("The Forked Process is near. 'Who is logged in right now? And from where?'")
    ask_shell("rival> ", {"who", "w"}, "`who` shows logged in users and their source.", inventory, key_name="Jade Key")

def challenge_cat(inventory):
    banner("Challenge 9 – The Lost Shell")
    show_box("Shell")
    slow("A script named script.sh sits atop the pedestal. 'Preview before you run, or perish.'")
    ask_shell("shell> ", {"cat script.sh", "less script.sh", "nano script.sh"}, "Use `cat`, `less`, or `nano` to read before executing.", inventory, key_name="Golden Key")

# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale(inventory):
    banner("THE FINAL DOOR")
    slow(f"You insert {len(inventory)} keys…")
    time.sleep(1)
    for k in inventory:
        slow(f"  • {k}")
        time.sleep(0.3)

    if len(inventory) >= 7:
        slow("\n🎉 Every lock clicks. The door swings wide — the Lost Shell is yours! 🏆")
    else:
        slow("\nSome locks remain sealed. Perhaps skipping has consequences… 😈")
        slow("GAME OVER – Try again and earn more keys!")

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
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
        print("\n\n💀  Escape aborted. Better luck next reboot.")
