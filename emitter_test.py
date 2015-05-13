
from unittest import TestCase
from emitter import Emitter


class TestEmitter(TestCase):
    def setUp(self):
        self.emitter = Emitter()

    def test_call_listeners(self):
        called = [False]

        def cb():
            called[0] = True

        self.emitter.on('hello.*', cb)
        self.emitter.emit('hello.foo')
        assert called[0]
        self.emitter.remove('hello.*', cb)
        assert self.emitter.listeners('hello') == []

    def test_pass_data_to_listeners(self):
        def cb(*args):
            assert args == ('a', 'b')

        self.emitter.on('data', cb)
        self.emitter.emit('data', 'a', 'b')

    def test_call_listeners_once(self):
        called = [False]

        def cb():
            called[0] = not called[0]

        self.emitter.on('once', cb, True)
        self.emitter.emit('*')
        self.emitter.emit('on*')
        assert called[0]

    def test_remove_listeners(self):
        self.emitter.on('foo', lambda x: x)
        self.emitter.on('bar', lambda x: x)

        self.emitter.remove('bar')
        self.emitter.remove('*')
        assert self.emitter.listeners('foo') == []
        assert self.emitter.listeners('bar') == []

    def test_emit_unknown_events(self):
        self.emitter.emit('quux')
        self.emitter.remove('wut')

    def test_provide_listeners(self):
        def cb(): pass

        self.emitter.on('quux', cb)
        assert self.emitter.listeners('*') == [cb]
