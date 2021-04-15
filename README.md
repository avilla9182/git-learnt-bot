# git-learnt-bot
This is a Discord Bot for coding practice. The bot will be running on a
raspberry pi and the bot will be reset weekly with updated code changes.
__NOTE__ Major work still being done to the repo!!!

## Software Requirements for Local Development
* Python 3.6 - Python 3.8
    * Python 3.9 is currently incompatible with Discord library
* pip3
* Discord.py version 1.7 or higher
* dotenv

## Steps to Running a bot
1. Create a Bot on discord by going to <https://discord.com/developers/applications>
1. Create a .env at the root of the repo and place the bot's token there with
   the variable name `TOKEN`
1. Run `main.py` in an open terminal
