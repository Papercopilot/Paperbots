import os
import json
import gspread
import pandas as pd
from .. import settings

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_settings(conf):
    """Load JSON file."""
    setting_path = os.path.join(settings.__path__[0], conf + '.json')
    with open(setting_path, 'r') as f:
        return json.load(f)
    
def save_json(path, data):
    """Save JSON file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    color_print('io', f'{path} saved.')
    
def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)
    
def color_print(type, msg):
    if type == 'info':
        # print(f'{bcolors.OKCYAN}[Info]{msg}{bcolors.ENDC}')
        print(f'[Info] {msg}')
    elif type == 'error':
        print(f'{bcolors.FAIL}[Error] {msg}{bcolors.ENDC}')
    elif type == 'success':
        print(f'{bcolors.OKGREEN}[Success] {msg}{bcolors.ENDC}')
    elif type == 'warning':
        print(f'{bcolors.WARNING}[Warning] {msg}{bcolors.ENDC}')
    elif type == 'io':
        print(f'{bcolors.OKBLUE}[IO] {msg}{bcolors.ENDC}')
    else:
        print(msg)
        
def gspread2pd(key, parse_header=False):
    gc = gspread.oauth()
    sh = gc.open_by_key(key)
    response = sh.sheet1.get_all_values() # header is included as row0
    df = pd.DataFrame.from_records(response)
    
    # process header if needed
    if parse_header:
        df.columns = df.iloc[0]
        df = df[1:]
        
    return df

def download_gspread_setting(key, json_path=None):
    try:
        gc = gspread.oauth()
        gc.open_by_key(key)
    except:
        authorized_user_path = '~/.config/gspread/authorized_user.json'
        if os.path.isfile(authorized_user_path):
            os.remove(authorized_user_path)
        
    # convert the loaded df to json and write as gform.json by default
    df = gspread2pd('1cWrKI8gDI-R6KOnoYkZHmEFfESU_rPLpkup8-Z0Km_0', parse_header=True)
    json_data = {df.columns[1]: df.set_index("conf").to_dict()[df.columns[1]]}
    save_json(os.path.join(settings.__path__[0], 'gform.json') if json_path == None else json_path, json_data)
        
def load_gspread_setting():
    """Load JSON file."""
    return load_settings('gform')