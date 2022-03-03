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
