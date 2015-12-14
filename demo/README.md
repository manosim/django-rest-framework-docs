## Setting up the demo project
A demo project to get you started with DRF docs development.


### Installation

    # Create the virtual environment
    pyvenv env

    # Install requirements
    env/bin/pip install -r requirements.txt

    # Install Django Rest Framework Docs
    env/bin/pip install -e ../

    # Run the project
    env/bin/python manage.py runserver

**Note**: You **do not** need a database or to run `migrate`.


### Viewing DRF Docs
Once you install and run the project go to [http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/docs/).


### Note
The demo project has no functionality at all. Its purpose is **only** for viewing the docs and developing DRF docs further.
