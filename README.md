hotinhere
=========

Wore a jacket to work? Not sure if you should wear it out to lunch? Yo, you don't need your jacket today!

Add HOTINHERE to your Yo contact list and get a "Yo" at 11:30 PST whenever the temperature is hotter than expected in SF. 

How to make it work:
Add your Yo app key to a file titled: "api.key"

Set up a cron for 11:30 PST; I'm using this as an example because my machine is on east coast time :P
30 14 * * * python /root/yo/hotinhere_yo.py
