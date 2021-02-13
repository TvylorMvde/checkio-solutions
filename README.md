You are given some string where you need to find its middle characters. The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.

![alt text](https://py-static.checkio.org/media/task/media/201695a7b7b341a6bac4d97269d1a341/middle.png)

<b>Input:</b> A string.

<b>Output:</b> The middle characters.

<b>Example:</b>
```
middle('example') == 'm'
middle('test') == 'es'    
middle('very-very long sentence') == 'o'
middle('I') == 'I'
middle('no') == 'no'
```

<b>How it is used: </b>For work with texts.

<b>Precondition:</b>
1 <= the length of the text <= 100