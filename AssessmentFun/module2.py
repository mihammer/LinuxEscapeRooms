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
        prompt="What's the correct syntax to append data to the existing file named 'record'?",
        options=[
            'echo "text" >> record',
            'echo "………" | record',
            'more record',
            'cat record'
        ],
        correct_index=0,
        explanation="✅ Use `echo \"text\" >> record` to append data to the file.",
        qnum=11
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to print only lines that have the word 'successfully' in /var/log/yum.log?",
        options=[
            'echo "successfully" /var/log/yum.log',
            'vi /var/log/yum.log | grep successfully',
            'less /var/log/yum.log | Successfully',
            'grep -i SuccessfullY /var/log/yum.log'
        ],
        correct_index=3,
        explanation="✅ `grep -i SuccessfullY /var/log/yum.log` prints lines (case-insensitive) containing 'successfully'.",
        qnum=12
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to view new records being appended to a file?\nFor example: /var/log/messages",
        options=[
            'cat /var/log/messages',
            'tail -f /var/log/messages',
            'less /var/log/messages',
            'more /var/log/messages'
        ],
        correct_index=1,
        explanation="✅ `tail -f /var/log/messages` follows new entries in real time.",
        qnum=13
    )

    ask_multiple_choice(
        prompt="A file named 'alphabets' contains the alphabet letters in mixed order one per line.\nWhat's the correct syntax to display the file contents sorted in reverse alphabetical order?",
        options=[
            'sort -n alphabets',
            'sort -disorder alphabets',
            'sort -r alphabets',
            'sort alphabets'
        ],
        correct_index=2,
        explanation="✅ `sort -r alphabets` sorts the file in reverse order.",
        qnum=14
    )

    ask_multiple_choice(
        prompt="Which command collects configuration/system/diagnostic information on RHEL and sometimes other distributions?",
        options=[
            'sosreport',
            'sar',
            'supportconfig',
            'kdump'
        ],
        correct_index=0,
        explanation="✅ `sosreport` is the go-to diagnostic info collector.",
        qnum=15
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to configure a service to start automatically across reboots on RHEL 7+?",
        options=[
            'service <daemon> reboot',
            'chkconfig <daemon>  on',
            'systemctl is-enabled <daemon>',
            'systemctl enable <daemon>'
        ],
        correct_index=3,
        explanation="✅ `systemctl enable <daemon>` makes the service auto-start on boot.",
        qnum=16
    )

    ask_multiple_choice(
        prompt="Which utility can provide historical data of system activity and resource utilization?",
        options=[
            'sar',
            'cat /proc/meminfo',
            'dmesg',
            'swapon'
        ],
        correct_index=0,
        explanation="✅ `sar` is the Swiss Army knife for system activity history.",
        qnum=17
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to list the cron jobs for the root user?",
        options=[
            'cat /etc/cron/root',
            'sudo crontab -l',
            'crontab -U root -l',
            'crontab -a | grep root'
        ],
        correct_index=1,
        explanation="✅ `sudo crontab -l` lists root's cron jobs.",
        qnum=18
    )

    ask_multiple_choice(
        prompt="How do you identify a soft link file (shortcut) in ls -l output?",
        options=[
            'First character of the output is s',
            'Second character of the output is l',
            'First character of the output is r',
            'First character of the output is l'
        ],
        correct_index=3,
        explanation="✅ The first character being 'l' means it's a symbolic link.",
        qnum=19
    )

def challenge_outro():
    banner("APPENDIX DEFEATED")
    slow("ROOT: 'You tamed the logs—for now. Enjoy your victory, hero of /var/log!'")
