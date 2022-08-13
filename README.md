export DISPLAY=:0
pyuic5.exe home.ui -o ../home.py
pyuic5.exe red.ui -o ../red.py
pyuic5.exe yellow.ui -o ../yellow.py
pyuic5.exe green.ui -o ../green.py
pyrcc5.exe picture.qrc -o ../picture_rc.py

cd ui/
run: ./gen_py.sh