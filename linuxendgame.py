#!/usr/bin/env python3
"""
LINUX: ENDGAME  – a cinematic command-line gauntlet
Author: Todd (with a nudge from Sam)
"""

import textwrap
import time
import sys

# ---------------------------------------------------------------------------
#  Utility helpers
# ---------------------------------------------------------------------------

def slow(text, delay=0.006):  # Fast scroll
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def shell(prompt="avenger@linux:~$ "):
    return input(prompt).strip()

# ---------------------------------------------------------------------------
#  Generic challenge wrapper (with hints)
# ---------------------------------------------------------------------------

def ask_shell(question, correct_cmds, explanation, reveal_answer=True, hint=None):
    attempts = 0
    while True:
        cmd = shell(question)
        cmd_lc = cmd.lower()

        if cmd_lc in {c.lower() for c in correct_cmds} or any(cmd_lc.startswith(c.lower()) for c in correct_cmds):
            slow("\n✅  Correct!")
            slow(explanation)
            break

        if cmd_lc == "hint" and hint:
            slow(f"💡 Hint: {hint}")
            continue

        attempts += 1
        if attempts == 3:
            slow("❌  Strike three!  Type `skip` to move on, `hint` for a clue, or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  Skipped. The rebellion moves on.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Nope. (Or type `hint` or `skip`.)")
        else:
            slow("❌  Nope. Try again or type `hint`.")

# ---------------------------------------------------------------------------
#  Intro & ambience
# ---------------------------------------------------------------------------

def intro():
    banner("LINUX: ENDGAME")
    slow(textwrap.dedent("""
        After the Snap, half your packets vanished.

        The surviving Dev-engers have built a Quantum Kernel
        to reverse the damage—if they can solve these Linux trials.

        ✅  Enter each answer as a real shell command or brief response.
        ✖️   After three misses you may type 'hint' or 'skip' (but glory lost).
    """))
    input("\n(Press Enter to begin your Time Heist…) ")

# ---------------------------------------------------------------------------
#  Scene helper
# ---------------------------------------------------------------------------

def holo(title="Holo-msg"):
    slow(rf"""
       .---------------------------.
      /  /=====================\  \
     |  |  {title:^19} |  |
      \  \=====================/  /  
       '---------------------------'
    """)

# ---------------------------------------------------------------------------
#  Challenges
# ---------------------------------------------------------------------------

def ch_crontab():
    banner("Challenge 1 – Time Heist Setup")
    holo("Edit Cron")
    slow("Doctor Strange: 'Manipulate the flow of time for your tasks. Edit your crontab.'")
    ask_shell("endgame> ",
              {"crontab -e", "sudo crontab -e"},
              "Time stream adjusted. Crontab modified.",
              hint="You're editing scheduled jobs for your user.")

def ch_date():
    banner("Challenge 2 – What Year Is It?")
    holo("Date Check")
    slow("Scott Lang: 'Time’s fuzzy. What’s the current date?'")
    ask_shell("endgame> ",
              {"date"},
              "Date verified. You’re in the correct timeline.",
              hint="Try a command that tells you today’s date.")

def ch_install_rhel():
    banner("Challenge 3 – DNFinity Stones")
    holo("Install Tool (RHEL)")
    slow("Rhodey: 'We need intel. Install “htop” on this RHEL node.'")
    ask_shell("endgame> ",
              {"sudo dnf install htop", "dnf install htop", "sudo yum install htop", "yum install htop"},
              "`htop` equipped. Vital signs online.",
              hint="Use `dnf` or `yum` with `install`.")

def ch_install_ubuntu():
    banner("Challenge 4 – APT-Vengers Assemble")
    holo("Install Tool (Ubuntu)")
    slow("Shuri: 'Same tool, different kingdom. Install “htop” here, too.'")
    ask_shell("endgame> ",
              {"sudo apt install htop", "apt install htop", "sudo apt-get install htop", "apt-get install htop"},
              "`htop` installed on the Ubuntu front.",
              hint="Try `apt install` or `apt-get install`.")

def ch_waagent():
    banner("Challenge 5 – Resource-Disk Reality Check")
    holo("Config Hunt")
    slow("Rocket: 'Does this VM have a /mnt resource disk? Which config file reveals the truth?'")
    ask_shell("endgame> ",
              {"/etc/waagent.conf", "cat /etc/waagent.conf", "less /etc/waagent.conf"},
              "Correct—the secret’s in /etc/waagent.conf.",
              hint="Try looking under `/etc/` for Azure Linux config files.")

def ch_restart_net():
    banner("Challenge 6 – Snap the Network (Back)")
    holo("Network Daemon")
    slow("Thor: 'Give the network a jolt. Restart the daemon!'")
    ask_shell("endgame> ",
              {"sudo systemctl restart network", "systemctl restart network",
               "sudo systemctl restart networkmanager", "systemctl restart networkmanager",
               "service network restart", "sudo service network restart"},
              "Bifrost restored—network daemon revived.",
              hint="Use `systemctl restart` or `service` to reboot the network.")

def ch_ip_addr():
    banner("Challenge 7 – Know Thy IP")
    holo("Address Check")
    slow("Natasha: 'Where on earth (or space) is this node? Show its IP.'")
    ask_shell("endgame> ",
              {"ip addr show", "ip addr"},
              "Coordinates locked—IP address displayed.",
              hint="Use a command that shows all IP interfaces.")

def ch_tcpdump():
    banner("Challenge 8 – Capture the Packets")
    holo("Network Traces")
    slow("Banner: 'Need to record network gamma rays. Which tool?'")
    ask_shell("endgame> ",
              {"tcpdump"},
              "`tcpdump` ready—sniffing packets like a pro.",
              hint="A popular packet sniffer used in the CLI.")

def ch_mounts():
    banner("Challenge 9 – Mounted Realities")
    holo("Disk Mounts")
    slow("Pepper: 'Show me every filesystem currently mounted.'")
    ask_shell("endgame> ",
              {"mount"},
              "All current mounts listed. Reality aligned.",
              hint="Classic one-word command to list mounts.")

def ch_lsblk():
    banner("Challenge 10 – Block Device Roll-Call")
    holo("Block Devices")
    slow("Peter Parker: 'How many block devices are we swinging with?'")
    ask_shell("endgame> ",
              {"lsblk"},
              "Block devices enumerated. Nice catch!",
              hint="Use a command that lists block devices visually.")

def ch_df():
    banner("Challenge 11 – The Space Stone")
    holo("Disk Space")
    slow("Captain Marvel: 'How much disk space remains before this place explodes?'")
    ask_shell("endgame> ",
              {"df", "df -h", "df -H"},
              "Disk space measured. We’re safe—ish.",
              hint="Shows filesystem space. Try adding `-h` to make it human-friendly.")

# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale():
    banner("MISSION ACCOMPLISHED")
    slow("With every command executed, the Quantum Kernel surges.\n"
         "Thanos’s errors are reversed, packets restored… and lunch shawarma awaits. 🎉\n")

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    intro()
    ch_crontab()
    ch_date()
    ch_install_rhel()
    ch_install_ubuntu()
    ch_waagent()
    ch_restart_net()
    ch_ip_addr()
    ch_tcpdump()
    ch_mounts()
    ch_lsblk()
    ch_df()
    finale()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Mission aborted. Until next Time Heist.")
