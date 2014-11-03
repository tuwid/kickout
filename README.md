kickout
=======

Python Script to Kick Users out of a linux system


tuwid@valhalla:~/Dropbox/kickout$ sudo ./kick.py 
[sudo] password for tuwid: 

1  -  tuwid pts/4 2014-11-03 19:30 (:0)
2  -  tuwid pts/2 2014-11-03 18:22 (:0)
3  -  tuwid pts/5 2014-11-03 18:23 (:0)
4  -  tuwid pts/6 2014-11-03 18:51 (:0)
5  -  tuwid pts/7 2014-11-03 19:31 (192.168.1.200)
6  -  tuwid pts/8 2014-11-03 19:31 (:0)
7  -  root pts/10 2014-11-03 19:31 (192.168.1.200)
8  -  tuwid pts/11 2014-11-03 19:31 (:0)

Please enter id of the user to kick : 7
tty pts/10 killed
tty pts/10 killed
tuwid@valhalla:~/Dropbox/kickout$ 

Meanwhile on the terminal

tuwid@valhalla:~$ ssh root@192.168.1.200
root@192.168.1.200's password: 
Welcome to elementary OS Luna (GNU/Linux 3.2.0-69-generic x86_64)

 * Website:  http://elementaryos.org
Last login: Sun Nov  2 18:13:57 2014 from localhost
root@valhalla:~# Connection to 192.168.1.200 closed by remote host.
Connection to 192.168.1.200 closed.
tuwid@valhalla:~$ 

