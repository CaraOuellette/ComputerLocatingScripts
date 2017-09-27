class Location:
    """A place in the world where there may have been given a computer.
    
    DOMAIN -- a dictionary mapping Domain names to Regions
    REGION -- a dictionary mapping Region names to Site names
    SITE -- a dictionary mapping Site names to specific Location objects
    format_prefixes --Changes a string into a list of strings.
    format_IP -- A method that changes a string in a list of integers.
    format_dicts -  Creates a "tree" (linked dictionaries) of location levels.
    """
    
    DOMAIN = {}
    # a dictionary mapping Domain names to Regions
    REGION = {}
    # a dictionary mapping Region names to Site names
    SITE = {}
    # a dictionary mapping Site names to specific Location objects

    def __init__(self, domain, region, site, name = "", prefixes = [], IP = ""):
        """Creates a new instance of the Location class.

        domain -- the highest level of locational organization
        region -- a high level of locational organization
        site -- the basic level of locational organization
        name -- a more specific location among sites
        prefixes -- A String corresponding to computer naming conventions.
        IP - a String corresponding to an IP address. Not IPv6 sensitive.

        Returns a Location object."""
        self.domain = domain
        self.region = region
        self. site = site
        self.name = name
        self.prefixes = self.format_prefixes(prefixes)
        self.IP = self.format_IP(IP)
        #If this location has other representations, document that
        #possible antiquated, based on mistaken conception of IP checking
        self.format_dicts(domain, region, site)

    def format_prefixes(self, prefixString):
        """Breaks up a string of prefixes into a list, comma delimited."""
        if not prefixString == "":
            lst = prefixString.split(",")
            return lst
        return []

    def format_IP(self, IP):
        """Breaks up a string of an IP into a list of 4 integers, period delimited."""
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

        def format_dicts(self, domain, region, site):
            """Creates a "tree" (linked dictionaries) to help index locations.
            
            First the location object is added to the SITE dictionary. If no
            key exists for the given site, then one is created. Next, the
            REGION dictionary is checked for the region parameter. If it is 
            present, then that list is checked for the site parameter. If this
            is not present, then it is added. If the region is not present, it
            is added along with the site as a one item list. The same step is 
            then repeated at the domain level.
            """
            if site in location.SITE:
                location.SITE[site].append(self)
            else:
                location.SITE[site] = [self]
            if region in location.REGION:
                if site not in location.REGION[region]:
                    location.REGION[region].append(site)
            else:
                location.REGION[region] = [site]
            if domain in location.DOMAIN:
                if region not in location.DOMAIN[domain]:
                    location.DOMAIN[domain].append(region)
            else:
                location.DOMAIN[domain] = [region]
