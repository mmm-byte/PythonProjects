# Installation and Setup

If you are new to Raspberry Pi, perhaps even the Raspberry Pi 4 or Raspberry Pi 400, and taken it out of the box. Now what? There are a million things you can do with your mini computer, from using it as a web server to turning into a retro arcade, but first you need to set up the Raspberry Pi. Note that, if this is a Raspberry Pi Pico microcontroller, the setup process is completely different so see our article on how to set up Raspberry Pi Pico.

If you bought your Pi as part of a kit, you probably got everything you need right in the box, but if you just have the board, you'll need the following:

1. **USB power adapter** like the official Raspberry Pi 4 power supply(opens in new tab)
2. **MicroSD card** (at least 8GB, but preferably 16 or 32GB(opens in new tab))
3. **USB card reader**(opens in new tab) unless one is built into your PC
And, unless you plan to do a headless install on the Raspberry Pi and use it via [remote desktop](https://github.com/mmm-byte/PythonProjects/blob/main/Support_Files/Remote%20Access%20the%20Raspberry%20Pi%20with%20VNC.md) or SSH (controlling it from a PC), you will need.
4. **Keyboard (wired or perhaps one of the best wireless keyboards)
5. **Mouse or other pointing device
6. **Monitor or TV
7. **HDMI cables

Note that the HDMI cable you need varies based on the Raspberry Pi you are using. Raspberry Pi 4 B and Pi 400 have dual, micro HDMI out ports so they require micro HDMI to HDMI cables(opens in new tab) or adapters. The Raspberry Pi Zero / Zero W and Zero 2 W have mini HDMI and therefore need mini HDMI to HDMI cables(opens in new tab) to connect to a display. All other Raspberry Pi models, including the 3 B, have standard HDMI ports and can use HDMI male to male cables to attach to your monitor or TV.

## Setting Up Your Raspberry Pi's Power
You can't set up a Raspberry Pi without a way to power it on. The Raspberry Pi 4 B and Raspberry Pi 400 (which is just a 4 B inside a keyboard) are powered via a USB Type-C port, which requires a charger that can output 5 volts and 3 amps. Most USB Type-C phone chargers don't have enough amps to get the job done, unless they have USB PD capability, but USB-C laptop chargers should all work. While it's unlikely to be a problem, note that Pi 4 models that were manufactured in 2019 or early 2020 have a bug which prevents them from charging over high-speed data cables that support USB 3.x 5 or 10 Gbps connections.

All other Raspberry Pi models, including the Raspberry Pi 3 B and Pi Zero / Zero W / Zero 2 W, get power via a micro USB port, which means that you can give it juice by connecting it to just about any of the many different third-party chargers or even by attaching it to one of your computer's USB ports. While you can get away with giving the board a lot less electricity (the Pi Zero W runs perfectly off of my laptop's USB port), the optimal power source for a Raspberry Pi 3 should have 5 volts and 2.5 amps, which also provides plenty of power for any peripherals you attach to its USB ports.

Raspberry Pi 3 B with power source

There are a number of power supplies that are made specifically for Raspberry Pis, including the official Raspberry Pi  4 power supply (opens in new tab) and the CanaKit 5V 2.5A supply (opens in new tab)for other Raspberry Pi models.

The Pi doesn't have a built-in power switch, so the default way to turn it on is to plug it in. You can also find power supplies with built-in on / off switches. However, to avoid data loss, you'll want to use the shutdown feature in your operating system (OS) before unplugging or switching it off. 

## An OS on a microSD Card
There are more than a dozen different OSes for Raspberry Pi, and there's even a way to run full Windows 11 on the Pi 4. However, Raspberry Pi OS, a special version of Debian Linux that's optimized for the Pi, is the best platform for most use cases so that's the one we'll be explaining how to set up.

The Raspberry Pi has no internal storage, but instead boots off of a a microSD memory card that you provide. Be sure to get a card that's at least 8GB, preferably 32GB or higher, and has class 10 speed (see our list of best Raspberry Pi microSD cards). It almost goes without saying, but you'll need some kind of card reader to write the OS to it from your PC.

## Remote Install for Raspberry Pi?
If you just want to experiment with the Pi or use it to control physical objects like lights, motors and sensors, you don't need to give it its own screen and keyboard. Follow our separate instructions for how to do a Remote install on the Raspberry Pi, and you can control the device from the desktop of your PC or Mac, using VNC or SSH remote access software.

