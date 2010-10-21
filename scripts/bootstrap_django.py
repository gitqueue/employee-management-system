""" This module sets up django environment so that other scripts need not worry about these mundane tasks.
"""

def main():
    try:
        from employee_management_system.settings import settings
    except ImportError:
        try:
            from employee_management_system import settings
        except ImportError:
            import sys
            sys.stderr.write('Can not find settings module. \n Aborting...')
            sys.exit(1)

    from django.core.management import setup_environ
    setup_environ(settings)

if __name__ == '__main__':
    main()
