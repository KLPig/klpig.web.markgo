class MarkGoLanguageError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'Not writen in markgo language.'


class MarkGoArgumentNumberError(Exception):
    def __init__(self, expected, instant):
        self.expected = expected
        self.instant = instant

    def __str__(self):
        return (f'Expect {self.expected} arguments, '
                f'but {self.instant} was given')


class MarkGoSyntaxError(Exception):
    def __init__(self, char):
        self.c = char

    def __str__(self):
        return f'Invalid syntax in character "{self.c}"'


class MarkGoProcessorError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid processor {self.name}'
