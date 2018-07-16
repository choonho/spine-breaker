# spine-breaker

# Architecture

Master is web server.
Breaker is thread agent at here or servers.


## Server killer
Breaker connects AWS resources by using credential at config file.
Stop EC2 instances by scheduler.

Before kill the host, Breaker anounces its schedule to master.
 
## Process killer
There is agent at each host.
agent connects to master, then 
1) if hostname is same with me
2) find process, if match, kill process by scheduler.

Before kill process, agent anounces its schedule to master.

# API
## master API

list breaker
list history
list scheduler
run schedule

# Master Web

Use Jenkins as Viewer
