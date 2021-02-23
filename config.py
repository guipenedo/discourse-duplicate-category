#  Copyright (c) 2021. Guilherme Penedo (@guipenedo)

import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

forum_api_key = config.get("forum", "api_key")
forum_api_user = config.get("forum", "api_user")
forum_url = config.get("forum", "url")
