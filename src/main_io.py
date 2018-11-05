import sys

def main():
    input_file = sys.argv[1]
    output_file_top10occupations = sys.argv[2]
    output_file_top10states = sys.argv[3]

    # TODO use default dict defaultdict(int)
    occupation_aggregate = {}
    state_aggregate = {}
    with open(input_file) as f:
        for line in f:
            # RF out if we need other conditionals and such
            words = line.split(";")
            if(words[0] == ""):
                # Header
                continue
            elif(words[2] == "CERTIFIED"):
                state_aggregate[words[12]] = state_aggregate.get(words[12], 0) + 1
                occupation_aggregate[words[22]] = occupation_aggregate.get(words[22], 0) + 1
    total_count = 0
    for k,v in state_aggregate.items():
        total_count = total_count + v
    with open(output_file_top10occupations) as f:
        pass




def read_chunk():
    pass



def process_data(line):
    pass



def gather_insights():
    pass



if(__name__ == "__main__"):
    main()
    
