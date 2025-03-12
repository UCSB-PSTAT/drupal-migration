# resources-computing-rstudio

# RStudio Server

## RStudio server - perelandra

Dedicated RStudio server. To be used by any PSTAT department student or professor that has been assigned a department account. You can connect to it from anywhere via your web browser using your department credentials and this URL: [https://perelandra.pstat.ucsb.edu/rstudio](https://perelandra.pstat.ucsb.edu/rstudio). Anyone accessing from outside the department I refer you to the tech note #2 below.

Tech notes:

 

Handling RStudio Stuck Processes:

1. If your R won't start in your RStudio session you need to email [helpdesk@pstat.ucsb.edu](mailto:helpdesk@pstat.ucsb.edu) letting us know so that we can verify your session is locked with the command: rstudio-server active-sessions and kill the appropriate PID.
2. If you'd like to fix this yourself, you can do that by logging into the RStudio server via terminal using the command: ssh {your\_username}@perelandra.pstat.ucsb.edu. After successfully logging in issue the command:  
     
   rstudio-server active-sessions
   
   That command will list all RStudio sessions, make sure yours are in that list then issue this command to kill all of them: pkill -u {your\_username}

Accessing RStudio While Not in Our Departmentm

1. To access [https://perelandra.pstat.ucsb.edu/rstudio](https://perelandra.pstat.ucsb.edu/rstudio) from outside our physical department you will need to utilize the campus VPN. Information on how to access the campus VPN can be found [**here**](https://www.ets.ucsb.edu/services/campus-vpn).

## Resources Menu

- [Department Member Resources -](/resources "Department Member Resources")
- [DataLab](/resources/statlab "DataLab")
- [Instructor Resources](/resources/instructor "Instructor Resources")
- [TA Resources](/resources/ta-resources "TA Resources")
- [Computing](/resources/computing "Computing")
  
  - [Computing Announcements](/resources/computing/announcements "Computing Announcements")
  - [Statlab](/resources/computing/statlab "Statlab")
  - [Lab Use &amp; Accounts](/resources/computing/lab-use "Lab Use & Accounts")
  - [File Management](/resources/computing/file-management "File Management")
  - [Software](/resources/computing/software "Software")
  - [Compute Cluster](/resources/computing/cluster "Compute Cluster")
  - [RAS Cluster](/resources/computing/ras "RAS Cluster")
  - [RStudio Server](/resources/computing/rstudio "RStudio Server")
  - [Email](/resources/computing/email "Email")
  - [Web Site Publishing](/resources/computing/website "Web Site Publishing")
  - [Wireless Access](/resources/computing/wireless "Wireless Access")
  - [Mail Room Copier](/resources/computing/copier "Mail Room Copier")
  - [Digital Petitions](/resources/computing/digital-petitions "Digital Petitions")
- [Employment](/about/employment "Employment")
- [Useful Academic Links](/resources/useful "Useful Academic Links")