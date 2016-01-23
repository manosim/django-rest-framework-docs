---
title:  "Settings"
source_filename: "settings"
order: 4
---

### How to set the settings
To set DRF docs' settings just include the dictionary below in Django's `settings.py` file.

    REST_FRAMEWORK_DOCS = {
        'HIDDEN': True
    }


### Settings Description

##### HIDDEN
You can use hidden to prevent your docs from showing up in different environments (ie. Show in development, hide in production). To do so you can use environment variables.

    REST_FRAMEWORK_DOCS = {
        'HIDDEN': os.environ.get('SHOW_DRFDOCS', False)
    }

Then set the value of the environment variable `SHOW_DRFDOCS` for each environment (ie. Use `.env` files)

### List of Settings

{:.table .table-striped}
| Setting | Type    | Options         | Default |
|---------|---------|-----------------|---------|
| HIDDEN  | Boolean | `True`, `False` | `False` |
|         |         |                 |         |
