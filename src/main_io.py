import sys
from collections import defaultdict

def main():
    """
    TODO think about better data structure, list of tuples might be better, perhaps a class for a self-sorting tuple manager, essentially a DB
    """
    input_file = sys.argv[1]
    output_file_top10occupations = sys.argv[2]
    output_file_top10states = sys.argv[3]

    occupation_aggregate = defaultdict(int)
    state_aggregate = defaultdict(int)
    with open(input_file) as f:
        for line in f:
            # RF out if we need other conditionals and such
            words = line.split(";")
            # Strip start/end \" tokens, they aren't in output example
            words = [i.strip("\"") for i in words]
            if(words[0] == ""):
                # Header
                continue
            elif(words[2] == "CERTIFIED"):
                state_aggregate[words[50]] = state_aggregate[words[50]] + 1
                # TODO make it choose 24 from the spec and header like "SOC"
                occupation_aggregate[words[24]] = occupation_aggregate[words[24]] + 1
    occ_perc = get_stats(occupation_aggregate)
    sort_and_print(occupation_aggregate, occ_perc, "TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n", output_file_top10occupations)
    state_perc = get_stats(state_aggregate)
    sort_and_print(state_aggregate, state_perc, "TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n", output_file_top10states)



def sort_and_print(aggregate, stats, header_string, output_file):
    """
    Returns nothing, side effect: creates and populates `output_file`
    TODO split into sort and print fn, clear parameter distinction, if this one goes over the number of lines per fn
    Parameters
    ----
    aggregate: Dict of values\n
    stats: Dict of totals and percentages\n
    """
    list_of_fields = []
    for k,v in aggregate.items():
        list_of_fields.append([k, v, str(stats[k]) + "%"])
    sorted_list_of_fields = sorted(list_of_fields, key = sort_by)
    # Gets the format of things needed as a list, converts all to string, joins with desired separator. TODO make sep, format and such parametric
    # TODO percentage floating point formatting when printing
    printable_list_of_fields = "\n".join([";".join(map(str,i)) for i in sorted_list_of_fields])
    with open(output_file, 'w') as f:
        f.write(header_string)
        f.write(printable_list_of_fields)



def sort_by(tuple_like):
    """
    https://stackoverflow.com/questions/24579202/

    ? scaling issues
    """
    return (-tuple_like[1], tuple_like[0])



def read_chunk():
    pass



def process_data(line):
    pass



def gather_insights():
    pass



def get_stats(the_dict):
    """
    Given a dictionary, returns a new dict with the percentages for each key
    """
    total_count = 0
    for k,v in the_dict.items():
        total_count = total_count + v
    percentage_dict = defaultdict(int)
    for k,v in the_dict.items():
        percentage_dict[k] = (100 * v) / total_count
    return percentage_dict



if(__name__ == "__main__"):
    main()
