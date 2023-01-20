# Cobalt Strike Beacon Notifier
A Cobalt Strike Beacon Notifier Via Telegram Bot.

## Features
* Showing the Name of the Current User
* Showing the Computer Name of the Current User
* Showing the Type and Version of the Operating System
* Showing the Type of the Process Exec Name
* Showing the Internal IP of the System
* Showing the Enternal IP of the System

## Languages
* ខ្មែរ Khmer (Cambodia) - Default
* English (International)

## Requirements
* Python3
* Python3 Pip

## Setup
```console
git clone https://github.com/lynxbinz/CS-Beacon-Notifier.git
cd CS-Beacon-Notifier
pip3 install requests
```
* Make sure you have changed the pyScript path in CSB-Notifier.cna script on the line 5
```console
$pyScript = "/home/[username]/[cs-path]/CS-Beacon-Notifier/pyScript.py";
```
* You can change the Default language to English in CSB-Notifier.cna script on the line 36
```console
@command = @('python3',$pyScript,$infoText_kh); # Change to $infoText_en and Save
```
* Now Load the script via Cobalt Strike Script Manager as show below
<p align="center">
    <img src="https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/images/load-cna-script.png" alt="Image" width="600" />
</p>

* Open the pyScript.py and replace with your Telegram Bot Token and Chat ID
```python
def telegram_bot_msgSender(msg):
    teleBot_token = "xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    teleBot_chatID = "xxxxxxxxxxxx"
```
* Saved and Done.

## Tested On
* Kali Linux 2022.4
* Cobalt Strike 4.7

### Khmer Version
<p align="left">
    <img src="https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/images/beacon-kh.png" alt="Image" width="800" />
</p>

### English Version

<p align="left">
    <img src="https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/images/beacon-en.png" alt="Image" width="800" />
</p>
