#start redis server
redis-server > log/rddt-redis.log &
echo 'redis-server pid is '
echo $!

#start main app on port 5001
python app.py > log/rddt-app.log &
echo 'app.py pid is '
echo $!

#start workers
for i in ${1:-1}
do
  python worker.py > log/rddt-worker.log &
  echo 'worker pid is '
  echo $!
done
