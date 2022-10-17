from __future__ import absolute_import,unicode_literals
from celery.utils.log import get_task_logger
from celery import shared_task
import logging
import csv
import random
import os
from celery.app.log import *
logger = logging.getLogger(__name__)
logger = get_task_logger(__name__)

first_names=('John','Andy','Joe')
last_names=('Johnson','Smith','Williams')

@shared_task
def generate_file(filename,count):
    prev_dir=os.getcwd()
    new_dir=os.path.join(os.getcwd(),"data")
    if not os.path.exists(new_dir):
        os.mkdir("data")
    os.chdir(new_dir)
    with open(f'{filename}.csv', 'w', newline='') as file:
        fieldnames = ['Random Name', 'Random Number']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(count):
            writer.writerow({'Random Name': random.choice(first_names)+" "+random.choice(last_names), 'Random Number': random.randint(1, 500)})
    os.chdir(prev_dir)
    return "Success"

# @shared_task
# class TaskFormat(logging.Formatter):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         try:
#             from celery._state import get_current_task
#             self.get_current_task = get_current_task
#             print(self.get_current_task)
#             logger.info(self.get_current_task)
#         except ImportError:
#             self.get_current_task = lambda: None

    # def generate_file(self,filename,count):
    #     prev_dir=os.getcwd()
    #     new_dir=os.path.join(os.getcwd(),"data")
    #     if not os.path.exists(new_dir):
    #         os.mkdir("data")
    #     os.chdir(new_dir)
    #     with open(f'{filename}.csv', 'w', newline='') as file:
    #         fieldnames = ['Random Name', 'Random Number']
    #         writer = csv.DictWriter(file, fieldnames=fieldnames)
    #         writer.writeheader()
    #         for i in range(count):
    #             writer.writerow({'Random Name': random.choice(first_names)+" "+random.choice(last_names), 'Random Number': random.randint(1, 500)})
    #     os.chdir(prev_dir)
    #     logger.info(self.get_current_task)
    #     print(self.get_current_task)
    #     logger.debug("Success")
    #     return "Success"