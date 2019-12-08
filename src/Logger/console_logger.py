import os
import sys
import time


class ConsoleLogger:

    @staticmethod
    def log_message(msg):
        print("\r{0}...".format(msg))
        # sys.stdout.write("\r{0}...".format(msg))
        # sys.stdout.flush()

    @staticmethod
    def clean():
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def log_with_await(cls, msg, await_time, unit_time=1):
        print("\r{}".format(msg))
        for i in range(0, await_time):
            print(await_time-i)
            time.sleep(unit_time)
        cls.clean()