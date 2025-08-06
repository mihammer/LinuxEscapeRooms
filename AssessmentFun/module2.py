from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap

def challenge_intro():
    banner("LINUX APPENDIX: LOGFILE MAYHEM")
    slow(textwrap.dedent("""
        [The air is thick with log rotation and mysterious errors.]
        ROOT: "You've escaped once, but can you navigate the wilds of /var/log? Every mistake in here echoes forever..."
    """))
    input("\n(Press Enter to face the chaos...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="What's the correct syntax to append data to the existing file named 'record'?\nType 'hint' for a clue!",
        options=[
            'echo "text" >> record',
            'echo "………" | record',
            'more record',
            'cat record'
        ],
        correct_index=0,
        explanation="✅ Use `echo \"text\" >> record` to append data to the file.",
        qnum=11,
        hint="The operator for appending is two greater-than signs with no space."
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to print only lines that have the word 'successfully' in /var/log/yum.log?\nType 'hint' for a clue!",
        options=[
            'echo "successfully" /var/log/yum.log',
            'vi /var/log/yum.log | grep successfully',
            'less /var/log/yum.log | Successfully',
            'grep -i SuccessfullY /var/log/yum.log'
        ],
        correct_index=3,
        explanation="✅ `grep -i SuccessfullY /var/log/yum.log` prints lines (case-insensitive) containing 'successfully'.",
        qnum=12,
        hint="You want a search that's case-insensitive. Which command does that?"
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to view new records being appended to a file?\nFor example: /var/log/messages\nType 'hint' for a clue!",
        options=[
            'cat /var/log/messages',
            'tail -f /var/log/messages',
            'less /var/log/messages',
            'more /var/log/messages'
        ],
        correct_index=1,
        explanation="✅ `tail -f /var/log/messages` follows new entries in real time.",
        qnum=13,
        hint="This command follows a file as it grows."
    )

    ask_multiple_choice(
        prompt="A file named 'alphabets' contains the alphabet letters in mixed order one per line.\nWhat's the correct syntax to display the file contents sorted in reverse alphabetical order?\nType 'hint' for a clue!",
        options=[
            'sort -n alphabets',
            'sort -disorder alphabets',
            'sort -r alphabets',
            'sort alphabets'
        ],
        correct_index=2,
        explanation="✅ `sort -r alphabets` sorts the file in reverse order.",
        qnum=14,
        hint="The option for reverse is a single dash and a single letter."
    )

    ask_multiple_choice(
        prompt="Which command collects configuration/system/diagnostic information on RHEL and sometimes other distributions?\nType 'hint' for a clue!",
        options=[
            'sosreport',
            'sar',
            'supportconfig',
            'kdump'
        ],
        correct_index=0,
        explanation="✅ `sosreport` is the go-to diagnostic info collector.",
        qnum=15,
        hint="This command sounds like it's asking for help."
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to configure a service to start automatically across reboots on RHEL 7+?\nType 'hint' for a clue!",
        options=[
            'service <daemon> reboot',
            'chkconfig <daemon>  on',
            'systemctl is-enabled <daemon>',
            'systemctl enable <daemon>'
        ],
        correct_index=3,
        explanation="✅ `systemctl enable <daemon>` makes the service auto-start on boot.",
        qnum=16,
        hint="Use the modern service manager and an 'enable' command."
    )

    ask_multiple_choice(
        prompt="Which utility can provide historical data of system activity and resource utilization?\nType 'hint' for a clue!",
        options=[
            'sar',
            'cat /proc/meminfo',
            'dmesg',
            'swapon'
        ],
        correct_index=0,
        explanation="✅ `sar` is the Swiss Army knife for system activity history.",
        qnum=17,
        hint="This command's name starts with 's' and is three letters long."
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to list the cron jobs for the root user?\nType 'hint' for a clue!",
        options=[
            'cat /etc/cron/root',
            'sudo crontab -l',
            'crontab -U root -l',
            'crontab -a | grep root'
        ],
        correct_index=1,
        explanation="✅ `sudo crontab -l` lists root's cron jobs.",
        qnum=18,
        hint="It's a command run as root, and the option lists jobs."
    )

    ask_multiple_choice(
        prompt="How do you identify a soft link file (shortcut) in ls -l output?\nType 'hint' for a clue!",
        options=[
            'First character of the output is s',
            'Second character of the output is l',
            'First character of the output is r',
            'First character of the output is l'
        ],
        correct_index=3,
        explanation="✅ The first character being 'l' means it's a symbolic link.",
        qnum=19,
        hint="Look for the very first character in the permissions string."
    )

def challenge_outro():
    banner("APPENDIX DEFEATED")
    slow("ROOT: 'You tamed the logs—for now. Enjoy your victory, hero of /var/log!'")
