import signal


class TimeOutException(Exception):
    pass


class ProcessTimeOut(object):

    def __init__(self):
        signal.signal(signal.SIGALRM, self.time_out_handler)
        self.TimeOutException = TimeOutException
        self.secs = 0
        self.minutes = 0
        self.hours = 0

    def time_out_handler(self, signum, frame):
        out_str = f'{self.hours} ' * (self.hours > 0)
        out_str += f'{self.minutes} ' * (self.minutes > 0)
        out_str += f'{self.secs} ' * (self.secs > 0)
        raise TimeOutException('FLow run for more than {}'.format(out_str))

    def start_timer(self, secs=0, minutes=0, hours=0):
        t = secs + 60 * minutes + hours * 3600
        self.secs = secs
        self.minutes = minutes
        self.hours = hours
        signal.alarm(t)

    @staticmethod
    def clear_timer():
        signal.alarm(0)
