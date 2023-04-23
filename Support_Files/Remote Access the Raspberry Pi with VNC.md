# Introduction
`VNC (Virtual Network Computing) is a system to share a graphical desktop, pretty similas to XRDP.
The difference is that you connect to the current session directly, unlike XRDP which creates a new session.
There are many VNC servers and clients you can use (RealVNC, TightVNC, UltraVNC, …).`

`VNC runs on port 5900.
You can NAT this port to make it available from the outside if needed, but it’s not the safest option, consider the next solution listed in this article.
`
## Installation
`Like SSH, VNC is already installed on any Raspberry Pi OS version so we just need to enable it.
To do this, open the Raspberry Pi configuration tool, go to the “Interfaces” tab and check the “Enabled” box on the VNC line.`

`That’s it, the VNC server is installed and ready to use.`

## For Windows
`From Windows it is the same thing, you can download and install RealVNC from their [official website](https://www.realvnc.com/fr/connect/download/viewer/windows/)
Then launch the software via the start menu, type the IP of the Raspberry Pi and here you are connected to the remote desktop.
The requested logins are the usual users of the system (for example pi/raspberry if you have not changed the password)`

