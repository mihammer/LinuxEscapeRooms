from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap

def challenge_intro():
    banner("LINUX ESCAPE ROOM: ROOT'S REVENGE")
    slow(textwrap.dedent("""
        [Screen flickers... Cursor blinks.]
        ROOT: "Welcome back, old friend. Think you can escape *my* terminal? Let's see if your skills are still sharp."
        ...
    """))
    input("\n(Press Enter to begin your escape...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="What is initrd (Initial RAM Disk)?",
        options=[
            "Disk partition where the boot loader is stored",
            "Temporary root file system before real root file system is mounted during the boot process",
            "It is the root file system mounted in rw (read|write) mode during boot process",
            "It contains all init programs for every runlevels"
        ],
        correct_index=1,
        explanation="✅ initrd is a temporary root filesystem used during the boot process before the real root is mounted.",
        qnum=1
    )

    ask_multiple_choice(
        prompt="Which folder is used by default to store non-system users' initial login directories?",
        options=["/etc", "/usr", "/bin", "/home"],
        correct_index=3,
        explanation="✅ /home is the default location for user home directories.",
        qnum=2
    )

    ask_multiple_choice(
        prompt="What does GRUB stand for?",
        options=[
            "Grub for Red Hat and Ubuntu Bootloader",
            "Grand Red Hat Unified Bootloader",
            "Grand Unified Bootloader",
            "Grand Rack Unix Bootloader"
        ],
        correct_index=2,
        explanation="✅ GRUB stands for Grand Unified Bootloader.",
        qnum=3
    )

    ask_multiple_choice(
        prompt="Which is the correct command to:\n1. Restart\n2. Shutdown?",
        options=[
            "1.restart    2.shutdown",
            "1.reboot     2.shutdown -h now",
            "1.reboot     2.exit",
            "1.reload     2.init 0"
        ],
        correct_index=1,
        explanation="✅ `reboot` restarts and `shutdown -h now` shuts down cleanly.",
        qnum=4
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to debug information of an SSH operation?",
        options=[
            "ssh -vv <user>@<IPADDRESS/Hostname>",
            "ssh -debug <user>@<IPADDRESS/Hostname>",
            "ssh -db <user>@<IPADDRESS/Hostname>",
            "ssh -verbo <user>@<IPADDRESS/Hostname>"
        ],
        correct_index=0,
        explanation="✅ `ssh -vv` enables verbose logging for SSH. More v's = more detail.",
        qnum=5
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to check memory utilization?",
        options=["meminfo", "memory", "free", "df"],
        correct_index=2,
        explanation="✅ `free` is the standard command to check memory usage.",
        qnum=6
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to change the user (linux) and group (azure) ownership of a file named learning_academy?",
        options=[
            "chmod linux:azure learning_academy",
            "chage linux azure learning_academy",
            "chown azure:linux learning_academy",
            "chown linux:azure learning_academy"
        ],
        correct_index=3,
        explanation="✅ `chown user:group filename` is the correct syntax.",
        qnum=7
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to grant read, write, and execute to user, and execute for others on learning_academy?",
        options=[
            "chmod u=rw,o-x learning_academy",
            "chown user=rwx,other=x learning_academy",
            "chmod 601 learning_academy",
            "chmod u=rwx,o=x learning_academy"
        ],
        correct_index=3,
        explanation="✅ `chmod u=rwx,o=x` sets the correct permissions.",
        qnum=8
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to locate a file named passwd?",
        options=[
            "search / passwd",
            "locale passwd /",
            "find / -name passwd",
            "locate / -name passwd"
        ],
        correct_index=2,
        explanation="✅ `find / -name passwd` searches from root by name.",
        qnum=9
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to update the timestamp of a file without modifying its contents?",
        options=[
            "vi <filename>",
            "cat <filename>",
            "nano <filename>",
            "touch <filename>"
        ],
        correct_index=3,
        explanation="✅ `touch` updates the modified time without altering contents.",
        qnum=10
    )

def challenge_outro():
    banner("ESCAPE ROOM: SUCCESS")
    slow("ROOT: 'Impressive. But was it luck, or skill? The logs never forget.'")
