# Script: Ops 401 Lab 1
# Authur: Will B. with the help of ChatGPT
# Date: 1/08/2024
# Resources Google, Bard, ChatGPT

# PowerShell cript to adjust auto screen lock

# Set Screen Lock Timeout (in seconds)
$timeoutInSeconds = 150

# Configure Automatic Screen Lock
powercfg /change standby-timeout-dc $timeoutInSeconds
powercfg /change standby-timeout-ac $timeoutInSeconds
powercfg /change monitor-timeout-dc $timeoutInSeconds
powercfg /change monitor-timeout-ac $timeoutInSeconds

# Display Configuration Status
powercfg /query SCHEME_CURRENT SUB_SLEEP STANDBYIDLE