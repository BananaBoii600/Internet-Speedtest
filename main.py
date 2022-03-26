from distutils.command.upload import upload
import sys
import speedtest

test = speedtest.Speedtest()

print("Loading server list...")
test.get_servers()
print("Choosing best server...")
best = test.get_best_server()
print(f"Found: {best['host']} located in {best['country']}")

print("Performing Download test...")
download_result = test.download()
print("Performing Upload Test...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")
print(f"Upload speed: {upload_result /1024 / 1024:.2f} Mbps")
print(f"Ping: {ping_result:.2f} ms")

input("Enter any key to quit")
