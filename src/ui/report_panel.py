# src/ui/report_panel.py

import wx
import os
import subprocess
import logging
import random

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
        # Generate a random engagement score
        score = round(random.uniform(76.0, 96.0), 2)
    
        # Write the score to a file in the src/ui directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        score_file_path = ('src/data/score.txt')
    
        try:
            with open(score_file_path, 'w') as score_file:
                score_file.write(str(score))
            logging.info(f"Score {score} written to {score_file_path}")
        except Exception as e:
            logging.error(f"Failed to write score to {score_file_path}: {e}")

        # Generate heatmap
        try:
            heatmap_script_path = os.path.join(current_dir, 'heatmaptrial.py')
            subprocess.run(['python', heatmap_script_path], check=True)
            logging.info("Heatmap generated successfully.")
        except Exception as e:
            logging.error(f"Failed to generate heatmap: {e}")
    
        # Get the absolute path of the Streamlit app
        streamlit_app_path = os.path.join(current_dir, 'streamlit_app.py')
    
        if os.path.exists(streamlit_app_path):
            subprocess.Popen(['streamlit', 'run', streamlit_app_path])
        else:
            wx.MessageBox(f"Error: File does not exist: {streamlit_app_path}", 'Error', wx.OK | wx.ICON_ERROR)