import csv
import datetime
import locationassociation.computer, locationassociation.location


class ImportTools:
    """A set of reading and writing functions to work with Computer and Location objects.

    Refer to Computer and Location docs to find specific details on formatting for these files.
    Only reads from .csv files, with fieldnames, altho partial fieldnames can be handled.

    read_computers -- File-reader for Computer .csv files. Returns list of Computer objects.
    read_locations -- File-reader for Location .csv files. Returns a list of Location objects.
    write_computers -- File-writer for Computer .csv files. Writes a list of Computer objects to a file.
    write_log -- File-writer for log files. Writes basic run-time information to a file.
    """

    def read_computers(cmpfile):
        """File-reader for Computer .csv files. Returns list of Computer objects."""
        with open(cmpfile, 'rt') as csvfile:
            computers = []
            compreader = csv.DictReader(csvfile, delimiter=',')
            for comp in compreader:
                compIP = ""
                if "IP" in compreader.fieldnames:
                    # specified IP
                    compIP = comp["IP"]
                computers.append(
                    locationassociation.computer.Computer(
                        comp['Device Name'], compIP)
                )
            return computers

    def read_locations(locfile):
        """File-reader for Location .csv files. Returns a list of Location objects."""
        locations = []
        with open(locfile, 'rt') as csvfile:
            
            locreader = csv.DictReader(csvfile)
            for loc in locreader:
                if "IP" in locreader.fieldnames:
                    locations.append(locationassociation.location.Location(
                        loc['Domain'],
                        loc['Region'],
                        loc['Site'],
                        "",
                        loc["Prefixes"], 
                        loc["IP"])
                        )
                else:
                    locations.append(locationassociation.location.Location(
                        loc['Domain'],
                        loc['Region'],
                        loc['Site'],
                        "",
                        loc["Prefixes"]),
                        ""
                        )
            return locations

    def write_computers(cmplist, destination):
        """File-writer for located comps (Name,IP,Domain,Location)"""
        with open(destination, 'wt') as csvfile:
            writer = csv.DictWriter(csvfile,
                        ["Device Name","IP", "Domain", "Region", "Site", "Location"])
            writer.writeheader()
            for comp in cmplist:
                row = {}
                row["Device Name"] = comp.name
                if not comp.IP == "":
                    tempIP = str(comp.IP)[1:-1]
                    row["IP"] = tempIP.replace(", ", ".")
                else:
                    row["IP"] = ""
                row["Domain"] = comp.domain
                row["Region"] = comp.region
                row["Site"] = comp.site
                row["Location"] = comp.site2
                writer.writerow(row)
                

    def write_log(name, locFile, locLoc, unlocFile, unlocLoc, logFolder):
        """Writes relevant information from a report to a log file.

        date -- The date and time the report was written
        name -- The name of the file that was processed
        locFile -- Name of the file representing newly located computers
        locLoc -- Location of that file
        unlocFile -- The name of the file representing unlocated computers
        unlocLoc -- Location of that file
        logFolder: Where to write the log file
        """
        newname = name.split(".")[0] + ".txt"
        rows = []
        rows.append("LOG FILE FOR ASSOCIATION PROCESS OF " + name)
        rows.append("Newly located computers were saved to " +
                   locLoc +"/" + locFile)
        rows.append("Still unlocated computers were saved to " +
                       unlocLoc +"/" + unlocFile)
        fullPath = logFolder + "//" + "resultsLog_" + newname
        with open(fullPath, 'wt') as logfile:
            for row in rows:
                logfile.write(row + "\n")
            logfile.write("File generated at "
                          + str(datetime.datetime.now()))
