import xml.etree.ElementTree as ET
import arcpy

xmlfile = 'C:\Excel\Input.xml'
element_tree = ET.parse(xmlfile)
root = element_tree.getroot()
agreement = root.findall(".//agreementdetail")
result = []
elements = ('agreementid', 'agreementtype')

for a in agreement:
    obj = {}
    for e in elements:
        obj[e] = a.find(e).text
    result.append(obj)

arcpy.AddMessage(result)
