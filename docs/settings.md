---
source_filename: settings
---

### How to set the settings
To set DRF docs' settings just include the dictionary below in Django's `settings.py` file.

    REST_FRAMEWORK_DOCS = {
        'HIDE_DOCS': True
    }


### Settings Description

##### HIDE_DOCS
You can use hidden to prevent your docs from showing up in different environments (ie. Show in development, hide in production). To do so you can use environment variables.

    REST_FRAMEWORK_DOCS = {
        'HIDE_DOCS': os.environ.get('HIDE_DRFDOCS', False)
    }

##### DESC_TABLE
You can use Table representation to make your fields list in the documentation clear. So We can change representation by adding single line inside the `REST_FRAMEWORK_DOCS` in `settings.py`.

    'DESC_TABLE': os.environ.get('DESCRIBE_TABLE', False)


Then set the value of the environment variable `HIDE_DRFDOCS` for each environment (ie. Use `.env` files)

### List of Settings

| Setting  | Type    | Options         | Default |
|----------|---------|-----------------|---------|
|HIDE_DOCS | Boolean | `True`, `False` | `False` |
|DESC_TABLE| Boolean | `True`, `False` | `False` |
