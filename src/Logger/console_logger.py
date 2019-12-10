import os
import sys
import time


class ConsoleLogger:

    logging_active = True

    @classmethod
    def log_message(cls, msg):
        # sys.stdout.flush()
        if cls.logging_active:
            # print("\r{0}".format(msg))
            sys.stdout.write(str(msg+"\n"))
            sys.stdout.flush()

    @classmethod
    def clean(cls):
        if cls.logging_active:
            os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def log_with_await(cls, msg, await_time, unit_time=1):
        if cls.logging_active:
            sys.stdout.write("{}".format(msg))
            sys.stdout.flush()
            for i in range(0, await_time):
                sys.stdout.write(str(await_time-i) + " ")
                time.sleep(unit_time)
                sys.stdout.flush()
            cls.clean()

    @classmethod
    def log_queue(cls, qtype, count, customer_symbol="*"):
        if cls.logging_active:
            stars = customer_symbol * count
            out = "{}: {}\n".format(qtype, stars)
            sys.stdout.write(out)
            sys.stdout.flush()




