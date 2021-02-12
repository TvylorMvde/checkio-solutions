Your task at hand is to find all the quotes in a given text. And, as per usual, do everything as quickly as possible. 😉</br>
You are given a string that consists of characters and a paired number of quotation marks. You need to return an Iterable consisting of the texts inside the quotation marks. But choose only quotes with double quotation marks ("). Single quotation marks (') aren’t appropriate.

<b>Input:</b> A string.

<b>Output:</b> An iterable.

<b>Example:</b>
```
find_quotes('"Greetings"') == ['Greetings']
find_quotes('Hi') == []
```