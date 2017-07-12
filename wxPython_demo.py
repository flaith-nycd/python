# Import wxPython module and system module
import wx
import sys


# Subclass wxPython frame
class WXFRAME(wx.Frame):
    def __init__(self, parent, title, size=(200, 100)):
        # Initialize super class
        wx.Frame.__init__(self, parent, title=title, size=size)

        # Set frame background color
        self.SetBackgroundColour('grey')

        # Create Status Bar
        self.CreateStatusBar()

        # Create the Menu
        menu = wx.Menu()

        # Add menu items to the menu and bind those items with event listener
        about = menu.Append(wx.ID_ABOUT, "About", "wxPython Demo")
        self.Bind(wx.EVT_MENU, self.about_, about)
        menu.AppendSeparator()
        exit = menu.Append(wx.ID_EXIT, "Exit", " Exit")
        self.Bind(wx.EVT_MENU, self.exit_, exit)

        # Create the menubar
        menuBar = wx.MenuBar()

        # Connect menu to menubar and set the MenuBar title
        menuBar.Append(menu, "File")

        # Connect the menubar to the frame
        self.SetMenuBar(menuBar)

        # Display the frame
        self.Show()

    # Exit function to close the program
    def exit_(self, e):
        sys.exit(0)

    # About function to show the about message
    def about_(self, e):
        wx.MessageBox("This is a wxPython demo...", "wxPython Demo", wx.OK | wx.ICON_INFORMATION)


# Create instance of wxPython application
app = wx.App()

# Ceeate the wx.Frame's instance
WXFRAME(None, "wxPython demo", (300, 300))

# Run the main GUI event loop
app.MainLoop()
