from __future__ import annotations

from random import randrange

from flower_market.price_list.observer_pattern.observer import Observer
from flower_market.price_list.observer_pattern.subject import Subject
from typing import List


class Broker(Subject):

    _coefficient: float = None
    _observers: List[Observer] = []

    @property
    def coefficient(self):
        return self._coefficient

    def attach(self, observer: Observer) -> None:
        print("Broker: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print(f"Broker: Notifying observers... {self._observers}")
        for observer in self._observers:
            observer.update(self)

    def its_time_to_fetch_prices(self) -> None:
        print("\nBroker: I'm doing something important.")
        self._coefficient = float(f"1.{randrange(0, 50)}")

        print(f"Broker: My coefficient has just changed to: {self._coefficient}")
        self.notify()

