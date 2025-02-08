import pandas as pd
import csv

from glob import glob

from FL.get_res import get_dfd_res


def calc_results(gt, len_gt, fl_res, flag):
    match = ''
    match_cnt = 0

    for gt_e in gt:
        if flag == 'DFD':
            gt_e = ''.join([i for i in gt_e if not i.isdigit()])

        if gt_e in fl_res:
            match = match + '1 | '
            match_cnt += 1
        else:
            match = match + '0 | '

    ajs = round(match_cnt / len_gt, 2)

    return match, match_cnt, ajs


##################################################################################################
#DFD issues
dfd, dfd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/input/dfd_deepfd.csv")
dd, dd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/input/dfd_dd.csv")
nl, nl_ajs_old = get_dfd_res("ALT_GT_CALCULATION/input/dfd_nl.csv")
um, um_ajs_old = get_dfd_res("ALT_GT_CALCULATION/input/dfd_um.csv")

res_file = "ALT_GT_CALCULATION/results/RF_res.csv"
res_ajs_file = "ALT_GT_CALCULATION/results/RF_res_ajs.csv"

search_folder_name = "ALT_GT/DeepFD_GT_BFS/"

##################################################################################################
# Mutants batchh 1

# dfd, dfd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_dfd.csv")
# dd, dd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_dd.csv")
# nl, nl_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_nl.csv")
# um, um_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_um.csv")
#
# res_file = "ALT_GT_CALCULATION/results/checked/AF_res.csv"
# res_ajs_file = "ALT_GT_CALCULATION/results/checked/AF_res_ajs.csv"
#
# search_folder_name = "ALT_GT/Mutants_GT_BFS_1/"

##################################################################################################
# Mutants batchh 2

# dfd, dfd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_CF_dfd.csv")
# dd, dd_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_CF_dd.csv")
# nl, nl_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_CF_nl.csv")
# um, um_ajs_old = get_dfd_res("ALT_GT_CALCULATION/checked/AF_CF_um.csv")
#
# res_file = "ALT_GT_CALCULATION/results/checked/AF_CF_res.csv"
# res_ajs_file = "ALT_GT_CALCULATION/results/checked/AF_CF_res_ajs.csv"
#
# search_folder_name = "ALT_GT/Mutants_GT_BFS_2/"

##################################################################################################

search_params = "*.tsv"

all_diff = {}
res_fdf = {}
res = []
res_ajs = []

# print(dfd)
# raise Exception()

files = glob(search_folder_name + search_params, recursive=True)

for file in files:
    with open(file) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        data_read = [row for row in rd if row[6].lower() == 'True'.lower()]

    if len(data_read) != 0:
        issue = file.replace(search_folder_name, '').split('_')[0]
        parent = data_read[0]
        pn_conf = parent[4].split(',')

        issue_diff = []
        for x in data_read:
            cn_conf = x[5].split(',')

            diff = []
            for i in range(len(pn_conf)):
                if pn_conf[i]!=cn_conf[i]:
                    diff.append(pn_conf[i].split('=')[0])

            issue_diff.append([x[1],diff])
        all_diff[issue] = issue_diff

for k, v in all_diff.items():
    max_ajs_dfd = 0
    max_ajs_dd = 0
    max_ajs_nl = 0
    max_ajs_um = 0

    for gt in v:
        flag = 'DFD'

        dfd_k = dfd[k]
        dd_k = dd[k]
        nl_k = nl[k]
        um_k = um[k]

        len_gt = len(gt[1])

        dfd_match, dfd_match_cnt, dfd_ajs = calc_results(gt[1], len_gt, dfd_k, 'DFD')

        dd_match, dd_match_cnt, dd_ajs = calc_results(gt[1], len_gt, dd_k, 'DD')
        nl_match, nl_match_cnt, nl_ajs = calc_results(gt[1], len_gt, nl_k, 'NL')
        um_match, um_match_cnt, um_ajs = calc_results(gt[1], len_gt, um_k, 'UM')

        if dfd_ajs > max_ajs_dfd: max_ajs_dfd = dfd_ajs
        if dd_ajs > max_ajs_dd: max_ajs_dd = dd_ajs
        if nl_ajs > max_ajs_nl: max_ajs_nl = nl_ajs
        if um_ajs > max_ajs_um: max_ajs_um = um_ajs

        res.append([k, gt[0], gt[1], len_gt, dfd_k, dfd_match, dfd_match_cnt, dfd_ajs,
                                             dd_k, dd_match, dd_match_cnt, dd_ajs,
                                             nl_k, nl_match, nl_match_cnt, nl_ajs,
                                             um_k, um_match, um_match_cnt, um_ajs])

    dfd_ajs_vals = dfd_ajs_old[k]
    dfd_ajs_vals.append(max_ajs_dfd)
    dfd_ajs_old[k] = dfd_ajs_vals

    dd_ajs_vals = dd_ajs_old[k]
    dd_ajs_vals.append(max_ajs_dd)
    dd_ajs_old[k] = dd_ajs_vals

    nl_ajs_vals = nl_ajs_old[k]
    nl_ajs_vals.append(max_ajs_nl)
    nl_ajs_old[k] = nl_ajs_vals

    um_ajs_vals = um_ajs_old[k]
    um_ajs_vals.append(max_ajs_um)
    um_ajs_old[k] = um_ajs_vals

    res_ajs.append([k, dfd_ajs_old[k][0], dfd_ajs_old[k][1],
                       dd_ajs_old[k][0], dd_ajs_old[k][1],
                       nl_ajs_old[k][0], nl_ajs_old[k][1],
                       um_ajs_old[k][0], um_ajs_old[k][1]])

# print(res)

with open(res_file, "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["issue", "GT_ID", "GT", "LEN_GT", "DFD_RES", "DSD_MATCH", "DFD_MATCH_CNT", "DFD_AJS",
                                                        "DD_RES", "DD_MATCH", "DD_MATCH_CNT", "DD_AJS",
                                                        "NL_RES", "NL_MATCH", "NL_MATCH_CNT", "NL_AJS",
                                                        "UM_RES", "UM_MATCH", "UM_MATCH_CNT", "UM_AJS"])  # write header
    writer.writerows(res)

with open(res_ajs_file, "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    writer.writerow(["issue", "DFD_AJS_OLD", "DSD_AJS_NEW",
                              "DD_AJS_OLD", "DD_AJS_NEW",
                              "NL_AJS_OLD", "NL_AJS_NEW",
                              "UM_AJS_OLD", "UM_AJS_NEW"])  # write header
    writer.writerows(res_ajs)
