#!E:\TeacherTree\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Flask-Boost==0.7.5','console_scripts','boost'
__requires__ = 'Flask-Boost==0.7.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Flask-Boost==0.7.5', 'console_scripts', 'boost')()
    )
