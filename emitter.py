
class Emitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, cb, once=False):
        if event not in self._listeners:
            self._listeners[event] = []

        self._listeners[event].append([cb, once])

    def remove(self, event=None, cb=None):
        listeners = {}
        if not event:
            listeners = self._listeners
        else:
            if event in self._listeners:
                listeners[event] = self._listeners[event]

        for k, v in listeners.items():
            for l in v:
                if l[0] == cb or not cb:
                    self._listeners[k].remove(l)

    def emit(self, event, *args):
        if event not in self._listeners:
            return

        for l in self._listeners[event]:
            l[0](*args)
            if l[1]:
                self._listeners[event].remove(l)