## Downloading and Installing Raspberry Pi 
Once you have all the components you need, use the following steps to create the boot disk you will need to set up your Raspberry Pi. These steps should work on a  using a Windows, Mac or Linux-based PC (we tried this on Windows, but it should be the same on all three).

1.  Insert a microSD card / reader into your computer.  

2.  Download and install the official Raspberry Pi Imager. Available for Windows, macOS or Linux, this app will both download and install the latest Raspberry Pi OS. There are other ways to do this, namely by downloading a Raspberry Pi OS image file and then using a third-party app to “burn it,” but the Imager makes it easier. 

3.  Click Choose OS.

4. Select Raspberry Pi OS (32-bit) from the OS menu (there are other choices, but for most uses, 32-bit is the best).  
Choose Raspberry Pi OS 32-bit

 4. Click Choose storage and pick the SD card you’re using. 
Click Choose Storage

5. Click the settings button or hit CTRL + SHIFT + X to enter settings.
Click Settings

6. Fill in settings fields as follows and then hit Save. All of these fields are technically optional, but highly recommended so that can get your Raspberry Pi set up and online as soon as you boot it. If you don't set a username and password here, you'll have to go through a setup wizard that asks you to create them on first boot.

- Set hostname: the name of your Pi. It could be "raspberrypi" or anything you  like.
* Enable SSH: Allow SSH connections to the Pi. Recommended.
+ Use password authentication / public key: method of logging in via SSH
- Set username and password: Pick the username and password you'll use for the Pi
* Configure wireless LAN: set the SSID and password of Wi-FI network
+ Wireless LAN country: If you're setting up Wi-Fi, you must choose this.
- Set locale settings: Configure keyboard layout and timezone (probably chosen correctly by default)

7. Click Write. The app will now take a few minutes to download the OS and write to your card.  
Click Write in Raspberry Pi Imager

## Booting Your Raspberry Pi for the First Time
After you're done writing the Raspberry Pi OS to a microSD card, it's time for the moment of truth.

1. Insert the microSD card into the Raspberry Pi.

2. Connect the Raspberry Pi to a monitor, keyboard and mouse.

3. Connect an Ethernet cable if you plan to use wired Internet.

4. Plug the Pi in to power it on. 

If you had used the Raspberry Pi Imager settings to create a username and password, you'll be able to go straight into the desktop environment, but if not, you will get a setup wizard.

## Using the Raspberry Pi First-Time Setup WIzard
If you chose a username and password in Raspberry Pi Imager settings, before writing the microSD card, you will get the desktop on first boot. But, if you did not, you'll be prompted to create a username and password and enter all the network credentials by a setup wizard on first boot. If that happens, follow these steps to finish setting up your Raspberry Pi.

1. Click Next on the dialog box.
Click Next

2. Set your country and and language and click Next. The default choices may already be the correct ones.
Set country and language

3. Enter a username and password you wish to use for your primary login. Click Next.
Enter username and password

4. Toggle Reduce the size of the desktop" to on if the borders of the desktop are cut off. Otherwise, just click Next.
Reduce the size of Raspberry Pi desktop

5. Select the appropriate Wi-Fi network on the screen after, provided that you are connecting via Wi-Fi. If you don't have Wi-Fi or are using Ethernet, you can skip this.
Select the Wi-Fi network

6. Enter your Wi-Fi password (unless you were using Ethernet and skipped). 
Enter Wi-Fi password

7. Click Next when prompted to Update Software. This will only work when you are connected to the Internet, and it can take several minutes. If you are not connected to the Internet, click Skip.
Click Next to updatge

8. Click Restart. 
Click restart

If you wish to change these settings later, you can find the region and password settings, along with many other options, by clicking on the Pi icon in the upper left corner of the screen and navigating to Preferences -> Raspberry Pi Configuration. You can configure Wi-Fi by clicking on the Wi-Fi / network icon on the taskbar. 

Selecting the Raspberry Pi Configuration Menu

## Changing Your Screen Resolution on Raspberry Pi
If you don't have enough desktop real estate, you may want to change your screen resolution to ensure that it matches what your display is capable of. If you are using a headless Pi and accessing it via VNC, you still probably want at least a 720p screen.

To change the Raspberry Pi resolution:

1. Open the Screen configuration menu by clicking on the Pi icon then selecting Preferences -> Screen Configuration.
Screen configuration

2. Right Click on the HDMI box and select your Resolution from the Resolution menu.
Select Resolution

3. Click the Check box. The screen resolution will update.
Click checkbox

4. Click Yes to reboot.
Click yes to reboot
