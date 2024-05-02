"""
+--------------------------------------------------+
| Windows 10/11 - Background Changer               |
|                                                  |
| Adapted from original Gehovies Witnesses script. |
| The script has been heavily modified to make it  |
| shorter, quicker and more reliable.              |
| The script will also now force the wallpaper     |
| to visually refresh instantly (in theory)        |
|                                                  |
| Original authors -> Owen Plimer, Sonosus         |
| This Ver: Auth -> Owen Plimer                    |
|                                                  |
| version: 3.0.0                                   |
| Date: 01/05/2024                                 |
+--------------------------------------------------+
"""

import ctypes


# Define the necessary constants
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02


bg_file = "U:\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper" # Location of the transcoded wallpaper file
custom_file_dir = r"" # Absolute path to the file you want to use as the wallpaper

wallpaper = "" # Will store the contents of the new background image fr future use


# Read in the contents of the new background file
with open(custom_file_dir, "rb") as in_file:
    wallpaper = in_file.read()


# Replace the old contents of the TranscodedWallpaper file in \Themes\
with open(bg_file, "wb") as out_file:
    out_file.write(wallpaper)


# Call the SystemParametersInfo function to set the wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, custom_file_dir, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
