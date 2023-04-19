class MealyStateMachine:
    def __init__(self):
        self.state = 'A'

    def mute(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'G':
            self.state = 'D'
            return 9
        elif self.state == 'B':
            self.state = 'G'
            return 3
        else:
            raise MealyError('mute')

    def look(self):
        if self.state == 'A':
            self.state = 'E'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('look')

    def click(self):
        if self.state == 'D':
            self.state = 'F'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 8
        else:
            raise MealyError('click')


class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


def main():
    return MealyStateMachine()


def test():
    o = main()
    o.mute()  # 0
    o.look()  # 2
    o.mute()  # 4
    o.click()  # 6
    o.click()  # 8
    o.mute()  # 9
    o.look()  # 5
    o.look()  # 7

    o = main()
    o.mute()  # 0
    o.look()  # 2
    try:
        o.look()  # MealyError
    except MealyError:
        pass
    o.mute()  # 4
    try:
        o.mute()  # MealyError
    except MealyError:
        pass
    o.click()  # 6
    try:
        o.look()  # MealyError
    except MealyError:
        pass
    o.click()
    o.mute()  # 9
    o.click()  # 6
    o.click()  # 8
    o.mute()  # 9
    o.look()  # 5
    o.look()  # 7
    o.click()  # 8
    o.mute()  # 9
    o = main()
    try:
        o.click()  # MealyError
    except MealyError:
        pass
    o.look()
    o = main()
    o.mute()
    o.mute()
