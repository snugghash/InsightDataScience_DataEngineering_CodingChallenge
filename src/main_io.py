import sys
import string

def main():
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
            # words = list(map(string.strip("\""), words))  # Partial fn?
            words = [i.strip("\"") for i in words]
            if(words[0] == ""):
                # Header
                continue
            elif(words[2] == "CERTIFIED"):
                state_aggregate[words[12]] = state_aggregate[words[12]] + 1

                # TODO make it choose 24 from the spec and header like "SOC"
                occupation_aggregate[words[24]] = occupation_aggregate[words[24]] + 1
    occ_perc = get_stats(occupation_aggregate)
    with open(output_file_top10occupations, 'w') as f:
        f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
        for k,v in occupation_aggregate.items():
            # Gets the format of things needed as a list, converts all to string, joins with desired separator. TODO make sep, format and such parametric
            # TODO percentage floating point formatting when printing
            f.write((';').join(map(str,[k[0:], v, str(occ_perc[k]) + '%'])) + '\n')

    state_perc = get_stats(state_aggregate)




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
    
