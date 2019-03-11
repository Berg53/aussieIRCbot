# aussieIRCbot

Bot used in freenode irc channel.

### Installing

Ensure pipenv is installed then run `pipenv install` from project root.

### Configuration

The settings-example.py is an example remove the -example and edit the content to suit.

### Running

To start the bot, run:

  `pipenv run aussiebot`

### Modules

  - Weather: Gets BOM weather reports and prints them to channel
  - Timezones: Gets timezones from pytz and prints them to channel
  - Insults: Insults users
  - Web_title: get the url users post and find the title and print back to irc.
  - News_Feed: Select between 5 feeds and up to 10 topics in each feed.
  - Greeter: responds to o/ and \o.
