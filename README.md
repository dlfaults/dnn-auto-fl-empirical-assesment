This replication package supports the results presented int the paper "An Empirical Study of Fault Localisation Techniques
for Deep Neural Networks".

The artefact structure:

Folder 'figures': Contains plots for FL part used in the paper

Folder 'Tool Outputs': Contains raw FL tool output

Folder ‘ALT_GT’: Contains raw neutrality analysis results

Folder 'ALT_GT_CALCULATION':
- Folder 'input': input files to calculate results with alternative GT
- Folder 'results': FL tool results when alternative GT is taken into account

File ‘FL Results.xlsx’ contains all the main results of the paper:
- Sheet'PT1_FULL': contains cleaned outputs of the tools and RC results based on the original ground truth (GT) based on 20 runs of the tools (one for DFD and NL) (part 1 of the benchmark)
- Sheet 'PT1_orig_GT_results_full_sum': contains tools' outputs stats, RC, PR, F3 results based on the original ground truth (GT)  (part 1 of the benchmark)
- Sheet 'PT1_orig_altGT_results_full': contains full results (RC, PR, F3) for the original GT and for the alternative GT (part 1 of the benchmark)
- Sheet 'PT1_F1F2_orig_altGT_res_full': contains full results (RC, PR, F3) with addition of F1 and F2 metrics for the original GT and for the alternative    (part 1 of the benchmark)
- Sheet 'PT1_F1F2 of orig_altGT_res_sum': contains best results (RC, PR, F1, F2 F3) metrics for the original GT and for the alternative    (part 1 of the benchmark)
- Sheet 'PT1_RES_table': rounded data of 'PT1_F1F2 of orig_altGT_res_sum'
- Sheet 'PT2_NEW REAL FAULTS': benchmark part 2, info on FL tool applicability
- Sheet 'PT2_res NEW REAL FAULTS': contains cleaned outputs of the tools and RC results based on the original ground truth (GT) based on 20 runs of the tools (one for DFD and NL) (part 2 of the benchmark)
- Sheet 'PT2_orig_gt_results_full': contains tools' outputs stats, RC, PR, F3 results based on the original ground truth (GT)  (part 2 of the benchmark)
- Sheet 'PT2_orig_gt_results_full': contains full results (RC, PR, F1, F2 F3) for the original GT and for the alternative GT (part 2 of the benchmark)
- Sheet 'PT2_orig_altGT_res_sum': contains best results (RC, PR, F1, F2 F3) metrics for the original GT and for the alternative    (part 2 of the benchmark)
- Sheet 'Timing RAW': contains all timing results for 20 tools runs (one for DFD and NL) over whole benchmark
- Sheet 'STAT RESULTS': contains statistical test results for timing results comparison

File 'FL Tables.xlsx': contains tables used in the publication: Table 1, Tables 5-13

Folder 'STAT_TEST_RC':
- File 'results_old_new.csv': Contains FL tools results that are used as input for statistical test of tools' performance
- File 'results_stat_test_power.csv': Contains statistical test results

File 'F1vsF2vsF3.xlsx': Contains comparison of main results for F1, F2, F3 metrics

Folder 'TIMING':
Folder ‘scripts’ contains the code used to process the results:
 - ‘stat_test.py’: calculates statistical significance of FL tools' results
 - 'timings_stat.py': applies statistical test to FL tools' timing results
 - 'calc_AJ.py': calculates alternative GT results (first batch of faults)
 - 'CALC_AJ_NEWRF.py': calculates alternative GT results (second batch of faults)
