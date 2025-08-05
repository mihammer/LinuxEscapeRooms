from utils import slow, banner, ask_shell
import textwrap

def holo(title="Sonar Beacon"):
    slow(rf"""
       .-------------------------------.
      /  /===========================\  \
     |  |       {title:^23}       |  |
      \  \===========================/  / 
       '-------------------------------'
    """)

def challenge_intro():
    banner("LINUX: DEPTHS")
    slow(textwrap.dedent("""
        You’re trapped in a submarine sinking beneath freezing waves.
        Water seeps through fractured bulkheads and alarms echo down
        the flooded corridors. Every console might be your last lifeline.

        ✅  Enter each answer as a real shell command or brief response.
        ✖️   After three misses you may type 'hint' or 'skip' (but a hatch might slam shut).
    """))
    input("\n(Press Enter if you dare to dive…) ")

def challenge_quiz():
    # 1. crontab -e
    banner("Challenge 1 – Pump Schedule")
    holo("Edit Flood Pumps")
    slow("Pressure’s rising. Reprogram the flood pumps via crontab to purge water every hour. Edit your user’s crontab!")
    ask_shell("depths> ",
              {"crontab -e", "sudo crontab -e"},
              "Pump schedule set. Water alarms quiet… briefly.",
              hint="Edit your user’s scheduled tasks.")

    # 2. date
    banner("Challenge 2 – Time Drift")
    holo("Clock Check")
    slow("The onboard clock is slipping—confirm the current date before systems fail.")
    ask_shell("depths> ",
              {"date"},
              "Date locked in. At least time still marches… somewhere.",
              hint="One command tells you today’s date.")

    # 3. dnf/yum install htop
    banner("Challenge 3 – Vital Tools (RHEL)")
    holo("Install Htop")
    slow("You need to monitor CPU and memory under extreme load. Install `htop` on this RHEL system.")
    ask_shell("depths> ",
              {"sudo dnf install htop", "dnf install htop", "sudo yum install htop", "yum install htop"},
              "`htop` installed. You glimpse runaway processes before they overwhelm you.",
              hint="Use `dnf` or `yum` with `install`.")

    # 4. apt install htop
    banner("Challenge 4 – Vital Tools (Ubuntu)")
    holo("Install Htop")
    slow("Another control station runs Ubuntu—install `htop` there too to keep an eye on resources.")
    ask_shell("depths> ",
              {"sudo apt install htop", "apt install htop", "sudo apt-get install htop", "apt-get install htop"},
              "`htop` is online. You track memory leaks even as water reaches your boots.",
              hint="Try `apt install` or `apt-get install`.")

    # 5. /etc/waagent.conf
    banner("Challenge 5 – Resource Hull Check")
    holo("Config Inspection")
    slow("Vital config files might reveal weak points. Which file under `/etc/` shows VM resource disk mounting options?")
    ask_shell("depths> ",
              {"/etc/waagent.conf", "cat /etc/waagent.conf", "less /etc/waagent.conf"},
              "You found `/etc/waagent.conf`. The hull’s endurance parameters are exposed.",
              hint="Look for Azure agent settings in `/etc`.")

    # 6. Restart network
    banner("Challenge 6 – Restore Comms")
    holo("Network Daemon")
    slow("Communications have cut out. Restart the network daemon before you lose contact entirely.")
    ask_shell("depths> ",
              {"sudo systemctl restart network", "systemctl restart network",
               "sudo systemctl restart networkmanager", "systemctl restart networkmanager",
               "service network restart", "sudo service network restart"},
              "Network rebooted. Faint pings return—perhaps rescue is near.",
              hint="Use `systemctl restart` or `service` to revive the network.")

    # 7. ip addr
    banner("Challenge 7 – Sonar Ping")
    holo("IP Address")
    slow("Ping echo request — find this node’s IP to hand off coordinates to HQ?")
    ask_shell("depths> ",
              {"ip addr show", "ip addr"},
              "IP address acquired. You transmit your location into the abyss.",
              hint="One command shows all network interfaces.")

    # 8. tcpdump
    banner("Challenge 8 – Packet Echo")
    holo("Network Sniffer")
    slow("Salvage every packet before they’re lost to the deep. Which tool captures them live?")
    ask_shell("depths> ",
              {"tcpdump"},
              "`tcpdump` active. You record every fragment of data like sonar pings.",
              hint="A classic CLI packet sniffer.")

    # 9. mount
    banner("Challenge 9 – Deck Mapping")
    holo("Mount Points")
    slow("Identify every filesystem mounted so you can log data before the pressure crushes disks.")
    ask_shell("depths> ",
              {"mount"},
              "Mount points listed. You chart your escape route through file systems.",
              hint="A one-word command to list mounts.")

    # 10. lsblk
    banner("Challenge 10 – Bulkhead Survey")
    holo("Block Devices")
    slow("How many block devices remain intact under this pressure? Enumerate them.")
    ask_shell("depths> ",
              {"lsblk"},
              "Block devices revealed. You note which drives might survive the crush.",
              hint="Use `lsblk` for a visual device tree.")

    # 11. df
    banner("Challenge 11 – Air Supply Gauge")
    holo("Disk Space")
    slow("Disk space dwindles like oxygen. Check how much remains before systems choke.")
    ask_shell("depths> ",
              {"df", "df -h", "df -H"},
              "Space confirmed. You race against time as corridors flood.",
              hint="Use `df` with `-h` for human-readable output.")

    challenge_outro()

def challenge_outro():
    banner("ESCAPE OR DROWN")
    slow(textwrap.dedent("""
        Sirens wail as water surges through the aft bulkhead.
        You execute the final commands, seal the compromised compartments,
        and initiate the emergency ballast dump.

        The submarine rises, creaking in protest, breaking the surface
        just as your console goes dark. You gasp, lungs burning,
        and watch the saltwater spray against the hull.

        You survived… for now. 🎉
    """))
