import threading
import time
from threaded_serializable_singleton import Singleton

instances = {}
threads = []


def create_singleton(value: str) -> None:
    singleton = Singleton(value=value)
    instances[str(id(singleton))] = 1


def check_singleton():
    print('Liczba instancji Singletona: ', len(instances))
    return len(instances)


def main():
    startTime = time.time()
    try:
        for _ in range(100):
            # Uruchomienie watkow
            try:
                for i in range(1000):
                    th = threading.Thread(target=create_singleton, name=f"th{i}", args=(f"th{i}",))
                    threads.append(th)
                    th.start()
            except Exception:
                print("Nie mozna uruchomic watkow")
            # Oczekiwanie na zakonczenie watkow
            for t in threads:
                t.join()
            count_instances = check_singleton()
            if count_instances > 1:
                raise Exception("Singleton not working")
    except KeyboardInterrupt:
        print(threads)
        print(len(threads))
    endTime = time.time()
    print('Czas dzialania: ', endTime - startTime)


if __name__ == "__main__":
    main()
