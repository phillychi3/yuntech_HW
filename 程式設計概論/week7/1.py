class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1

    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"


class Clock(Stopwatch):
    def __init__(self, hours=0, minutes=0, seconds=0):
        super().__init__()
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        super().tick()
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
            if self.hours >= 24:
                self.hours = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


def clockCheck(h, m, s):
    clock = Clock(h, m, s)
    for _ in range(5):
        print(clock)
        clock.tick()
    print()


def stopWatchCheck(n):
    stopWatch = Stopwatch()
    for i in range(n):
        stopWatch.tick()
        if i > n - 7:
            print(stopWatch)
    print()


stopWatchCheck(63)
stopWatchCheck(3603)
clockCheck(5, 59, 57)
clockCheck(12, 29, 58)
clockCheck(23, 59, 58)
