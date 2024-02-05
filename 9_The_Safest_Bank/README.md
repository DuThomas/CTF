# CTF 9 - The Safest Bank

## Table: cardinfo

| contract_nbr | token | FLAG3 | creditcard_nbr | expiry | type  | name | debt  |
|--------------|-------|-------|----------------|--------|-------|------|-------|
| ...          | ...   | ...   | ...            | ...    | ...   | ...  | ...   |
| ...          | ...   | ...   | ...            | ...    | ...   | ...  | ...   |
| ...          | ...   | ...   | ...            | ...    | ...   | ...  | ...   |
| ...          | ...   | ...   | ...            | ...    | FLAG2 | ...  | ...   |
| ...          | ...   | ...   | ...            | ...    | ...   | ...  | FLAG1 |
| ...          | ...   | FLAG4 | ...            | ...    | ...   |      | ...   |

## SETUP

1. Deploy your challenge instance
1. Open a terminal and connect to your instance with:

    ``` bash
    ssh {unix_username}@syssec-lab.s3.eurecom.fr -p {port_number}
    ```

## EXPLOIT

1. Copy paste the content of **[`auto_exploit`](auto_exploit)** in the terminal to get the full flag.
