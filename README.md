# InsightDataScience_DataEngineering_CodingChallenge

## Problem

Take data on immigration trends in `.csv` format from `input` directory and produce top 10 states and occupations with certified visa applications in separate files. Primary goal is scalability and reusability.

## Running

1. Place data files in .csv format in input directory.
1. Execute `run.sh`.
1. Peruse output files in output directory.

Previous output files will be overwritten to preserve idempotence.

There are no user tunable parameters for now, any changes must be done using code.

## Approach

From the given 10-line example, we see there's a header

* Assume order of elements is same in all inputs
* Assume separator is always `;`

[Efficient line by line reading of large files](https://stackoverflow.com/questions/8009882/how-to-a-read-large-file-line-by-line-in-python)
Since we require tracking the occupations and states, we can store their details in memory - they're categorical, finite (don't scale with file size) and small in number.
Since we need their percentages of the total, we can add to the solution line by line.
The procedural functions to be performed to get the required result:

1. Open and read file efficiently.
1. Check for certified applications
1. Store counts for each state, occupation.
1. Once whole file is read, sort categorical stats and get top 10.
1. Print to output files.

Each of these should be separately testable.