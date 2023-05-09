# Parsing Common Log Format to JSON Project

## Table of Contents

- [Introduction](#Introduction)
- [Tools Used](#Tools-Used)
- [Approach to Problem](#Approach-to-Problem)
- [Learning Outcomes](#Learning-Outcomes)
- [References](#References)

<h2 id="#Introduction">Introduction</h2>

The premise of this project is to parse Common Log Format logs into a readable format which will then output the desired fields by the user. The initial regular expression implentation seperates the information into 8 different catagories/fields, *IP_of_requesting_host*, *Remote_user*, *Timestamp*, *Request_from_client*, *HTTP_response_code*, *Size_of_bytes_returned*, *Http_referer*, and *Http_user_agent*. To further output the desired data, another script was ran which will take the .json file that was created in the previous step and output the information as per the users choice. The final report will be linked in the [References section](#References).

<h2 id="#Tools-Used">Tools Used</h2>

The tools used here are the following:

1. [Python](https://www.python.org/downloads/)
2. [log2json](https://github.com/fauzanelka/log2json)

<h2 id="#Approach-to-Problem">Approach to Problem</h2>

1. Used [log2json](https://github.com/fauzanelka/log2json) to parse the initial Common Log Format.
2. Used Python to create another script that will take the .json file that was created in the previous step and output the information as per the users choice (8 different catagories/fields, *IP_of_requesting_host*, *Remote_user*, *Timestamp*, *Request_from_client*, *HTTP_response_code*, *Size_of_bytes_returned*, *Http_referer*, and *Http_user_agent*).

<h2 id="#Learning-Outcomes">Learning Outcomes</h2>

1. Learned how to pull Github repositories.
2. Understood the concept of Common Log Format and how it relates to cybersecurity.
3. Learned how to read Common Log Format files.

## References

1. [Written report linked here](https://github.com/JacYuan1/Common-Log-Format-to-JSON-Project/blob/main/Logs%20Example.pdf)
2. [Code linked here](https://github.com/JacYuan1/Common-Log-Format-to-JSON-Project/blob/main/script.py)
