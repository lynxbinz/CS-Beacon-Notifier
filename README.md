# CS Beacon Notifier
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
```
git clone https://github.com/lynxbinz/CS-Beacon-Notifier.git
cd CS-Beacon-Notifier
pip3 install requests
```
* Make sure you have changed the pyScript path in the CSB-Notifier.cna script on the line 5
```
$pyScript = "/home/[username]/[cs-path]/CS-Beacon-Notifier/pyScript.py";
```
* You can change the Default language to English in the CSB-Notifier.cna script on the line 36
```
@command = @('python3',$pyScript,$infoText_kh); # Change to $infoText_en and Save
```
* Now Load the script via Cobalt Strike Script Manager as show below

* ![Load CNA Script](https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/load-cna-script.png?raw=true | width=300)

* Open the pyScript.py and replace with your Telegram Bot Token and Chat ID
```
def telegram_bot_msgSender(msg):
    teleBot_token = 'xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    teleBot_chatID = 'xxxxxxxxx'
```
* Saved and Done.

## Tested On
* Kali Linux 2022.4
* Cobalt Strike 4.7

* Khmer Version

* ![Beacon Notifier KH](https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/beacon-kh.png?raw=true | width=300)

* English Version

* ![Beacon Notifier EN](https://github.com/lynxbinz/CS-Beacon-Notifier/blob/main/beacon-en.png?raw=true | width=300)
