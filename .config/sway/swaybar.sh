datetime=$(date +'%Y-%m-%d %I:%M %p')

uptime=$(uptime -p)

uname=$(uname -rs)

cpu=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')

echo CPU: $cpu' | '$uname' | '${uptime#* }' | '$datetime
