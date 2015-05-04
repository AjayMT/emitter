
# emitter
A simple event emitter for python.

## Installation
```sh
$ pip install emitter
```
or
```sh
$ python setup.py install
```

## API
### emitter.Emitter()
Event emitter class.

### Emitter#on(event, cb, once=False)
Add a listener for `event` with callback `cb`. If `once` is provided as true, the listener will be removed after it is called.

### Emitter#emit(event, args...)
Call all listeners for `event` with `args`.

### Emitter#remove(event=None, cb=None)
Remove listener `cb` for `event`. If `cb` is None, all listeners for `event` are removed. If `event` and `cb` are None, all listeners are removed.

## Running tests
```
$ pyvows
```

### License
MIT.
