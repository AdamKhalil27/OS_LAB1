#Example 1: List all storage devices on Ubuntu
import subprocess

def list_storage_devices():
  command = "lsblk"
  result = subprocess.run (command, shell=True, stdout=subprocess.PIPE, text=True)
  print(result.stdout)

list_storage_devices()

#Example 2: Check available disk space on a specific storage device
import subprocess

def check_disk_space (device):
  command = f"df -h {device}"
  result = subprocess.run (command, shell=True, stdout=subprocess.PIPE, text=True)
  print(result.stdout)

check_disk_space("/dev/sda1")
     

#Example 3: Mount a storage device

import subprocess

def mount_device(device, mount_point):
  command = f"sudo mount {device} {mount_point}"
  result = subprocess.run (command, shell=True, stdout=subprocess.PIPE, text=True)
  print(result.stdout)

mount_device("/dev/sdb1", "/mnt/mydisk")
     

#Example 4: Format a storage device (WARNING: Data loss can occur)
import subprocess

def format_device (device, tilesystem type):
  command = f"sudo mkfs.{filesystem_type} {device}"
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
  print(result.stdout)

#Be cautious when using this function, as it will erase data on the device.
#format device("/dev/sdc1", "ext4")
     

#Example 5: Unmount a storage device import subprocess
import subprocess

def unmount_device (mount_point):
  command = f"sudo umount {mount_point}"
  result = subprocess.run (command, shell=True, stdout=subprocess.PIPE, text=True)
  print(result.stdout)

unmount_device("/mnt/mydisk")
     

#Example 6: List mounted storage devices
import subprocess

def list_mounted_devices():
    # Run the 'mount' command with grep to list mounted storage devices and store the result
    command = "mount | grep '/dev/sd'"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    # Print the output of the command
    print(result.stdout)



     

#Example 7: Check disk usage of a directory
import subprocess

def check_directory_disk_usage(directory):
    # Run the 'du' command to check disk usage of a directory and store the result
    command = f"du -sh {directory}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    # Print the output of the command
    print(result.stdout)

     

#Example 8: Create a new directory
import subprocess

def create_directory(directory):
    # Run the 'mkdir' command to create a new directory and store the result
    command = f"mkdir {directory}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    # Print the output of the command
    print(result.stdout)

     

import subprocess

# Example 9: Remove a directory (WARNING: Irreversible deletion)
def remove_directory(directory):
    # Run the 'rm' command to remove a directory (use with caution, irreversible) and store the result
    command = f"sudo rm -r {directory}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    # Print the output of the command
    print(result.stdout)

# Example 10: Get storage device information
def get_device_info(device):
    # Run the 'udevadm' command to get information about a device and store the result
    command = f"udevadm info -q property -n {device}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    # Print the output of the command
    print(result. stdout)

# Main test part (Usage of the functions)
if __name__ == "__main":
    # Test each function with appropriate parameters
    list_storage_devices()
    check_disk_space("/dev/sda1")
    mount_device("/dev/sdb1", "/mnt/mydisk")

    # Be cautious with the following line, as it erases data on the device
    format_device("/dev/sdc1", "ext4")

    unmount_device("/mnt/mydisk")
    list_mounted_devices()
    check_directory_disk_usage("/home/user/documents")
    create_directory("/tmp/new_directory")

    # Be cautious with the following line, as it's an irreversible deletion
    #remove_directory("/tmp/new_directory")
    get_device_info("/dev/sda1")
