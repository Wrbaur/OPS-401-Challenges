# Script: Ops 401 
# Class 4 Lab  
# Authur: Will B. with the help of ChatGPT
# Date: 1/11/2024
# Resources Google, Bard, ChatGPT, Andrew Carrol 

# The purpose of this script is to automate the process of setting the passward parameters and to eliminate SMBv1 driver

# Script to Apply Security Configurations

# Function to Configure Password Policy
function Set-PasswordPolicy {
    # Create a new COM object for Shell.Application
    $secpol = New-Object -ComObject Shell.Application

    # Access the security policy settings using the specified namespace
    $securityPolicy = $secpol.Namespace('::{FD6905CE-952F-41F1-9A6F-135D9C6622CC}').GetSecurityPolicy()

    # Set the minimum password length to 6 characters
    $securityPolicy.MinimumPasswordLength = 6

    # Enable password complexity
    $securityPolicy.PasswordComplexity = 1

    # Apply the updated password policy settings
    $securityPolicy.SetPassword()
}

# Function to Configure SMB v1 Client Driver
function Set-SMBv1ClientDriver {
    # Set the start type of the SMB v1 client driver service to 4 (Disable driver)
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10" -Name "Start" -Value 4
}

# Apply Password Policy
Set-PasswordPolicy

# Apply SMB v1 Client Driver Configuration
Set-SMBv1ClientDriver