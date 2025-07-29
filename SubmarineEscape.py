#!/usr/bin/env python3
"""
LINUX: DEPTHS  – a harrowing command-line escape from a stricken submarine
Author: Todd Hammer
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

def shell(prompt="engineer@submarine-shell:~$ "):
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
            slow("❌  Third misfire! The hull’s cracking—type `skip` to flood this compartment, `hint` for a clue, or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  You bail out of this station. Cold water rushes in.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Still wrong. Metal groans under pressure. (Try `hint` or `skip`.)")
        else:
            slow("❌  That didn’t work… The lights flicker. Try again or type `hint`.")

# ---------------------------------------------------------------------------
#  Intro & ambience
# ---------------------------------------------------------------------------

def intro():
    banner("LINUX: DEPTHS")
    slow(textwrap.dedent("""
        You’re trapped in a submarine sinking beneath freezing waves.
        Water seeps through fractured bulkheads and alarms echo down
        the flooded corridors. Every console might be your last lifeline.

        ✅  Enter each answer as a real shell command or brief response.
        ✖️   After three misses you may type 'hint' or 'skip' (but a hatch might slam shut).
    """))
    input("\n(Press Enter if you dare to dive…) ")

# ---------------------------------------------------------------------------
#  Scene helper
# ---------------------------------------------------------------------------

def holo(title="Sonar Beacon"):
    slow(rf"""
       .-------------------------------.
      /  /===========================\  \
     |  |       {title:^23}       |  |
      \  \===========================/  /
       '-------------------------------'
    """)

# ---------------------------------------------------------------------------
#  Challenges
# ---------------------------------------------------------------------------

def ch_crontab():
    banner("Challenge 1 – Pump Schedule")
    holo("Edit Flood Pumps")
    slow("Pressure’s rising. Reprogram the flood pumps via crontab to purge water every hour. Edit your user’s crontab!")
    ask_shell("depths> ",
              {"crontab -e", "sudo crontab -e"},
              "Pump schedule set. Water alarms quiet… briefly.",
              hint="Edit your user’s scheduled tasks.")

def ch_date():
    banner("Challenge 2 – Time Drift")
    holo("Clock Check")
    slow("The onboard clock is slipping—confirm the current date before systems fail.")
    ask_shell("depths> ",
              {"date"},
              "Date locked in. At least time still marches… somewhere.",
              hint="One command tells you today’s date.")

def ch_install_rhel():
    banner("Challenge 3 – Vital Tools (RHEL)")
    holo("Install Htop")
    slow("You need to monitor CPU and memory under extreme load. Install `htop` on this RHEL system.")
    ask_shell("depths> ",
              {"sudo dnf install htop", "dnf install htop", "sudo yum install htop", "yum install htop"},
              "`htop` installed. You glimpse runaway processes before they overwhelm you.",
              hint="Use `dnf` or `yum` with `install`.")

def ch_install_ubuntu():
    banner("Challenge 4 – Vital Tools (Ubuntu)")
    holo("Install Htop")
    slow("Another control station runs Ubuntu—install `htop` there too to keep an eye on resources.")
    ask_shell("depths> ",
              {"sudo apt install htop", "apt install htop", "sudo apt-get install htop", "apt-get install htop"},
              "`htop` is online. You track memory leaks even as water reaches your boots.",
              hint="Try `apt install` or `apt-get install`.")

def ch_waagent():
    banner("Challenge 5 – Resource Hull Check")
    holo("Config Inspection")
    slow("Vital config files might reveal weak points. Which file under `/etc/` shows VM resource disk mounting options?")
    ask_shell("depths> ",
              {"/etc/waagent.conf", "cat /etc/waagent.conf", "less /etc/waagent.conf"},
              "You found `/etc/waagent.conf`. The hull’s endurance parameters are exposed.",
              hint="Look for Azure agent settings in `/etc`.")

def ch_restart_net():
    banner("Challenge 6 – Restore Comms")
    holo("Network Daemon")
    slow("Communications have cut out. Restart the network daemon before you lose contact entirely.")
    ask_shell("depths> ",
              {"sudo systemctl restart network", "systemctl restart network",
               "sudo systemctl restart networkmanager", "systemctl restart networkmanager",
               "service network restart", "sudo service network restart"},
              "Network rebooted. Faint pings return—perhaps rescue is near.",
              hint="Use `systemctl restart` or `service` to revive the network.")

def ch_ip_addr():
    banner("Challenge 7 – Sonar Ping")
    holo("IP Address")
    slow("Ping echo request — find this node’s IP to hand off coordinates to HQ?")
    ask_shell("depths> ",
              {"ip addr show", "ip addr"},
              "IP address acquired. You transmit your location into the abyss.",
              hint="One command shows all network interfaces.")

def ch_tcpdump():
    banner("Challenge 8 – Packet Echo")
    holo("Network Sniffer")
    slow("Salvage every packet before they’re lost to the deep. Which tool captures them live?")
    ask_shell("depths> ",
              {"tcpdump"},
              "`tcpdump` active. You record every fragment of data like sonar pings.",
              hint="A classic CLI packet sniffer.")

def ch_mounts():
    banner("Challenge 9 – Deck Mapping")
    holo("Mount Points")
    slow("Identify every filesystem mounted so you can log data before the pressure crushes disks.")
    ask_shell("depths> ",
              {"mount"},
              "Mount points listed. You chart your escape route through file systems.",
              hint="A one-word command to list mounts.")

def ch_lsblk():
    banner("Challenge 10 – Bulkhead Survey")
    holo("Block Devices")
    slow("How many block devices remain intact under this pressure? Enumerate them.")
    ask_shell("depths> ",
              {"lsblk"},
              "Block devices revealed. You note which drives might survive the crush.",
              hint="Use `lsblk` for a visual device tree.")

def ch_df():
    banner("Challenge 11 – Air Supply Gauge")
    holo("Disk Space")
    slow("Disk space dwindles like oxygen. Check how much remains before systems choke.")
    ask_shell("depths> ",
              {"df", "df -h", "df -H"},
              "Space confirmed. You race against time as corridors flood.",
              hint="Use `df` with `-h` for human-readable output.")

# ---------------------------------------------------------------------------
#  Finale
# ---------------------------------------------------------------------------

def finale():
    banner("ESCAPE OR DROWN")
    slow(textwrap.dedent("""
        Sirens wail as water surges through the aft bulkhead.
        You execute the final commands, seal the compromised compartments,
        and initiate the emergency ballast dump.

        The submarine rises, creaking in protest, breaking the surface
        just as your console goes dark. You gasp, lungs burning,
        and watch the saltwater spray again3st the hull.

        You survived… for now. 🎉
    """))

# ---------------------------------------------------------------------------
#  Main driver
# ---------------------------------------------------------------------------

def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
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
        print("\n\n💀  You abandon ship into icy depths. Silence is your only companion.") 
