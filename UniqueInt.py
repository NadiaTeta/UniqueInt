#!/usr/bin/python3
import os
class UniqueInt:
  def __init__(self):
    self.seen = [False] * 2047
  def read_integers_from_file(file_path):
    """
    Reads integers from a file and returns a list of unique integers.
    """
    unique_integers = set()
    try:
      with open(file_path, 'r') as file:
        for line in file:
          try:
            integer = int(line.strip())
            unique_integers.add(integer)
          except ValueError:
            # Skip lines with non-integer content
            pass
    except FileNotFoundError:
      print(f"File '{file_path}' not found.")
      return sorted(unique_integers)

def write_unique_integers_to_file(unique_integers, output_file_path):
  """
  Writes unique integers to an output file.
  """
try:
  with open(output_file_path, 'w') as output_file:
    for integer in unique_integers:
        output_file.write(f"{integer}\n")
   print(f"Unique integers written to '{output_file_path}'.")
except IOError:
    Print(f"Error eriting to '{output_file_path}'.")

if __name__ == "__main__":
  input_file_path = "/UniqueInt/sample_input_for_students/sample_02.txt"
  output_file_path = "/UniqueInt/results_for_sample_inputs/sample_02.txt_result.txt

unique = list(set(sorted_numbers))

with open("results.txt", "a") as n:
  for i in unique:
      n.write(str(i) + "\n")
=======
unique_integers = read_integers_from_file(input_file_path)
write_unique_integers_to_file(unique_integers, output_file_path)
>>>>>>> origin/main
