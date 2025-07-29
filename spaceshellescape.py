import textwrap, time, sys

# ---------------------------------------------------------------------------
#  Utility helpers (unchanged)
# ---------------------------------------------------------------------------

def slow(text, delay=0.006):  # Fast scroll for CLI game
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def shell(prompt="astronaut@space-shell:~$ "):
    return input(prompt).strip()

# ---------------------------------------------------------------------------
#  Generic challenge wrapper (keys removed)
# ---------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, hint="", reveal_answer=True):
    attempts = 0
    while True:
        cmd = shell(question)
        cmd_lc = cmd.lower()

        if cmd_lc == "hint":
            slow(f"💡 Hint: {hint}")
            continue

        if cmd_lc in correct_cmds or any(cmd_lc.startswith(c) for c in correct_cmds):
            slow("\n✅  Correct!")
            slow(explanation)
            break

        attempts += 1
        if attempts == 3:
            slow("❌  Strike three! The oxygen meter ticks down. Type `skip` to flee this module, `hint` for a clue, or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  You bail out. The station’s ominous hum follows you as you retreat.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer lurking in the logs was: `{correct_sample}`")
                break
            else:
                slow("❌  Wrong again. The lights flicker ominously. (Try `hint` or `skip`.)")
        else:
            slow("❌  That’s not it… The temperature gauge spikes. Try again or type `hint`.")

# ---------------------------------------------------------------------------
#  Intro & ambience (Dark space style)
# ---------------------------------------------------------------------------

def intro():
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

# ---------------------------------------------------------------------------
#  Scene helper
# ---------------------------------------------------------------------------

def holo(title="Distress Beacon"):
    slow(rf"""
       .-------------------------------.
      /  /===========================\  \
     |  |     {title:^23}     |  |
      \  \===========================/  /
       '-------------------------------'
    """)

# ---------------------------------------------------------------------------
#  Challenges (Now truly perilous)
# ---------------------------------------------------------------------------

def ch_add_user():
    banner("Challenge 1 – Infiltrate or Perish")
    holo("Crew Register")
    slow("The terminal sparks as you approach. A voice crackles: 'Authorize stardust or be erased.' Create user `stardust`—your last chance.")
    ask_shell(
        "space-shell> ",
        {"sudo useradd stardust", "useradd stardust"},
        "A new operator breathes life into the logs. You live… for now.",
        hint="Command that adds a user. Don’t let your alias slip into oblivion."
    )

def ch_free():
    banner("Challenge 2 – Memory Overload")
    holo("Resource Scan")
    slow("Red alerts flood the display: 'Memory corruption detected.' Report free memory before it vanishes.")
    ask_shell(
        "space-shell> ",
        {"free", "free -h"},
        "Memory snapshot secured, but the shell whispers warnings of leaks everywhere.",
        hint="Think of ‘no cost’—and human-readable sanity."
    )

def ch_top():
    banner("Challenge 3 – Under Siege")
    holo("System Overview")
    slow("You feel the station shudder. Real-time CPU and memory stats are required to avoid certain disaster!")
    ask_shell(
        "space-shell> ",
        {"top"},
        "You see rogue tasks clawing at the core. At least you know what you face.",
        hint="This command shows the top predators in process form."
    )

def ch_kill():
    banner("Challenge 4 – Exterminate the Menace")
    holo("Terminate 1045")
    slow("A phantom process (PID 1045) screams in the logs. It’s devouring cycles—kill it before it kills you.")
    ask_shell(
        "space-shell> ",
        {"kill 1045", "kill -9 1045"},
        "Silence. The system exhales… but something else stirs in the dark.",
        hint="Ending a process is literal. Use its PID like a scalpel."
    )

def ch_chmod():
    banner("Challenge 5 – Breach the Locks")
    holo("Unlock Hatch")
    slow("A sealed hatch bars your path to the core. File runme.sh demands 755 permissions to release its hold on the deck.")
    ask_shell(
        "space-shell> ",
        {"chmod 755 runme.sh", "chmod 755"},
        "The hatch groans open. A stale breeze carries distant screams.",
        hint="File mode 755. Unleash the hatch."
    )

def ch_del_user():
    banner("Challenge 6 – Purge the Traitor")
    holo("Crew Member Delete")
    slow("Operator `nebula` went rogue, broadcasting your coordinates to the void. Delete the account before they summon the horror.")
    ask_shell(
        "space-shell> ",
        {"sudo userdel nebula", "userdel nebula"},
        "Nebula’s profile vanishes. Your heartbeat steadies… barely.",
        hint="Opposite of useradd. Start with `userdel`."
    )

def ch_grep():
    banner("Challenge 7 – Hunt the Word")
    holo("Log Analysis")
    slow("Your HUD flickers: ‘Find “orbit” in starlogs.txt or we’re scrap.’ Every second, the shell pulses with red.")
    ask_shell(
        "space-shell> ",
        {"grep orbit starlogs.txt", "grep orbit"},
        "The pattern glows in the text—intel extracted from chaos.",
        hint="Use the text-hunting beast: grep."
    )

def ch_symlink():
    banner("Challenge 8 – Forge the Lifeline")
    holo("Symbolic Links")
    slow("Systems collapsing, you need a shortcut to the comms deck. Create a symbolic link or be trapped forever. (Give the command to create a symlink.")
    ask_shell(
        "space-shell> ",
        {"ln -s target link", "ln -s"},
        "A slender link appears, a fragile lifeline in the breach.",
        hint="‘ln -s’ for symbolic link. It’s your rope out."
    )

def ch_iostat():
    banner("Challenge 9 – I/O Cataclysm")
    holo("Disk Performance")
    slow("The fusion core’s I/O is spiking. If you don’t stabilize it, the station will implode around you. Check the I/O stats!")
    ask_shell(
        "space-shell> ",
        {"iostat"},
        "Diagnostics complete. Core trembles but holds—for this moment.",
        hint="Combine IO with stats—iostat."
    )

def ch_support():
    banner("Challenge 10 – Last Support Beacon")
    holo("Diagnostic Tools")
    slow("Your comms are dying. Use a single command from a Red Hat or SUSE environment to gather diagnostic data!")
    ask_shell(
        "space-shell> ",
        {"sosreport", "supportconfig", "sosreport supportconfig"},
        "Beacon launched. Rescue… or ruin… is on its way.",
        hint="One starts with ‘sos’, the other sounds like your cry for help."
    )

# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale():
    banner("MISSION OR OBLIVION")
    slow("Sirens wail as the core breaches containment. You sprint through the smoking corridor,\n"
         "launching yourself into your escape pod. The shell’s claws reach for you—but then silence.\n"
         "Did you win… or did you awaken something worse? 🎉\n")

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
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
        print("\n\n💀  You jettison yourself into the void. Silence follows. Good luck…") 
