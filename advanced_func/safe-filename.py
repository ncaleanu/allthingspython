import re
"""
Let a secure filename consist of:
- English letters or a number (a-zA-Z0-9) at beginning.
-  **only** English letters, numbers and symbols among these four: `-_()`.
- a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""

def is_filename_safe(filename):
    regex = '^[A-Za-z0-9]+[A-Za-z0-9-()_]*\.{1}(png|jpg|jpeg|gif)$'
    return re.match(regex, filename) is not None

filename = input("Save file as (include extension): ")
print(is_filename_safe(filename))