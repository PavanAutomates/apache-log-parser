# Apache Log Parser

## Overview
This tool parses Apache Combined Log Format files and generates comprehensive statistics about web server logs.

## Requirements
- Python 3.x

## Installation
1. Clone the repository
2. (Optional) Create a virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


## Project Structure

apache-log-parser/
│
├── example/           # Sample log files
│   └── logfile.log
│
├── scripts/           # Log generation utilities
│   └── generate-logs.py
│
├── log_parser.py      # Main log parsing script
└── README.md          # Project documentation


## Usage
Basic Usage
   To parse a log file and generate statistics:
   bash
   python log_parser.py -f /path/to/logfile.log

Command-Line Arguments
   -f or --file: Path to the log file (Required)
   Example:
   bash
   python log_parser.py -f example/logfile.log

## Sample Log Generation
Generate Sample Logs

   Basic Log Generation
   bash
   python scripts/generate-logs.py -f example/sample.log

   Verbose Output
   bash
   python scripts/generate-logs.py -f example/sample.log -v

   Aggressive Log Generation (Faster)
   bash
   python scripts/generate-logs.py -f example/sample.log --aggressive

Log Generation Options
   -f FILE: Specify output log file location
   -v: Enable verbose output
   --aggressive: Speed up log generation