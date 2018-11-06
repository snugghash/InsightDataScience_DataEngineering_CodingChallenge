import sys
from collections import defaultdict

def main():
    """
    TODO think about better data structure, list of tuples might be better, perhaps a class for a self-sorting tuple manager, essentially a DB
    """
    input_file = sys.argv[1]
    output_file_top10occupations = sys.argv[2]
    output_file_top10states = sys.argv[3]

    occupation_aggregate, state_aggregate = tuple(get_relevant_data_from_file(input_file))

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
        list_of_fields.append([k, v, f"{stats[k]:.1f}%"])
    sorted_list_of_fields = sorted(list_of_fields, key = sort_by)
    top10_sorted_list_of_fields = sorted_list_of_fields[:10]
    # Gets the format of things needed as a list, converts all to string, joins with desired separator. TODO make sep, format and such parametric
    # TODO percentage floating point formatting when printing
    printable_list_of_fields = "\n".join([";".join(map(str,i)) for i in top10_sorted_list_of_fields])
    with open(output_file, 'w') as f:
        f.write(header_string)
        f.write(printable_list_of_fields)



def sort_by(tuple_like):
    """
    https://stackoverflow.com/questions/24579202/

    ? scaling issues
    """
    return (-tuple_like[1], tuple_like[0])



def get_relevant_data_from_file(filename, binary_selector_field = 2, binary_selector_field_value = "CERTIFIED", list_of_fields = ["SOC_NAME", "WORKSITE_STATE"], separator = ";"):
    """
    ? perhaps remove default arg
    Parameters
    ----
    filename: file to read from
    binary_selector_field, binary_selector_field_value: Strings, field that has to be `binary_selector_field_value` to get data from it, in our case field 2="CERTIFIED"
    list_of_fields: String names of fields to get data. Positions change across inputs, must use strings.
    ? Split up for better tests again
    """
    field_numbers = [0] * len(list_of_fields)
    aggregates = [defaultdict(int), defaultdict(int)]
    with open(filename) as f:
        for line in f:
            # RF out if we need other conditionals and such
            words = line.split(separator)
            # Strip start/end \" tokens (it strips ALL \" though), they aren't in output example
            quoteless_words = [i.strip("\"") for i in words]
            if(quoteless_words[0] == ""):
                # Header line, find the positions of the needed data
                for i,field in enumerate(list_of_fields):
                    for j,e in enumerate(quoteless_words):
                        if(e == field):
                            field_numbers[i] = j
            elif(quoteless_words[binary_selector_field] == binary_selector_field_value):
                # If CERTIFIED, get data
                for i,field_number in enumerate(field_numbers):
                    aggregates[i][quoteless_words[field_number]] = aggregates[i][quoteless_words[field_number]] + 1
    return aggregates



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
