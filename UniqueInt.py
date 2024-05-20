#!/usr/bin/python3
with open(input_file_path, "r") as x:
  lines = x.readlines()

numbers = [ int(line.strip()) for line in lines ]

sorted_numbers = sorted(numbers)

unique = list(set(sorted_numbers))

with open("results.txt", "a") as n:
  for i in unique:
      n.write(str(i) + "\n")
