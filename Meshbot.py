#!python3
# -*- coding: utf-8 -*-

"""
Simple Message Receiver
========================

This script connects to a Meshtastic device via its TCP interface
and displays received messages in the terminal.

Device IP: 192.168.xxx.xx

Author:
- Pilotkosinus

MIT License
"""

import logging
import time
from meshtastic.tcp_interface import TCPInterface
from pubsub import pub

# Importiere das Dictionary mit den Befehlen
from commands import COMMANDS

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Define the Meshtastic device IP
DEVICE_IP = "192.168.xxx.xx"

def message_listener(packet=None, interface=None):
    """
    Callback function to handle incoming messages.

    :param packet: The incoming packet from the Meshtastic device.
    :param interface: The Meshtastic interface instance (TCPInterface).
    """
    if not packet:
        return  # Falls kein Packet übergeben wurde

    if "decoded" in packet:
        message = packet["decoded"].get("text", "")
        sender_id = packet.get("from", "Unknown")

        if message:
            # Zeige jede Nachricht im Terminal an
            logger.info(f"Message from {sender_id}: {message}")

            # In Kleinschreibung umwandeln, um groß-/kleinschreibung zu ignorieren
            msg_stripped_lower = message.strip().lower()

            # Prüfe, ob die (kleingeschriebene) empfangene Nachricht in COMMANDS ist
            if msg_stripped_lower in COMMANDS:
                command_func = COMMANDS[msg_stripped_lower]
                command_func(sender_id, interface)

def main():
    """
    Connects to the Meshtastic device and listens for messages.
    """
    logger.info("Connecting to Meshtastic device...")
    
    try:
        # Connect to the Meshtastic device using its TCP interface
        interface = TCPInterface(hostname=DEVICE_IP)

        # Subscribe to the message receive topic.
        pub.subscribe(message_listener, "meshtastic.receive")

        logger.info("Connected successfully. Listening for messages...")

        # Keep the script running to listen for messages
        while True:
            time.sleep(1)

    except Exception as e:
        logger.error(f"Error connecting to Meshtastic device: {e}")

if __name__ == "__main__":
    main()
