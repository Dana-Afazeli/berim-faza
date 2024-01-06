def uunifast(u, task_criticalities, rng, hc_redundancy):
    rep = {'high':hc_redundancy, 'low':1}
    while True:
        utilizations = []
        sumU = u
        n = len(task_criticalities)
        for i in range(1, n):
            nextSumU = sumU * rng.random() ** (1.0 / (n - i))
            utilizations.append((sumU - nextSumU)/rep[task_criticalities[i]])
            sumU = nextSumU

        utilizations.append(sumU / rep[task_criticalities[-1]])
        
        if all(ut <= 1 for ut in utilizations):
            return utilizations
