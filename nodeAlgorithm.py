class node:
    def __init__(self, name):
        self.dictValue = name
        self.value = float('inf')
        self.next = []
        self.before = None
        self.END = False
        self.START = False