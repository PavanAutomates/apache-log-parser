#!/usr/bin/env python3

import re
import argparse
from collections import Counter

# Regex to parse the Combined Log Format
LOG_PATTERN = re.compile(
    r'(?P<host>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<resource>\S+) \S+" (?P<status>\d{3}) (?P<size>\d+|-)(?: "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)")?'
)

def human_readable_size(size_in_bytes):
    """Convert bytes to a human-readable format."""
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

def parse_log_line(line):
    """Parse a log line and return a dictionary of values."""
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    data = match.groupdict()
    data["size"] = int(data["size"]) if data["size"] != "-" else 0
    data["status"] = int(data["status"])
    return data

def process_log_file(file_path):
    """Process the log file and collect statistics."""
    total_requests = 0
    total_data = 0
    resource_counter = Counter()
    host_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            log_entry = parse_log_line(line)
            if not log_entry:
                continue

            # Update statistics
            total_requests += 1
            total_data += log_entry["size"]
            resource_counter[log_entry["resource"]] += 1
            host_counter[log_entry["host"]] += 1
            status_counter[log_entry["status"] // 100] += 1

    return {
        "total_requests": total_requests,
        "total_data": total_data,
        "resource_counter": resource_counter,
        "host_counter": host_counter,
        "status_counter": status_counter,
    }

def calculate_statistics(stats):
    """Calculate and print statistics section-wise."""
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Total Data Transmitted: {human_readable_size(stats['total_data'])}")

    # Most requested resource
    most_requested_resource, resource_count = stats["resource_counter"].most_common(1)[0]
    resource_percentage = (resource_count / stats["total_requests"]) * 100
    print(f"\nMost requested resource: {most_requested_resource}")
    print(f"  Total requests for {most_requested_resource}: {resource_count}")
    print(f"  Percentage of requests for {most_requested_resource}: {resource_percentage:.10f}%")

    # Remote host with most requests
    top_host, host_count = stats["host_counter"].most_common(1)[0]
    host_percentage = (host_count / stats["total_requests"]) * 100
    print(f"\nRemote host with the most requests: {top_host}")
    print(f"  Total requests from {top_host}: {host_count}")
    print(f"  Percentage of requests from {top_host}: {host_percentage:.10f}%")

    # Status code percentages
    print("\nHTTP Status Code Percentages:")
    for status_class, count in stats["status_counter"].items():
        percentage = (count / stats["total_requests"]) * 100
        print(f"  {status_class}xx: {percentage:.10f}%")

def main():
    """Main function to parse arguments and process the log file."""
    parser = argparse.ArgumentParser(description="Analyze web server log files.")
    parser.add_argument("-f", "--file", required=True, help="Path to the log file.")
    args = parser.parse_args()

    try:
        stats = process_log_file(args.file)
        calculate_statistics(stats)
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
