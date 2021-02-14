Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

<b>Input:</b> A password as a string.

<b>Output:</b> Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

<b>Example:</b>
```
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True
```
<b>How it is used:</b> If you are worried about the security of your app or service, you can check your users' passwords for complexity. You can use these skills to require that your users passwords meet more conditions (punctuations or unicode).

<b>Precondition:</b>
re.match("[a-zA-Z0-9]+", password)</br>
0 < len(password) ≤ 64