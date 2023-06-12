import queue

class Track:
    def __init__(self, num_steps: int):
        self._queue: queue.Queue[bytes] = queue.Queue(maxsize=num_steps)

    def queue(self, audio_bytes: bytes):
        self._queue.put(audio_bytes, block=True)

    def step(self):
        return self._queue.get(block=True)
