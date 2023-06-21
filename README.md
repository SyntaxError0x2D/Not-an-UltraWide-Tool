# Not-an-UltraWide-Tool
### nUWt (not an ultrawide tool) is a tool to 16:9-fy your games etc; meant for ultrawide users.

## What? how? when?
I've had a issue with some games (mainly souls) not supporting ultrawide resolutions, so I decided to create a tool to help make the expirience a bit more bearable.
So what does this do? It allows you to remove the top bar of a chosen windowed application, and move it anywhere you want to. So the main use case for me is to move the game to the left quadrent 
leaving the rest of the screen free for a music player etc. This works well in tandem with windows powertoys to align the music player perfectly.
![alt text](https://github.com/syntaxerror0x2d/Not-an-UltraWide-Tool/blob/main/demonstration.png?raw=true)
So that leaves two more questions:
How, and that's with sheer will power and a wee bit of help from chatGPT. It helped me write the function to remove the top bar, though I modified it a bit. Rest is completely my own code.
No but seriously this uses the ctypes library to communicate the changes in the window styling, and the pygetwindow module to move, resize and handle the information about currently opened windows.
This also uses tkinter for the GUI. I suck at it, feel free to make it better.
When: Now, download, test, tweek!

### Dependencies:
windows 10 (only tested one, might work on 7 / 11)

python3.8+
##### python modules:
   - tkinter

   - pygetwindow

   -  ctypes

   - sys


#### Notes
As this is in very early development I haven't made awfully customizable, nor added a help any where in the app so I'll add it here:

How to select an item:

    Click on the item or use the arrows keys to navigate to it.
    
How to 16:9-fy / how to undo it:

    Navigate to it, and press enter to 16:9-fy it, or backspace to undo it

Does this work with all games / apss?

    No :(
Recomended to turn "Autmatically hide taskbar while in desktop mode" on in taskbar settings! 
   
## Download:

Click -> [Releases](https://github.com/SyntaxError0x2D/Not-an-UltraWide-Tool/releases)

