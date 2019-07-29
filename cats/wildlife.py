from cats import Cat


class Wildlife(Cat):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def sleep(self):
        return ''

    def run(self, t):
        if t % 500000 == 0:
            print('Hi Nastia! My name is %s' % self.name)
