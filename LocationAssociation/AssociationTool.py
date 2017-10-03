class AssociationTool:

    def compareByIP(comp, location):
        """check whether IPs match in a sophisticated way.

        Returns a string. "" If no match found.
        comp: A Computer.
        locations: A list of locations
        """
        temploc = ""
        if not comp.IP == [0, 0, 0, 0]:
            for loc in locations:
                if comp.IP[0] == location.IP[0] and comp.IP[1] == location.IP[1]:
                    if comp.IP[2] >= location.IP[2]:
                        temploc = location.site
        return temploc

    def compareByName(name, locations):
        """Compare the 3-5 letters of Computer name to find a  location.

        Returns a string. "" if no match foumnd.
        name: String. A computer's name.
        locations: a list of Locations.
        """
        for loc in locations:
            if loc.prefixes:
                for prefix in loc.prefixes:
                    if name[0:5] == prefix:
                        return loc.site
                    elif name[0:4] == prefix:
                        return loc.site
                    elif name[0:3] == prefix:
                        return loc.site
                    elif name[0:2] == prefix:
                        return loc.site
        return ""

    """Deprecated function. Slated for removal.    
    def compareByDomain(computer, locations):
        ""Check to see what action should be taken based on  domain name.

        Returns true if a location is found, false otherwise.
        ""
        if computer.domain == "apotex.ca" or computer.domain == "APOTEX":
            computer.location = AssociationTool.compareByName(
                computer.name, locations)
            # did it get a name?
            if computer.location == "":
                computer.location = "Unknown"
                return False
        elif computer.domain == "api.apotexpharmachem.com":
            computer.location = "apotex pharmachem"
        elif computer.domain == "apodmz.net":
            computer.location = "dmz access"
        elif computer.domain == "apotex.com.in":
            computer.location = "India"
        elif computer.domain == "avevadds.local":
            computer.location = "Aveva Florida"
        elif computer.domain == "strplx.net":
            if computer.name[0:2] == "TN":
                computer.location = "Starplex Tennessee"
            else:
                computer.location = "Starplex"
        else:
            computer.location = "Unknown"
            return False
        return True
        """
