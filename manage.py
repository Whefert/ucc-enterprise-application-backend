#!/usr/bin/env python

# Name of Enterprise App: UCC Vault
# Developers:20204527- Jaevanie Ferguson, 20202583 - Jefferson Daley, 20214987 - Jadian Ellis, 20211691 - Shanieka Davis
# Version: 1.0
# Version Date: December 14, 2024
# Purpose: Enterprise application that encompasses all of the UCC's academic and strategic business units. The first version of the app 
# focuses primarily on data related to the registry department

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ucc.settings')
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
