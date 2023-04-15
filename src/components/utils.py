import os
import sys
import dill

import numpy as np
import pandas as pd

from src.exception import CustomException


def save_object(file_path, object):
    try:
        directory_path = os.path.dirname(file_path)

        os.makedirs(directory_path, exist_ok=True)

        with open(file_path, "wb") as file_object:
            dill.dump(object, file_object)

    except Exception as exception:
        raise CustomException(exception, sys)