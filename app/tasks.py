__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import acitoolkit as ACI
import sys
import creds


def getHealthColor(item):
    if item > 90:
        item_color = 'green'
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



    tenant = "ACME Prod Network"
    tenant_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod')
    tenant_bgcolor = getHealthColor(tenant)

    application = "People Soft Financial"
    application_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin')
    app_bgcolor = getHealthColor(application_health)

    epg1 = "Web Front End"
    epg2 = "Middleware"
    epg3 = "Database"

    epg1_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-web')
    epg2_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-app')
    epg3_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-peopleSoft-fin/epg-db')

    epg1_bgcolor = getHealthColor(epg1_health)
    epg2_bgcolor = getHealthColor(epg2_health)
    epg3_bgcolor = getHealthColor(epg3_health)

    data = []
    data.append([{'name' : application, 'health' : application_health, 'bgcolor' : app_bgcolor},
            {'name' : epg1, 'health' : epg1_health, 'bgcolor' : epg1_bgcolor},
            {'name' : epg2, 'health' : epg2_health, 'bgcolor' : epg2_bgcolor},
            {'name' : epg3, 'health' : epg3_health, 'bgcolor' : epg3_bgcolor}])


    application2 = "People Soft Dev"
    application_health2 = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-people-soft-dev')
    app2_bgcolor = getHealthColor(application_health2)


    epg4 = "Web Front End"
    epg5 = "Middleware"
    epg6 = "Database"

    epg4_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-people-soft-dev/epg-web')
    epg5_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-people-soft-dev/epg-app')
    epg6_health = ACI.HealthScore.get_by_dn(session, 'uni/tn-acme-prod/ap-people-soft-dev/epg-db')

    epg4_bgcolor = getHealthColor(epg4_health)
    epg5_bgcolor = getHealthColor(epg5_health)
    epg6_bgcolor = getHealthColor(epg6_health)

    data.append([{'name': application2, 'health': application_health2, 'bgcolor': app2_bgcolor},
                 {'name': epg4, 'health': epg4_health, 'bgcolor': epg4_bgcolor},
                 {'name': epg5, 'health': epg5_health, 'bgcolor': epg5_bgcolor},
                 {'name': epg6, 'health': epg6_health, 'bgcolor': epg6_bgcolor}])

    return data