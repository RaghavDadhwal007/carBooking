#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carBooking.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable (Right click on mycomputer and go to properties -> Advance system setting -> Environment Variable )? Did you "
            "forgot to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
