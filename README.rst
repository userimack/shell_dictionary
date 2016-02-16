**shell_dictionary**

It is a dictionary formed using the api of `Glosbe <https://glosbe.com/a-api>`_
. We can access this dictionary to find the meaning of any word from the terminal.


To use it first of all clone the repo  and cd into it and then type  "chmod 755 dict" to change the file permission. Then type dict <word whose meaning you want>. That's it.

To access the file from anywhere in terminal just move the cloned directory to home directory and then edit the .profile file and add the line  PATH="~/shell_dictionary:$PATH"   at the end and then log out and log in again. 

That's it.