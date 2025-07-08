import textwrap, time, sys

# ---------------------------------------------------------------------------
#  Utility helpers (unchanged)
# ---------------------------------------------------------------------------

def slow(text, delay=0.008):  # Fast scroll for CLI game
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def shell(prompt="padawan@death-shell:~$ "):
    return input(prompt).strip()

# ---------------------------------------------------------------------------
#  Generic challenge wrapper (keys removed)
# ---------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, reveal_answer=True):
    attempts = 0
    while True:
        cmd = shell(question)
        cmd_lc = cmd.lower()

        if cmd_lc in correct_cmds or any(cmd_lc.startswith(c) for c in correct_cmds):
            slow("\n✅  Correct!")
            slow(explanation)
            break

        attempts += 1
        if attempts == 3:
            slow("❌  Strike three!  Type `skip` to move on or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  Skipped.  The rebellion moves on.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Nope.  (Or type `skip`.)")
        else:
            slow("❌  Nope.  Try again.")


# ---------------------------------------------------------------------------
#  Intro & ambience (Star Wars style)
# ---------------------------------------------------------------------------

def intro():
    banner("ESCAPE FROM THE DEATH SHELL")
    slow(textwrap.dedent("""
        A long time ago in a data center far, far away...

        The Galactic Empire has unleashed the DEATH SHELL, a weaponised OS
        set to overwrite all open–source freedoms in the galaxy. Guided by
        the ghost of Old Sys‑Wan Kenobi, you must complete a series of Linux
        trials aboard the battle‑station to sabotage it from within.

        ✅  Answer each prompt with a real shell command (or brief text answer).
        ✖️   After three misses you may type 'skip' to continue (but glory lost!).
    """))
    input("\n(Press Enter to begin your mission…) ")

# ---------------------------------------------------------------------------
#  Scene helper
# ---------------------------------------------------------------------------

def holo(title="Holo‑msg"):
    slow(rf"""
       .---------------------------.
      /  /=====================\  \
     |  |  {title:^19} |  |
      \  \=====================/  /
       '---------------------------'
    """)

# ---------------------------------------------------------------------------
#  Challenges (Star Wars themed)
# ---------------------------------------------------------------------------

def ch_add_user():
    banner("Challenge 1 – I Am the User You're Looking For")
    holo("User Create")
    slow("Stormtrooper login console demands a new account for undercover access. Create a user named `snadella`.")
    ask_shell("death-shell> ", {"sudo useradd snadella", "useradd snadella"},
              "User `snadella` has been created. You're in.")

def ch_free():
    banner("Challenge 2 – The RAM Awakens")
    holo("Memory Check")
    slow("C‑3PO: 'I calculate memory efficiency is critical for survival. How much memory is free?'")
    ask_shell("death-shell> ", {"free", "free -h"}, "Memory status displayed. Vital stats acquired.")

def ch_top():
    banner("Challenge 3 – Getting to the top of it.")
    holo("System Stats")
    slow("R2‑D2 plugs in, awaiting the resource overview. Display current system resource usage, including memory and cpu.")
    ask_shell("death-shell> ", {"top"}, "System performance metrics are now visible.")

def ch_kill():
    banner("Challenge 4 – Attack of the PID")
    holo("Terminate 1045")
    slow("A Sith process (PID 1045) consumes the CPUs. End it!")
    ask_shell("death-shell> ", {"kill 1045", "kill -9 1045"}, "Process eliminated. Balance restored.")

def ch_chmod():
    banner("Challenge 5 – You don't have permission to access this file")
    holo("Unlock File")
    slow("A locked datapad requires 755 permissions to open the hatch. Adjust file permissions for `runme.sh`.")
    ask_shell("death-shell> ", {"chmod 755 runme.sh", "chmod 755"}, "Access granted. Hatch unlocked.")

def ch_del_user():
    banner("Challenge 6 – Order 66: Remove dvader")
    holo("User Delete")
    slow("Alas, dvader has joined the dark side – delete the account.")
    ask_shell("death-shell> ", {"sudo userdel dvader", "userdel dvader"}, "dvader060 has been purged from the records.")

def ch_grep():
    banner("Challenge 7 – A Grep Hope")
    holo("Search Scroll")
    slow("Leia whispers: 'Find the word *rebellion* in the stolen plans.txt.' using grep")
    ask_shell("death-shell> ", {"grep rebellion plans.txt", "grep rebellion"}, "Search complete. Intel located.")

def ch_symlink():
    banner("Challenge 8 – The Phantom Link")
    holo("Symbolic Links")
    slow("Sys‑Wan: 'What command creates a symbolic link, young Padawan?'")
    ask_shell("death-shell> ", {"ln -s", "ln -s target link"}, "A symbolic link has been forged.")

def ch_iostat():
    banner("Challenge 9 – The I/O Strikes Back")
    holo("Disk Perf")
    slow("The fusion core groans. Determine disk I/O stats fast!")
    ask_shell("death-shell> ", {"iostat"}, "Diagnostics complete. Core is stable—for now.")

def ch_support():
    banner("Challenge 10 – Revenge of the Support Tools")
    holo("Diagnostic Tools")
    slow("Name one of the two diagnostic collectors trusted by the Rebellion support team. One for Red Hat or one for SUSE.")
    ask_shell("death-shell> ", {"sosreport", "supportconfig", "sosreport supportconfig"},
              "Support tools accepted. Rebellion support authorized.")


# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale():
    banner("MISSION COMPLETE")
    slow("The main reactor overloads… You sprint to the Falcon and jump to hyperspace! 🎉\n")

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    intro()
    ch_add_user()
    ch_free()
    ch_top()
    ch_kill()
    ch_chmod()
    ch_del_user()
    ch_grep()
    ch_symlink()
    ch_iostat()
    ch_support()
    finale()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Mission aborted. May the source be with you next time.")
