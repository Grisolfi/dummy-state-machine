from model.container import Container
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 4

def run(containeres):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exeggutor:
        for container in containeres:
            exeggutor.submit(container.start)

if __name__ == '__main__':

    u = Container('ubuntu')
    d = Container('debian')
    c = Container('centos')
    o = Container('opensuse', timeout=2)
    containeres = [u, d, o, c]
    run(containeres)

    
    