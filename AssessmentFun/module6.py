from utils import slow, banner, holo, shell, random_story_event, ask_multiple_choice
import textwrap
import random

EXTRA_TAUNTS = [
    "\nROOT: 'Is your disk full, or just your mind?'",
    "\nROOT: 'I swapped your swap. Good luck paging your way out of this.'",
    "\nROOT: 'Pro tip: The only thing more fragile than your storage is your ego.'",
    "\nROOT: 'Mount failure? Maybe try... unplugging and plugging back in?'",
    "\nROOT: 'UUID? More like U-R-stuck!'"
]

def root_taunt():
    if random.random() < 0.5:
        slow(random.choice(EXTRA_TAUNTS))
    else:
        random_story_event()

def challenge_intro():
    banner("STORAGE: ROOT OF ALL SPACE PROBLEMS")
    slow(textwrap.dedent("""
        [A mysterious ticking echoes from deep within your file system...]
        ROOT: "Welcome to storage chaos! Filesystems corrupted, disks swapped, fstab entries misaligned.
        Let's see if you can keep your data safe, or if you'll run out of space... and patience!"
    """))
    input("\n(Press Enter to test your storage resilience...) ")

def challenge_quiz():
    ask_multiple_choice(
        prompt="Which is the recommended disk to set up for swapping?\nType 'hint' for a clue!",
        options=[
            "OS disk",
            "Data disk",
            "Resource disk",
            "NFS/CIFS Share"
        ],
        correct_index=2,
        explanation="✅ Resource disk is recommended for swap—just remember, it’s temporary!",
        qnum=1,
        hint="This disk is temporary and designed for fast local storage on VMs."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Customers should only use the resource disk to store their volatile data because:\nType 'hint' for a clue!",
        options=[
            "The resource disk can be removed from the Azure portal",
            "The resource disk gets formatted when the VM is shut down.",
            "The resource disk will be provisioned and formated when VM switches over to new host during redeploy, resize and service healing.",
            "The resource disk is slower than a data disk"
        ],
        correct_index=2,
        explanation="✅ Resource disk can be wiped anytime the VM is moved, resized, or redeployed.",
        qnum=2,
        hint="It disappears or is reformatted when the VM moves, resizes, or is redeployed."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="How would you detect but not autocorrect filesystem corruption?\nType 'hint' for a clue!",
        options=[
            "fsck -a <device>",
            "sync",
            "mkfs2 <device>",
            "fsck -n <device>"
        ],
        correct_index=3,
        explanation="✅ `fsck -n <device>` checks for errors, but doesn't attempt repair.",
        qnum=3,
        hint="The answer is an fsck option that prevents making changes."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="A user is not able to create any file locally on a mounted filesystem, but the device can be unmounted and remounted successfully. What WOULDN'T be the reason for this behaviour?\nType 'hint' for a clue!",
        options=[
            "The filesystem is corrupted.",
            "df -h shows 100% disk utilization.",
            "df -h shows disk is available but df -ih shows 100% inode utilization.",
            "mount command shows the following details\n/dev/sdc1 on /mnt/resource type ext4 (ro,relatime,seclabel,data=ordered)"
        ],
        correct_index=0,
        explanation="✅ If you can remount the device, it’s probably *not* due to a corrupted filesystem.",
        qnum=4,
        hint="If you can unmount and remount, the filesystem is probably *not* corrupted."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="What is the correct syntax to show the filesystem type of the mounted mountpoints?\nType 'hint' for a clue!",
        options=[
            "df -h",
            "fdisk",
            "df -Th",
            "du -sh"
        ],
        correct_index=2,
        explanation="✅ `df -Th` displays filesystem type and usage.",
        qnum=5,
        hint="Add a capital T to the classic disk free command."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Which is the correct sequence of steps for creating an ext4 file system on a new disk(sdd) and making it mount automatically across reboots?\nType 'hint' for a clue!",
        options=[
            "fdisk /dev/sdd , n (creating a new partition), select default for all, w  (save) , partprobe to update the kernel about the new partition, mkfs.ext4 /dev/sdd1, create a mountpoint and add its entry in /etc/fstab",
            "fdisk /dev/sdd , p (creating a new partition, select default for all, w (save) and mkfs.ext4 /dev/sdd1 and add the entry in /etc/fstab",
            "fdisk /dev/sdd , n (creating a new partition), select default for all, w  (save) , partprobe to update the kernel about the new partition and mkfs.ext4 /dev/sdd1 and use the mount command to mount the newly created file system",
            "fdisk /dev/sdd , n (creating a new partition), select default for all, w  (save) and mkfs.ext4 /dev/sdd1 and use the mount command to mount the newly created file system"
        ],
        correct_index=0,
        explanation="✅ The correct process: fdisk, partprobe, mkfs.ext4, mountpoint, and /etc/fstab entry.",
        qnum=6,
        hint="Look for the answer that mentions partprobe, mkfs.ext4, and an fstab entry."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="Which is the recommended way of specifying the block device in /etc/fstab file to mount a filesystem?\nType 'hint' for a clue!",
        options=[
            "Use disk Universally Unique Identifier (UUID)",
            "Use disk names",
            "Use LUN number",
            "Use disk URL"
        ],
        correct_index=0,
        explanation="✅ UUIDs are stable across reboots, unlike device names.",
        qnum=7,
        hint="This method is stable, unique, and recommended by Linux docs."
    )
    root_taunt()

    ask_multiple_choice(
        prompt="What is the correct syntax to check the size of a file?\nType 'hint' for a clue!",
        options=[
            "df -h <filename>",
            "du -sh <filename>",
            "fdisk <filename>",
            "cat <filename>"
        ],
        correct_index=1,
        explanation="✅ `du -sh <filename>` reports size in a human-readable format.",
        qnum=8,
        hint="It's the disk usage command with human-readable and summary flags."
    )
    root_taunt()

def challenge_outro():
    banner("STORAGE BOSS: SPACE RECLAIMED")
    slow("ROOT: 'I see you’ve mounted a defense… this time. Watch your fstab. I never truly unmount.'")
