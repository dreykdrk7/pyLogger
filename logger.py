from colorify import *          # COLORIFY API: https://pypi.org/project/colorify/
from datetime import datetime   # DATETIME OBJECTS: https://docs.python.org/3/library/datetime.html#datetime-objects
from platform import system
from pathlib import Path
from os.path import exists

class Logger():

    init_colorify()
    def __init__(self, identifier):
        self.process_name = identifier
        self.datetime_format = '%d/%m/%Y %H:%M:%S'
        self.string_format = '%DATETIME% ||%CATEGORY%|| %MESSAGE%'
        self.color_palette = {
            'datetime': {
                'font-color': C.cyan,
                'background-color': None
            },
            'info': {
                'font-color': C.white,
                'background-color': C.blue
            },
            'exception': {
                'font-color': C.white,
                'background-color': C.orange
            },
            'error': {
                'font-color': C.white,
                'background-color': C.red
            },
            'warning': {
                'font-color': C.white,
                'background-color': C.yellow
            },
            'critical': {
                'font-color': C.white,
                'background-color': C.crimson
            },
        }
        self.logs_fullpath = ''
        self.file_name = ''

        self.get_logs_path()
        self.get_filename()


    def datetime_now(self):
        now = datetime.now()
        return now.strftime(self.datetime_format)

    
    def set_datetime_format(self, format):
        self.datetime_format = format


    def get_datetime_format(self):
        return self.datetime_format


    def create_path(self):
        try:
            os.system(f'mkdir {self.logs_fullpath}')
        except:
            print('Error creating log folder. Please, check the execution privileges and try again.')


    def file_exists(self):
        path = Path(f'{self.logs_fullpath}/{self.file_name}')
        if not path.is_file():
            return False
        else:
            return True
    

    def get_logs_path(self):
        if system() == 'Windows':
            self.logs_fullpath = f'.\\logs\\{self.process_name}'
        else:
            self.logs_fullpath = f'./logs/{self.process_name}'


    def get_filename(self):
        dt = datetime.now()
        day_number = dt.weekday()
        month_number = dt.month
        if len(str(month_number)) < 2:
            month_number = f'0{month_number}'

        if day_number == 0:
            self.file_name = f'{self.process_name}_{dt.day}{month_number}{dt.year}.log'
        else:
            last_monday = dt.day-day_number
            self.file_name = f'{self.process_name}_{last_monday}{month_number}{dt.year}.log'

        if self.file_exists() == False:
            try:
                self.create_new_log()
            except:
                print('Error creating log file. Please, check the execution privileges and try again.')
                

    def create_new_log(self):
        if not exists(self.logs_fullpath):
            self.create_path()
        
        dt = datetime.now()
        month = str(dt.month)
        if len(month) == 1:
            month = f'0{month}'

        header = f'\n\n*******************************************************************************\n' \
                f'*******************************************************************************\n' \
                f'*********                                                             *********\n' \
                f'*********                                                             *********\n' \
                f'*********    Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet    *********\n' \
                f'*********                                                             *********\n' \
                f'*********                  Creation date: {dt.day}/{month}/{dt.year}' \
                f'                  *********\n' \
                f'*********                                                             *********\n' \
                f'*********                                                             *********\n' \
                f'*******************************************************************************\n' \
                f'*******************************************************************************\n\n\n\n'

        f = open(f'{self.logs_fullpath}/{self.file_name}', 'a')
        f.write(header)
        f.close()
        self.info(f'Log file has been created successfully for "{self.process_name}".')


    def add_new_record(self, new_reg):
        if self.file_exists() == False:
            self.create_new_log()
        f = open(f'{self.logs_fullpath}/{self.file_name}', 'a')
        f.write(f'{new_reg}\n')
        f.close()


    def info(self, message, username=None, thread='Default'):
        string_splitted = self.string_format.split('%')
        msg = ''
        new_reg = ''
        for sub_section in string_splitted:
            if len(sub_section) > 1:
                response = self.select_section(sub_section, thread, username, 'info', message)
                msg += response[0]
                new_reg += response[1]
        print(msg)
        self.add_new_record(new_reg)


    def exception(self, message, username=None, thread='Default'):
        string_splitted = self.string_format.split('%')
        msg = ''
        new_reg = ''
        for sub_section in string_splitted:
            if len(sub_section) > 1:
                response = self.select_section(sub_section, thread, username, 'exception', message)
                msg += response[0]
                new_reg += response[1]
        print(msg)
        self.add_new_record(new_reg)


    def error(self, message, username=None, thread='Default'):
        string_splitted = self.string_format.split('%')
        msg = ''
        new_reg = ''
        for sub_section in string_splitted:
            if len(sub_section) > 1:
                response = self.select_section(sub_section, thread, username, 'error', message)
                msg += response[0]
                new_reg += response[1]
        print(msg)
        self.add_new_record(new_reg)


    def warning(self, message, username=None, thread='Default'):
        string_splitted = self.string_format.split('%')
        msg = ''
        new_reg = ''
        for sub_section in string_splitted:
            if len(sub_section) > 1:
                response = self.select_section(sub_section, thread, username, 'warning', message)
                msg += response[0]
                new_reg += response[1]
        print(msg)
        self.add_new_record(new_reg)


    def critical(self, message, username=None, thread='Default'):
        string_splitted = self.string_format.split('%')
        msg = ''
        new_reg = ''
        for sub_section in string_splitted:
            if len(sub_section) > 1:
                response = self.select_section(sub_section, thread, username, 'critical', message)
                msg += response[0]
                new_reg += response[1]
        print(msg)
        self.add_new_record(new_reg)


    def select_section(self, sub_section, thread, username, category, message):
        switch_case = {
            'DATETIME': self.sect_datetime(),
            'THREAD': self.sect_thread(thread),
            'USERNAME': self.sect_username(username),
            'CATEGORY': self.sect_category(category),
            'MESSAGE': self.sect_message(message)
        }
        return switch_case.get(sub_section, self.sect_default(sub_section))


    def sect_datetime(self):
        dt = self.datetime_now()
        msg = colorify(f'{dt}', self.color_palette['datetime']['font-color'], self.color_palette['datetime']['background-color'])
        new_reg = dt
        return [msg, new_reg]


    def sect_thread(self, thread):
        return [thread, thread]


    def sect_username(self, username):
        if username is None:
            username = self.process_name.upper()
        return [username, username]


    def sect_category(self, category):
        text = f' {category.upper()} '
        msg_colored = colorify(text, self.color_palette[category]['font-color'], self.color_palette[category]['background-color'])
        return [msg_colored, text]
    

    def sect_message(self, msg):
        return [msg, msg]

    def sect_default(self, chars):
        return [chars, chars]
