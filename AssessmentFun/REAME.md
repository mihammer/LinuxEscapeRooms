# ROOT’S REVENGE – Linux Escape Room

## Overview
**ROOT’S REVENGE** is a text-based “escape room” game designed to help students review the **six core modules** from the *Linux Foundations* training course.  
Each module is presented as a themed challenge where you face ROOT’s taunts and solve Linux questions to progress.  

The goal is to make review sessions **fun, interactive, and memorable** while reinforcing key Linux concepts.

---

## Purpose
This escape room is intended for:
- Students completing the *Linux Foundations* course.
- Anyone wanting to review and test their Linux knowledge in an engaging way.
- Instructors looking for an interactive review activity.

The six modules match the course’s core learning areas:

| Module # | Title                                           |
|----------|-------------------------------------------------|
| 1        | Linux OS Fundamentals – ROOT’S Revenge          |
| 2        | Logfile Mayhem – Linux Appendix                 |
| 3        | Package Management – The Update Apocalypse      |
| 4        | Linux on Azure – Azure Agent Ops                |
| 5        | Network Concepts – The Root of All Problems     |
| 6        | Storage Concepts – Root of All Space Problems   |

---

## How to Run
1. Ensure you have **Python 3** installed.
2. Clone or download this repository to your local machine.
3. In your terminal, navigate to the folder containing the game files.
4. Run:
      python3 assessment.py
5. Follow on-screen prompts to choose a challenge module or access settings.



## Gameplay

* Select a module from the **Main Menu**.
* Read the scenario introduction.
* Answer multiple-choice questions to proceed.
* You may encounter ROOT’s random **taunts** or **story events** between questions.
* Finish all questions in a module to see your outro message.

### Controls During Questions

You can type:

* `A`, `B`, `C`, or `D` – to answer the current question.
* `hint` – to see a helpful clue (if available).
* `skip` – to skip the current question and move on.
* `quit` – to quit the current module and return to the main menu.

---

## Settings Menu

From the main menu, choose **Settings** to customize your gameplay:

| Setting            | Description                                         |
| ------------------ | --------------------------------------------------- |
| **Typing delay**   | Controls text “slow scroll” speed (0 for instant).  |
| **Color**          | (Reserved) Toggle color text output on/off.         |
| **Taunts**         | Enable or disable ROOT’s taunts/story events.       |
| **Shuffle MC**     | Shuffle multiple-choice answer order.               |
| **Reveal answers** | Show the explanation after a correct answer.        |
| **Spacing**        | Add a blank line between questions for readability. |
| **Seed**           | Set a random seed for repeatable question shuffles. |

**Commands in Settings:**

```
delay <n>       # e.g., delay 0.003
color on/off
taunts on/off
shuffle on/off
reveal on/off
spacing on/off
seed <int>      # e.g., seed 42
back            # return to main menu
```

---

## File Structure

```
.
├── assessment.py         # Main game menu and loop
├── utils.py              # Shared game functions, settings, and flow control
├── module1.py … module6.py # Module scripts (intro, quiz, outro)
├── questions/            # JSON files with module question sets
└── README.md             # This file
```

---

## Tips

* If you want the **Welcome Banner** to stay longer, adjust the `assessment.py` `main()` to pause before showing the main menu.
* All questions are in JSON files; you can easily add, edit, or translate them.
* Perfect for use in classrooms, workshops, or self-study.

---

## License

This project is provided for educational purposes.
You may modify and adapt it for your training needs.

```
