from openpyxl import Workbook
import sys
'''
File: placeback.py
Creator: Fenway Powers and Hanji Xu
Created: 2021
Updated: Mon Oct 17 21:23:57 2021
'''

workbook = Workbook()
sheet = workbook.active


def placeback(sequence):
  new = []
  while True:
    if len(sequence) == 1:
      new.append(sequence[0])
      break
    num = sequence[0]
    sequence.remove(num)
    sequence.append(num)
    new.append(sequence[0])
    sequence.remove(sequence[0])
  return new


def solution(sequence):
  values = {}
  for i in range(len(sequence)):
    values[sequence[i]] = i + 1

  values = dict(sorted(values.items(), key=lambda x: x))
  solution = []
  for i in values:
    solution.append(values[i])

  return solution


alphabet = {
  1: "A",
  2: "B",
  3: "C",
  4: "D",
  5: "E",
  6: "F",
  7: "G",
  8: "H",
  9: "I",
  10: "J",
  11: "K",
  12: "L",
  13: "M",
  14: "N",
  15: "O",
  16: "P",
  17: "Q",
  18: "R",
  19: "S",
  20: "T",
  21: "U",
  22: "V",
  23: "W",
  24: "X",
  25: "Y",
  26: "Z"
}

number = 7
solution_mode = True
excel_mode = False
outputfile = "placeback.xlsx"

if len(sys.argv) == 1:
  print('''No arguments given, running Solution mode with default value 7...
  To get help info, run "python3 placeback.py -help".
  ''')
elif len(sys.argv) > 1:
  for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-help" or sys.argv[i] == "-h":
      print(
        '''Welcome to Placeback-Solution, a program that solves placeback for any integer.
      Developed by Fenway Powers and Hanji Xu.
      
      To run, you can simply execute "python3 placeback.py".

      Custom arguments:
      you may specify the integer by simply including an integer in your parameters.
        Exmaple: "python3 placeback.py 7"

      To create a spreadsheet with all solutions up to the integer input:
      "-o [file.xlsx]"
        Example: "python3 placeback.py 500 -o placeback500.xlsx"
      ''')
      sys.exit(0)
    elif sys.argv[i].isdecimal():
      number = int(sys.argv[i])
    elif sys.argv[i] == "-o":
      excel_mode = True
      solution_mode = False
      if sys.argv[i + 1].endswith(".xlsx") and len(
          sys.argv[i + 1]) > 5 and "?" not in sys.argv[i + 1]:
        outputfile = sys.argv[i + 1]
      else:
        print("Error: invalid filename or extension.\nExiting...")
        sys.exit(0)

if solution_mode:
  sequence = [x for x in range(1, number + 1)]
  sequence = placeback(sequence)
  print("placeback:", sequence)
  print("solution for " + str(number) + " cards: " + str(solution(sequence)))

if excel_mode:
  for i in range(1, number + 1):
    if i % 100 == 0 or i == number:
      print("currently at solution for: ", i)
    length = i
    sequence = [x for x in range(1, length + 1)]
    sequence = placeback(sequence)
    solutionn = solution(sequence)
    sheet["A" + str(i)] = str(sequence)
    sheet["B" + str(i)] = str(solutionn)

    counter2 = 1
    column = 3
    for i in range(1, len(sequence)):
      if sequence[i] - sequence[i - 1] != (2**counter2):
        counter2 += 1
        sheet[alphabet[column] + str(i)] = sequence[i]
        column += 1

  workbook.save(filename=outputfile)
