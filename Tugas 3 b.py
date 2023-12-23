import numpy as np

j = [i for i in range(0, 26)]
k = np.sin(j)

# Mencetak judul
print("j\t k")

# Mencetak masing-masing pasangan nilai j dan k dalam satu baris terpisah
for ji, ki in zip(j, k):
    print(f"{ji}\t {ki}")
