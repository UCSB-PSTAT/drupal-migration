# resources-computing-announcements

# Computing Announcements

## Requesting Access to JupyterHub

As a faculty member, instructor, or researcher you can request a JupyterHub instance to support your work and facilitate learning. Please follow this link to [request JupyterHub instance](https://help.lsit.ucsb.edu/hc/en-us/articles/4925937111323-Requesting-JupyterHub).

*If you are a **student** looking to access JupyterHub for your course work, please check you syllabus, or with your TA or your faculty instructor for how to access the JupyterHub instance that is available to you.*

## Zoom Conferencing Software

Our campus has a site license to Zoom conferencing software and if you need to hold your lectures for your class remotely please see how to use zoom [HERE](https://www.it.ucsb.edu/zoom-video-conferencing).

Zoom can be used for:

1. Conferences
2. Meetings
3. Lectures

## RStudio server - perelandra

I've added a new dedicated RStudio server to our compute infrastructure. You can connect to it from anywhere via your web browser using your department credentials and this URL: [http://perelandra.pstat.ucsb.edu/rstudio](http://perelandra.pstat.ucsb.edu/rstudio)

Tech notes:

1. If your R won't start in your RStudio session you need to email [help@pstat.ucsb.edu](mailto:help@pstat.ucsb.edu) letting us know so that we can verify your session is locked with the command: rstudio-server active-sessions and kill the appropriate PID.
2. To access [http://perelandra.pstat.ucsb.edu/rstudio](http://perelandra.pstat.ucsb.edu/rstudio) from outside our physical department you will need to utilize the campus VPN. Information on how to access the campus VPN can be found [**here**](https://www.ets.ucsb.edu/services/campus-vpn).

## Mini-Lab in Mailroom

All three of the PC's in the mailroom are now on Windows 10. Each has Matlab, SAS, R and Rstudio, Mathematica. And all three can print to the copier a few feet away.

## Mac Computers and Out-of-Control icdd Process

Do to the fact that our campus network is very large and most IP's are public. When you connect your Mac to the network a process called icdd goes across the network looking for image capture devices. The devices it looks for includes any scanning device (aka almost all printers and copiers). The process builds a list and continually updates that list as the devices come on and off the network. Below are the steps to disable icdd process from your Mac.

If you have Mac OS El Capitain and above you'll need to first disable System Integrated Protection (SIP). To do that follow the below instructions:

1. Reboot your computer holding down the command+R keys, this boots you into Recovery mode.
2. In Recovery Mode go to "Utilities" Menu and click on "Terminal"
3. In Terminal type, "csrutil **disable**" and press Enter
4. Reboot your mac by typeing "shutdown -r now"

Your Mac will now reboot with SIP disabled. When your Mac is finished rebooting and your logged into your account do the following steps:

1. Launch the "Terminal" app by either navigating to your "Applications" Folder then to the "Utilities" Folder where you'll find the "Terminal" app. Or you can just type the word "Terminal" in the spyglass search on the upper right of the menu bar.
2. Once in terminal type, "sudo -s" to elevate your permissions to root.
3. Then type, "cd /System/Library/Image\\ Capture/Support"
4. Once in that directory type, "ls" to list the files. In that directory you'll see the "icdd" file.
5. To disable the file type, "mv icdd icdd-disabled" this will rename the file making the OS unable to launch it.

Now that icdd is disabled you'll need to re-enable SIP, follow the below steps to do that:

1. Reboot your computer holding down the command+R keys, this boots you into Recovery mode.
2. In Recovery Mode go to "Utilities" Menu and click on "Terminal"
3. In Terminal type, "csrutil **enable**" and press Enter
4. Reboot your mac by typeing "shutdown -r now"

That's it.

Now if you ever what to re-enable the icdd process you can follow the above instructions and where it says type, "mv icdd icdd-disabled" instead type, "mv icdd-disabled icdd".

## Changing Department Password (NOT UCSBNetID)

Now that we are using a more robust authentication system for our department we are finally able to offer you the ability to change your own department-wide account password. The department account I'm refering to is the one that you were assigned when you first started in this deparment. The department account gives you access to our compute servers, clusters and our wireless access on the 5th floor. To change your password click [**HERE**](https://kingslanding.pstat.ucsb.edu/setting/changeps.php)

**\*We put some requirements on changing your new password to avoid simple and easily guessed passwords:**

**Password requirements: Minimum of 8 characters. At least 1 english uppercase character (A-Z), 1 english lowercase character (a-z), 1 Base 10 digit (0-9) and 1 special character (ie., !, $, #, %)**

## Remote Application Server (RAS)

Utilizing VMware, Windows server and [**Parallels RAS**](https://www.parallels.com/products/ras/remote-application-server/) software we've added a new research cluster. This cluster utilizes virtualized GUI statistical software like: R, Matlab and SAS to do research. All running jobs are load balanced over the entire cluster giving your jobs peak performance. You can easily start a job on your office computer then disconnect leave and at anytime reconnect to the existing running job from either another computer, laptop, tablet or even from your phone.  Running these applications requires specialized accounts on the cluster, to request one for yourself please click [**HERE.**](https://regulation.pstat.ucsb.edu/ras/request_account.htm) To request access for a group please have each member of the group make an individual request and put in the project title field, your group project name.

### RAS Client Software:

Make sure to download the [**RAS client software**](https://www.parallels.com/products/ras/download/client/) for either Windows, Mac, Linux, iOS, Android, Chrome or Windows Phone. This is required to optimize your virtualized application performance.

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