# print-to-remarkable
Print plugin to directly print documents from Windows to a reMarkable tablet.

This repository contains the files and instructions needed to set up a printer on a Windows (10) device which sends the printed documented to a connected reMarkable device as a .pdf file. The plugin makes use of the several external tools, including:
- Multi File Port Monitor, a printer port that allows redirecting standard input from the printer to an external program
- Ghostscript, a program that converts postscript into pdf
- rmapy, an (unofficial) reMarkable API python library

Setting up the plugin is non-trivial. Furthermore, as there are four different systems (Windows Print Spooler Service, Multi File Port Monitor, Ghostscript, and Python) running in separate languages, it is prone to errors. After much debugging, it runs on my own laptop, but don't expect it to work out of the box on your own. See this as an alpha-alpha version of the plugin.

# Setup
1. Download and install [Multi File Port Monitor](https://sourceforge.net/projects/mfilemon/) and [Ghostscript](https://www.ghostscript.com/). You will also need a Python 3 installation.
2. Download this repository and unzip it in a location of your choice.
3. Manually set up a new printer in Windows (Control Panel>Hardware and Sound>Devices and Printers>Add a new printer>"The printer I want isn't listed"). Choose local printer from the menu options and create a new port of the type "Multi File Port Monitor". Give it any name you want.
4. Configure your new port. The crucial bit here is the user command box, where you need to enter the full path leading to the file "handler.bat" in the folder you downloaded from this repository. Enter anything into the filename pattern box - it is not used but required for configuration. Make sure that "Use pipe to send data to user command" is checked. 
5. If you have never used the Python reMarkable API, you must first connect your device. Go to [my.remarkable.com](my.remarkable.com) and get a code for a new desktop device. Open setup.py in an editor of your choice, enter the code as a string in the highlighted section of the code, and run.

Assuming you encountered no errors during these steps, the plugin should be ready to use.
