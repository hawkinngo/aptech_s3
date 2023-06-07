# import pandas as pd

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/panicpotatoe/dataset-practical-stats/main/state.csv"
# )

# print(df.columns)

# total_state = len(df)
# total_murder_rate = df["Murder.Rate"].sum()
# mean_murder_rate = total_murder_rate / total_state
# print(mean_murder_rate)

# i = 0
# total_mr = 0
# for i_rec, rec in df.iterrows():
#     total_mr += rec["Murder.Rate"]
#     i += 1

# mean_mr = total_mr / i
# print(mean_mr)


# mean_mr_least = sum([df["Murder.Rate"][i] for i in range(len(df))]) / len(df)
# print(mean_mr_least)

import random

ran_list = random.sample(range(1, 3000000), 2000000)

aaa = [i for i in ran_list]

print(sum(aaa))

bbb = lambda a=0: a + 5
print(bbb())
