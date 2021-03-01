# State Machine with Py Transitions

Container model is an abstraction on what happens in a docker container execution 
but you could customize your workflow.  
Main app creates some instances of container and execute its cycle inside a threadpool. You could also configure the max workers for Threadpool 
## Container

Inside container model, there is five states and it will be executed in the following order:

1. waiting
1. pulling
1. running
1. sending
1. done 

There is also five methods on_<state_name> where is the callback function associated with the state_name, you can add your custom behavior for each state here.

By default, Container does not have any timeout. But you pass as argument on object construction. This implementation only receive one timeout value and applies it to each state execution.

There is a method on_timeout that is called when timeout is reached, you can add custom behavior to timeout event on Machines

## References:
1. https://github.com/pytransitions/transitions
2. https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor