import signal


class TimeOutException(Exception):
    pass


class ProcessTimeOut(object):

    def __init__(self):
        signal.signal(signal.SIGALRM, self.time_out_handler)
        self.TimeOutException = TimeOutException

    @staticmethod
    def time_out_handler(signum, frame):
        raise TimeOutException('FLow run for more than 20 hours...')

    @staticmethod
    def start_timer(secs=0, minutes=0, hours=0):
        t = secs + 60 * minutes + hours * 3600
        signal.alarm(t)

    @staticmethod
    def clear_timer():
        signal.alarm(0)
