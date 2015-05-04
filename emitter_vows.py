
import emitter
from pyvows import Vows, expect


@Vows.batch
class Emitter(Vows.Context):
    def topic(self):
        return emitter.Emitter()

    def should_call_listeners(self, topic):
        called = [False]

        def cb():
            called[0] = True

        topic.on('hello', cb)
        topic.emit('hello')
        expect(called[0]).to_be_true()
        topic.remove('hello', cb)
        expect(topic._listeners['hello']).to_be_empty()

    def should_pass_data_to_listeners(self, topic):
        topic.on('data', lambda a, b: expect((a, b)).to_equal(('a', 'b')))
        topic.emit('data', 'a', 'b')

    def can_call_listeners_only_once(self, topic):
        called = [False]

        def cb():
            called[0] = not called[0]

        topic.on('once', cb, True)
        topic.emit('once')
        topic.emit('once')
        expect(called[0]).to_be_true()

    def should_remove_listeners(self, topic):
        topic.on('foo', lambda x: x)
        topic.on('bar', lambda x: x)

        topic.remove('bar')
        topic.remove()
        expect(topic._listeners['foo']).to_be_empty()
        expect(topic._listeners['bar']).to_be_empty()
