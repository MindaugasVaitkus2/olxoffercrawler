import datetime


class Logger(object):
    LOG_FILE = "crawlerlog.txt"
    LAST_RUN_FILE = "lastrun.txt"
    DATE_NOW_FORMATTED = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def new_log(msg, error=False):
        if error:
            log_msg = "[Error {date}]\n".format(date=Logger.DATE_NOW_FORMATTED)
        else:
            log_msg = "[Crawl {date}]\n".format(date=Logger.DATE_NOW_FORMATTED)
        
        with open(Logger.LOG_FILE, "a") as f:
            f.write(log_msg)
            f.write(msg)
            f.write("\n\n")
            
    def get_last_run():
        with open(Logger.LAST_RUN_FILE, "r") as f:
            last_run = f.readline().strip()

        return last_run       

    def save_last_run():
        with open(Logger.LAST_RUN_FILE, "w") as f:
            f.write(Logger.DATE_NOW_FORMATTED)
