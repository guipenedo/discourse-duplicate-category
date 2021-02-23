# Discourse duplicate category
This simple script uses [Discourse's REST API](https://docs.discourse.org/) to duplicate a category, which is not possible directly through the frontend.

## Features
- Copy category colors
- Copy category images
- Copy category permission groups
- Optionally replace the original permission groups with new ones directly
- Copy category settings (wiki, subcategory display options, etc)
- Copy category description (the auto generated about post is edited with the contents of the origin category's about post)
- Sub categories are recursively copied

Unfortunately the list of allowed tags is not copied at this time.

## Obtaining an API key
![On settings, click on API and then on the key icon to create a new API Key](media/create_api_key.png)

## Configuration
Rename the `config.ini.default` file to `config.ini`.
Fill in the options:
```ini
[forum]
api_key= # put your API key here
api_user= # the username of the user associated with this API key
url= # Discourse installation base url, without trailing /
```

## Installation
1. Create a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
1. [Activate](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment) it
1. Install the requirements
```shell
$ pip install -r requirements.txt
```

## Running
1. [Activate](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)
   the virtual environment you created
1. While in the main directory, run
   ```shell
   python3 main.py
   ```
1. Choose a category to **copy from** (origin) by name
1. Choose the name of the **new category** (destination)
1. Choose the new category's **slug**
1. Optionally, type in "yes" to indicate a group replacement mapping
   Example, to replace *astro-studs* with *math-studs* and *astro-teach* with *math-teach*:
   ```
   Would you like to replace groups from the previous category with different ones, already created? (yes/no) yes
   How many groups? 2
   Old group 1/2: astro-studs
   New group 1/2: math-studs
   Old group 2/2: astro-teach
   New group 2/2: math-teach
   ```
   Please note that *math-studs* and *math-teach* groups ***must already exist***.
1. The script will now recursively duplicate the category and its subcategories
