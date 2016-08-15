__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import acitoolkit as ACI
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

def getHealth():
    session = ACI.Session(creds.apicurl, creds.apicuser, creds.apicpass)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)



    tenant = ACI.Tenant.get_deep(session, names=['acme-prod'])[0]
    tenant.dn = 'uni/tn-acme-prod'

    apps = ACI.AppProfile.get(session, tenant)

    for app in apps:
        app.dn = tenant.dn + "/ap-%s" % (app.name)
        app.health = ACI.HealthScore.get_by_dn(session, app.dn)
        app.bgcolor = getHealthColor(app.health)

        epgs = ACI.EPG.get(session, parent=app, tenant=tenant)
        for epg in epgs:
            epg.dn = app.dn + "/epg-%s" % (epg.name)
            epg.health = ACI.HealthScore.get_by_dn(session, epg.dn)
            epg.bgcolor = getHealthColor(epg.health)


    return apps