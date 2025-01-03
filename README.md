# Meshtastic Info Bot

A simple bot that receives messages from a Meshtastic device via the TCP interface and responds to them.

## Overview

This project consists of two Python scripts:
- **Meshbot.py**: Listens for messages sent by the Meshtastic device over the network and processes them.
- **commands.py**: Defines commands the bot can respond to.

### Features
- Receive messages via the Meshtastic TCP interface
- Respond to custom commands

## Requirements

Before starting, make sure the following requirements are met:

1. **Hardware**
   - A Heltec V3 device or another Meshtastic-compatible device.
   - A network that connects your computer and the Meshtastic device.

2. **Software**
   - Python 3.7 or higher
   - The following Python packages:
     - `meshtastic`
     - `pubsub`

## Installation

### 1. Clone the Repository
Download the project files by cloning this repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Install Dependencies
Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate   # For Windows

pip install meshtastic pubsub
```

### 3. Adjust the Script
Edit the file `Meshbot.py` and replace the placeholder IP (`192.168.xxx.xx`) with the IP address of your Meshtastic device.

## Usage

### 1. Start the Bot
Run the main script:

```bash
python Meshbot.py
```

If everything is configured correctly, you will see a message indicating that the bot is connected to the Meshtastic device and is listening for messages.

### 2. Send Messages
Send a message from your Meshtastic device using one of the defined commands. Example:

```
!hello
```

The bot will respond with:

```
Hello, I am the Meshtastic Info Bot!
```

## Commands
The available commands are defined in the `COMMANDS` dictionary in the file `commands.py`. Currently, the following commands are available:

| Command     | Description                        |
|-------------|------------------------------------|
| `!hello`    | The bot responds with a greeting.  |

You can add more commands by extending the `commands.py` dictionary.

## Customization

### Adding More Commands
1. Define a new function in `commands.py`. Example:

    ```python
    def weather_command(sender_id, interface):
        interface.sendText("The current weather is sunny!", destinationId=sender_id)
    ```

2. Add the new command to the `COMMANDS` dictionary:

    ```python
    COMMANDS = {
        "!weather": weather_command,
        # additional commands...
    }
    ```

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

## Author
- Created by **Pilotkosinus** 

