from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap

def challenge_intro():
    banner("CLOUD COMMAND: AZURE AGENT OPS")
    slow(textwrap.dedent("""
        [A digital storm brews over your Azure dashboard. Alarms flash: waagent out of sync!]
        ROOT: "Welcome, Azure Operator. I've left a few... surprises in your waagent and LIS driver configs.
        Will you bring stability to your VMs, or will Root's chaos reign in the cloud?"
    """))
    input("\n(Press Enter to accept your Azure Ops mission...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="Which task does not require waagent's help?\nType 'hint' for a clue!",
        options=[
            "Logging to a Linux VM with an existing user",
            "Deploying a Custom Script Extension to a Linux VM",
            "Successfully taking Backup of a Linux VM",
            "Creating a user for the Linux VM from Azure Portal"
        ],
        correct_index=0,
        explanation="✅ Logging in with an existing user doesn't need waagent.",
        qnum=1,
        hint="This task is entirely local to the Linux OS—waagent isn’t involved."
    )

    ask_multiple_choice(
        prompt="How would you check the waagent service status in Ubuntu 20.04 LTS?\nType 'hint' for a clue!",
        options=[
            "waagent –status",
            "systemctl status walinuxagent",
            "walinuxagent –version",
            "systemctl waagent status"
        ],
        correct_index=1,
        explanation="✅ `systemctl status walinuxagent` is the proper check for Ubuntu 20.04+.",
        qnum=2,
        hint="The service is called 'walinuxagent' and you want its status."
    )

    ask_multiple_choice(
        prompt="Where would you check the libraries for waagent and other related extensions?\nType 'hint' for a clue!",
        options=[
            "/var/lib/azure",
            "/usr/lib/waagent",
            "/var/lib/waagent",
            "/usr/lib/azure"
        ],
        correct_index=2,
        explanation="✅ `/var/lib/waagent` holds libraries for waagent and extensions.",
        qnum=3,
        hint="It's under /var/lib and matches the agent name."
    )

    ask_multiple_choice(
        prompt="What's the correct syntax to list the loaded LIS drivers?\nType 'hint' for a clue!",
        options=[
            "hv_utils –version",
            "modinfo hv_utils and check the vermagic",
            "lsmod | grep -E '(hyperv|hv)'",
            "lsmod hv_utils"
        ],
        correct_index=2,
        explanation="✅ `lsmod | grep -E '(hyperv|hv)'` shows loaded LIS drivers.",
        qnum=4,
        hint="You want to see all modules with hyperv or hv in their name."
    )

    ask_multiple_choice(
        prompt="What is the recommended way of upgrading the LIS drivers?\nType 'hint' for a clue!",
        options=[
            "Download and install from https://aka.ms/lis",
            "Upgrade the Kernel",
            "Install hyper-v package from repository",
            "None of these"
        ],
        correct_index=1,
        explanation="✅ The recommended way is to upgrade the kernel.",
        qnum=5,
        hint="LIS drivers are baked right into the Linux kernel these days."
    )

    ask_multiple_choice(
        prompt="There is a known issue with the waagent version running in the customer’s virtual machine. What is the recommended action plan?\nType 'hint' for a clue!",
        options=[
            "Share the known issue details with the customer and suggest upgrading the waagent from the repository",
            "Share the known issue details with  the customer and suggest upgrading the waagent from GitHub",
            "Raise a ticket to Azure Linux Escalation Team for confirming this issue",
            "Raise a ticket to AzLinux Product group to confirm this issue"
        ],
        correct_index=0,
        explanation="✅ Share the known issue and recommend upgrading waagent from the repository.",
        qnum=6,
        hint="The best answer is to recommend an upgrade from official repos, not GitHub or a ticket."
    )

    ask_multiple_choice(
        prompt="Where would you look for logs of azure extensions deployed via waagent?\nType 'hint' for a clue!",
        options=[
            "/var/log/waagent",
            "/var/log/azure",
            "/var/lib/azure",
            "/etc/waagent.conf"
        ],
        correct_index=1,
        explanation="✅ `/var/log/azure` is where Azure extension logs live.",
        qnum=7,
        hint="Look in /var/log/—the folder name matches the cloud provider."
    )

def challenge_outro():
    banner("AZURE AGENT OPS: CLOUD RESTORED")
    slow("ROOT: 'You outmaneuvered my Azure chaos... but I'll be back, Operator. The cloud is always shifting.'")
