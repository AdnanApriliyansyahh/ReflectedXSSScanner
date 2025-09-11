# Reflected XSS Scanner

Python script to perform automated XSS testing by injecting payloads from a wordlist into the target URL parameter.

### Features

• Supports custom target URL with injectable parameter.

• Reads payloads from a wordlist file.

• Automatically reports reflected payloads that may indicate XSS.

### Usage

```
python3 main.py -u "http://target.com/page.php?param=" -w payload.txt
```
-u → target URL containing the injectable parameter.

-w → path to the payload wordlist.


### Example

```
python3 main.py -u "http://www.target.com/graph.php?cmd=" -w /payload/xss.txt
```

```
python3 main.py -u "http://target.com/graph.php" -w /payload/xss.txt -p cmd
```








