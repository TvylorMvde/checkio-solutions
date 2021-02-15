An IP network is a set of routers that communicate routing information using a protocol. A router is uniquely identified by an IP address.</br>
In IPv4, an IP address consists of 32 bits, canonically represented as 4 decimal numbers of 8 bits each. The decimal numbers range from 0 (00000000) to 255 (11111111).</br>
Each router has a "routing table" that contains a list of IP addresses, for the router to know where to send IP packets.</br>
<b>Route summarization in IP networks</b></br>
As the network grows large (hundreds of routers), the number of IP addresses in the routing table increases rapidly. Maintaining a high number of IP addresses in the routing table would result in a loss of performances (memory, bandwidth and CPU resources limitation).</br>

Route summarization, also called route aggregation, consists in reducing the number of routes by aggregating them into a "summary route".

Let's consider the following example:

![alt text](https://py-static.checkio.org/media/task/media/49d80613705b46d8a5ed24088088d65a/summarize.PNG)

We have 4 routers connected to <b>A</b>. <b>A</b> is aware about all 4 IP addresses, because it has a direct interface to each of them. However, <b>A</b> will not send them all to <b>B</b>.
Instead, it will aggregate the addresses into a summary route, and send this new route to <b>B</b>.
This implies that:

- Less bandwidth is used on the link between <b>A</b> and <b>B</b>.
- <b>B</b> saves memory: it has only one route to store in its routing table
- <b>B</b> saves CPU resources: there are less entries to consider when handling incoming IP packets

<b>Computing a summary route:</b>

<b>A</b> has all 4 addresses stored in its routing table.

<br>
    Address 1	    172.16.12.0</br>
    Address 2	    172.16.13.0</br>
    Address 3	    172.16.14.0</br>
    Address 4	    172.16.15.0</br>
</b>

A will convert these IP addresses to binary format, align them and find the boundary line between the common prefix on the left (highlighted in red), and the remaining bits on the right.

<b>Address 1</b>	    10101100	00010000	00001100	00000000</br>
<b>Address 2</b>	    10101100	00010000	00001101	00000000</br>
<b>Address 3</b>	    10101100	00010000	00001110	00000000</br>
<b>Address 4</b>	    10101100	00010000	00001111	00000000</br>

<b>A</b> creates a new IP address made of the common bits, and all other bits set to "0".
This new IP address is converted back to decimal numbers.
Finally, <b>A</b> computes the number of common bits, also called "subnet".

The summary route is this new IP address, followed by a slash and the subnet: 172.16.12.0/22

<b>Input:</b> A list of strings containing the IP addresses

<b>Output:</b> A string containing the summary route, represented as an IP address, followed by a slash and the subnet.

<b>Example:</b>
```
checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"
```
<b>Preconditions:</b></br>
all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",d) for d in data))</br>
all(-1 < int(n) < 256 for n in d.split(".") for d in data)</br>
len(data) == len(set(data)) and len(data) > 1</br>