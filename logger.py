from colorify import *          # COLORIFY API: https://pypi.org/project/colorify/
from datetime import datetime   # DATETIME OBJECTS: https://docs.python.org/3/library/datetime.html#datetime-objects
from platform import system
from pathlib import Path
from os.path import exists

class Logger():

    init_colorify()
    def __init__(self, bot):
        self.process_name = bot
        self.datetime_format = '%d/%m/%Y %H:%M:%S'
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
            print("ERROR AL CREAR EL DIRECTORIO DE REGISTRO DE LOGS.\n¡¡¡COMPRUEBE LOS PERMISOS DE EJECUCIÓN!!!")


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
                print('ERROR AL CREAR EL ARCHIVO DE LOG.\n¡¡¡COMPRUEBE LOS PERMISOS DE EJECUCIÓN!!!')
                

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
                 f'*********                Fecha del creación: {dt.day}/{month}/{dt.year}' \
                 f'               *********\n' \
                 f'*********                                                             *********\n' \
                 f'*********                                                             *********\n' \
                 f'*******************************************************************************\n' \
                 f'*******************************************************************************\n\n\n\n'

        f = open(f'{self.logs_fullpath}/{self.file_name}', 'a')
        f.write(header)
        f.close()
        self.info(f'Se ha creado el log de registro para "{self.process_name}".')


    def add_new_record(self, category, dt, username, message):
        if self.file_exists() == False:
            self.create_new_log()
        new_log = f'{dt} || {username} || {category} || {message}'
        f = open(f'{self.logs_fullpath}/{self.file_name}', 'a')
        f.write(f'{new_log}\n')
        f.close()


    def info(self, message, username=None):
        dt = self.datetime_now()
        if username is None:
            username = self.process_name.upper()
        msg = colorify(f"{dt}", C.cyan)
        msg += f' || {username} ||'
        msg += colorify(" INFO ", C.white, C.blue)
        msg += f'|| {message}'
        print(msg)
        self.add_new_record("INFO", dt, username, message)


    def exception(self, message, username=None):
        dt = self.datetime_now()
        if username is None:
            username = self.process_name.upper()
        msg = colorify(f"{dt}", C.cyan)
        msg += f' || {username} ||'
        msg += colorify(" EXCEPTION ", C.white, C.orange)
        msg += f'|| {message}'
        print(msg)
        self.add_new_record("EXCEPTION", dt, username, message)


    def error(self, message, username=None):
        dt = self.datetime_now()
        if username is None:
            username = self.process_name.upper()
        msg = colorify(f"{dt}", C.cyan)
        msg += f' || {username} ||'
        msg += colorify(" ERROR ", C.white, C.red)
        msg += f'|| {message}'
        print(msg)
        self.add_new_record("ERROR", dt, username, message)


    def warning(self, message, username=None):
        dt = self.datetime_now()
        if username is None:
            username = self.process_name.upper()
        msg = colorify(f"{dt}", C.cyan)
        msg += f' || {username} ||'
        msg += colorify(" WARNING ", C.white, C.yellow)
        msg += f'|| {message}'
        print(msg)
        self.add_new_record("WARNING", dt, username, message)


    def critical(self, message, username=None):
        dt = self.datetime_now()
        if username is None:
            username = self.process_name.upper()
        msg = colorify(f"{dt}", C.cyan)
        msg += f' || {username} ||'
        msg += colorify(" CRITICAL ", C.white, C.crimson)
        msg += f'|| {message}'
        print(msg)
        self.add_new_record("CRITICAL", dt, username, message)
