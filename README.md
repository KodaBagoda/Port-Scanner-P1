## Python Port Scanner

This Python script scans a user-specified target IP address for open ports.

**Features:**

* Scans a range of ports specified by the user.
* Identifies open ports and displays them on the console.
* Uses sockets for network communication.

**Dependencies:**

* No external libraries required. Uses the built-in `socket` module.

**Usage:**

1. Clone this repository.
2. Open a terminal and navigate to the project directory.
3. Edit the `target` variable in the script (`port_scanner.py`) to the desired IP address.
4. Run the script using `python port_scanner.py`.
5. The script will scan the default port range (1-1024) and report any open ports.

**Example:**

```
python port_scanner.py

Scanning target: 192.168.*.***

Port 22 is open (SSH)
Port 80 is open (HTTP)
```

**Customizing Port Range (Optional):**

* Edit the `start_port` and `end_port` variables in the script to define the desired port range. 

**Disclaimer:**

* Running port scanners on systems you don't own is illegal. Use this script only for authorized scans on your own network.
* Be aware of potential security risks associated with port scanning.

**Contributing:**

Feel free to fork this repository and make improvements! Here are some ideas:

* Implement multithreading for faster scanning.
* Add functionality to identify common services running on open ports.
* Allow users to specify the target IP address and port range from the command line.

**Note:** This is a basic example. It's recommended to be cautious and responsible when using port scanning tools.
