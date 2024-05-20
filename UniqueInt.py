class UniqueInt:
    def __init__(self):
        self.seen_integers = [False] * 2047  # Initialize boolean array for integers (-1023 to 1023)

    def read_next_item_from_file(self, input_file_stream):
        for line in input_file_stream:
            try:
                integer = int(line.strip())  # Remove leading/trailing whitespaces
                if -1023 <= integer <= 1023:
                    yield integer
            except ValueError:
                # Skip lines with non-integer input
                pass

    def process_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as input_file:
            for integer in self.read_next_item_from_file(input_file):
                self.seen_integers[integer + 1023] = True

        unique_integers = [i - 1023 for i, seen in enumerate(self.seen_integers) if seen]

        with open(output_file_path, 'w') as output_file:
            for integer in unique_integers:
                output_file.write(f"{integer}\n")

if __name__ == "__main__":
    unique_int_processor = UniqueInt()
    input_file = "/home/tetabianca/UniqueInt/sample_input_for_students/sample_01.txt"
    output_file = "/home/tetabianca/UniqueInt/results_for_sample_inputs/sample_01.txt_result.txt"
    unique_int_processor.process_file(input_file, output_file)
