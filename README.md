# Color Picker Tray App

A simple color picker tray app for both Windows and Linux.

## How to run on your machine

### Requirements
- Python 3.x

### Steps
Open a terminal window, and run the following commands:
1. `git clone https://github.com/youssef-attai/color-picker-tray.git`
2. `cd color-picker-tray`
3. Make sure you have `virtualenv` installed, then run `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python color_copy_tray.py`

You should now be able to see the application icon in the tray.

![App icon](https://github.com/youssef-attai/color-picker-tray/blob/master/color_icon.png)


## Notes
- When you pick a color, its HEX value or RGB value (depending on what you chose from the menu) gets copied to the clipboard.
