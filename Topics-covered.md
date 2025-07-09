
Below are a list of commands covered in the Linux escape rooms
_________________________________________________________________

## "deathshellescape.py" Star Wars–themed escape room game:

### 🧠 Topics by Challenge:

1. **User Management – Add User**
   `useradd`, `sudo useradd`

2. **Memory Usage**
   `free`, `free -h`

3. **System Monitoring**
   `top`

4. **Process Management – Kill a Process**
   `kill`, `kill -9`

5. **File Permissions**
   `chmod 755`

6. **User Management – Delete User**
   `userdel`, `sudo userdel`

7. **Text Searching**
   `grep`

8. **Symbolic Links**
   `ln -s`

9. **Disk I/O Statistics**
   `iostat`

10. **System Diagnostic Tools**
    `sosreport`, `supportconfig`


---------------------------------------------------

## linuxendgame.py -  Avengers-style "Time Heist" narrative
Here's a list of **Linux topics** covered in the Marvel-themed game **“LINUX: ENDGAME”**:

### 🧠 Topics by Challenge:

1. **Crontab Editing**
   `crontab -e`, `sudo crontab -e`

2. **Check System Date**
   `date`

3. **Install Packages (RHEL/Fedora)**
   `dnf install`, `yum install`

4. **Install Packages (Ubuntu/Debian)**
   `apt install`, `apt-get install`

5. **Azure Resource Disk Config**
   `cat /etc/waagent.conf`

6. **Restart Network Services**
   `systemctl restart network`, `networkmanager`, or `service network restart`

7. **View IP Address**
   `ip addr show`, `ip addr`

8. **Packet Capture**
   `tcpdump`

9. **View Mounted Filesystems**
   `mount`

10. **List Block Devices**
    `lsblk`

11. **Check Disk Space**
    `df`, `df -h`, `df -H`


---------------------------------------------------

## linuxescaperoom.py - 


**FSTAB & Filesystem Devices**
Detect an invalid device path (/dev/sdzzz) in `/etc/fstab`.
Topic: Filesystem mounting and Linux disk naming

**CPU Usage via top**
Identify the command (httpd) using the most CPU.
Topic: Process monitoring with `top`

**Log Files & tail**
Know where logs are (/var/log) and how to read the last lines of a log file.
Topics: Log file locations, using `tail`

**Check Kernel Version**
Use `uname -r` or `uname -a` to get running kernel info.
Topic: System and kernel identification

**Check SSH Daemon Status**
Determine if sshd is running using `systemctl`, service, or ps/pgrep.
Topic: Service management and process checks

**View Environment Variables (PATH)**
Display the current `PATH` variable using `echo`, `printenv`.
Topic: Environment variables and shell configuration

**Azure Serial Console**
Know that “Serial Console” can be used when SSH is blocked on Azure.
Topic: Cloud troubleshooting (Azure-specific)

**Find Which Python Will Run**
Use `which`, `type -a`, or command -v to locate the python binary.
Topic: Command resolution and executable lookup

------------------------------------------------------

## raidersofthelostshell.py

**Current Working Directory**
Command: `pwd`
Topic: Navigation basics

**Listing Hidden Files**
Command: `ls -a`
Topic: File visibility and dotfiles

**Viewing Running Processes**
Command: `ps`
Topic: Process management

**Kernel Version**
Command: `uname -r` / `uname -a`
Topic: System/kernel identification

**Checking if SSH is Running**
Commands: `systemctl` status sshd, service ssh status, pgrep sshd, etc.
Topic: Systemd/service status, SSH daemon

**Viewing Last 10 Lines of a Log File**
Commands: `tail`, `tail -n 10`
Topic: Log analysis and file inspection

**Sorting Files by Modification Time**
Commands: `ls -lt`, `ls -t`
Topic: File timestamps and sorting

**Who Is Logged In**
Commands: `who`, `w`
Topic: User sessions and login tracking

**Viewing File Contents**
Commands: `cat`, `less`, `nano`
Topic: File inspection before execution



## All commands covered:
Here's a consolidated list of **Linux commands** used across all the escape room games you mentioned:

---

### 🔧 **User Management**

* `useradd`, `sudo useradd`
* `userdel`, `sudo userdel`

---

### 📊 **System Monitoring & Process Management**

* `top`
* `ps`
* `kill`, `kill -9`
* `pgrep`
* `w`
* `who`

---

### 💾 **Disk & Filesystem**

* `df`, `df -h`, `df -H`
* `mount`
* `lsblk`
* `cat /etc/fstab`
* `cat /etc/waagent.conf`

---

### 🔐 **Permissions & Ownership**

* `chmod 755`

---

### 🧩 **File & Directory Operations**

* `pwd`
* `ls`, `ls -a`, `ls -lt`, `ls -t`
* `cat`, `less`, `nano`
* `tail`, `tail -n 10`
* `ln -s`
* `which`, `type -a`, `command -v`

---

### 🔍 **Searching & Text Processing**

* `grep`

---

### 🧠 **Environment Variables & System Info**

* `echo $PATH`, `printenv`
* `uname -r`, `uname -a`
* `date`
* `free`, `free -h`

---

### 🔄 **Service & Network Management**

* `systemctl status/restart sshd/network`
* `service ssh/network restart`
* `ip addr show`, `ip addr`

---

### 🌐 **Networking & Packet Inspection**

* `tcpdump`

---

### 🧰 **Diagnostics & Utilities**

* `sosreport`, `supportconfig`
* `iostat`

---

### 🕰️ **Scheduling**

* `crontab -e`, `sudo crontab -e`

---

### 📦 **Package Management**

* `dnf install`, `yum install`
* `apt install`, `apt-get install`

---

Let me know if you want this grouped by difficulty level, theme, or turned into a printable cheat sheet!
