# src/ui/report_panel.py

import wx
import os
import subprocess

class ReportPanel(wx.Panel):
    def __init__(self, parent):
        super(ReportPanel, self).__init__(parent, style=wx.TRANSPARENT_WINDOW)
        self.init_ui()

    def init_ui(self):
        self.SetBackgroundColour(wx.Colour(255, 255, 255, 0))  # Transparent background

        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.video_choice = wx.Choice(self, choices=self.get_video_files())
        self.video_choice.SetBackgroundColour("#FFD700")  # Gold
        self.video_choice.SetForegroundColour(wx.BLACK)
        self.video_choice.Bind(wx.EVT_CHOICE, self.on_select_video)
        vbox.Add(self.video_choice, flag=wx.LEFT | wx.TOP, border=10)

        

        self.generate_report_button = wx.Button(self, label="Generate Report")
        self.generate_report_button.SetFont(font)
        self.generate_report_button.SetBackgroundColour("#2196F3")  # Blue
        self.generate_report_button.SetForegroundColour(wx.WHITE)
        self.generate_report_button.Bind(wx.EVT_BUTTON, self.generate_report)
        vbox.Add(self.generate_report_button, flag=wx.LEFT | wx.TOP, border=10)

        self.SetSizerAndFit(vbox)

    def get_video_files(self):
        return [f for f in os.listdir('.') if f.endswith('.avi')]

    def on_select_video(self, event):
        pass  # No action needed here for now


    def generate_report(self, event):
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        streamlit_app_path = os.path.join(current_dir, 'streamlit_app.py')
    
        if os.path.exists(streamlit_app_path):
            subprocess.Popen(['streamlit', 'run', streamlit_app_path])
        else:
            wx.MessageBox(f"Error: File does not exist: {streamlit_app_path}", 'Error', wx.OK | wx.ICON_ERROR)
