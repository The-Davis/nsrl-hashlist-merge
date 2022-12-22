from os import path
from datetime import datetime


class DME_Logger:

    def __init__(self, appname, log_file):
        self.log_file = log_file
        if not path.exists(self.log_file):
            with open(self.log_file, 'a') as outfile:
                outfile.write('=========== ' + appname + ' log for ' + self.get_log_date() + ' ===========\n')
        self.log_cache = []

    def get_log_date(self):
        return datetime.now().strftime('%Y-%m-%d')

    def get_log_time(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def write_event(self, event):
        event = self.get_log_time() + ': ' + event + '\n'
        with open(self.log_file, 'a') as outfile:
            outfile.write(event)

    def log_event(self, event):
        self.log_cache.append(self.get_log_time() + ': ' + event + '\n')

    def write_cache(self):
        with open(self.log_file, 'a') as outfile:
            for event in self.log_cache:
                outfile.write(event)
        self.log_cache = []
