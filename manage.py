#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()






# admin login details 
# rahulkumar--> Rahul@12345 , 20bec081--> Rahul@12345 


# to start cd django_project
# virtualenv py_env --python=python3 
# source py_env/bin/activate
# pip install django 
# pip install django-crispy-forms
# python3 manage.py runserver