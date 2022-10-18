# Placeback-Solution

Placeback-Solution is a program that solves placeback for any integer.

Developed by Fenway Powers and Hanji Xu in 2021.

Placeback is a lot easier to explain by showing the process, so here is a video of the solution for x = 7:

<https://user-images.githubusercontent.com/31604245/196319717-ca665d69-82c6-457f-87ac-68b4d6072e5f.mp4>

So, the solution shown in this video is: [4, 1, 6, 2, 5, 3, 7], which results in [1, 2, 3, 4, 5, 6, 7].

Placeback-Solution can give you the correct list of numbers for any integer.

It can also output each solution and its "mapping" list to an Excel Spreadsheet file. This is mainly used for looking at patterns in the solutions.

## Prerequisites: 

* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* You will also need a program that can view .xlsx files, such as:
* [LibreOffice](https://www.libreoffice.org/)

## Example Use: 

To run, you can simply execute `python3 placeback.py`.

Custom arguments:
* you may specify the integer by simply including an integer in your parameters.
* Example: `python3 placeback.py 7`

* To create a spreadsheet with all solutions up to the integer input: `-o [file.xlsx]`
* Example: `python3 placeback.py 500 -o placeback500.xlsx`

You can also run the code directly in [replit.com](https://replit.com/@FenwayPowers/Placeback-Solution).
