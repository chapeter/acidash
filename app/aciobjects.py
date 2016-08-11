import acitoolkit as ACI
import sys
import creds


class Tenant(object):
    """
    Class used to describe a Tenant
    """

    def __init__(self, url, username, password, tenant):
        self.url = url
        self.username = username
        self.password = password
        self.session = ACI.Session(self.url, self.username, self.password, verify_ssl=False)
        self.session.login()
        self.tenant = ACI.Tenant(tenant)
        self.applications = self.getApplications

    @property
    def getApplications(self):
        children = ACI.Tenant(self.tenant).get_children()
        return children