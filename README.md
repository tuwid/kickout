kickout
=======

Python Script to Kick Users out of a linux system


tuwid@valhalla:~/Dropbox/kickout$ sudo ./kick.py <br>
[sudo] password for tuwid: <br>

1  -  tuwid pts/4 2014-11-03 19:30 (:0) <br>
2  -  tuwid pts/2 2014-11-03 18:22 (:0) <br>
3  -  tuwid pts/5 2014-11-03 18:23 (:0) <br>
4  -  tuwid pts/6 2014-11-03 18:51 (:0) <br>
5  -  tuwid pts/7 2014-11-03 19:31 (192.168.1.200) <br>
6  -  tuwid pts/8 2014-11-03 19:31 (:0) <br> 
7  -  root pts/10 2014-11-03 19:31 (192.168.1.200) <br>
8  -  tuwid pts/11 2014-11-03 19:31 (:0) <br>

Please enter id of the user to kick : 7 <br>
tty pts/10 killed <br>
tty pts/10 killed <br>
tuwid@valhalla:~/Dropbox/kickout$ <br> 

Meanwhile on the terminal <br>

tuwid@valhalla:~$ ssh root@192.168.1.200 <br>
root@192.168.1.200's password:  <br>
Welcome to elementary OS Luna (GNU/Linux 3.2.0-69-generic x86_64) <br>

Last login: Sun Nov  2 18:13:57 2014 from localhost <br>
root@valhalla:~# Connection to 192.168.1.200 closed by remote host. <br>
Connection to 192.168.1.200 closed. <br>
tuwid@valhalla:~$ 

