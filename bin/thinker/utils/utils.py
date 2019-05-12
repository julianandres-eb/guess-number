class Utils:

    def __init__(self):
        print("0")

    def get_class(self, fullClassName):
        parts = fullClassName.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m