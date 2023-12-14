import csv

import pandas as pd

from POSTRMUT.statistical_killing import is_diff_sts, power_calculation



result_types = ["O", "OA"]
tools = ["DFD", "DD", "NL", "UM"]
metrics = ["RC"]#, "PR", "F3"

df = pd.read_csv("results_old_new.csv")
# print(df)

res_file = "results_stat_test_power.csv"
stat_results = [["TYPE", "TOOL_1", "TOOL_2", "METRIC", "IS_STS", "P_VALUE", "EFFECT_SIZE", "POWER"]]

for r_type in result_types:
    for i in range(len(tools)):
        for j in range(i+1,4):
            for metric in metrics:
                data_1 = df[(df['TYPE']==r_type) & (df["TOOL"]==tools[i])]
                data_1 = data_1[metric].tolist()

                data_2 = df[(df['TYPE'] == r_type) & (df["TOOL"] == tools[j])]
                data_2 = data_2[metric].tolist()
                # print(i, j)
                is_sts, p_value, effect_size = is_diff_sts(data_1, data_2)

                power_val = power_calculation(data_1, data_2)
                print(power_val)

                stat_results.append([r_type, tools[i], tools[j], metric, is_sts, p_value, effect_size, power_val])

with open(res_file, "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerows(stat_results)