# interrupt Process Timer

Based on code from: Ref: https://code-maven.com/python-timeout

This little function can be used when a time limit for some process is needed. 
For example if you build [Prefect.io](https://www.prefect.io/) flows and want to limit how long a flow is allowed to run.

### Installation
directly from git:    
`pip3 install git+git://github.com/youdar/process_interupt_timer.git`

One can also download the code and 
`pip3 install <path>/process_interupt_timer`

### Usage example
```python  
from datetime import timedelta
from prefect import task, Flow
from prefect.schedules import CronSchedule
from process_interupt_timer import ProcessTimeOut

@task(max_retries=3, retry_delay=timedelta(minutes=10), log_stdout=True)
def task_1():
    # do some things
    return True
    
@task(max_retries=3, retry_delay=timedelta(minutes=10), log_stdout=True)
def next_task(r):
    # do some things
    return True
    
def main():
    # Example for some schedule
    schedule = CronSchedule("30 * * * *")
    
    # Create a timeout object
    fo = ProcessTimeOut()

    with Flow("My flow name", schedule=schedule) as flow:
        # Set timeout time
        fo.start_timer(hours=2)
        
        # The flow tasks
        r1 = task_1()
        r2 = next_task(r1)

        # Clear timeout alert if  task is done
        fo.clear_timer()

    # To register flow
    flow.register(project_name="My Precet project")


if __name__ == "__main__":
    main()

```  
