# interrupt Process Timer

Based on code from: Ref: https://code-maven.com/python-timeout
This little function can be used when a time limit for some process is needed. 


### Installation
directly from git:    
`pip3 install git+git://github.com/youdar/process_interupt_timer.git`

One can also download the code and 
`pip3 install <path>/process_interupt_timer`

### Usage example
```python  
from process_interupt_timer import ProcessTimeOut
import time


def task_1():
    # do some things
    time.sleep(60 * 60 * 2)
    return True
    
    
def main():
    fo = ProcessTimeOut()

    # Set timeout time
    fo.start_timer(hours=1, minutes=5)
    
    # run the task
    r1 = task_1()

    # Clear timeout alert if  task is done
    fo.clear_timer()


if __name__ == "__main__":
    main()

```  
