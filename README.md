# Apache Log Parser

## Project Overview

A sophisticated Python-based log analysis tool designed to parse and extract meaningful insights from Apache Combined Log Format files. This project demonstrates proficiency in Python scripting, data parsing, and log analysis techniques.

## Features

- Robust log file parsing
- Comprehensive statistical analysis
- Error-tolerant design
- Flexible command-line interface

## Installation

### Prerequisites

- Python 3.x
- No external library dependencies

### Setup

```bash
# Clone the repository
git clone https://github.com/PavanAutomates/apache-log-parser.git
cd apache-log-parser
```

## Usage

### Basic Parsing

```bash
# Parse a log file and generate statistics
python log_parser.py -f /path/to/logfile.log
```

### Command-Line Arguments

- `-f` or `--file`: Path to the log file (Required)

## Project Structure

```
apache-log-parser/
├── examples/           # Sample log files
│   └── example1.log
│   └── example2.log
│   └── real_apache_logs.log
├── scripts/           # Log generation utilities
│   └── generate-logs.py
├── log_parser.py      # Main log parsing script
└── README.md          # Project documentation
```

## Sample Output

```
Total Requests: 10000
Total Data Transmitted: 2.56 GiB

Most requested resource: /favicon.ico
  Total requests for /favicon.ico: 807
  Percentage of requests for /favicon.ico: 8.0700000000%

Remote host with the most requests: 66.249.73.135
  Total requests from 66.249.73.135: 482
  Percentage of requests from 66.249.73.135: 4.8200000000%

HTTP Status Code Percentages:
  2xx: 91.7100000000%
  4xx: 2.1700000000%
  3xx: 6.0900000000%
  5xx: 0.0300000000%
```

## Error Handling

- Skips malformed log entries
- Provides clear error messages
- Continues processing valid log entries


## About

Developed as a technical assessment project demonstrating Python log parsing capabilities.