from transitions import Machine
from transitions.extensions.states import Timeout
from transitions.extensions.states import add_state_features
import time
import random

@add_state_features(Timeout)
class CustomMachine(Machine):
    pass

class Container:

    def __init__(self, name, timeout=0):
        self.name = name

        self.states = [
            {'name': 'waiting', 'timeout': timeout, 'on_timeout': self.on_timeout},
            {'name': 'pulling', 'timeout': timeout, 'on_timeout': self.on_timeout},
            {'name': 'running', 'timeout': timeout, 'on_timeout': self.on_timeout},
            {'name': 'sending', 'timeout': timeout, 'on_timeout': self.on_timeout},
            'stopped'
        ]
        self.machine = CustomMachine(model=self, states=self.states, initial='waiting')
        self.machine.add_ordered_transitions()
        self.set_callbacks()
        self.results = None
    
    def set_callbacks(self):
        self.machine.on_enter_pulling('on_pulling')
        self.machine.on_enter_running('on_running')
        self.machine.on_enter_sending('on_sending')
        self.machine.on_enter_stopped('on_stopped')
    
    def on_timeout(self):
        print("{0} timeout in {1}".format(self.name, self.state))
        self.to_stopped(success=False)

    def start(self):
        self.start_time = time.time()
        self.to_pulling()

    def on_pulling(self):
        print("{0} Pulling...".format(self.name))
        time.sleep(random.randint(1,5))
        self.next_state()

    def on_running(self):
        print("{0} Running...".format(self.name))
        time.sleep(random.randint(1,10))
        self.next_state()

    def on_sending(self):
        print("{0} Sending...".format(self.name))
        time.sleep(random.randint(1,3))
        self.next_state()

    def on_stopped(self, success):
        self.end_time = time.time()
        self.results = {
            'reporter': self.name,
            'time': (self.end_time - self.start_time),
            'error': not success
        }
        print("{} DONE!".format(self.name))

    def get_results(self):
        return self.results


