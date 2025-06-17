from flask import Flask, render_template, request # Added render_template here
from scapy.all import ARP, Ether, srp
import ipaddress
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    devices = []
    error_message = None

    if request.method == 'POST':
        ip_range = request.form.get('ip_range')

        if os.name == 'posix' and os.geteuid() != 0:
            error_message = "Scapy requires root privileges on Linux/macOS. Please run this script with sudo."
        elif os.name == 'nt' and not os.access("NUL", os.W_OK):
             error_message = "Scapy might require Administrator privileges on Windows."

        if error_message:
            return render_template('index.html', error=error_message)

        if ip_range:
            try:
                network = ipaddress.ip_network(ip_range, strict=False)
                
                ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(network)), timeout=2, verbose=0)
                
                for sent_packet, received_packet in ans:
                    devices.append({
                        'ip': received_packet.psrc,
                        'mac': received_packet.hwsrc,
                        'hostname': 'N/A'
                    })
            except ValueError:
                error_message = "Invalid IP range format. Please use a valid format like 192.168.1.0/24 or 192.168.1.1/24."
            except PermissionError:
                error_message = "Permission denied. Please ensure you have sufficient privileges to run network scans (e.g., run as Administrator/root)."
            except Exception as e:
                error_message = f"An unexpected error occurred during the scan: {e}"

    return render_template('index.html', devices=devices, error=error_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

