Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.

![alt text](https://py-static.checkio.org/media/task/media/835d2a2492b24aa682da086afed4f6a1/example.png)


<b>Input:</b> Two arguments. Both strings.

<b>Output:</b> Boolean.

<b>Example:</b>
```
isometric_strings('add', 'egg') == True
isometric_strings('foo', 'bar') == False
```

<b>Precondition:</b>
both strings are the same size