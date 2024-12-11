import psutil
import time
import curses
import datetime
from collections import deque
import pyfiglet
from colored import fg, attr
import subprocess
VERSION = "Alpha-release-0.1"   
def generate_fancy_text(text):
    try:
        ascii_art = pyfiglet.figlet_format(text, font="slant")
        return ascii_art.split('\n')
    except Exception as e:
        return [text] 

def draw_splash_screen(screen):
    max_y, max_x = screen.getmaxyx()
    corewatch_lines = generate_fancy_text("CoreWatch")
    loading_messages = [
        "Loading all components...",
        "Connecting CPU resource...",
        "Gathering system information...",
        "Initializing display modules...",
        "Finalizing setup..."
    ]

    spinner = ['|', '/', '-', '\\'] 
    num_iterations = 30  

    start_y = max_y // 2 - len(corewatch_lines) // 2 - 3
    start_x = max_x // 2 - max(len(line) for line in corewatch_lines) // 2

    for i in range(num_iterations):
        screen.clear()

       
        for j, line in enumerate(corewatch_lines):
            if line.strip():  
                color_index = (j * 4 // len(corewatch_lines)) + 1
                screen.addstr(start_y + j, start_x, line, curses.color_pair(color_index))

       
        message_index = (i // 6) % len(loading_messages)
        screen.addstr(start_y + len(corewatch_lines) + 2, start_x, loading_messages[message_index])

      
        loading_text = f"Loading {spinner[i % len(spinner)]}"
        screen.addstr(start_y + len(corewatch_lines) + 4, start_x, loading_text)

        
        timer_text = f"Time remaining: {3 - i // 10}.{9 - i % 10}s"
        screen.addstr(start_y + len(corewatch_lines) + 6, start_x, timer_text)

        screen.addstr(max_y - 2, max_x // 2 - len("GitHub: @powercomp750") // 2, "GitHub: @powercomp750")

        version_text = f"Version: {VERSION}"
        screen.addstr(max_y - 4, max_x // 2 - len(version_text) // 2, version_text)

      
        screen.refresh()

    
        time.sleep(0.1)

def draw_current_time(screen, y, x, color_pair):

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    screen.addstr(y, x, f"Time: {current_time}", curses.color_pair(color_pair))

def draw_bordered_box(screen, start_y, start_x, height, width, title, color_pair):
    
    screen.attron(curses.color_pair(color_pair))
    screen.addstr(start_y, start_x, "┌" + "─" * (width - 2) + "┐")
    for i in range(1, height - 1):
        screen.addstr(start_y + i, start_x, "│")
        screen.addstr(start_y + i, start_x + width - 1, "│")
    screen.addstr(start_y + height - 1, start_x, "└" + "─" * (width - 2) + "┘")
    screen.addstr(start_y, start_x + 2, f" {title} ", curses.color_pair(color_pair))
    screen.attroff(curses.color_pair(color_pair))

def draw_progress_bar(screen, y, x, width, percent, label, color_pair):
    
    filled_length = int(percent * width)

    screen.addstr(y, x, f"{label}: {percent * 100:.1f}%", curses.color_pair(color_pair))

    
    for i in range(width):
        if i < filled_length:
            screen.addstr(y + 1, x + i, "█", curses.color_pair(color_pair))
        else:
            screen.addstr(y + 1, x + i, " ", curses.color_pair(2))  

def draw_graph(screen, y, x, width, height, data, label, color_pair):
    
    if not data:
        return

    max_val = max(data) if max(data) > 0 else 1
    screen.addstr(y, x, label, curses.color_pair(color_pair))
    screen.addstr(y + 1, x, "┌" + "─" * width + "┐", curses.color_pair(color_pair))
    for h in range(height):
        screen.addstr(y + 2 + h, x, "│")
        screen.addstr(y + 2 + h, x + width + 1, "│")
    screen.addstr(y + 2 + height, x, "└" + "─" * width + "┘", curses.color_pair(color_pair))

  
    for idx, val in enumerate(data):
        if idx < width:
            bar_height = int((val / max_val) * height) 
            for h in range(height):
                if height - h <= bar_height:
                    screen.addstr(y + 2 + h, x + idx + 1, "█", curses.color_pair(color_pair))
                else:
                    screen.addstr(y + 2 + h, x + idx + 1, " ", curses.color_pair(2))

def draw_processes(screen, start_y, start_x, height, width, color_pair):

    screen.addstr(start_y, start_x, "PID   NAME              CPU%", curses.color_pair(color_pair))
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                       key=lambda p: p.info['cpu_percent'], reverse=True)[:5]
    for i, proc in enumerate(processes):
        try:
            pid = proc.info['pid']
            name = proc.info['name'][:15]
            cpu = proc.info['cpu_percent']
            screen.addstr(start_y + i + 1, start_x, f"{pid:<6}{name:<16}{cpu:>5.1f}%", curses.color_pair(3))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def draw_uptime(screen, y, x, color_pair):
 
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_str = str(datetime.timedelta(seconds=int(uptime_seconds)))
    screen.addstr(y, x, f"Uptime: {uptime_str}", curses.color_pair(color_pair))

def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(True) 
    stdscr.timeout(1000)  

   
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)    
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)  
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)  
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)      

    progress_color = 1

    max_y, max_x = stdscr.getmaxyx()

   
    box_height = min(max_y // 4, 12)  
    box_width = min(max_x // 2 - 4, 40)  


    cpu_history = deque([0]*30, maxlen=30)
    memory_history = deque([0]*30, maxlen=30)

    draw_splash_screen(stdscr)

    while True:
        stdscr.clear()

       
        time_y = 0
        time_x = max_x // 2 - 10
        draw_current_time(stdscr, time_y, time_x, 4)

        
        draw_bordered_box(stdscr, 2, 2, box_height, box_width, "CPU", 1)
        cpu_percent = psutil.cpu_percent(interval=None)
        cpu_history.append(cpu_percent)
        draw_progress_bar(stdscr, 3, 4, box_width - 4, cpu_percent / 100, "CPU", progress_color)
        draw_graph(stdscr, 5, 4, min(len(cpu_history), box_width - 4), 4, list(cpu_history), "CPU", 0)

        
        draw_bordered_box(stdscr, 2, box_width + 6, box_height, box_width, "RAM", 2)
        memory_info = psutil.virtual_memory()
        memory_percent = memory_info.percent
        memory_history.append(memory_percent)
        draw_progress_bar(stdscr, 3, box_width + 8, box_width - 4, memory_percent / 100, "RAM", progress_color)
        stdscr.addstr(6, box_width + 8, f"Used: {memory_info.used // (1024 ** 2)}MB / Total: {memory_info.total // (1024 ** 2)}MB", curses.color_pair(2))
        draw_graph(stdscr, 4, box_width + 8, min(len(memory_history), box_width - 4), 4, list(memory_history), "RAM ", 2)

        
        draw_bordered_box(stdscr, box_height + 3, 2, box_height, box_width, "Disk", 7)
        disk_info = psutil.disk_usage('/')
        disk_percent = disk_info.percent
        disk_name = "Root Disk"  
        disk_speed = "N/A"      
        draw_progress_bar(stdscr, box_height + 4, 4, box_width - 4, disk_percent / 100, "Disk", progress_color)
        stdscr.addstr(box_height + 6, 4, f"{disk_name}: Used: {disk_info.used // (1024 ** 3)}GB / Total: {disk_info.total // (1024 ** 3)}GB", curses.color_pair(7))
        stdscr.addstr(box_height + 7, 4, f"Speed: {disk_speed}", curses.color_pair(7))

      
        draw_bordered_box(stdscr, box_height + 3, box_width + 6, box_height, box_width, "Processes", 3)
        draw_processes(stdscr, box_height + 4, box_width + 8, box_height - 2, box_width - 2, 3)

        stdscr.addstr(max_y - 2, max_x // 2 - len("GitHub: @powercomp750") // 2, "GitHub: @powercomp750", curses.color_pair(2))

    
        key = stdscr.getch()
        if key == ord('q'):
            break
            
        if key == ord('Q'):
        	break

        
        max_y, max_x = stdscr.getmaxyx()

if __name__ == "__main__":
    curses.wrapper(main)
