from utils import slow, banner, ask_shell, holo
import textwrap
import time

def challenge_intro():
    banner("SSHD: CONTACT LOST")
    slow(textwrap.dedent("""
        🚨  WARNING: Critical systems failure detected.
        Your ship has been flung off-course—navigation and comms are down.
        Only a barely-alive terminal connects you to the universe.
        
        Mission Control can only help if you restore secure comms—using
        SSH and pure skill, before life support is totally lost.

        Every challenge brings you closer to home… or to the void.
        💡  Type 'hint' if you’re desperate. After three fails, 'skip' is allowed—but only cowards skip.

        Time to reboot your destiny. Good luck, Space Cadet.
    """))
    input("\n(Press Enter to access the emergency shell…) ")

def challenge_quiz():
    # Challenge 1 – Boot status
    banner("Challenge 1 – Ship Boot Mystery")
    holo("Boot Confirmation")
    slow(textwrap.dedent("""
        Your SSH session freezes. Before you panic, did the ship's OS actually finish booting?
        
        A) Rerun `ssh` with `-vvv` to get debug output.
        B) Ping the ship's public IP address.
        C) Open the Azure Portal Serial Console.
        D) Restart the VM from Mission Control.
    """))
    while True:
        choice = input("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  SSH debug only shows connection attempts—it won’t prove the ship booted.")
        elif choice == "B":
            slow("❌  Ping checks the network, not the OS. The ship could be pingable, but dead inside!")
        elif choice == "C":
            slow("✅  Correct! Serial Console shows live boot output and a login prompt, even if networking is borked.")
            break
        elif choice == "D":
            slow("❌  Restarting blindly risks making things worse. Check before you reboot!")
        else:
            slow("❓  Please enter A, B, C, or D.")
    slow("Now you know: the ship’s heart is still beating. Dive in for diagnostics!")

    # Challenge 2 – SSHD status
    banner("Challenge 2 – Daemon on the Run")
    holo("SSHD Status")
    slow("OS is up, but sshd is gone like a rogue escape pod. Check its status!")
    ask_shell(
        "space-ssh> ",
        {"sudo systemctl status sshd", "systemctl status sshd"},
        "SSHD is running (or not)—now you have your answer.",
        hint="Use systemctl for service investigations."
    )

    # Challenge 3 – Review config
    banner("Challenge 3 – The Config Conundrum")
    holo("SSHD Config")
    slow("Something changed the ship’s security settings… Review the SSHD config file.")
    ask_shell(
        "space-ssh> ",
        {"vi /etc/ssh/sshd_config", "nano /etc/ssh/sshd_config", "cat /etc/ssh/sshd_config"},
        "That config holds the secrets—find the port, root login, and authentication details.",
        hint="The file is /etc/ssh/sshd_config. Open it!"
    )

    # Challenge 4 – Logs
    banner("Challenge 4 – Ghosts in the Logs")
    holo("SSHD Logs")
    slow("SSHD won’t start. If only the logs could speak… oh wait, they do! Use journalctl to read them.")
    ask_shell(
        "space-ssh> ",
        {"sudo journalctl -u sshd", "journalctl -u sshd"},
        "The logs spill the beans—maybe a syntax error is dooming you.",
        hint="journalctl -u sshd will show the story."
    )

    # Challenge 5 – Firewall
    banner("Challenge 5 – Firewall: The Final Frontier")
    holo("Port Blocked?")
    slow(textwrap.dedent("""
        SSH connections are refused. Shields are up! Check the ship's internal firewall.
        A) Run `netstat -tulpn | grep :22`
        B) Inspect Network Security Group rules in Mission Control
        C) List firewall rules on the ship (e.g., `sudo iptables -L`)
        D) Restart the firewall service with `sudo systemctl restart firewalld`
    """))
    while True:
        choice = input("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  netstat only shows listening ports, not firewall rules.")
        elif choice == "B":
            slow("❌  NSGs are great, but you need to check the ship’s own defenses.")
        elif choice == "C":
            slow("✅  Correct! List firewall rules to see if port 22 is being vaporized.")
            break
        elif choice == "D":
            slow("❌  Restarting the firewall is risky—inspect before you poke!")
        else:
            slow("❓  Please enter A, B, C, or D.")
    slow("Now you see the shields—time to lower port 22’s defenses!")

    # Challenge 6 – TCP test
    banner("Challenge 6 – TCP Pathways")
    holo("TCP Path Check")
    slow("SSH works internally, but not from home base. What tool tests if port 22 is reachable?")
    ask_shell(
        "space-ssh> ",
        {"nc", "telnet", "psping", "test-netconnection"},
        "A working handshake means port 22 is clear for docking.",
        hint="Use netcat (nc), telnet, or PowerShell for port testing."
    )

    # Challenge 7 – Live log
    banner("Challenge 7 – Real-Time Alarm")
    holo("Live Auth Log")
    slow("You need to watch live SSH login attempts—what command lets you do this? Use journalctl to follow the logs.")
    ask_shell(
        "space-ssh> ",
        {"sudo journalctl -f -u sshd", "journalctl -f -u sshd"},
        "You’re now monitoring the drama in real time.",
        hint="-f means 'follow' in journalctl."
    )

    # Challenge 8 – Debugging
    banner("Challenge 8 – Maximum Clarity Mode")
    holo("Increase Verbosity")
    slow("Logs are vague. What LogLevel unlocks all secrets in sshd_config? What should we set log level to in the sshd_config?")
    ask_shell(
        "space-ssh> ",
        {"loglevel debug3", "edit sshd_config loglevel debug3", "sudo vi /etc/ssh/sshd_config", "sshd_config"},
        "LogLevel DEBUG3 reveals all the universe’s errors.",
        hint="Edit LogLevel to DEBUG3 in sshd_config."
    )

    # Challenge 9 – Custom Port
    banner("Challenge 9 – Port Where?")
    holo("Custom Port?")
    slow("SSH is listening somewhere—but not on 22! Find the configured port.")
    ask_shell(
        "space-ssh> ",
        {"grep Port /etc/ssh/sshd_config", "cat /etc/ssh/sshd_config | grep Port", "cat /etc/ssh/sshd_config"},
        "You find a weird port. Maybe 2222? No wonder home base can’t connect.",
        hint="Search for Port in sshd_config."
    )

    # Challenge 10 – SSH verbosity
    banner("Challenge 10 – Verbose Orbits")
    holo("Verbose Mode")
    slow(textwrap.dedent("""
        The SSH client only shrugs. Which flag enables full debug output?
        A) `ssh -v user@ship`
        B) `ssh -vv user@ship`
        C) `ssh -vvv user@ship`
        D) `ssh --verbose user@ship`
    """))
    while True:
        choice = input("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  One -v is okay, but three is epic.")
        elif choice == "B":
            slow("❌  Two is closer, but we want the full telemetry stream.")
        elif choice == "C":
            slow("✅  Correct! `ssh -vvv` gives you everything.")
            break
        elif choice == "D":
            slow("❌  --verbose is not a thing for SSH.")
        else:
            slow("❓  Please enter A, B, C, or D.")
    slow("Run `ssh -vvv` for the most cosmic detail. Home Base is almost in range!")

def challenge_outro():
    banner("MISSION ACCOMPLISHED")
    slow("With one last keystroke, the comms burst back to life. Your ship stabilizes. Home Base is online. You’re a shell hero in space. 🚀🛰️\n")

# Main driver, for standalone test/run (adjust as needed for your framework)
def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    challenge_intro()
    challenge_quiz()
    challenge_outro()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Lost in the stars. May your next connection succeed.")

