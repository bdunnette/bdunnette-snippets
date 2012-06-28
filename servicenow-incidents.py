#!/usr/bin/env python

import sys
from xml.dom.minidom import parse, parseString
from mechanize import ParseResponse, urlopen, urljoin, Browser

incident_fields = {"short_description", "priority"}

def getIncidents():
    uri = "http://umnprd.service-now.com/"
    br = Browser()
    br.set_handle_robots(False)

    response1 = br.open(uri)
    br.select_form("lform")
    br["j_username"] = sys.argv[1]
    br["j_password"] = sys.argv[2]
    br.submit()
    br.select_form(nr=0)
    br.submit()
    response3 = br.open(urljoin(uri, "incident_list.do?XML&sysparm_query=active=true^assignment_groupLIKECLA%20East%20Bank"))
    incidents_xml = str(response3.get_data())
    incidents = parseString(incidents_xml)
    return incidents
    
def handleIncidents(incident_list):
    print "<html>"
    incidents = incident_list.getElementsByTagName("incident")
    makeIncidentTable(incidents)
    print "</html>"
    
def makeIncidentTable(incidents):
    print "<table>"
    print "<tr>"
    for field_name in incident_fields:
        print "<th>%s</th>" % field_name
    print "<tr>"
    for incident in incidents:
        makeIncidentRow(incident)
    print "</table>"
    
def makeIncidentRow(incident):
    print "<tr>"
    for field_name in incident_fields:
        print "<td>%s</td>" % incident.getElementsByTagName(field_name)[0].firstChild.nodeValue
    print "</tr>"
    
handleIncidents(getIncidents())
