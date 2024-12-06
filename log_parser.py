import argparse
import re
from collections import defaultdict
import os

class LogParser:
    def __init__(self, log_file_path):
        """
        Initialize the log parser with the given log file path
        
        :param log_file_path: Path to the Apache log file
        """
        self.log_file_path = log_file_path
        self.total_requests = 0
        self.total_data_transmitted = 0
        self.resource_requests = defaultdict(int)
        self.host_requests = defaultdict(int)
        self.status_code_counts = defaultdict(int)

    def parse_log(self):
        """
        Parse the log file and collect statistics
        """
        # Apache Combined Log Format regex pattern
        log_pattern = re.compile(
            r'(\S+) \S+ \S+ \[([^\]]+)\] "([^"]*)" (\d+) (\d+) "([^"]*)" "([^"]*)"'
        )

        try:
            with open(self.log_file_path, 'r') as log_file:
                for line in log_file:
                    match = log_pattern.match(line.strip())
                    
                    if not match:
                        # Skip lines that don't match the expected format
                        continue

                    # Extract log components
                    remote_host, timestamp, request, status_code, bytes_sent, referrer, user_agent = match.groups()

                    # Track total requests
                    self.total_requests += 1

                    # Track data transmitted
                    try:
                        self.total_data_transmitted += int(bytes_sent)
                    except ValueError:
                        pass

                    # Track resource requests
                    try:
                        resource = request.split()[1]
                        self.resource_requests[resource] += 1
                    except (IndexError, ValueError):
                        pass

                    # Track host requests
                    self.host_requests[remote_host] += 1

                    # Track status code percentages
                    self.status_code_counts[status_code[0] + 'xx'] += 1

        except FileNotFoundError:
            print(f"Error: Log file not found at {self.log_file_path}")
            return False
        
        return True

    def print_statistics(self):
        """
        Print collected log file statistics
        """
        if self.total_requests == 0:
            print("No valid log entries found.")
            return

        # Most requested resource
        most_requested_resource = max(self.resource_requests, key=self.resource_requests.get)
        resource_request_count = self.resource_requests[most_requested_resource]
        resource_request_percentage = (resource_request_count / self.total_requests) * 100

        # Remote host with most requests
        most_requested_host = max(self.host_requests, key=self.host_requests.get)
        host_request_count = self.host_requests[most_requested_host]
        host_request_percentage = (host_request_count / self.total_requests) * 100

        # Print statistics
        print("Log File Statistics:")
        print(f"Total number of requests: {self.total_requests}")
        print(f"Total data transmitted: {self.total_data_transmitted} bytes")
        
        print("\nMost Requested Resource:")
        print(f"Resource: {most_requested_resource}")
        print(f"Total requests: {resource_request_count}")
        print(f"Percentage of requests: {resource_request_percentage:.2f}%")
        
        print("\nRemote Host with Most Requests:")
        print(f"Host: {most_requested_host}")
        print(f"Total requests: {host_request_count}")
        print(f"Percentage of requests: {host_request_percentage:.2f}%")
        
        print("\nHTTP Status Code Percentages:")
        for code_class, count in sorted(self.status_code_counts.items()):
            percentage = (count / self.total_requests) * 100
            print(f"{code_class} status codes: {percentage:.2f}%")

def main():
    parser = argparse.ArgumentParser(description='Apache Log File Statistics Parser')
    parser.add_argument('-f', '--file', required=True, help='Path to the log file')
    args = parser.parse_args()

    log_parser = LogParser(args.file)
    if log_parser.parse_log():
        log_parser.print_statistics()

if __name__ == "__main__":
    main()
