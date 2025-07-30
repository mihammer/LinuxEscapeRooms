
import textwrap, time, sys

def slow(text, delay=0.006):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def banner(text):
    bar = "=" * len(text)
    slow(f"\n{bar}\n{text}\n{bar}")

def shell(prompt="lost@death-shell:~$ "):
    return input(prompt).strip()

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
            slow("❌  Strike three!  Type `skip` to move on, `hint` for a clue, or try again.")
        elif attempts > 3:
            if cmd_lc == "skip":
                slow("↩️  Skipped. The rebellion moves on.")
                if reveal_answer:
                    correct_sample = next(iter(correct_cmds))
                    slow(f"📘  The answer was: `{correct_sample}`")
                break
            else:
                slow("❌  Nope. (Try again, or type `hint` or `skip`.)")
        else:
            slow("❌  Nope. Try again or type `hint`.")

def holo(title="Holo‑msg"):
    slow(rf"""
       .---------------------------.
      /  /=====================\  \
     |  |  {title:^19} |  |
      \  \=====================/  / 
       '---------------------------'
    """)

def intro_ssh():
    banner("SSHD: A NEW HOPE")
    slow(textwrap.dedent("""
        It is a period of network instability. Rebel servers, hidden across
        the cloud, have lost secure contact with mission control.

        As a Field SSH Knight, your task is to restore access using nothing
        but your wits, your shell, and the sacred logs.

        🛰️  Investigate each scenario with the correct Linux commands.
        💡  Type 'hint' if you're stuck. Type 'skip' to move on after 3 attempts.
    """))
    input("\n(Press Enter to begin your mission…) ")

def ch_boot():
    banner("Challenge 1 – Is the VM Alive?")
    holo("Boot Confirmation")

    slow(textwrap.dedent("""
        Your SSH hangs—before you start troubleshooting inside the VM,
        you need to know: did it actually finish booting?
        
        What’s the best first step?
        
        A) Rerun `ssh` with `-vvv` to get debug output.
        B) Ping the VM’s public IP address.
        C) Open the Azure Portal Serial Console.
        D) Restart the VM from the Azure Portal.
    """))

    while True:
        choice = shell("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  Nice try, but SSH debug won’t tell you if the OS ever booted.")
        elif choice == "B":
            slow("❌  Ping checks network reachability, not whether the VM’s OS is up.")
        elif choice == "C":
            slow("✅  Correct! The Serial Console in Azure Portal shows kernel messages and a login prompt.")
            break
        elif choice == "D":
            slow("❌  Restarting without checking wastes time; let’s confirm it’s already running first.")
        else:
            slow("❓  Please enter A, B, C, or D.")

    slow("Great—now that you know the VM is up, you can safely dive into in‑VM diagnostics!")  


def ch_sshd_status():
    banner("Challenge 2 – Attack of the SSHD")
    holo("SSHD Status")
    slow("The OS is up, but sshd is MIA. Check its service status.")
    ask_shell(
        "ssh-hope> ",
        {"sudo systemctl status sshd", "systemctl status sshd"},
        "SSHD is running (or it's not) – either way, now you know.",
        hint="Use `systemctl` to investigate the sshd service."
    )

def ch_config_review():
    banner("Challenge 3 – Return of the Config")
    holo("SSHD Config")
    slow("Something’s off. Maybe the config was changed? Let's review the ssh configuration file.")
    ask_shell(
        "ssh-hope> ",
        {"vi /etc/ssh/sshd_config", "nano /etc/ssh/sshd_config", "cat /etc/ssh/sshd_config"},
        "The config is in your hands. Look for port, root login, and auth settings.",
        hint="What file holds sshd settings? Open it with vi, nano, or cat."
    )

def ch_sshd_logs():
    banner("Challenge 4 – A New Log")
    holo("SSHD Logs")
    slow("It won’t start, and it’s not telling you why... unless you ask the logs.")
    ask_shell(
        "ssh-hope> ",
        {"sudo journalctl -u sshd", "journalctl -u sshd"},
        "The logs reveal much. Maybe even a syntax error.",
        hint="This command shows logs from systemd-managed services."
    )

