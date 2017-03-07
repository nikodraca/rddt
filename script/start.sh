#start redis server
redis-server > log/rddt-redis.log &
echo 'KILL TO STOP: redis-server pid is '
echo $!

#start main app on port 5001
python app.py > log/rddt-app.log 2>&1 &
echo 'KILL TO STOP: app.py pid is '
echo $!

#start workers

for ((i = 1; i <= ${1:-1}; i++))
do
  python worker.py > log/rddt-worker.log 2>&1 &
  echo 'worker pid is '
  echo $!
done
