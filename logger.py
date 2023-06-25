from colorify import *
from datetime import datetime
from platform import system
from pathlib import Path
from os.path import exists

class Logger:
    init_colorify()

    color_palette = {
        'datetime': {'font-color': C.cyan, 'background-color': None},
        'info': {'font-color': C.white, 'background-color': C.blue},
        'exception': {'font-color': C.white, 'background-color': C.orange},
        'error': {'font-color': C.white, 'background-color': C.red},
        'warning': {'font-color': C.white, 'background-color': C.yellow},
        'critical': {'font-color': C.white, 'background-color': C.crimson},
    }

    def __init__(self, identifier):
        self.process_name = identifier
        self.datetime_format = '%d/%m/%Y %H:%M:%S.%f'
        self.string_format = '%DATETIME% || %CATEGORY% || %THREAD% || %USERNAME% || %MESSAGE%'

        self.logs_fullpath = ''
        self.file_name = ''

        self.get_logs_path()
        self.get_filename()


    def set_string_format(self, string_format):
        self.string_format = string_format


    def get_string_format(self):
        return self.string_format


    def datetime_now(self):
        now = datetime.now()
        return now.strftime(self.get_datetime_format())


    def set_datetime_format(self, format):
        self.datetime_format = format


    def get_datetime_format(self):
        return self.datetime_format


    def create_path(self):
        if not exists(self.logs_fullpath):
            try:
                os.makedirs(self.logs_fullpath)
            except:
                print('Error creating log folder. Please, check the execution privileges and try again.')


    def file_exists(self):
        path = Path(f'{self.logs_fullpath}/{self.file_name}')
        return path.is_file()


    def get_logs_path(self):
        if system() == 'Windows':
            self.logs_fullpath = os.path.join('logs', self.process_name)
        else:
            self.logs_fullpath = os.path.join('logs', self.process_name)


    def get_filename(self):
        self.create_path()
        dt = datetime.now()
        month = str(dt.month).zfill(2)

        if dt.weekday() == 0:
            self.file_name = f'{self.process_name}_{dt.day}{month}{dt.year}.log'
        else:
            last_monday = dt.day - dt.weekday()
            self.file_name = f'{self.process_name}_{last_monday}{month}{dt.year}.log'

        if not self.file_exists():
            try:
                self.create_new_log()
            except:
                print('Error creating log file. Please, check the execution privileges and try again.')


    def create_new_log(self):
        self.create_path()
        dt = datetime.now()
        month = str(dt.month).zfill(2)

        header = f'\n\n{"*" * 79}\n' \
                 f'{"*" * 79}\n' \
                 f'{"*" * 9}{" " * 61}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 61}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 18}AUTOCOINER SUPABASE - EVENT LOG{" " * 18}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 61}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 14}Creation date: {dt.day}/{month}/{dt.year}{" " * 14}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 61}{"*" * 9}\n' \
                 f'{"*" * 9}{" " * 61}{"*" * 9}\n' \
                 f'{"*" * 79}\n' \
                 f'{"*" * 79}\n\n\n\n'

        file_path = Path(f'{self.logs_fullpath}/{self.file_name}')
        with file_path.open('a') as f:
            f.write(header)

        self.info(f'Log file has been created successfully for "{self.process_name}".')


    def add_new_record(self, new_reg):
        if not self.file_exists():
            self.create_new_log()

        with open(f'{self.logs_fullpath}/{self.file_name}', 'a') as f:
            f.write(f'{new_reg}\n')


    def info(self, message, username=None, thread='Default'):
        msg = self.process_format_string(self.string_format, thread, username, 'info', message)
        print(msg)
        self.add_new_record(msg)


    def exception(self, message, username=None, thread='Default'):
        msg = self.process_format_string(self.string_format, thread, username, 'exception', message)
        print(msg)
        self.add_new_record(msg)


    def error(self, message, username=None, thread='Default'):
        msg = self.process_format_string(self.string_format, thread, username, 'error', message)
        print(msg)
        self.add_new_record(msg)


    def warning(self, message, username=None, thread='Default'):
        msg = self.process_format_string(self.string_format, thread, username, 'warning', message)
        print(msg)
        self.add_new_record(msg)


    def critical(self, message, username=None, thread='Default'):
        msg = self.process_format_string(self.string_format, thread, username, 'critical', message)
        print(msg)
        self.add_new_record(msg)


    def process_format_string(self, string, thread, username, category, message):
        sections = {
            'DATETIME': str(self.datetime_now()),
            'THREAD': self.format_section(thread),
            'USERNAME': self.format_section(username),
            'CATEGORY': self.format_category(category),
            'MESSAGE': self.format_section(message)
        }
        for section in sections:
            string = string.replace(f'%{section}%', sections[section])
        return string


    def format_category(self, category):
        if category in self.color_palette:
            font_color = self.color_palette[category]['font-color']
            background_color = self.color_palette[category]['background-color']
            return colorify(f'[{category.upper()}]', font_color, background_color)
        else:
            return ''


    def format_section(self, section, length=None):
        section = str(section)
        if length is not None and len(section) > length:
            section = section[:length-3] + '...'
        return section
