# resources-computing-cluster

# Compute Cluster

## The Cluster Computing Environment

![](http://kingslanding.pstat.ucsb.edu/computing/images/tower.jpg)The compute cluster is a VMware cluster of three linked nodes. Each node has 56 cores, 256GB of RAM and are connected to a 12TB RAID. One of the features of this VMware cluster is it's ability to move compute servers between the nodes for failover and load balancing. Clusters are usually deployed to improve performance and/or availability over that provided by a single computer, while typically being much more cost-effective than single computers of comparable speed or availability.

### Establishing a connection

With your ssh client, you can establish a connection through “ssh”.

The hostname of the main compute node is: denali.pstat.ucsb.edu

*This is a standalone node, consisting of two 10-core processors (20 total cores) at 2.60GHz each and 128GB RAM.*

or:

This system is offline for specific grant use only

The hostname of the alternate node is: wavelet.pstat.ucsb.edu

*This is a standalone node, consisting of two 10-core processors (20 total cores) at 2.60GHz each and 128GB RAM.*

 

*Note: For security reasons we have moved our cluster computer behind the campus VPN to limit access to only campus UCSBNetID authorized personal. Please click [**HERE**](https://www.ets.ucsb.edu/services/campus-vpn) to get directions and download software for intalling on your device to allow access.*

 

Use your department login and password.

Now you are ready to do all the features in the cluster. Remember the cluster is UNIX based, so you may need to know some simple UNIX commands.

We will have to run Xming in the background on Windows machines to do graphic features on the cluster. Xming is free and can be downloaded 

[![](https://kingslanding.pstat.ucsb.edu/computing/themes/mambo/icons/web.gif)here](http://www.straightrunning.com/XmingNotes/ "Outgoing link (in new window)")

### Condo Cluster at CNSI/MRL

Our department also has access to the Condo cluster at CNSI/MRL called Braid (specs can be found [here](http://csc.cnsi.ucsb.edu/clusters/braid).) To get access to this cluster please fill out this [form](https://regulation.pstat.ucsb.edu/cnsi/request_account.htm). Once granted access you will be given a unique password with instructions on how to change it.

### Documentation

Please see the help [pages](http://csc.cnsi.ucsb.edu/docs) for help on using R and Matlab on the braid cluster. Be aware even though the documents refer to the Knot cluster they still apply to the Braid cluster simply replace the work 'knot' with 'braid' and you'll have exactly what you need to run R and Matlab jobs in a cluster environment.

 

Please always submit jobs that take more than a few minutes to the job queue. **Do not run long jobs on the head node.**

### If you do not have SSH client in your PC

If you don't know what a “ssh client” is, it might not be installed on your PC. Download one client from the web for FREE! It is called “PUTTY”.

[![](https://kingslanding.pstat.ucsb.edu/computing/themes/mambo/icons/web.gif)Grab it here.](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "Outgoing link (in new window)")

On the PSTAT Lab PC's, it's already installed. In the SSH client, make sure that you set the 'Forward X11 Packets' option.

[Instructions on Setting up X11 forwarding](https://kingslanding.pstat.ucsb.edu/computing/X11 "X 11")

* * *

If you need help, please email at [helpdesk@pstat.ucsb.edu](mailto:helpdesk@pstat.ucsb.edu "Write an email (mail client launch)")

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
    
    - [Cluster Commands](/resources/computing/cluster/commands "Cluster Commands")
  - [RAS Cluster](/resources/computing/ras "RAS Cluster")
  - [RStudio Server](/resources/computing/rstudio "RStudio Server")
  - [Email](/resources/computing/email "Email")
  - [Web Site Publishing](/resources/computing/website "Web Site Publishing")
  - [Wireless Access](/resources/computing/wireless "Wireless Access")
  - [Mail Room Copier](/resources/computing/copier "Mail Room Copier")
  - [Digital Petitions](/resources/computing/digital-petitions "Digital Petitions")
- [Employment](/about/employment "Employment")
- [Useful Academic Links](/resources/useful "Useful Academic Links")