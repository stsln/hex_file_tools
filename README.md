# HEX file tools

Designed to read, edit and combine multiple hex files into one.

Developed with Python 3.10 and PySide6 (Qt 6).
An annotation of types has been made.

### Functional button in UI

* add file - adds a hex file selected from the folder to work with
  (to make the file the main one, right-click on it)
* add region - adds a new hex region to the main hex file
* delete - deletes the selected hex regions
* in hex - exports the selected regions to a hex file
* in bin - exports the selected regions to a bin file
* merge - merges all the added files into one (Start Linear Address Record is not added)
* save - saves the modified hex region

### Install dependencies
```
pip install -r requirements.txt
```

### Converting UI to Python file
```
pyside6-rcc files.qrc -o files_rc.py
pyside6-uic design.ui -o design.py
```
Be sure to change the encoding to UTF-8

### Creating a distribution .exe file
```
pyinstaller -F -w main.py
```

### Design project UI in Figma
```
https://www.figma.com/file/pUv7CKzEWwojVQZW0q51wL/Hex-Files-Tools
```

### Future features
* Restoring to the original state
* Support for other types
* Extension of editing regions (highlighting, etc.)

### Help
If you have any problems or want to offer functionality, write a question in the Issues.

### Author

Stepan Burimov

### Copyright

Copyright (c) 2022 Stepan Burimov

### License

Licensed under the GNU GPLv3.


Разработано с любовью ❤️

Made in Russia 🇷🇺
