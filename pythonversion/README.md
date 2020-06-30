# Expert system
Little expert system developed in Python

## Requirements 🖥️
1. Install Python3 :
    - Linux : run `sudo apt-get install python3`
    - Windows : [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe)

2. Clone the repository

**OR**

## Run It With Docker

Will run using the `facts.txt` and `rules.txt` at the root of the repo.

- `docker pull docker.pkg.github.com/vareversat/expert-system/pythonexpert:latest`
- `docker run -it docker.pkg.github.com/vareversat/expert-system/pythonexpert:latest`

## Use it ⚙️
Two files are important here :
- `facts.txt` : References all the facts of our system. You can add new facts in the file **(separated with commas and without space)**

### Syntax :
>**✔️ Good :**
>> D,C,D

>**❌ Bad :**
>> D , C ,DD,P

___

- `rules.txt` : Reference all the rules of our system. (Example : `A^B=>X` stands for *if A and B then X*). You can add new rules **with a line break at the end of the line**

### Syntax :

>**✔️ Good :**
>> A^B=>X <br>
>> D^E=>Z

>**❌ Bad :**
>> A^B=>X  D^E=>Z

___


## Understand it 🧠

To use it, you need to run `python3 main.py`

Example of output :

```
######## Results ######## 

### Rules ###
|A ^ B => X
|-D- ^ -E- => -Z-
|A ^ O ^ J => Q

### Facts ###
[D, E, Z]
```

Letters surrounded by an hyphen (`-D-`) are marked. It's mean that the fact is already `true` or became `true` (example : `-D- ^ -E- => -Z-`. Here `Z` became `true` because `D` and `E` were `true` )


