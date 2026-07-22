Analyze the Apache-style access log at /app/access.log and write the resulting report to /app/report.json.

The output must be a valid JSON object containing exactly these fields:

- total_requests: an integer representing the number of non-empty log entries.
- unique_ips: an integer representing the number of distinct client IP addresses.
- top_path: a string containing the request path that appears most frequently. Parse paths from GET, POST, PUT, DELETE, HEAD, and PATCH requests.

Success criteria:

1. /app/report.json exists, is valid JSON, and contains exactly the fields total_requests, unique_ips, and top_path.
2. total_requests equals the number of non-empty entries in /app/access.log.
3. unique_ips equals the number of distinct client IP addresses in /app/access.log.
4. top_path equals the most frequently requested path in /app/access.log.