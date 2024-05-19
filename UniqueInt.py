#!/usr/bin/python3
with open("sample_input_for_students/sample_01", "r") as x:
  lines = x.readlines()

numbers = [ int(line.strip()) for line in lines ]

sorted_numbers = sorted(numbers)

unique = list(set(sorted_numbers))

with open("results_for_sample_inputs/sample_01.txt_result", "a") as n:
  for i in unique:
      n.write(str(i) + "\n")
