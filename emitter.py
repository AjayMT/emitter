
from fnmatch import fnmatch


class Emitter:
    def __init__(self):
        """Event emitter class."""
        self._listeners = {}

    def _query(self, ev):
        return {e: l for e, l in self._listeners.items() if fnmatch(e, ev)}

    def listeners(self, event):
        """Get all the listeners for an event.

        Arguments:
        event -- Event name. Can be a glob pattern.
        """
        cbs = [ls for e, ls in self._listeners.items()
               if fnmatch(event, e) or fnmatch(e, event)]

        return [l[0] for l in ls for ls in cbs]

    def on(self, event, cb, once=False):
        """Add an event listener.

        Arguments:
        event -- Event name. Can be a glob pattern.
        cb -- Function to be called when event is fired.
        once -- Whether or not to remove the listener after it's called.
          Defaults to False.
        """
        if event not in self._listeners:
            self._listeners[event] = []

        self._listeners[event].append([cb, once])

    def remove(self, event, cb=None):
        """Remove event listener(s).

        Arguments:
        event -- Event name. Can be a glob pattern.
        cb -- Callback to be removed. If None, removes all callbacks
          for specified event(s).
        """
        for e, v in self._query(event).items():
            for l in v:
                if l[0] == cb or not cb:
                    self._listeners[e].remove(l)

    def emit(self, event, *args):
        """Fire/emit an event, calling all listeners.

        Arguments:
        event -- Event name. Can be a glob pattern.
        *args -- Args to be passed to listeners
        """
        events = {e: l for e, l in self._listeners.items()
                  if fnmatch(event, e) or fnmatch(e, event)}

        if not events:
            return

        for ev, v in events.items():
            for l in v:
                l[0](*args)
                if l[1]:
                    self._listeners[ev].remove(l)
