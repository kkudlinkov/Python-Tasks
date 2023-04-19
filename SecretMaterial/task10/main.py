class Mealy:
    def __init__(self):
        self.state = 'A'

    def chalk(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'H'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'C'
            return 9
        elif self.state == 'H':
            self.state = 'E'
            return 11
        else:
            raise MealyError('chalk')

    def share(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'H'
            return 4
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 8
        elif self.state == 'H':
            self.state = 'H'
            return 10
        else:
            raise MealyError('share')


class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    return Mealy()


def test():
    o = main()
    try:
        o.share()
    except MealyError:
        pass
    assert o.chalk() == 0
    assert o.share() == 1

    assert o.chalk() == 3
    assert o.chalk() == 5
    try:
        o.chalk()
    except MealyError:
        pass
    assert o.share() == 6
    assert o.chalk() == 7
    assert o.share() == 8
    assert o.chalk() == 11

    o = main()
    assert o.chalk() == 0
    assert o.share() == 1
    assert o.share() == 4
    assert o.share() == 10

    o = main()
    assert o.chalk() == 0
    assert o.chalk() == 2
    assert o.share() == 10

    o = main()
    assert o.chalk() == 0
    assert o.share() == 1
    assert o.chalk() == 3
    assert o.chalk() == 5
    assert o.share() == 6
    assert o.chalk() == 7
    assert o.chalk() == 9


test()
