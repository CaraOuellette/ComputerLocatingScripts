import csv
import datetime
import LocationAssociation.Computer, LocationAssociation.Location

class ImportTools:
    """A set of reading and writing functions to work with Computer and Location files.

    Refer to Computer and Location docs to find specific details on formatting.
    Only reads from .csv files, with fieldnames, altho partial fieldnames can be handled.

    """

    def read_Computers(cmpfile):
        """File-reader for Computer .csv files. Returns list of Computers."""
        with open(cmpfile, 'rt') as csvfile:
            computers = []
            compreader = csv.DictReader(csvfile, delimiter=',')
            for comp in compreader:
                compIP = ""
                if "IP" in compreader.fieldnames:
                    # specified IP
                    compIP = comp["IP"]
                if "Domain" in compreader.fieldnames:
                    # specified domain name
                    computers.append(LocationAssociation.Computer.Computer(comp['Device Name'], compIP, comp['Domain']))
                else:
                    # unspecified
                    computers.append(
                        LocationAssociation.Computer.Computer(comp['Device Name'], compIP))
            return computers

    def read_Locations(locfile):
        """File-reader for Location .csv files. Returns a list of Locations."""
        with open(locfile, 'rt') as csvfile:
            locations = []
            locreader = csv.DictReader(csvfile, delimiter=',')
            try:
                for loc in locreader:
                    if "IP" in locreader.fieldnames:
                        
                        locations.append(LocationAssociation.Location.Location(loc["Name"],
                                                  loc["Prefixes"], loc["IP"]))
                    else:
                        locations.append(LocationAssociation.Location.Location(loc["Name"], loc["Prefixes"]))
                return locations
            except KeyError:
                print("The supplied file was improperly formatted." +
                "Check that 'Device Name' and 'Prefixes' field names "
                +"are present.")
            finally:
                return locations

    def write_Computers(cmplist, destination):
        """File-writer for located comps (Name,IP,Domain,Location)"""
        with open(destination, 'wt') as csvfile:
            writer = csv.DictWriter(csvfile,
                                ["Device Name", "IP", "Domain", "Location"])
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
                row["Location"] = comp.location
                writer.writerow(row)
                

    def writeLog(name, locFile, locLoc, unlocFile, unlocLoc, logFolder):
        """Writes relevant information from a report to a log file.
        
        date: The date and time the report was written
        name: the name of the file that was processed.
        locFile: name of the file representing newly located computers
        locLoc: location of that file
        unlocFile: name of the file representing still unlocated computers
        unlocLoc: location of that file
        logFolder: where to write the log file
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
            logfile.write("File generated at " + str(datetime.datetime.now()))
