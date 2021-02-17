This function creates an List of lists. that represents a two-dimensional grid with the given number of rows and cols. This grid should contain the integers from <b>start</b> to <b>start + rows * cols - 1</b> in ascending order, but the elements of every odd-numbered row have to be listed in descending order, so that when read in ascending order, the numbers zigzag through the two-dimensional grid.

<b>Input:</b> Two ints rows and cols. One optional argument start.

<b>Output:</b> List of lists.

<b>Example:</b>
```
create_zigzag(3, 5) == [
        [1,2,3,4,5],
        [10,9,8,7,6],
        [11,12,13,14,15]
    ]
create_zigzag(5, 1) == [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
create_zigzag(3, 3, 5) == [
        [5, 6, 7],
        [10, 9, 8],
        [11, 12, 13]
    ]
```

<i>The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen</i>