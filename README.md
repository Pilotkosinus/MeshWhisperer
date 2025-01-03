# Meshtastic Info Bot

Ein einfacher Bot, der Nachrichten von einem Meshtastic-Gerät über die TCP-Schnittstelle empfängt und darauf reagiert.

## Überblick

Dieses Projekt besteht aus zwei Python-Skripten:
- **Meshbot.py**: Hört auf Nachrichten, die vom Meshtastic-Gerät über das Netzwerk gesendet werden, und verarbeitet sie.
- **commands.py**: Definiert Befehle, auf die der Bot reagieren kann.

### Features
- Empfang von Nachrichten über die Meshtastic TCP-Schnittstelle
- Reaktion auf benutzerdefinierte Befehle

## Voraussetzungen

Bevor du startest, stelle sicher, dass die folgenden Anforderungen erfüllt sind:

1. **Hardware**
   - Ein Heltec V3-Gerät oder ein anderes Meshtastic-kompatibles Gerät.
   - Ein Netzwerk, über das dein Rechner und das Meshtastic-Gerät verbunden sind.

2. **Software**
   - Python 3.7 oder höher
   - Die folgenden Python-Pakete:
     - `meshtastic`
     - `pubsub`

## Installation

### 1. Repository klonen
Lade die Projektdateien herunter, indem du dieses Repository klonst:

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Abhängigkeiten installieren
Erstelle eine virtuelle Umgebung und installiere die erforderlichen Pakete:

```bash
python3 -m venv venv
source venv/bin/activate  # Für Linux/Mac
venv\Scripts\activate   # Für Windows

pip install meshtastic pubsub
```

### 3. Skript anpassen
Bearbeite die Datei `Meshbot.py` und ersetze die Platzhalter-IP (`192.168.xxx.xx`) durch die IP-Adresse deines Meshtastic-Geräts.

## Verwendung

### 1. Bot starten
Führe das Hauptskript aus:

```bash
python Meshbot.py
```

Wenn alles korrekt konfiguriert ist, siehst du eine Meldung, dass der Bot mit dem Meshtastic-Gerät verbunden ist und auf Nachrichten wartet.

### 2. Nachrichten senden
Sende eine Nachricht von deinem Meshtastic-Gerät mit einem der definierten Befehle. Beispiel:

```
!hallo
```

Der Bot wird darauf mit einer Antwort reagieren:

```
Hallo, ich bin der Meshtastic Info Bot!
```

## Befehle
Die verfügbaren Befehle werden im Dictionary `COMMANDS` in der Datei `commands.py` definiert. Aktuell gibt es folgende Befehle:

| Befehl     | Beschreibung                            |
|------------|----------------------------------------|
| `!hallo`   | Der Bot antwortet mit einer Begrüßung. |

Du kannst weitere Befehle hinzufügen, indem du das Dictionary in `commands.py` erweiterst.

## Anpassung

### Weitere Befehle hinzufügen
1. Definiere eine neue Funktion in `commands.py`. Beispiel:

    ```python
    def weather_command(sender_id, interface):
        interface.sendText("Das aktuelle Wetter ist sonnig!", destinationId=sender_id)
    ```

2. Füge den neuen Befehl dem Dictionary `COMMANDS` hinzu:

    ```python
    COMMANDS = {
        "!wetter": weather_command,
        # weitere Befehle...
    }
    ```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei `LICENSE`.

## Autor
- Erstellt von **Pilotkosinus** 
