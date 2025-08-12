from utils import slow, banner, ask_shell
import textwrap
import time

def show_box(label="Mysterious"):
    slow(r"""
      ______________________
     / ____________________ \
    | |                    | |
    | |    {0:^14}    | |
    | |____________________| |
     \______________________/
    """.format(label))

def challenge_intro():
    banner("GRAIN SILO DEFUSER")
    slow(textwrap.dedent("""
           ||     Trapped in a grain silo with a ticking bomb made from a
          ||||    Raspberry Pi, a leaf blower, and a suspicious amount of
          ||||    duct tape. McGyver would be proud—if you make it out alive.
         ||||||
        ||||||||  The dusty console before you is your only tool.
        ||||||||  Each Linux command snips a wire, disables a sensor, or
        ||||||||  unlocks a new compartment.
        ||||||||  
                         
        ⚡ Type like your life depends on it (because it does).
        ⚡ After three missteps, type 'hint' or 'skip' (but every skip
           leaves another wire uncut).

        The digital clock is counting down… GO!
    """))
    input("\n(Press Enter to cut the red wire…) ")

def challenge_quiz():
    # 1. Fstab
    banner("Challenge 1 – Sabotaged Wiring (fstab)")
    slow("The silo shakes. A boot error flashes up and `/etc/fstab` blinks on the grain-dusted screen:")
    print(r"""
# <file system> <mount point> <type> <options> <dump> <pass>
1: UUID=102ee66d-b0c0-4d1c-8087-f5c32873987e /        ext4 defaults 0 1
2: /dev/sda1                               /boot     ext2 defaults 0 2
3: /dev/sdzzz                              /home     ext4 defaults 0 2
""")
    slow("Which number is the bogus wire (bad config)? (Type just the number)")
    ask_shell("> ", {"3"},
        "‘/dev/sd-zzz’ isn’t a real disk—if you’d cut that wire for real, you’d be toast.",
        hint="Device names are usually sda1, sdb2, etc. Never sdzzz.")

    # 2. top/CPU
    banner("Challenge 2 – Hot Circuit (CPU Hog)")
    slow("A ‘top’ readout scrolls by, like green numbers on an old-school detonator:")
    print("""
PID   USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
1245  root      20   0  392344  84212  10200 S   0.3  2.1   0:02.34 sshd
2842  postgres  20   0  865320 123456  18532 S   1.1  5.8   1:24.56 postgres
9111  apache    20   0  432456  65234   9056 R  45.2  4.1   5:45.89 httpd
1324  root      20   0  128000  10240   2048 S   0.0  0.5   0:01.11 systemd
""")
    slow("Which process is about to blow the CPU fuse?")
    ask_shell("> ", {"httpd", "apache"},
        "`httpd` is melting the CPU. Quick—hit that process!",
        hint="Match the highest %CPU to its command.")

    # 3. Log location and tail
    banner("Challenge 3 – Log Silo Secrets")
    show_box("Log Box")
    slow("A rusted box opens. A whisper: “Where do the logs live, farmhand?”")
    ask_shell("log> ", {"/var/log", "var/log"},
        "Most logs hide in `/var/log`—good work, silo ninja.",
        hint="Starts with `/var`, relates to system messages.")

    slow("You find a wrinkled slip: 'messages'. To snip the next wire, show the final 10 log lines.")
    ask_shell("log-paper> ",
        {"tail -n 10 /var/log/messages", "tail /var/log/messages -n 10", "tail /var/log/messages"},
        "`tail -n 10` grabs those last crucial clues.",
        hint="Use `tail` to see the end of a file.")

    # 4. Kernel version
    banner("Challenge 4 – The Kernel Core")
    show_box("Kernel Box")
    slow("A chirpy voice from a grain elevator speaker: “What command reveals the **running kernel version**?”")
    ask_shell("kernel-box> ",
        {"uname -r", "uname -a"},
        "`uname -r` spills the kernel version. You almost hear applause.",
        hint="Ends in ‘name’, starts with ‘u’.")

    # 5. SSH daemon
    banner("Challenge 5 – SSH Sensor")
    show_box("SSH Box")
    slow("Can’t SSH into the silo, but check if the daemon is alive anyway.")
    ask_shell("ssh-box> ",
        {"systemctl status ssh", "systemctl status sshd",
         "service ssh status", "service sshd status",
         "ps -ef | grep sshd", "pgrep sshd"},
        "`systemctl status sshd` shows the service’s pulse.",
        hint="Try `systemctl`, `service`, or a process check.")

    # 6. PATH
    banner("Challenge 6 – Environmental Duct Tape")
    show_box("PATH Box")
    slow("Quick, print the $PATH env-var—the only way to find the right tool in a pinch!")
    ask_shell("path-box> ",
        {"echo $path", "echo $PATH", "printenv path", "printenv PATH"},
        "`echo $PATH`—never leave home without it.",
        hint="Use `echo` or `printenv`.")

    # 7. Azure serial console
    banner("Challenge 7 – Plan C: Azure Console")
    show_box("Azure Box")
    slow("SSH’s fried. What Azure tool lets you see the boot screen anyway?")
    ask_shell("azure-box> ",
        {"serial console", "console"},
        "The Azure Serial Console’s your digital crowbar.",
        hint="It’s a special console that works even when SSH doesn’t.")

    # 8. Which python
    banner("Challenge 8 – Pythonic Diffuser")
    show_box("Python Box")
    slow("Which command shows what `python` binary will execute if you type ‘python’? Your last hope!")
    ask_shell("python-box> ",
        {"which python", "type -a python", "command -v python"},
        "`which python` tells you which python runs—just in time.",
        hint="Try `which`, `type`, or `command` plus `python`.")

    challenge_outro()

def challenge_outro():
    banner("FINAL SECONDS")
    slow("You mash the last key. The timer pauses. A tense silence…")
    time.sleep(2)
    slow("…and then: 🎉  The bomb defuses! You stumble out, grain in your hair and a heroic grin on your face.")
    slow("Will anyone believe your story? Only if you pass the next Linux escape room…")

