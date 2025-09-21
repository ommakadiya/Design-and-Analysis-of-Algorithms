def jobScheduling(jobs, deadlines, profits):
    n = len(jobs)
    
    job_data = list(zip(jobs, deadlines, profits))

    
    job_data.sort(key=lambda x: x[2], reverse=True)

    
    max_deadline = max(deadlines)
    schedule = [0] * max_deadline

    job_sequence = [None] * max_deadline

    total_profit = 0

    for job, deadline, profit in job_data:
        
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[j] == 0:
                schedule[j] = 1
                job_sequence[j] = job
                total_profit += profit
                break

    print("Scheduled jobs:", [job for job in job_sequence if job is not None])
    print("Max profit:", total_profit)
    return job_sequence


jobs = ["a", "b", "c", "d", "e","f"]
deadlines = [2, 1, 3, 1, 2, 1]
profits = [100, 20, 35, 27, 30,28]
jobScheduling(jobs, deadlines, profits)