import numpy as np
import multiprocessing as mp
import time
import matplotlib.pyplot as plt

def MonteCarlo(num_points):
    rng = np.random.default_rng()
    x = rng.uniform(-1, 1, num_points)
    y = rng.uniform(-1, 1, num_points)
    r2 = x*x + y*y

    inside = r2 <= 1.0
    pi_est = 4.0 * inside.mean(dtype=np.float64)

    inside_points  = np.stack((x[inside],  y[inside]),  axis=0)  # (2, I)
    outside_points = np.stack((x[~inside], y[~inside]), axis=0)  # (2, O)
    return pi_est, inside_points, outside_points

def plot(inside_points, outside_points):
    plt.figure(figsize=(6,6))

    plt.scatter(inside_points[0], inside_points[1], color='red', s=1, label='Inside Circle')
    plt.scatter(outside_points[0], outside_points[1], color='blue', s=1, label='Outside Circle')

    plt.title('Monte Carlo Simulation of Pi')
    plt.show()


def main():
    num_points = 10_000_000


    # Single process is a lot faster then multoprocess when computing the Monte Carlo simulation because the function needs to return big arrays
    t0 = time.perf_counter()
    pi_est, inside, outside = MonteCarlo(num_points)
    timer = time.perf_counter() - t0
    print(pi_est)
    print(inside.shape, outside.shape)
    print(timer)

    plot(inside, outside)

    n_proc = 8 #mp.cpu_count()
    print(n_proc)
    chunk = num_points // n_proc
    sizes = [chunk] * n_proc
    sizes[-1] += num_points - chunk * n_proc  # handle remainder

    t0 = time.perf_counter()
    with mp.Pool(processes=n_proc) as pool:
        results = pool.map(MonteCarlo, sizes)
    time_mp = time.perf_counter() - t0

    pi_parts, inside_parts, outside_parts = zip(*results)

    total_points = num_points
    total_inside = sum(arr.shape[1] for arr in inside_parts)
    pi_est_mp = 4.0 * total_inside / total_points

    inside_all = np.concatenate(inside_parts, axis=1)
    outside_all = np.concatenate(outside_parts, axis=1)



    print(pi_est_mp)
    print(inside_all.shape,outside_all.shape)
    print(time_mp)




if __name__ == "__main__":
    main()
