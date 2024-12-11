# CoreWatch
This is my working project for Operating System class. 

Terminal based system monitoring tool completely written in Python for Linux

Simply launch the app and get your system usage with 4 major components displaying -> CPU usage, RAM usage, Disk usage and top CPU consuming applications. 

## Features
 - Icy blue theme (This can feel cooler)
 - Minimal application with NO bloatware
 - Improved splashscreen and better graphics
 - Realtime resource usage based on workload
 - System clock with seconds
 - MIT License
   
## Runtime
 - Simply download the package from Releases section
 - Setup up executable permission
   ```
   chmod +x coreWatch
   ```
 - Run using this command:
   ```
   ./coreWatch
   ```

## Supported Platforms
This project is created in modified version of i3-window manager running in Ubuntu 24.04 LTS.

I've tested this application on Kali Linux and Linux Mint and it works pretty well there.
Since the application is entirely coded in Python and uses python modules, this should work fine in other versions of linux. 

For other platforms like Windows and Mac, application is very unstable and therefore is decpricted.

## Codebase
Project uses Python3 with following modules
- <code>psutil</code>
- <code>time</code>
- <code>curses</code>
- <code>datetime</code>
- <code>deque</code>
- <code>pyfiglet</code>
- <code>colored</code>
- <code>subprocess</code>

## Privacy
No internet, nothing userdata is collected, this is only a system monitoring application.

## 🤝Contributions
Your contributions are welcome! If you find any issues or want to add enhancements, feel free to submit a pull request.

## 📝License
This project is licensed under the <a href="https://github.com/powercomp750/CoreWatch-sysmonitor/blob/main/LICENSE">MIT License</a>


