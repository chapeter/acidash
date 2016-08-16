__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import sys
import creds


def getHealthColor(item):
    if item > 90:
        item_color = '#52b918'
    elif item < 80:
        item_color = 'red'
    else:
        item_color = 'yellow'
    return item_color

import acitoolkit as ACI

def getHealth():
    #Define Session credentials.  This is pulled from creds.py
    session = ACI.Session(creds.apicurl, creds.apicuser, creds.apicpass)

    #Login, with some error checking
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    #Aquire the Tenant ojbect.  We are using the get_deep method to
    # aquire more information about the tenant
    tenant = ACI.Tenant.get_deep(session, names=['acme-prod'])[0]

    ##At this time the Uni objects don't seem to have a DN attribute
    ##We need to fixup our own, will be used soon
    tenant.dn = 'uni/tn-acme-prod'

    ##Here we are going to get all the applications in the tenant
    ##We could have also obtained this by looking at our tenant's children
    apps = ACI.AppProfile.get(session, tenant)

    ##For each application in the tenant we need to do some things
    for app in apps:
        ##Here we are doing the same DNS Fixup
        app.dn = tenant.dn + "/ap-%s" % (app.name)
        ##
        ##Here is where we are going to aquire the healthscore of the app
        ##The HealthScore Class's methods NEED the DN of the object
        ##Which is why we are doing all the DN fixup
        ##
        app.health = ACI.HealthScore.get_by_dn(session, app.dn)

        ##Here we are getting the color we are matching up against the health score
        app.bgcolor = getHealthColor(app.health)

        ##Below we are doing the same for EPGS in App, as we did Apps in Tenants
        epgs = ACI.EPG.get(session, parent=app, tenant=tenant)
        for epg in epgs:
            epg.dn = app.dn + "/epg-%s" % (epg.name)
            epg.health = ACI.HealthScore.get_by_dn(session, epg.dn)
            epg.bgcolor = getHealthColor(epg.health)


    ##We are going to return the apps object.  We could trim out a lot of info, but what we are needing
    ##is object.name, object.health, and object.bgcolor to create the tables we see
    return apps