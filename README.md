# Mac Address Changer

<h2>Description</h2>
This project is a MAC Address Changer tool written in Python. It enables users to modify the MAC address of a specified network interface on their system. Changing the MAC address can be beneficial for various reasons, including enhancing privacy, testing network configurations, and bypassing certain network restrictions, or masquerading as an authentic user. This tool is easy to use, requiring only the network interface and the new MAC address as command-line inputs.

The project utilizes Python's subprocess library to execute system commands, making it compatible with Unix-based systems where ifconfig is available. Users can run this script with a few simple commands to change their MAC address temporarily.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>Subprocess</b> 
- <b>Optparse</b>

<h2>Environments Used </h2>

- <b>Kali Linux</b> 
- <b>PyCharm</b>

<h2>Skills Learned</h2>

- <b>Command-Line Argument Parsing</b>: Using the optparse library to capture user inputs for flexible script control.
- <b>System Command Execution</b>: Leveraging Python's subprocess module to run Unix commands (ifconfig) to manage network interfaces.
- <b>MAC Address Manipulation</b>: Understanding the structure of MAC addresses and how they can be temporarily altered on network interfaces.
- <b>Error Handling</b>: Implementing input validation to ensure required arguments are provided, guiding users to use the script correctly.
- <b>Networking Fundamentals</b>: Gaining experience in basic network configuration and understanding how MAC addresses influence network identity.

<h2>Program Walthrough</h2>
<ol>
  <li><b>Importing Required Libraries</b>
    <ul>
      <li><b>subprocess</b>: Executes system commands for changing MAC addresses on the specified interface.</li>
      <li><b>optparse</b>: Parses command-line options, allowing users to specify the interface and new MAC address.</li>
    </ul>
  </li>
  <li><b>Function</b> - <code>get_args()</code>
    <ul>
      <li><b>Defines command-line arguments:</b>
        <ul>
          <li><code>-i</code> or <code>--interface</code>: The network interface to be modified (e.g., <code>eth0</code>, <code>wlan0</code>).</li>
          <li><code>-m</code> or <code>--mac</code>: The new MAC address to assign.</li>
        </ul>
      </li>
      <li>Checks for required arguments, displaying an error if any are missing to prompt correct usage.</li>
    </ul>
  </li>
  <li><b>Function</b> - <code>change_mac(interface, new_mac)</code>
    <ul>
      <li>Accepts <code>interface</code> and <code>new_mac</code> as inputs from the command-line arguments.</li>
      <li>Prints a message indicating that the MAC address change is in progress.</li>
      <li><b>Executes three commands:</b>
        <ul>
          <li>Brings down the specified network interface (<code>ifconfig interface down</code>).</li>
          <li>Assigns the new MAC address (<code>ifconfig interface hw ether new_mac</code>).</li>
          <li>Brings the interface back up (<code>ifconfig interface up</code>).</li>
        </ul>
      </li>
      <li>This sequence temporarily changes the MAC address for the selected network interface.</li>
    </ul>
  </li>
  <li><b>Main Program Execution</b>
    <ul>
      <li><code>get_args()</code> is called to parse and capture user inputs for the network interface and MAC address.</li>
      <li>These inputs are passed to <code>change_mac()</code>, which initiates the MAC address change process.</li>
    </ul>
  </li>
</ol>

<h3>Example Usage</h3>

```commandline 
python Mac_Changer.py -i eth0 -m 00:11:22:33:44:55
````

<ul>
  <li>This command changes the MAC address of the <code>eth0</code> interface to <code>00:11:22:33:44:55</code>.</li>
  <li>After execution, <code>eth0</code> will have the new MAC address until the next reboot or manual change.</li>
</ul>



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
