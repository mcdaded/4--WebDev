To start a new project is easy:
    django-admin startproject mysite

creates a site directory and some starter code for the project. Also creates a project folder which has base
settings and configuration for the project as a whole.

To start a new app in the project in the site simply run the following in the same directory as manage.py:
    python manage.py startapp polls

Now we can create a view for the app here and

To migrate changes to the site simply run:
    python manage.py migrate

When adding a new app to the project, need to add it to the mysite\urls.py and settings.
    url(r'^app_name/', include('{app_name}.urls'))

Whenever changing the polls app need to make a migration, if there are model changes make a sql migration and then
migrate the changes:
    python manage.py makemigrations {app_name}
    python sqlmigrate {app_name} {migration_number} # python manage.py sqlmigrate polls 0001
    python manage.py migrate

to interactively work with the models and settings, run everything in the manage.py file:

import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()