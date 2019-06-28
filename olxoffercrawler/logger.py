import datetime


class Logger(object):
    LOG_FILE = "crawlerlog.txt"

    def new_log(msg, error=False):
        date_now_formatted = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
        if error:
            log_msg = "[Error {date}]\n".format(date=date_now_formatted)
        else:
            log_msg = "[Crawl {date}]\n".format(date=date_now_formatted)
        
        with open(Logger.LOG_FILE, "a") as f:
            f.write(log_msg)
            f.write(msg)
            f.write("\n\n")
            
