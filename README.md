# Pivot_io
I did this project to understand Django at a greater level

# To Try this out you have to follow the steps: #
### I'm not sure about the mac commands so make sure you google anything if it doesn't work ###

* Clone the repository into a directory.
* You must have Python 3.8.5 or higher, but beware the packages might not work as intended if the version changes.
* To create the virtual Environment open you command-line:
  * Windows:
    python -m venv 'env_name'.
  * Mac:
    python3 source 'env_name'.
* Once the venv is created you must activate it and install the required packages.
* To activate it:
  * Windows:
    Execute the command 'env_name'\Scripts\activate.
  * Mac:
    Execute the command source 'env_name'/bin/activate.
    
#### (This is very important before you proceed. Make sure you activate) ####
* The requirements.txt is included in the repository so jus execute the command pip install -r requirements.txt
* You can also choose to install them one by one.
* Once the packages are installed now the only thing left is to run the application.
* Execute python manage.py runserver (Make sure you are in the directory with the file manage.py).
* Enter the address 127.0.0.1:8000 in your browser to view.


## If you want your own data in the database ##
You must connect a postgres database and run migrations (google how to run migrations in a django project) once again and before running migrations do delete the files inside migrations directory inside every directory in  the project.

## Postgres SQL ##
In the settings.py file in Pivot_io package or simply directory in line 80 you can find the connected database. Replace the data with your respective username and password and the port needs to be changed for postgres by default it is 5432 but if you want to use a different database just check the django compatible database.

## Switching to the default database sqlite 2 ##
Replace the DATABASES dictionary with
    
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
This will use the sqlite 3 database.

