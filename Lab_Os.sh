

%%writefile lab_session.sh

#!/bin/bash

# Lab Session: Analyzing and Storing Logs and Archiving Files

# Part 1: Analyzing and Storing Logs

# Step 1: View System Logs
echo "Step 1: Viewing System Logs"
cat /var/log/syslog
echo

# Step 2: Filter Logs for SSH Connections
echo "Step 2: Filtering Logs for SSH Connections"
cat /var/log/syslog | grep ssh
echo

# Step 3: Store Filtered Logs in a File
echo "Step 3: Storing Filtered Logs in ssh_logs.txt"
cat /var/log/syslog | grep ssh > ssh_logs.txt
echo "Filtered logs stored in ssh_logs.txt"

!chmod +x lab_session.sh
     

!./lab_session.sh
%%writefile lab_session.sh

#!/bin/bash

echo "Step 1: Viewing System Logs"
cat /var/log/syslog
echo

# Step 2: Filter Logs for SSH Connections
echo "Step 2: Filtering Logs for SSH Connections"
cat /var/log/syslog | grep ssh
echo

# Step 3: Store Filtered Logs in a File
echo "Step 3: Storing Filtered Logs in ssh_logs.txt"
cat /var/log/syslog | grep ssh > ssh_logs.txt
echo "Filtered logs stored in ssh_logs.txt"

# Step 4: Create Sample Files
echo "Step 4: Creating Sample Files"
touch file1.txt file2.txt file3.txt
echo "Sample files created: file1.txt, file2.txt, file3.txt"
echo

# Step 5: Archive Files with tar
echo "Step 5: Archiving Files with tar"
tar -czvfi my_archive.tar.gz file1.txt file2.txt file3.txt
echo "Files archived in my_archive.tar.gz"
echo

# Step 6: Copy the Archive to Home Directory
echo "Step 6: Copying the Archive to Home Directory"
cp my_archive.tar.gz ~/my_archive.tar.gz
echo "Archive copied to home directory"
echo

# Step 7: Extract Files from the Archive
echo "Step 7: Extracting Files from the Archive"
tar -xzvf my_archive.tar.gz
echo "Files extracted from the archive"

# Conclusion
echo "Conclusion: You've learned how to analyze and store system logs and how to archive and copy files using the tar command in a shell script."
