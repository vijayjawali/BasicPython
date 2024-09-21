class CPU:
    def __init__(self, model):
        self.model = model

    def process(self):
        print(f"{self.model} CPU is processing data.")


class RAM:
    def __init__(self, size):
        self.size = size

    def load(self):
        print(f"{self.size}GB RAM is loading data.")


class Computer:
    def __init__(self, cpu_model, ram_size):
        self.cpu = CPU(cpu_model)
        self.ram = RAM(ram_size)

    def start(self):
        self.cpu.process()
        self.ram.load()
        print("Computer is starting up.")


# Usage
my_computer = Computer("Intel i7", 16)
my_computer.start()
