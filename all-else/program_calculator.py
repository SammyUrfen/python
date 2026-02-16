def sort_arrival_time(arrival_time, burst_time):
    for i in range(len(arrival_time)):
        for j in range(i+1, len(arrival_time)):
            if arrival_time[i] > arrival_time[j]:
                arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            elif arrival_time[i] == arrival_time[j]:
                if burst_time[i] > burst_time[j]:
                    arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
                    burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
    return arrival_time, burst_time


arrival_time = [1, 2, 1, 4]
burst_time = [3, 4, 2, 4]

arrival_time, burst_time = sort_arrival_time(arrival_time, burst_time)
uptime = arrival_time[0]
total_wait_time = 0
for i in range(len(arrival_time)):
    start_time = uptime
    completion_time = start_time + burst_time[i]
    turnaround_time = completion_time - arrival_time[i]
    waiting_time = turnaround_time - burst_time[i]
    print(f"Process {i+1}:")
    print(f"  Start Time: {start_time}")
    print(f"  Completion Time: {completion_time}")
    print(f"  Turnaround Time: {turnaround_time}")
    print(f"  Waiting Time: {waiting_time}")
    uptime += burst_time[i]
    print()
    total_wait_time += waiting_time

average_wait_time = total_wait_time / len(arrival_time)
print(f"Total Waiting Time: {total_wait_time}")
print(f"Average Waiting Time: {average_wait_time}")