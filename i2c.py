import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/meetfietsApp/Raspi-Driver-SPS30')
import sps30Service
os.system("/meetfietsApp/Raspi-Driver-SPS30/sps30-service.py 1")
if rdy == 1:
    print('OKE')