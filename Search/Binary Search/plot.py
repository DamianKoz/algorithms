from matplotlib import pyplot as plt
import math
import os

fig, ax = plt.subplots()

# O(n)
n = [x for x in range(1, 100000)]

# O(logn)
logn = [math.log(x, 2) for x in range(1, 100000)]

ax.plot(n)
ax.plot(logn)
plt.xlabel("Number of Entries")
plt.ylabel("Worst number of Steps needed to find an entry")
plt.title("O(n) vs O(logn)")
plt.legend(["O(n)", "O(Logn)"])


path = os.path.join("Search", "Binary Search", "runtime.jpg")
# plt.savefig("Search/Binary Search/runtime_binary_search.jpg")
plt.savefig(path, dpi=300)