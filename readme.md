# Cutelog Test Interface
This Python app is for testing the ZMQ SUB interface added to cutelog.

# Generate ui_scc.py

> pyuic5 ui_scc.ui -o ui_scc.py

# Build
## Build command
> pyinstaller --onefile main.pyw 

## Build error 
    "UnicodeDecodeError: 'utf-8' codec can't decode byte 0x94 in position 183: invalid start byte" or similar
Build fix error in pyinstaller compat.py

[Stackoverflow](https://stackoverflow.com/questions/47692960/error-when-using-pyinstaller-unicodedecodeerror-utf-8-codec-cant-decode-byt)

[GitHub Pull Request](https://github.com/pyinstaller/pyinstaller/pull/3895)

# EXE "failed to execute script main"
Do not forget to copy **scc_conf.ini** in exe-folder.

# Configuration
App uses a ini file to save settings. It is updated when changing internal settings.
It may be edited manually but you do not need to.

**scc.conf.ini**

    [TCP]
    host = 127.0.0.1
    port = 19996
    use = False

    [ZMQ]
    host = 127.0.0.1
    port = 19997
    use = True

