"""
Author:     LanHao
Date:       2020/11/16
Python:     python3.6

"""


from celery import shared_task


@shared_task
def add_log(data):
    print("add_log")