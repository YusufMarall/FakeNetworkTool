import subprocess

def banner():
    print("""
 ,---.  .--.  ,-. .-.,---.  .-. .-.,---. _______ .-.  .-. .---.  ,---.   ,-. .-._______  .---.   .---.  ,-.     
 | .-' / /\ \ | |/ / | .-'  |  \| || .-'|__   __|| |/\| |/ .-. ) | .-.\  | |/ /|__   __|/ .-. ) / .-. ) | |     
 | `-./ /__\ \| | /  | `-.  |   | || `-.  )| |   | /  \ || | |(_)| `-'/  | | /   )| |   | | |(_)| | |(_)| |     
 | .-'|  __  || | \  | .-'  | |\  || .-' (_) |   |  /\  || | | | |   (   | | \  (_) |   | | | | | | | | | |     
 | |  | |  |)|| |) \ |  `--.| | |)||  `--. | |   |(/  \ |\ `-' / | |\ \  | |) \   | |   \ `-' / \ `-' / | `--.  
 )\|  |_|  (_)|((_)-'/( __.'/(  (_)/( __.' `-'   (_)   \| )---'  |_| \)\ |((_)-'  `-'    )---'   )---'  |( __.' 
(__)          (_)   (__)   (__)   (__)                   (_)         (__)(_)            (_)     (_)     (_)     
    """)

def create_fake_network(interface, ssid, channel):
    
    subprocess.run(["ifconfig", interface, "down"], check=True)
    
    
    subprocess.run(["iwconfig", interface, "mode", "monitor"], check=True)
    
    
    subprocess.run(["ifconfig", interface, "up"], check=True)
    
    
    subprocess.run(["iwconfig", interface, "channel", str(channel)], check=True)
    
    
    airbase_command = ["airbase-ng", "-e", ssid, "-c", str(channel), interface]
    subprocess.Popen(airbase_command)
    
    print(f"Fake network '{ssid}' created on {interface} at channel {channel}")
banner()

interface = input("Enter the wireless interface you want to use: ")
network_count = int(input("How many fake networks are we setting up today? "))


networks = []
for i in range(network_count):
    ssid = input(f"Enter the SSID for network {i+1}: ")
    channel = int(input(f"Enter the channel for network {i+1}: "))
    networks.append((ssid, channel))

for ssid, channel in networks:
    create_fake_network(interface, ssid, channel)
