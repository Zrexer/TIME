# Running in Termux 

apt update &&
apt upgrade &&
pkg install python3 && 
pkg install git &&
git clone https://github.com/Zrexer/TIME && 
cd TIME && 
pip3 install -r requirements.txt &&
python run_for_t.py 
