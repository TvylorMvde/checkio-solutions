Hey, are you ready for a Scrabble game party?

You have a list of words and you have to find only one that is the most valuable among them.

<b>Rules:</b>

The worth of each word is equivalent to the sum of letters which it consists of.

The values of the letters are as follow:

e, a, i, o, n, r, t, l, s, u = 1</br>
d, g = 2</br>
b, c, m, p = 3</br>
f, h, v, w, y = 4</br>
k = 5</br>
j, x = 8</br>
q, z = 10

For example, the worth of the word 'dog' is 5, because 'd' = 2, 'o' = 1 and 'g' = 2.

![alt text](https://py-static.checkio.org/media/task/media/22eb44f2e71e4da08538c234964641c9/words.png)

<b>Input:</b> A list of words.

<b>Output:</b> The most valuable word.

<b>Example:</b>
```
worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
```
<b>How it is used:</b> For the lexicographic analysis of the texts.

<b>Precondition:</b>
2 <= words <= 10
Real words only
lowercase letters only