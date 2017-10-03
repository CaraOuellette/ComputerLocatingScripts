class Computer:
    """An abstract represntation of a computer, emphasizing relevant attributes.
    
    format_IP -- Returns a list of ints from a string representing an IP address (not IPv6.)
    """

    def __init__(self, name, IP):
        """Returns a Computer object."""
        self.name = name.upper()
        self.IP = self.formatIP(IP)
        self.domain = ""
        self.region = ""
        # general
        self.site = ""
        #more specific
        self.site2 = ""
        #anticipating future requirements
        """self.user = ""
        self.model = ""
        self.cluster = ""
        self.hub = ""
        self.CPUs = ""
        self.cores = """""

    def formatIP(self, IP):
        """Returns a list of ints from a string representation of an IP address.
        IPv6 is not supported, and will be returned as [0,0,0,0].
        """
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
