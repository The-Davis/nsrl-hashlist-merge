import PySimpleGUI as sg
import os.path
import dme_config
import dme_logger
import sys
import traceback

class Controller:

    def __init__(self):
        self.config = dme_config.DME_Config(self)
        self.logger = dme_logger.DME_Logger(self.config.appname, self.config.log_file)
        self.logger.log_event('App started.')
        self.window = None
        try:
            self.main_window()
        except Exception as e:
            self.logger.log_event(traceback.format_exc())
            self.exit()

    def crash(self, error):
        self.logger.log_event(error)
        self.exit()

    def exit(self):
        self.logger.log_event('App shutting down.')
        self.logger.write_cache()
        if self.window: self.window.close()
        sys.exit()

    def show_window(self):
        if self.window:
            self.window.UnHide()

    def hide_window(self):
        if self.window:
            self.window.Hide()

    def main_window(self):
        layout = [
            [
                sg.Button("New Case"),
                sg.VerticalSeparator(),
                sg.Button("Review Notes"),
                sg.VerticalSeparator(),
                sg.Button("Generate CoA"),
                sg.VerticalSeparator(),
                sg.Button("Update Configuration"),
            ],
            [
                sg.HorizontalSeparator(),
            ],
            [
                sg.Button("Exit"),
            ],
        ]
        self.window = sg.Window(self.config.appname, layout)

        # Create an event loop
        while True:
            event, values = self.window.read()
            # End program if user closes window or
            # presses the OK button
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            elif event == 'New Case':
                break
            elif event == 'Review Notes':
                self.hide_window()
            elif event == 'Generate CoA':
                break
            elif event == 'Update Configuration':
                self.hide_window()
                self.config.update_config()
        self.exit()

if __name__ == "__main__":
    Controller()
