<h1 align="center">CoreWatch</h1>

<p align="center">
<img src="https://img.shields.io/badge/version-Alpha 0.1-gold"> <img src="https://img.shields.io/badge/release-stable-gree"> <a href="https://hits.sh/github.com/powercomp750/CoreWatch-sysmonitor/"><img alt="Hits" src="https://hits.sh/github.com/powercomp750/CoreWatch-sysmonitor.svg?color=fe7d37"/></a> <img src="https://img.shields.io/badge/Platforms-Linux-silver"> <a href="https://github.com/powercomp750/CoreWatch-sysmonitor/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-cyan.svg"/></a>
</p>

This is my working project for Operating System class. 


Terminal based system monitoring tool completely written in Python for Linux

Simply launch the app and get your system usage with 4 major components displaying -> CPU usage, RAM usage, Disk usage and top CPU consuming applications. 

![image](https://github.com/user-attachments/assets/f479948a-a5b8-48d7-9832-131cb94f0849)

## 🎥Here is a working demo
[coreWatch-demo.webm](https://github.com/user-attachments/assets/2cb6170b-4116-4c03-8f88-9520de4accbd)


## ✨Features
 - Icy blue theme (This can feel cooler)
 - Minimal application with NO bloatware
 - Improved splashscreen and better graphics
 - Realtime resource usage based on workload
 - System clock with seconds
 - MIT License
   
## ⚡Runtime
 - Simply download the package from Releases section
 - Grant executable permission
   
   ```
   chmod +x coreWatch
   ```
 - Run using this command:
   
   ```
   ./coreWatch
   ```

   After runtime, exit the application by pressing <code>q</code> or <code>Q</code> key, both will work.

## 💻Supported Platforms
This project is created in modified version of i3-window manager running in Ubuntu 24.04 LTS.

I've tested this application on Kali Linux and Linux Mint and it works pretty well there.
Since the application is entirely coded in Python and uses python modules, this should work fine in other versions of linux. 

For other platforms like Windows and Mac, application is very unstable and therefore is deprecated.

## 📋Troubleshooting/issues
If you encounter issues with the splash screen text not displaying correctly as in preview, you need to install <code>pyfiglet</code> module on your system.
```
pip install pyfiglet
```
This issue is seen on some Linux systems where they lack the required module. Even the executable package bundles all modules but this module needs to be installed on running systems too.

If you're facing any other issues regarding this app, report that issue immediately here [Issues](https://github.com/powercomp750/CoreWatch-sysmonitor/issues)

## 📂Codebase
Project uses Python3 with following modules
- <code>psutil</code>
- <code>time</code>
- <code>curses</code>
- <code>datetime</code>
- <code>deque</code>
- <code>pyfiglet</code>
- <code>colored</code>
- <code>subprocess</code>

## 🔐Privacy
No internet, nothing userdata is collected, this is only a system monitoring application.

## 🤝Contributions
Your contributions are welcome! If you find any issues or want to add enhancements, feel free to submit a pull request.

## 📝License
This project is licensed under the <a href="https://github.com/powercomp750/CoreWatch-sysmonitor/blob/main/LICENSE">MIT License</a>


