
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

## EXPLOIT

1. Copy paste the content of **[`auto_exploit`](auto_exploit)** in the terminal to get the root shell.

1. Once you get the root shell, you can cat the flag

    ```bash
    cat flag
    ```
