Given the grade percentage for the course, calculate and return the letter grade that would appear in the Ryerson’s grade transcript, as defined on the page Ryerson Grade Scales. The letter grade should be returned as a string that consists of the uppercase letter followed by the possible modifier "+" or "-" .

<b>Input:</b> Int. Grade percentage.

<b>Output:</b> Str. The letter grade.

<b>Example:</b>

The initial code contains grade table as raw string. Feel free to change it in any way.
```
ryerson_letter_grade(45) == "F"
ryerson_letter_grade(62) == "C-"
```
<b>Precondition:</b> argument can be from 0 to 150

<i>The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen</i>