
# CTF 8 - Knock Knock

## SETUP

1. Deploy your challenge instance
1. Open two terminals ***(Terminal 1 and Terminal 2)*** and connect to your instance with:

    ``` bash
    ssh {unix_username}@syssec-lab.s3.eurecom.fr -p {port_number}
    ```

    > example: ssh <root@syssec-lab.s3.eurecom.fr> -p 30200
1. Open another Terminal ***(Terminal 3)*** and run the python script **[`hash_bruteforce.py`](hash_bruteforce.py)**

    ``` bash
    python3 hash_bruteforce.py {unix_username}
    ```

    > example: python3 hash_bruteforce.py root  
      Enter the nonce:

    It will ask you to enter the nonce. We will get back to this in the next steps.

## ATTACK

1. In **Terminal 1**, connect to server with netcat on port 9999.

    ```bash
    nc localhost 9999
    ```

    > Welcome to challenge_03!  
      Here is your nonce: 12345  
      Please send me a string s of the format:  
      [your username]-[nonce]-[random_bytes]  
      If the first 3 bytes of sha256(s) are all 0, you can continue!

    *Every time you connect to the server, you will get a different nonce. You need to find a string **s** that when hashed with sha256, the first 3 bytes are all 0.*
1. Copy the nonce from the previous step and paste it in **Terminal 3**.

    > Enter the nonce: 12345  
      root-12345-3356731

    *The script will generate a string **s** with the format [your username]-[nonce]-[random_bytes]. It can take around ten seconds or more to find the correct string*

1. In **Terminal 1** paste the string **s** you got from Terminal 3.

    > *Welcome to challenge_03!*  
      *Here is your nonce: 56786*  
      *Please send me a string s of the format:*  
      *[your username]-[nonce]-[random_bytes]*  
      *If the first 3 bytes of sha256(s) are all 0, you can   continue!*  
      root-12345-3356731  
      Good job! Now please go on to access the secret vault  

    *You will need repeat those 3 steps several times before you get the flag.*
    After solving this first part, you will get the following message:
    > Good job! Now please go on to access the secret vault

1. Then, you will have around five seconds to connect to three different ports in the right order, with UDP protocol.

    4.1. Port scanning

    The ports you need to find are between 1 and 65535, and they are open only for the next five seconds after you send your string and get the message:
    > Good job! Now please go on to access the secret vault

    The objective is to check every port between 1 and 65535, and find the first port that is open.  
    Since we only have five seconds, we cannot check the 65535 ports in one time: we need to split the work.  
    > Example: 1-10000, 10001-20000, 20001-30000, 30001-40000, 40001-50000, 50001-60000, 60001-65535

    4.1.1. In **Terminal 2** run the following command with the different port ranges:

    ```bash
    nc -uv -w0 127.0.0.1 {port_range}
    ```

    > Example: nc -uv -w0 127.0.0.1 1-10000

    *Make sure that this command ends before "Too slow!" appears in **Terminal 1**. You can reduce the port ranges if needed.*

    If an open port is found, you will get the following message:
    > Connection to 127.0.0.1 22222 port [udp/*] succeeded!

    *If more than five ports are open, you should try again with the same port ranges. Because some random ports, that we don't need, can be open.*

    To be sure that you found the right port, you can solve the first part again and check if the port is still open.

    ```bash
    nc -uv -w 0 127.0.0.1 22222
    ```

    > Connection to 127.0.0.1 22222 port [udp/*] succeeded!

    We can confirm that the port 22222 is my *port1*.

    4.1.2. To find *port2* you can repeat the same steps as for *port1*, but before scanning the ports, you need to connect to *port1*.

    ```bash
    nc -uv -w 0 127.0.0.1 {port1}
    nc -uv -w0 127.0.0.1 {port_range}
    ```

    > Example:  
      nc -uv -w 0 127.0.0.1 22222  
      nc -uv -w 0 127.0.0.1 1-10000

    4.1.3. Same thing for *port3*, you need to connect to *port1* and *port2* before scanning the ports.

    ```bash
    nc -uv -w 0 127.0.0.1 {port1}
    nc -uv -w 0 127.0.0.1 {port2}
    nc -uv -w0 127.0.0.1 {port_range}
    ```

    > Example:  
      nc -uv -w 0 127.0.0.1 22222  
      nc -uv -w 0 127.0.0.1 11111  
      nc -uv -w 0 127.0.0.1 1-10000

    4.2. Once you found the three ports, solve the first part again in Terminal 1, and connect to the three ports in the right order in **Terminal 2**. If everything is correct, you will get the flag from the server.

    ```bash
    nc -uv localhost {port1}
    nc -uv localhost {port2}
    nc -uv localhost {port3}
    ```

    > Example:  
      nc -uv -w 0 127.0.0.1 22222  
      nc -uv -w 0 127.0.0.1 11111  
      nc -uv -w 0 127.0.0.1 33333

    **Terminal 2**  
    > Connection to 127.0.0.1 22222 port [udp/\*] succeeded!  
      Connection to 127.0.0.1 11111 port [udp/\*] succeeded!  
      Connection to 127.0.0.1 33333 port [udp/\*] succeeded!

    **Terminal 1**  
    > *Welcome to challenge_03!*  
      *Here is your nonce: 43244*  
      *Please send me a string s of the format:*  
      *[your username]-[nonce]-[random_bytes]*  
      *If the first 3 bytes of sha256(s) are all 0, you can continue!*  
      *root-12345-3356731*  
      *Good job! Now please go on to access the secret vault*  
      You did it! Congratz!  
      Here, have a secret: SysSec{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}
