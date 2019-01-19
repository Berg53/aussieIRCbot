# aussieIRCbot

Bot used in freenode irc channel.

### Running

Ensure pipenv is installed. Run `pipenv shell` from project root.

To start the bot, run:

  `python src/aussie_bot.py`

### Modules

  - Weather: Gets BOM weather reports and prints them to channel
  - Timezones: Gets timezones from pytz and prints them to channel
  - Insults: Insults users
  - Web_title: get the url users post and find the title and print back to irc.
  -News_Feed: Select between 5 feeds and up to 10 topics in each feed.
  
  ### Settings
  The settings.py~ is an example remove the ~ and edit the content to suit.
