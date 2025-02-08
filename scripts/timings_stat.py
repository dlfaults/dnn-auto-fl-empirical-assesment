import pandas as pd
from scipy.stats import ranksums

# Load the input CSV file
def process_csv(input_file, output_file):
    # Read the input file
    data = pd.read_csv(input_file)

    # Prepare an empty list to store results
    results = []

    # Group by 'id'
    for program_id, group in data.groupby('id'):
        # Get the unique tools for this ID
        tools = group['tool'].unique()

        # Compare all pairs of tools
        for i, tool1 in enumerate(tools):
            for tool2 in tools[i + 1:]:
                if tool1 in ['DFD', 'NL'] and tool2 in ['DFD', 'NL']:
                    continue
                # Get the runtimes for both tools
                time1 = group[group['tool'] == tool1]['time'].values
                time2 = group[group['tool'] == tool2]['time'].values

                # Replicate the single value 20 times if needed
                if len(time1) == 1 and len(time2) == 20:
                    time1 = time1.repeat(20)
                elif len(time2) == 1 and len(time1) == 20:
                    time2 = time2.repeat(20)

                # Perform the Wilcoxon unpaired test (ranksums test)
                if len(time1) == len(time2):
                    stat, p_value = ranksums(time1, time2)

                    # Determine the outcome
                    outcome = p_value < 0.05

                    # Append the result
                    results.append({
                        'id': program_id,
                        'tool 1': tool1,
                        'tool 2': tool2,
                        'p-value': p_value,
                        'outcome': outcome
                    })
                else:
                    print("ALARM:", program_id, tool1, tool2)

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)

    # Save to the output file
    results_df.to_csv(output_file, index=False)

# Specify the input and output files
input_file = "TIMING/timing_all.csv"
output_file = "TIMING/timing_stat.csv"

# Run the function
process_csv(input_file, output_file)
