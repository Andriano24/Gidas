# G.I.D.A.S. - Genshin Impact Dialogue Autoskip Script

> **DISCLAIMER:** You are using this software at your own risk. I am not responsible for anything that happens to your account.

## Overview

A simple script that detects if there is an active dialogue to skip.

## How it works

* Runs only if the script is enabled and the active window is the game.
* Captures a frame from a region of the screen.
* Analyzes pixels of the frame.
* If a dialogue is found, it presses the "F" key at a random pace.

*No injections or memory readings are happening at any time.*

## Usage

### Option 1: From releases (Recommended)

1. Download the executable from the latest release.
2. Open the executable.

### Option 2: From source

1. Download or clone the repository:

```text
git clone git@github.com:Andriano24/Gidas.git
cd Gidas
```

1. Create a virtual environment

```text
python -m venv .venv
```

1. Activate the virtual environment.

```text
.\.venv\Scripts\activate
```

1. Download the dependencies.

```text
pip install -r .\requirements.txt
```

1. Run the script.

```text
python main.py
```

## Controls

| Key | Action | Description |
| --- | ------ | ----------- |
| **F9** | Toggle | Enables or disables the script |
| **F10** | Benchmark | Shows a benchmark summary of the resources the script uses |

## Limitations

* The only screen size supported is 1920x1080.
* The game has to run in fullscreen or borderless.
* No custom keybinds support.
* No controller support.
* Always chooses the first option.
