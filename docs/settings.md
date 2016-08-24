---
source_filename: settings
---

### How to set the settings
To set DRF docs' settings just include the dictionary below in Django's `settings.py` file.

    REST_FRAMEWORK_DOCS = {
        'HIDE_DOCS': True,
        'MODULE_ROUTERS': {
            'project.accounts.urls': 'accounts_router',
        },
        'DEFAULT_MODULE_ROUTER': 'router',
        'DEFAULT_ROUTER': 'project.urls.default_router',
    }


### Settings Description

##### HIDE_DOCS
You can use hidden to prevent your docs from showing up in different environments (ie. Show in development, hide in production). To do so you can use environment variables.

    REST_FRAMEWORK_DOCS = {
        'HIDE_DOCS': os.environ.get('HIDE_DRFDOCS', False)
    }

Then set the value of the environment variable `HIDE_DRFDOCS` for each environment (ie. Use `.env` files)

##### MODULE_ROUTERS
Use this setting to manually bind url modules to a router instance. The router must be defined in the module, or imported in the module.
For instance, if the router of an app called 'gifts' is 'gifts_router', and the router of another app called 'scuba_diving' is 'scuba_diving_router', the MODULE_ROUTERS setting should look like:

    'MODULE_ROUTERS': {
        'gifts.urls': 'gift_router',
        'scuba_diving.urls': 'scuba_diving_router'
    }

If there is no entry for a given module, if this setting is not set, or if it is set to None, the value of the DEFAULT_MODULE_ROUTER setting is used. 

##### DEFAULT_MODULE_ROUTER
When set, the value of this setting will be used to find a router for a urls module. If there is no router having the DEFAULT_MODULE_ROUTER name, the setting is ignored and the value of DEFAULT_ROUTER is used.

##### DEFAULT_ROUTER
When defined, this setting must describe a python dotted path leading to the router that should be used when MODULE_ROUTERS and DEFAULT_MODULE_ROUTER are not set.
This parameter is useful when there is only one router for your whole API.

### List of Settings

| Setting             | Type                                                      | Options         | Default |
|---------------------|-----------------------------------------------------------|-----------------|---------|
|HIDE_DOCS            | Boolean                                                   | `True`, `False` | `False` |
|MODULE_ROUTERS       | dict of python dotted paths -> router instance name       |                 | `None`  |
|DEFAULT_MODULE_ROUTER| str representing a default router instance name           |                 | `None`  |
|DEFAULT_ROUTER       | str representing a python dotted path to a router instance|                 | `None`  |
