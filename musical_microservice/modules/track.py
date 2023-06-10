import queue

class Track:
    def __init__(self, num_steps: int):
        self.queue: queue.Queue[bytes] = queue.Queue(maxsize=num_steps)

    def queue(self, audio_bytes: bytes):
        self.queue.put_nowait(audio_bytes)

    def step(self):
        return self.queue.get_nowait()
