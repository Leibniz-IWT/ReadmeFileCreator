
This file lists modules PyInstaller was not able to find. This does not
necessarily mean this module is required for running you program. Python and
Python 3rd-party packages include a lot of conditional or optional module. For
example the module 'ntpath' only exists on Windows, whereas the module
'posixpath' only exists on Posix systems.

Types if import:
* top-level: imported at the top-level - look at these first
* conditional: imported within an if-statement
* delayed: imported from within a function
* optional: imported within a try-except-statement

IMPORTANT: Do NOT post this list to the issue-tracker. Use it as a basis for
           yourself tracking down the missing module. Thanks!

excluded module named _frozen_importlib - imported by importlib (optional), importlib.abc (optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named _frozen_importlib_external - imported by importlib._bootstrap (delayed), importlib (optional), importlib.abc (optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named _winreg - imported by platform (delayed, optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named java - imported by platform (delayed), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named 'java.lang' - imported by platform (delayed, optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level), xml.sax._exceptions (conditional)
missing module named vms_lib - imported by platform (delayed, conditional, optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named msvcrt - imported by subprocess (conditional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level), getpass (optional)
missing module named _winapi - imported by encodings (delayed, conditional, optional), subprocess (conditional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named winreg - imported by platform (delayed, optional), mimetypes (optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level), urllib.request (delayed, conditional, optional)
missing module named nt - imported by os (conditional, optional), ntpath (conditional, optional), shutil (conditional), pathlib (conditional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named 'org.python' - imported by pickle (optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level), xml.sax (delayed, conditional)
missing module named org - imported by copy (optional), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (top-level)
missing module named PyQt5.sip - imported by PyQt5 (top-level), /Users/tomruiter/Desktop/ReadmeCreator/macOS/fbs/src/main/python/main.py (optional)
missing module named rsa - imported by fbs_runtime.licensing (top-level)
