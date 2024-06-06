from typing import Callable, Optional, Any, List, Dict
from threading import Thread

class BetterThread:
    def __init__(self, target: Callable[..., Any], daemon = True, args: Optional[List] = None, kwargs: Optional[Dict] = None):
        self.target = target
        self.args = args if args is not None else []
        self.kwargs = kwargs if kwargs is not None else {}
        self._thread = Thread(target=self._middleman_function, daemon=daemon)
        self._callback = None
        self.value = None

    def _middleman_function(self):
        self.value = self.target(*self.args, **self.kwargs)
        if self._callback:
            self._callback(self.value)

    def start(self):
        self._thread.start()

    def join(self):
        self._thread.join()

    def connect(self, callback: Callable[[Any], None]):
        self._callback = callback
