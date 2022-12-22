from appdirs import *
import os
from pathlib import Path
import json
import PySimpleGUI as sg
from datetime import datetime


class DME_Config:

    def __init__(self, controller):
        self.controller = controller
        self.appname = "DME NSRL Hashlist Merge Tool"
        self.appauthor = "CoV DFS"
        self.config_dir = user_data_dir(self.appname, self.appauthor, roaming=True)
        Path(self.config_dir).mkdir(parents=True, exist_ok=True)
        self.config_file = self.config_dir + '\\config.json'
        self.config_data = self.read_config()
        self.cache_dir = user_cache_dir(self.appname, self.appauthor)
        Path(self.cache_dir).mkdir(parents=True, exist_ok=True)
        self.log_dir = user_log_dir(self.appname, self.appauthor)
        Path(self.log_dir).mkdir(parents=True, exist_ok=True)
        log_date = datetime.today().strftime('%Y%m%d')
        log_file = '\\%s_log.txt' % log_date
        self.log_file = self.log_dir + log_file
        self.examiner_name = ''
        self.initials = ''
        self.nsrl_source_path = ''
        self.ecf_template_path = ''
        self.analytical_notes_template_path = ''
        self.preliminary_review_form_template_path = ''
        self.preliminary_review_folder_path = ''
        self.coa_template_path = ''
        self.approved_equipment_log_password = ''
        self.notes_backup_path = ''
        self.first_time_running = 1
        self.unserialize_config()
        self.check_config()

    def normalize_path_string(self):
        if isinstance(self.nsrl_source_path, str):
            self.nsrl_source_path = self.nsrl_source_path.replace('/','\\')
        if isinstance(self.ecf_template_path, str):
            self.ecf_template_path = self.ecf_template_path.replace('/','\\')
        if isinstance(self.analytical_notes_template_path, str):
            self.analytical_notes_template_path = self.analytical_notes_template_path.replace('/','\\')
        if isinstance(self.preliminary_review_form_template_path, str):
            self.preliminary_review_form_template_path = self.preliminary_review_form_template_path.replace('/','\\')
        if isinstance(self.preliminary_review_folder_path, str):
            self.preliminary_review_folder_path = self.preliminary_review_folder_path.replace('/','\\')
        if isinstance(self.coa_template_path, str):
            self.coa_template_path =  self.coa_template_path.replace('/','\\')

    def write_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config_data, f)

    def read_config(self):
        if os.path.exists(self.config_file) and os.path.isfile(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def serialize_config(self):
        self.config_data['examiner_name'] = self.examiner_name
        self.config_data['initials'] = self.initials
        self.config_data['nsrl_source_path'] = self.nsrl_source_path
        self.config_data['ecf_template_path'] = self.ecf_template_path
        self.config_data['analytical_notes_template_path'] = self.analytical_notes_template_path
        self.config_data['preliminary_review_form_template_path'] = self.preliminary_review_form_template_path
        self.config_data['preliminary_review_folder_path'] = self.preliminary_review_folder_path
        self.config_data['coa_template_path'] = self.coa_template_path
        self.config_data['approved_equipment_log_password'] = self.approved_equipment_log_password
        self.config_data['notes_backup_path'] = self.notes_backup_path
        self.config_data['first_time_running'] = self.first_time_running

    def unserialize_config(self):
        if 'nsrl_source_path' in self.config_data:
            self.nsrl_source_path = self.config_data['nsrl_source_path']
        if 'initials' in self.config_data:
            self.initials = self.config_data['initials']
        if 'ecf_template_path' in self.config_data:
            self.ecf_template_path = self.config_data['ecf_template_path']
        if 'analytical_notes_template_path' in self.config_data:
            self.analytical_notes_template_path = self.config_data['analytical_notes_template_path']
        if 'preliminary_review_form_template_path' in self.config_data:
            self.preliminary_review_form_template_path = self.config_data['preliminary_review_form_template_path']
        if 'preliminary_review_folder_path' in self.config_data:
            self.preliminary_review_folder_path = self.config_data['preliminary_review_folder_path']
        if 'coa_template_path' in self.config_data:
            self.coa_template_path = self.config_data['coa_template_path']
        if 'approved_equipment_log_password' in self.config_data:
            self.approved_equipment_log_password = self.config_data['approved_equipment_log_password']
        if 'notes_backup_path' in self.config_data:
            self.notes_backup_path = self.config_data['notes_backup_path']
        if 'first_time_running' in self.config_data:
            self.first_time_running = self.config_data['first_time_running']

    def check_config(self):
        # make sure mandatory config values are set
        do_set_config = False
        if self.examiner_name == '': do_set_config = True
        if self.initials == '': do_set_config = True
        if self.nsrl_source_path == '' or not os.path.exists(self.nsrl_source_path): do_set_config = True
        if self.ecf_template_path == '' or not os.path.exists(self.ecf_template_path): do_set_config = True
        if self.analytical_notes_template_path == '' or not os.path.exists(self.analytical_notes_template_path): do_set_config = True
        if self.preliminary_review_form_template_path == '' or not os.path.exists(self.preliminary_review_form_template_path): do_set_config = True
        if self.preliminary_review_folder_path == '' or not os.path.exists(self.preliminary_review_folder_path): do_set_config = True
        if self.coa_template_path == '' or not os.path.exists(self.coa_template_path): do_set_config = True
        if self.approved_equipment_log_password == '': do_set_config = True
        if self.first_time_running:
            do_set_config = True
            # set defaults
            self.ecf_template_path = 'X:\\Documentation\\Templates\\ECF'
            self.analytical_notes_template_path = 'X:\\Documentation\\Templates\\Analytical_Notes\\Current'
            self.preliminary_review_form_template_path = 'X:\\Documentation\\Templates\\DME_Preliminary_Review_Form\\Current'
            self.preliminary_review_folder_path = ''
            self.coa_template_path = 'X:\\Documentation\\Templates\\CoA\\Current'
            self.approved_equipment_log_password = 'DME'

        if do_set_config:
            self.first_time_running = 0
            self.update_config()
        else:
            self.write_config()

    def update_config(self):
        layout = [
            [
                sg.Text('Examiner Name                                  '),
                sg.In(default_text=self.examiner_name, size=(25, 1), enable_events=True, key="-EXAMINER_NAME-"),
            ],
            [
                sg.Text('Examiner Initials                                 '),
                sg.In(default_text=self.initials, size=(25, 1), enable_events=True, key="-INITIALS-"),
            ],
            [
                sg.Text('Case Folder Path                                '),
                sg.In(default_text=self.nsrl_source_path, size=(25, 1), enable_events=True, key="-nsrl_source_path-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('ECF Template Path                             '),
                sg.In(default_text=self.ecf_template_path, size=(25, 1), enable_events=True, key="-ECF_TEMPLATE_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('Analytical Notes Template Path            '),
                sg.In(default_text=self.analytical_notes_template_path, size=(25, 1), enable_events=True, key="-ANALYTICAL_NOTES_TEMPLATE_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('Preliminary Review Form Template Path'),
                sg.In(default_text=self.preliminary_review_form_template_path, size=(25, 1), enable_events=True, key="-PRELIMINARY_REVIEW_FORM_TEMPLATE_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('Preliminary Review Folder Path             '),
                sg.In(default_text=self.preliminary_review_folder_path, size=(25, 1), enable_events=True, key="-PRELIMINARY_REVIEW_FOLDER_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('Certificate of Analysis Template Path    '),
                sg.In(default_text=self.coa_template_path, size=(25, 1), enable_events=True, key="-COA_TEMPLATE_PATH-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Button("Save Configuration"),
            ],
        ]

        # Create the window
        window = sg.Window(self.appname + ' Configuration', layout)
        # Create an event loop
        while True:
            event, values = window.read()
            if event == "Save Configuration":
                self.examiner_name = values['-EXAMINER_NAME-']
                self.initials = values['-INITIALS-']
                self.nsrl_source_path = values['-nsrl_source_path-']
                self.ecf_template_path = values['-ECF_TEMPLATE_PATH-']
                self.analytical_notes_template_path = values['-ANALYTICAL_NOTES_TEMPLATE_PATH-']
                self.preliminary_review_form_template_path = values['-PRELIMINARY_REVIEW_FORM_TEMPLATE_PATH-']
                self.preliminary_review_folder_path = values['-PRELIMINARY_REVIEW_FOLDER_PATH-']
                self.normalize_path_string()
                self.serialize_config()
                self.check_config()
                break
            elif event == sg.WIN_CLOSED:
                break
        window.close()
        self.controller.show_window()


def main():
    config = DME_Config()
if __name__ == "__main__":
    main()
