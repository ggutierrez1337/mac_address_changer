import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    # Only capturing the arguments
    parser.add_option("-i", "--interface", dest="interface", help="Interface to Change the MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    # Variables for capturing the values of the options (args)
    (options, arguments) = get_args()
    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for info")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC. Use --help for info")
    return(options)
def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + "to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"], shell=True)
    subprocess.call(["ifconfig", interface, "hw ether", new_mac], shell=True)
    subprocess.call(["ifconfig", interface, "up"], shell=True)

options = get_args()
change_mac(options.interface, options.new_mac)
