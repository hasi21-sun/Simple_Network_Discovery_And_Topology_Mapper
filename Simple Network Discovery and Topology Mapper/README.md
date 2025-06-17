# 🗺️ Network Discovery Tool (Basic)

A Python-based web application built with **Flask** and **Scapy** to identify active devices on a local network via ARP scanning. This project lays the groundwork for a full-featured network utility dashboard by combining a minimal backend with a multi-utility web frontend.

---

## ✨ Implemented Features

### ✅ Network Scanner (ARP-based)
- Scans a user-specified local IP range (e.g., `192.168.1.0/24`)
- Detects and displays active devices using ARP requests
- Displays IP and MAC address of each discovered device in a neat web table

### ✅ Web Interface (Flask)
- Clean form-based UI built with HTML/CSS served via Flask templates
- Dynamically renders scanning results on the same page

---

## 🚧 Planned Backend Features (Frontend Already Present)

The UI (index.html) includes input forms for the following utilities, which are **currently non-functional** but ready to be integrated:

- 🔍 DNS Lookup
- 🏓 Ping Test
- 🔐 Port Scanner
- 🌐 GeoIP Locator
- 🖥️ HTTP Server
- ↪️ Proxy Server

> 🛠️ These are excellent candidates for future enhancement via Flask routes and Python modules.

---

## 📁 Project Structure

```
network_tool_project/
├── app.py               # Flask app with ARP scanning logic
├── templates/
│   └── index.html       # Frontend HTML UI
```

---

## 🛠️ Technologies Used

- **Python 3** – core logic
- **Flask** – web framework
- **Scapy** – low-level network packet crafting and ARP scanning
- **HTML5 & CSS3** – frontend structure and styling

---

## ⚙️ Setup & Installation

### 🔁 Step 1: Set up Project Files

Create a folder called `network_tool_project` and place:

- `app.py` in the root
- `index.html` in a subfolder named `templates/`

### 📦 Step 2: Install Dependencies

```bash
pip install Flask scapy
```

### 🪟 For Windows Users Only: Install Npcap

Scapy requires **Npcap** to send ARP packets.  
Download from: [https://nmap.org/npcap](https://nmap.org/npcap)

> ✅ During installation, check **"Install Npcap in WinPcap API-compatible Mode"**

---

## ▶️ How to Run

Since ARP scanning needs low-level access, run as an **administrator (Windows)** or use `sudo` (Linux/Mac):

### 🔧 Linux/Mac:
```bash
cd path/to/network_tool_project
sudo python app.py
```

### 🪟 Windows:
Right-click Command Prompt → “Run as Administrator”
```bash
cd path\to\network_tool_project
python app.py
```

Once the app starts, visit:
```
http://127.0.0.1:5001
```

---

## 🌐 Usage

1. Open browser at `http://127.0.0.1:5001`
2. In **Network Discovery Tool**, input your local subnet:
   - Examples: `192.168.0.0/24`, `192.168.1.0/24`
3. Click "Scan Network"
4. Results (IP + MAC addresses) will appear in a table

---

## ⚠️ Notes

- **Run as admin/root**: Scapy requires elevated permissions
- **Local LAN only**: Scans devices on the same subnet
- **Development server**: Flask's built-in server is for local testing only

---


## 🧑‍💻 Authors

- P. UdayKiran  
- Team: S. Hasika,  R. Sidhartha Chowdary, N. Chaithanya Krishna
- 💡 Guided by: Mrs. Sahana D S,
                Assistant Professor,
                Department of CSE,
                GITAM School of Technology, 
                GITAM( Deemed to be University),
                Bengaluru


---

## 📜 License  
**MIT License** — free to use, share, and modify with attribution.