def ch_firewall():
    banner("Challenge 5 – The Firewall Debacle")
    holo("Port Blocked?")
    
    slow(textwrap.dedent("""
        Connection attempts to SSH are refused—something’s guarding the gate.
        How should you check the VM’s firewall status?
        
        A) Run `netstat -tulpn | grep :22`
        B) Inspect Network Security Group rules in Azure Portal
        C) List firewall rules on the VM (e.g., `sudo iptables -L`)
        D) Restart the firewall service with `sudo systemctl restart firewalld`
    """))

    while True:
        choice = shell("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  `netstat` shows open ports but won’t tell you about firewall rules blocking them.")
        elif choice == "B":
            slow("❌  NSG rules matter too, but here we’re focused on the VM’s internal firewall first.")
        elif choice == "C":
            slow("✅  Correct! Listing the VM’s firewall rules (iptables, ufw, or firewall‑cmd) reveals if port 22 is blocked.")
            break
        elif choice == "D":
            slow("❌  Restarting the firewall won’t show you its current rules—let’s inspect before touching it.")
        else:
            slow("❓  Please enter A, B, C, or D.")

    slow("Now that you’ve confirmed the firewall rules, you can open or adjust port 22 as needed!")  


def ch_network_test():
    banner("Challenge 6 – Rogue Packets")
    holo("TCP Path Check")
    slow("It works from inside the subnet... but not outside? Let's test the TCP path to port 22. Just give a base command...")
    ask_shell(
        "ssh-hope> ",
        {"nc", "telnet", "psping", "test-netconnection"},
        "A clean TCP handshake means the port is reachable!",
        hint="Forget ping. Test port 22 with netcat, nc, telnet, or PowerShell."
    )

def ch_live_monitor():
    banner("Challenge 7 – The Journalctl Awakens")
    holo("Live Auth Log")
    slow("Does the server *know* someone is connecting? How can you see live attempts?")
    ask_shell(
        "ssh-hope> ",
        {"sudo journalctl -f -u sshd", "journalctl -f -u sshd"},
        "You’re now monitoring live SSH connection attempts.",
        hint="Use `-f` to follow the action in real time."
    )

def ch_debug_level():
    banner("Challenge 8 – Debug of the Jedi")
    holo("Increase Verbosity")
    slow("The logs are vague. How can we turn up the signal to DEBUG3.")
    ask_shell(
        "ssh-hope> ",
        {"loglevel debug3", "edit sshd_config loglevel debug3", "sudo vi /etc/ssh/sshd_config", "sshd_config"},
        "Debugging enabled. Let the truth flood the logs.",
        hint="Which LogLevel gives you max output in sshd_config?"
    )

def ch_custom_port():
    banner("Challenge 9 – Port of No Return")
    holo("Custom Port?")
    slow("SSH is listening... just not on 22. Check the config for the port.")
    ask_shell(
        "ssh-hope> ",
        {"grep Port /etc/ssh/sshd_config", "cat /etc/ssh/sshd_config | grep Port", "cat /etc/ssh/sshd_config"},
        "Port 2222?! No wonder you're locked out.",
        hint="Search the config file for the port setting."
    )

def ch_ssh_verbosity():
    banner("Challenge 10 – SSH Client Debugging")
    holo("Verbose Mode")

    slow(textwrap.dedent("""
        Your SSH connection fails without much detail.
        To diagnose client‑side what’s happening, which option turns on full verbosity?

        A) `ssh -v user@vm`
        B) `ssh -vv user@vm`
        C) `ssh -vvv user@vm`
        D) `ssh --verbose user@vm`
    """))

    while True:
        choice = shell("Choose [A/B/C/D]: ").upper()
        if choice == "A":
            slow("❌  Single `-v` gives some detail but not the full picture.")
        elif choice == "B":
            slow("❌  Double `-vv` is more verbose but there’s still one more level.")
        elif choice == "C":
            slow("✅  Correct! `-vvv` enables maximum verbosity for the SSH client.")
            break
        elif choice == "D":
            slow("❌  `--verbose` isn’t a valid SSH flag—stick with the `-v` family.")
        else:
            slow("❓  Please enter A, B, C, or D.")

    slow(textwrap.dedent("""
        Now you can rerun:
          `ssh -vvv user@vm`
        and inspect every step of the connection handshake.
    """))


def finale_ssh():
    banner("MISSION COMPLETE")
    slow("Access restored. You can now log in. SSHD is secure once more. 🚀")

def main():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    intro_ssh()
    ch_boot()
    ch_sshd_status()
    ch_config_review()
    ch_sshd_logs()
    ch_firewall()
    ch_network_test()
    ch_live_monitor()
    ch_debug_level()
    ch_custom_port()
    ch_ssh_verbosity()
    finale_ssh()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n💀  Mission aborted. May the logs guide you next time.")
