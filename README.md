This replication package supports the results presented int the paper "An Empirical Study of Fault Localisation Techniques
for Deep Learning".

The artefact structure:

File ‘Tool_Outputs.zip’ contains raw outputs of the tools.

File ‘ALT_GT.zip’ contains raw neutrality analysis results.

Folder ‘scripts’ contains the code used to process the results:
 - ‘stat_test.py’ calculates statistical significance of results that are for convenience all stored in the ‘results_old_new.csv’

The ‘FL Results.xlsx’ contains all the main results of the paper:

On ‘FULL (20)’ sheet one can found cleaned outputs of the tools and the Recall (RC) results based on the original ground truth (GT) based on 20 runs of the tools (or 20 instances of each model in the case of DeepFDF).

On the sheet ‘orig_GT_results_full_summary’ we provide full results on the benchmark calculated using the original GT, including the averages. The evaluation metrics include Recall, Precision (PR), and F3 score (Tables 4-8).

The ‘orig_altGT_results_full’ sheet, in addition to the original GT results, cointans all the alternative ground truth options and results of the tools on these GTs.

The orig_altGT_results_summary' sheet gathers and compares the RC, PR, F3 results for all the tools before and after the alternative ground truth.

The ‘new_res_table’ sheet contains the Table 10 of the paper.

The sheet ‘Timing (20)’ contains the average execution time measurements for all the tools on 20 repetitions (1 repetition for DFD as it handles the stability issue internally) (Table 12).
