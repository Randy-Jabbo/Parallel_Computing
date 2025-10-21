import math
import time
import argparse
import multiprocessing as mp
import math
import matplotlib.pyplot as plt

def Primes(N):
    # Compute the first N prime numbers using the Sieve algorithm
    if N < 6:
        limit = 15
    else:
        limit = int(N * (math.log(N) + math.log(math.log(N)))) + 3

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b"\x00" * (((limit - p*p) // p) + 1)

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes[:N]


def worker(numbers):
    # I am using a strategy called the segmented sieve to find primes in a given range of numbers
    #each call of the worker function finds all primes in the given list of numbers
    if not numbers:
        return []

    lo = numbers[0]
    hi = numbers[-1]
    if hi < 2:
        return []

    base_limit = int(math.isqrt(hi))
    base = bytearray(b"\x01") * (base_limit + 1)
    base[0:2] = b"\x00\x00"
    for p in range(2, int(base_limit ** 0.5) + 1):
        if base[p]:
            base[p*p:base_limit+1:p] = b"\x00" * (((base_limit - p*p) // p) + 1)

    base_primes = [i for i, v in enumerate(base) if v]
    seg = bytearray(b"\x01") * (hi - lo + 1)
    for p in base_primes:
        start = max(p * p, ((lo + p - 1) // p) * p)
        for m in range(start, hi + 1, p):
            seg[m - lo] = 0

    return [lo + i for i, v in enumerate(seg) if v and lo + i >= 2]

def plot_primes(primes):
    k = range(1, len(primes) + 1)
    plt.figure(figsize=(7, 4))
    plt.scatter(k, primes, linewidth=1)
    plt.title("First N Primes")
    plt.tight_layout()
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", "--N", type=int, required=True) # get argument from terminal for number of primes to find
    args = parser.parse_args()
    N = args.N

    t0 = time.perf_counter()
    primes_single = Primes(N)
    time_s = time.perf_counter() - t0 # single process time is faster than multiprocess for finding primes
    # print(time_s)

    plot_primes(primes_single)

    n_proc = mp.cpu_count() # get number of available processors in pericular computer

    search_limit = N * 12
    numbers = list(range(2, search_limit)) # get the range of numbers to search for primes

    chunk_size = len(numbers) // n_proc or 1
    chunks = [numbers[i*chunk_size : (i+1)*chunk_size] for i in range(n_proc-1)]
    chunks.append(numbers[(n_proc-1)*chunk_size:]) # break the numebers into chunks for each process

    t0 = time.perf_counter()
    with mp.Pool(n_proc) as pool:
        results = pool.map(worker, chunks) # run the mulriprocess prime search
    dt_mp = time.perf_counter() - t0

    all_primes = sorted(p for chunk in results for p in chunk) # put all the found primes together and sort them
    primes_mp = all_primes[:N]

    print(f"slower multiprocess strategy: {dt_mp}")
    print(f"faster single process:{time_s}") # we can see that single process is faster for finding primes
    print(len(primes_mp))

if __name__ == "__main__":
    main()
