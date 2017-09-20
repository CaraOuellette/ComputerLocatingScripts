class Computer:

    def __init__(self, name, IP, domain="apotex.ca"):
        self.name = name.upper()
        self.IP = self.formatIP(IP)
        self.domain = domain
        self.location = ""

    def formatIP(self, IP):
        """breaks up a string representation of an IP into list of 4 ints"""
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
