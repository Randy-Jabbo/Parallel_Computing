
    pi_est, inside, outside = MonteCarlo(num_points)

    n_proc = mp.cpu_count()
    chunk = num_points // n_proc


    with mp.Pool(processes=n_proc) as pool:
        results = pool.map(MonteCarlo, [chunk] * n_proc)

    pi_est, inside_returns, outside_returns = zip(*results)

    total_points = chunk * n_proc
    # adds all the points generated inside the circle from each process to the total
    total_inside = sum(arr.shape[1] for arr in inside_returns) 
    pi_est = 4.0 * total_inside / total_points

    inside = np.concatenate(inside_returns, axis=1)
    outside = np.concatenate(outside_returns, axis=1)