# aussieIRCbot

Bot used in freenode irc channel.

### Running

Ensure pipenv is installed. Run `pipenv install` and `pipenv shell` from project root.

To start the bot, run:

  `twistd -ny src/irc_bot.tac`

Override settings with environment variables:

  `IRC_HOST`
  `IRC_PORT`
  `NICK`
  `CHANNEL`
  `LOG_FILE_NAME`
  `LOG_FILE_LOCATION`
  `SCROLLBACK_SIZE`
  `COMMAND_CHARACTER`
  `JOIN_MESSAGE`

Or set them in `src/config.py`.

### Modules

  - Weather: Gets BOM weather reports and prints them to channel
  - Timezones: Gets timezones from pytz and prints them to channel
  - Insults: Insults users
