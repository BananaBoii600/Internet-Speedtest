import speedtest
import tkinter as tk

test = speedtest.Speedtest()

def start_btn():
    screen.title("Loading Server List")
    test.get_servers()
    screen.title("Choosing Best Server")
    best = test.get_best_server()
    screen.title(f"Found: {best['host']} located in {best['country']}")

    screen.title("Performing Download Test...")
    download_result = test.download()
    screen.title("Performing Upload Test...")
    upload_result = test.upload()
    ping_result = test.results.ping

    label.config(text=f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")
    babel.config(text=f"Upload speed: {upload_result /1024 / 1024:.2f} Mbps")
    sabel.config(text=f"Ping: {ping_result:.2f} ms")
    screen.title("Internet Speedtest")

screen = tk.Tk()
screen.title("Internet Speedtest")
screen.geometry("500x200")
screen.config(bg="White")

label = tk.Label(screen, bg = "white", fg = "black", font = ("Arial", 15))
label.pack()
babel = tk.Label(screen, bg = "white", fg = "black", font = ("Arial", 15))
babel.pack(pady=5)
sabel = tk.Label(screen, bg = "white", fg = "black", font = ("Arial", 15))
sabel.pack(pady=10)
start_btn = tk.Button(screen, text="Start Speedtest", bg="green", font=("Arial", 15), command = start_btn)

start_btn.pack(pady = 15, side = "bottom",)

screen.mainloop()