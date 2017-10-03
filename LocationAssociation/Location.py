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

    def __init__(self, domain, region, site, name = "", prefixes = "", IP = ""):
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
        self.site = site
        self.name = name
        self.prefixes = self.format_prefixes(prefixes)
        self.IP = self.format_IP(IP)
        self.format_dicts(domain, region, site)

    def format_prefixes(self, prefixString):
        """Breaks up a string of prefixes into a list, comma delimited."""
        if not prefixString == "" and prefixString is not None:
            xyz = prefixString.split(",")
            return xyz
        return []

    def format_IP(self, IP):
        """Breaks up a string of an IP into a list of 4 integers, period delimited."""
        if not IP == "" and IP is not None:
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
        if site in Location.SITE:
            Location.SITE[site].append(self)
        else:
            Location.SITE[site] = [self]
        if region in Location.REGION:
            if site not in Location.REGION[region]:
                Location.REGION[region].append(site)
        else:
            Location.REGION[region] = [site]
        if domain in Location.DOMAIN:
            if region not in Location.DOMAIN[domain]:
                Location.DOMAIN[domain].append(region)
        else:
            Location.DOMAIN[domain] = [region]
        return True