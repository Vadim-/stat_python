import numpy as np
from random import randint
import matplotlib.pyplot as pl

# rows=days x columns=hours 
n_days  = 30
n_hours = 24
random_month = np.random.randint(0, 9, (n_days, n_hours))

# find probability for of particular hour in each day
day_prob = []
for d in range(n_days):
	hour_prob = []
	for h in range(n_hours):
		hour_prob.append(random_month[d][h] / float(sum(random_month[d])))
	day_prob.append(hour_prob)

# find average probability per day = normalise per hour of the day
sum_hour_prob = np.zeros(24).reshape(24,1)
for d in range(n_days):
	for h in range(n_hours):
		sum_hour_prob[h] = sum(sum_hour_prob[h], day_prob[d][h])
average_prob_per_hour = sum_hour_prob / sum(sum_hour_prob)

# sum over rows
average_event_count_per_hour = random_month.sum(axis=0) / float(n_hours)  

index = np.arange(n_hours)
fig = pl.figure()

ax1 = fig.add_subplot(111)
ax1.bar(index, average_event_count_per_hour, width=0.5)
ax2 = fig.add_subplot(212)
ax2.bar(index, average_prob_per_hour, width=0.5)
pl.tight_layout()
pl.show()
