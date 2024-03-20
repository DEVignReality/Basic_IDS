Basic Intrusion Detection System (IDS)

This Basic Intrusion Detection System (IDS) is a Python-based tool designed for educational purposes to monitor network traffic for suspicious activities, specifically focusing on DNS queries. It logs all DNS requests passing through the network and alerts the administrator of each request.
Features

    Network Traffic Monitoring: Listens to network traffic and captures packets in real-time.
    DNS Request Detection: Specifically looks for DNS query requests and logs relevant information.
    Alerting: Alerts the system administrator for every DNS request detected.
    Logging: Records details of the network traffic and DNS requests into a text file for later analysis.

Requirements

    Python 3.x

    Scapy: A powerful Python-based tool used for network packet manipulation. You can install it using pip:

    bash

    pip install scapy

    Administrative or root privileges: Required for network traffic monitoring.

Setup and Running

    Clone this repository to your local machine or download the IDS.py script.

    Navigate to the project directory:

    bash

cd ~/path_to_your_directory/Cybersecurity_Projects/IDS

Run the script with root privileges:

bash

    sudo python3 IDS.py

    Observe the detected DNS requests in real-time and review the generated log file (ids_log.txt) for all captured events.

How It Works

The script uses Scapy to sniff network packets and filters for DNS requests. For each DNS request captured, the script logs the following information:

    Timestamp of the request
    Source IP address
    Destination IP address
    Requested domain name

This information is logged into ids_log.txt and an alert message is printed to the console.
Customization

You can customize the script to monitor different types of traffic or to implement more sophisticated alerting mechanisms based on your specific needs. However, ensure to comply with all applicable laws and regulations regarding network traffic monitoring.
Disclaimer

This Basic IDS is for educational and testing purposes only. Ensure you have proper authorization before monitoring network traffic in any environment. Unauthorized use of this tool could violate privacy rights and laws.
Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.
License

This project is open source and available under the MIT License.
