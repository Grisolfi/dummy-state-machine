from model.container import Container
from concurrent.futures import ThreadPoolExecutor

MAX_WORKERS = 2

if __name__ == '__main__':

    u = Container('ubuntu')
    d = Container('debian')
    c = Container('centos')
    o = Container('opensuse', timeout=5)
    containeres = [u, d, c, o]

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exeggutor:
        for container in containeres:
            exeggutor.submit(container.start)
    
    for container in containeres:
        container.get_results()