from collections import Counter

def count_ips(log_file):
    ip_counter = Counter() 

    try:
        # Open the log file
        with open(log_file, 'r') as f:
            for line in f:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Try to extract the IP address from the log line
                try:
                    ip = line.split()[0]  # Assuming IP is the first part of the line
                    ip_counter[ip] += 1  # Count the IP occurrence
                except IndexError:
                    print(f"Malformed line (no IP found): {line.strip()}")  # Debugging print
                    
        # Get the top 3 most common IPs
        top_ips = ip_counter.most_common(3)
        return top_ips

    except FileNotFoundError:
        print(f"Error: The file {log_file} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    log_file = 'access_logs.txt'  # Path to your Apache log file

    # Call the function to count the IPs and print the top 3 IPs
    top_ips = count_ips(log_file)
    
    if top_ips:
        print("Top 3 IPs with most requests:")
        for ip, count in top_ips:
            print(f"{ip}: {count} requests")
    else:
        print("No IPs counted.")
