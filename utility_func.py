import os
import pathlib
from datetime import datetime

from extensions_directory_map import ext_dir_map


def get_mapping_dict(managing_dir):
    mapping = {}
    for k, v in ext_dir_map.items():
        for sub_k in k:
            mapping[sub_k] = os.path.join(managing_dir, *v)
    return mapping


def get_year_month():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%b")
    return year, month


def create_path(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


def create_destination_file_path_with_year_month(ext_dir):
    create_path(os.path.join(ext_dir, *get_year_month()))


def get_absolute_file_destination_path(ext_dir, new_name):
    create_destination_file_path_with_year_month(ext_dir)
    return os.path.join(ext_dir, *get_year_month(), new_name)


def get_absolute_file_source_path(folder_to_track, file_name):
    return os.path.join(folder_to_track, file_name)
