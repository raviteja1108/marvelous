echo "Running flask server"
echo "Your IP is:"
ip a | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
python3 $PWD/Server/Flask_API.py 0.0.0.0:5000
