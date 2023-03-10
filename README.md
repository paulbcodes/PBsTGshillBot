# PBsTGshillBot - Telegram messenger / crypto shill bot
A Telegram messanger program in python which sends messages to chosen channels at selected intervals.

## Purpose
This was designed to be able to send the same same crypto promotional message to the channels of your choosing.

It can be used to send messsages of any type to channels of which you are members of and are allowed to post in.

## Built Using
* Python
* telethon

## Requirements
* Python3
* telethon

## Installation
You will need python3 installed.
Then:
```
pip install telethon
```
To start the bot
```
python main.py
```

## Usage Instructions
* Prior to starting the program you should enter the relevenat details into the files contained in the data_dir directory. Channel details in channel_info and telegram details in telethon_vars.
* You need to enter the channel id numbers of the input channel (the channel you send the message from) and of all channels you want the message to send to. Example channel id number *********, in channel_info.
* Once the program is running you will be asked to enter various bits of information when you first run the program. 
* After you enetr your phone number a code will be sent to your telegram account on your phone to allow you to link the program to your account.
* You should not need to enter these details on uses subsequent to the first time. 
* When the program is running use telegram and send your message from the input channel. The message will send at the intervals you set to the channels you set.
* You can have more than one bot running at the same time on the same machine with different telegram accounts.
* If using more than one bot at the same time you can use the same input channel to save time if all the bots are sending the same message. Different messages require different input channels.

## Example channel codes / channel_info file
* {"input_channel":["-517831485"],"receiving_channel":["-593537629", "1268766805"]}
* 1 input channel only.
* Multiple output channels allowed seperated by a ,
* The codes are for example format only and are (probably) not real channels.
* Channel codes can be found in the address bar on the telegram desktop version (there may be other ways to get channel codes)

## Example telethon_vars file
* {"api_id":"8641129","api_hash":"57a7bc69fe2ed7d7e277b97fe61bf5a1","phone_num":"+447611944513"}
* Phone numbers as per the telegram account with country code.
* You will need to get an api id and hash from telegram.
* Log in to your Telegram core: https://my.telegram.org.
* Go to 'API development tools' and fill out the form then copy the api id and hash.
* The api id / hash and the phone number are for example only and are (probably) not real.
