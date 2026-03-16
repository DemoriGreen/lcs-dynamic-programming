import random
import json

DNA = ["A","C","G","T"]

def generate_sequence(length):
    return "".join(random.choice(DNA) for _ in range(length))

sizes = [10, 20, 50, 100, 500, 1000]

data = {}

for size in sizes:
    data[size] = {
        "seq1": generate_sequence(size),
        "seq2": generate_sequence(size)
    }

with open("dna_sequences.json","w") as f:
    json.dump(data, f, indent=4)

print("DNA sequences generated.")
