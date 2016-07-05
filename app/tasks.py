__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import acitoolkit as ACI
import sys


apicurl = 'http://10.94.238.68'
apicuser = 'admin'
apicpass = 'cisco123'

def getHealth():
    session = ACI.Session(apicurl, apicuser, apicpass)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        sys.exit(0)

    tenant = "ACME Prod Network"
    tenant_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod')
    #print tenant, tenant_health
    if tenant_health > 90:
        tenant_bgcolor = 'green'
    elif tenant_health < 80:
        tenant_bgcolor = 'red'
    else:
        tenant_bgcolor = 'yellow'

    application = "People Soft Financial"
    application_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin')
    #print application, application_health
    if application_health > 90:
        app_bgcolor = 'green'
    elif application_health < 80:
        app_bgcolor = 'red'
    else:
        app_bgcolor = 'yellow'

    epg1 = "Web Front End"
    epg2 = "Middleware"
    epg3 = "Database"

    epg1_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-web')
    epg2_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-app')
    epg3_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-db')

    if epg1_health > 90:
        epg1_bgcolor = 'green'
    elif epg1_health < 80:
        epg1_bgcolor = 'red'
    else:
        epg1_bgcolor = 'yellow'

    if epg2_health > 90:
        epg2_bgcolor = 'green'
    elif epg2_health < 80:
        epg2_bgcolor = 'red'
    else:
        epg2_bgcolor = 'yellow'

    if epg3_health > 90:
        epg3_bgcolor = 'green'
    elif epg3_health < 80:
        epg3_bgcolor = 'red'
    else:
        epg3_bgcolor = 'yellow'

    #print epg1, epg1_health
    #print epg2, epg2_health
    #print epg3, epg3_health

    data = [{'name' : tenant, 'health' : tenant_health, 'bgcolor' : tenant_bgcolor},
            {'name' : application, 'health' : application_health, 'bgcolor' : app_bgcolor},
            {'name' : epg1, 'health' : epg1_health, 'bgcolor' : epg1_bgcolor},
            {'name' : epg2, 'health' : epg2_health, 'bgcolor' : epg2_bgcolor},
            {'name' : epg3, 'health' : epg3_health, 'bgcolor' : epg3_bgcolor}]
    return data