from src.process_interupt_timer import ProcessTimeOut
import time


def loop(n):
    for sec in range(n):
        # print("sec {}".format(sec))
        time.sleep(1)


def test_exception_raised():
    o = ProcessTimeOut()
    try:
        o.start_timer(2)
        loop(4)
    except o.TimeOutException as e:
        assert True


def test_cancel_process_timer():
    o = ProcessTimeOut()
    o.start_timer(4)
    loop(2)
    o.clear_timer()
    loop(2)

