import os
import glob
import argparse
import sys

def read_config(file_path, verbose=False):
    """
    Reads a configuration file and includes the contents of any included files recursively.
    
    :param file_path: Path to the configuration file to read, or None to read from stdin.
    :param verbose: Flag to control verbose output.
    :return: The expanded content of the configuration as a list of strings.
    """
    expanded_content = []

    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        base_path = os.path.dirname(file_path)
    else:
        lines = sys.stdin.readlines()
        base_path = os.getcwd()

    for line in lines:
        if line.strip().startswith('[include '):
            included_pattern = line.strip()[9:-1].strip()
            expanded_content.append(f"#### In-place expansion pattern: {included_pattern}\n")
            included_files = glob.glob(os.path.join(base_path, included_pattern))
            for included_file in sorted(included_files):
                if verbose:
                    print(f"Expanding file: {included_file}", file=sys.stderr)
                expanded_content.append(f"#### In-place expansion begin reading from {included_file}\n")
                expanded_content.extend(read_config(included_file, verbose))
                expanded_content.append(f"#### In-place expansion end reading from {included_file}\n")
               
        else:
            expanded_content.append(line)

    return expanded_content

def main():
    """
    Parses command-line arguments and expands all included configuration files starting from the main configuration file or standard input.
    """
    parser = argparse.ArgumentParser(description="Expand configuration files by including referenced files.")
    parser.add_argument('input', nargs='?', help='Path to the main configuration file (optional, reads from stdin if not provided)')
    parser.add_argument('-o', '--output', help='Path to the output file where the expanded content will be written')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose messages to stderr')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    verbose = args.verbose

    expanded_content = read_config(input_file, verbose)
    
    if output_file:
        with open(output_file, 'w') as out_file:
            out_file.writelines(expanded_content)
    else:
        sys.stdout.writelines(expanded_content)

if __name__ == "__main__":
    main()
