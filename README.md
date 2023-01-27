# heaps-random
Scripts to make heaps of random files.

## Step 1

Make a directory

```bash
mkdir random_files

cd random_files
```

## Step 2

Make files

```bash
dd if=/dev/urandom bs=1024 count=102400 | split -a 4 -b 1k - file.
```

This line of bash script uses the `dd` command to read 102400 blocks of 1024 bytes each from the /dev/urandom input file (`if=/dev/random`), which is a special file that generates random data. It then pipes the output of this command to the `split` command. 

The split command then takes that input and splits it into 1 kilobyte (`1k`) files, using a 4 character suffix (`-a 4`) and naming the output files "`file`" with a suffix (e.g. `fileaa`, `fileab`, `fileac`, etc).
