class Location:
    """A place in the world where Apotex employees may have been given a computer.
    """
    # A dictionary mapping Location names to the number of duplicate names
    instances = {}

    def __init__(self, name, prefixes, IP):
        """Creates a new instance of the Location class.

        name: a String representing a real-world location
        prefixes: a list of strings corresponding to naming conventionS.
        IP: a list of 4 integers corresponding to an IP address's four octets.
        If IPv6 used, list is empty.

        Returns a Location object."""
        self.name = name
        self.prefixes = self.formatPrefixes(prefixes)
        if len(prefixes) < 1:
            self.hasPrefixes = False
        else:
            self.hasPrefixes = True
        self.IP = self.formatIP(IP)
        if self.name in Location.instances.keys():
            self.instance = len(Location.instances[self.name]) + 1
            Location.instances[self.name].append(self)
        else:
            self.instance = 1
            Location.instances[self.name] = [self]

    def formatPrefixes(self, prefixString):
        """breaks up a string of prefixes into a list separated by commas"""
        if not prefixString == "":
            lst = prefixString.split(",")
            return lst
        return []

    def formatIP(self, IP):
        """breaks up a string of an IP into a list of 4 integers"""
        if "." in IP:
            finIP = IP.split(".")
            if len(finIP) < 4:
                return [0, 0, 0, 0]
            elif len(finIP) > 4:
                return finIP[0:3]
            else:
                realIP = []
                for item in finIP:
                    realIP.append(int(item))
                return realIP
        else:
            return [0, 0, 0, 0]
