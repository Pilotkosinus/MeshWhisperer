# commands.py

def hello_command(sender_id, interface):
    """
    Dieser Befehl wird ausgeführt, wenn ein User "!Hallo" sendet.
    """
    if interface:
        interface.sendText(
            "Hallo, ich bin der Meshtastic Info Bot!", 
            destinationId=sender_id
        )
    else:
        print("WARNUNG: Kein Interface verfügbar, um Antwort zu senden.")


# Ein Dictionary, das Befehle (Strings) einer Funktion zuordnet
COMMANDS = {
    "!hallo": hello_command,
    # Später kannst du hier weitere Befehle ergänzen, z.B.:
    # "!Wetter": weather_command,
    # "!Ping": ping_command,
    # usw.
}
