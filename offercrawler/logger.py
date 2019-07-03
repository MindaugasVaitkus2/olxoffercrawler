import datetime


class Logger(object):
    LAST_RUN_FILE = "lastrun.txt"
    CURRENT_DATETIME = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")

    def get_last_run(self):
        with open(Logger.LAST_RUN_FILE, "r") as f:
            return f.readline()
      
    def save_last_run(self):
        with open(Logger.LAST_RUN_FILE, "w") as f:
            f.write(Logger.CURRENT_DATETIME)
