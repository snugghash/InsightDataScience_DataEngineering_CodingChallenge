import sys

def main():
    input_file = sys.argv[1]
    output_file_top10occupations = sys.argv[2]
    output_file_top10states = sys.argv[3]

    with open(input_file) as f:
        for line in f:
            print(line)

if(__name__ == "__main__"):
    main()
    
