"""
Linux Escape Room – Sim-Shell Edition (Fixed & Fast Scroll)
"""

import textwrap, time, sys

# ---------------------------------------------------------------------------
#  Utility helpers
# ---------------------------------------------------------------------------

def slow(text, delay=0.008):  # 👈 FAST SCROLL!
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

def ask_shell(question, correct_cmds, explanation, inventory, key_name=None, reveal_answer=True):
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
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Nope.  (Or type `skip`.)")
        else:
            slow("❌  Nope.  Try again.")

# ---------------------------------------------------------------------------
#  Intro & ambience
# ---------------------------------------------------------------------------

def intro():
    banner("WELCOME TO THE LINUX ESCAPE ROOM")
    slow(textwrap.dedent("""
 
        Dim LEDs flicker above countless servers. A lone terminal waits for input.
        You remember the rules:
          • Solve each puzzle to unlock the exit.
          • Type like you’re really at a shell.
          • After three wrong commands you may choose to 'skip' (but keys matter!).

        Type 'help' at any prompt for a hint.
    """))
    input("\n(Press Enter to start) ")

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
     \______________________/
    """.format(label))

# ---------------------------------------------------------------------------
#  Challenges
# ---------------------------------------------------------------------------

def challenge_fstab(inventory):
    banner("Challenge 1 – Corrupted fstab")
    slow("The terminal prints a boot error and displays `/etc/fstab`:")
    print(r"""
# <file system> <mount point> <type> <options> <dump> <pass>
1: UUID=102ee66d-b0c0-4d1c-8087-f5c32873987e /        ext4 defaults 0 1
2: /dev/sda1                               /boot     ext2 defaults 0 2
3: /dev/sdzzz                              /home     ext4 defaults 0 2
""")
    slow("One line is bogus. Which number is wrong? (Type just the number)")
    ask_shell("> ", {"3"},
              "Explanation: '/dev/sdzzz' doesn’t follow normal Linux disk naming. It’s invalid.",
              inventory, key_name="Brass Key")

def challenge_top(inventory):
    banner("Challenge 2 – CPU Hog Hunt")
    slow("A `top` snapshot scrolls by:")
    print("""
PID   USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
1245  root      20   0  392344  84212  10200 S   0.3  2.1   0:02.34 sshd
2842  postgres  20   0  865320 123456  18532 S   1.1  5.8   1:24.56 postgres
9111  apache    20   0  432456  65234   9056 R  45.2  4.1   5:45.89 httpd
1324  root      20   0  128000  10240   2048 S   0.0  0.5   0:01.11 systemd
""")
    slow("Which command is devouring the CPU?")
    ask_shell("> ", {"httpd", "apache"},
              "`httpd` shows 45 % CPU – clearly hogging resources.",
              inventory, key_name="Copper Key")

def mini_box(inventory, label, question, correct_cmds, explanation, key_name):
    show_box(label)
    slow(f"The {label.lower()} box clicks and speaks:\n“{question}”")
    ask_shell(label + " box> ", correct_cmds, explanation, inventory, key_name=key_name)
    slow(f"The {label.lower()} box pops open revealing a small compartment…")

def challenge_logs(inventory):
    banner("Challenge 3 – Log Lore")
    mini_box(inventory, "Log",
             "Where do most Linux log files live?",
             {"/var/log", "var/log"},
             "Standard distros store logs under `/var/log`.",
             "Iron Key")

    slow("\nInside the Log box you find a crumpled paper entitled 'messages'.")
    slow("To read the final 10 lines you need the right command…")
    ask_shell("log-paper> ",
              {"tail -n 10 /var/log/messages", "tail /var/log/messages -n 10",
               "tail /var/log/messages"},
              "The `tail -n 10` command outputs the end of a file.",
              inventory)

def challenge_kernel(inventory):
    banner("Challenge 4 – Know Thy Kernel")
    show_box("Kernel")
    slow("Letters appear: “Which command reveals the **running kernel version**?”")
    ask_shell("kernel-box> ",
              {"uname -r", "uname -a"},
              "`uname -r` prints kernel version; `-a` gives full system info.",
              inventory, key_name="Steel Key")

def challenge_sshd(inventory):
    banner("Challenge 5 – Where’s my SSH?")
    mini_box(inventory, "SSH",
             "You can’t SSH remotely but you’re on console. Check if sshd is running.",
             {"systemctl status ssh", "systemctl status sshd",
              "service ssh status", "service sshd status",
              "ps -ef | grep sshd", "pgrep sshd"},
             "`systemctl status sshd` shows the daemon’s status.",
             key_name="Obsidian Key")

def challenge_path(inventory):
    banner("Challenge 6 – PATH Enlightenment")
    mini_box(inventory, "PATH",
             "Print the PATH env-var for the current user:",
             {"echo $path", "echo $PATH", "printenv path", "printenv PATH"},
             "`echo $PATH` shows directories searched for executables.",
             key_name="Silver Key")

def challenge_azure_console(inventory):
    banner("Challenge 7 – Azure Plan B")
    mini_box(inventory, "Azure",
             "On Azure, SSH is blocked. What lets you see the boot screen?",
             {"serial console", "console"},
             "Azure Serial Console gives low-level VM access even when SSH fails.",
             key_name="Azure Blue Key")

def challenge_python_ver(inventory):
    banner("Challenge 8 – Python Showdown")
    mini_box(inventory, "Python",
             "Which command shows what `python` binary will be used?",
             {"which python", "type -a python", "command -v python"},
             "`which python` or `type -a python` shows which executable runs.",
             key_name="Golden Key")

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

    if len(inventory) >= 6:
        slow("\n🎉 Every lock clicks. The steel door swings open — you are FREE! 🏆")
    else:
        slow("\nSome locks remain sealed. Maybe those skipped questions mattered… 😈")
        slow("GAME OVER (for now)")

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    inventory = []
    intro()
    challenge_fstab(inventory)
    challenge_top(inventory)
    challenge_logs(inventory)
    challenge_kernel(inventory)
    challenge_sshd(inventory)
    challenge_path(inventory)
    challenge_azure_console(inventory)
    challenge_python_ver(inventory)
    finale(inventory)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Escape aborted. Better luck next reboot.")