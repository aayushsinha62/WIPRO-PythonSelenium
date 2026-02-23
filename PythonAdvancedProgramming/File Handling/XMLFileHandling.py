# import xml.etree.ElementTree as ET
#
# #read xml file
#
# tree=ET.parse("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//employee.xml")
# root=tree.getroot()
#
# print(root.tag)
#
# #get first child node/tag
#
# print(root[0].tag)
# print(root[1].tag)
#
#
# #get attributes of the child node
#
# print(root[0].attrib)
#
# #fetch all the attributes in the child node
#
# for employee in root.findall("employee"):
#     emp_id=employee.get("id")
#     print(emp_id)
#
# for emp in root.findall("employee"):
#     name=emp.find("name").text
#     role=emp.find("role").text
#     exp=emp.find("experience").text
#     print(emp_name)
#
# #root to child nodes to attributes of child nodes to text of attributes
#
# #write the data to xml file
#
# #create the child nodes
#
#
# tree=ET.parse("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//employee.xml")
#
# #create the root element
#
# root=ET.element("employees")
#
# #create the child elements
#
# emp1=ET.SubElement(root, "employee", id="101")
# ET.SubElement(emp2,"name").text=
#
# encoding="utf-8", xml_declaration=True)
#
# #updating the xml
#
# tree.ET.parse("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//update.xml")
# root=tree.getroot()
#
# for emp in root.findall("employee"):
#     if emp.get("id")=="101":
#         emp.find("experience").text="16"
#
# tree.write("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//update.xml", encoding="utf-8",xml_declaration=True)
#
#
#
#
#

# import xml.etree.ElementTree as ET
# #read XML file and parse to a variable tree
# tree=ET.parse(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\employee.xml")
# root=tree.getroot() #get the root element
# print(root.tag)
# #get the first child node/tag
# print(root[0].tag)
# print(root[1].tag)
# #get the attributes of the child node
# print(root[0].attrib)
# print(root[1].attrib)
#
# #fetch all the attributes in child node
# for employee in root.findall(("employee")):
#     emp_id=employee.get("id")
#     print(emp_id)
#     emp_name=employee.get("name")
#     print(emp_name)
#
# #fetch xml tag values
# #first_emp=root.find("employee id")
# #print(first_emp.find("name".text))
# for emp in root.findall(("employee")):
#     name=emp.find("name").text
#     role=emp.find("role").text
#     exp=emp.find("experience").text
#     print(name,role,exp)
#
# #writing the data to xml file
# #create the child nodes
#
# #create child elements
# emp1=ET.SubElement(root,"employee",id="101")
# ET.SubElement(emp1, "name").text="harsha"
# ET.SubElement(emp1, "role").text="tester"
# ET.SubElement(emp1, "experience").text="5"
#
# emp2=ET.SubElement(root,"employee",id="102")
# ET.SubElement(emp2, "name").text="amit"
# ET.SubElement(emp2, "role").text="dev"
# ET.SubElement(emp2, "experience").text="3"
# #write to file
# tree=ET.ElementTree(root)
# tree.write(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\writexml.xml",encoding="utf-8", xml_declaration=True)
#
# #updating the xml
# tree=ET.parse(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\updatexml.xml")
# root=tree.getroot()
# for emp in root.findall("employee"):
#     if emp.get("id")=="101":
#         emp.find("experience").text ="16"
# tree.write(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\updatexml.xml",encoding="utf-8", xml_declaration=True)