class Pylounge:
    def __init__(self, videos) -> None:
        self._videos = [*videos]
    def __iter__(self):
        return self
    def __next__(self):
        if self._videos:
            return self._videos.pop()
        else:
            raise StopIteration

pylounge = Pylounge(['1', '2', '3', '4'])
for video in pylounge:
    print(video)