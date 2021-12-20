def XMLtoYAML(xml_way, yaml_way):
    """Преобразователь из XML в YAML"""
    xml = open(str(xml_way), 'r', encoding="utf-8")
    yaml = open(str(yaml_way), 'w', encoding="utf-8")

    list_xml = xml.readlines()
    count_tab = 0

    for text in list_xml:
        line = text

        while len(line) != 0:
            if line[0] == ' ' or line[0] == '\n' or line[0] == '\t':
                line = line[1:]
            elif "</" in line[:2]:
                count_tab -= 1
                l = line.find(">")
                line = line[l + 1:]
            elif "<" in line[0]:
                f = line.find("<")
                l = line.find(">")
                yaml.write(count_tab * '\t' + line[f + 1:l] + ":" + '\n')
                line = line[l + 1:]
                count_tab += 1
            else:
                if "<" in line:
                    f = line.find("<")
                    if ":" in line[:f] or line[:f].isdigit():
                        yaml.write(count_tab * '\t' + "'" + line[:f] + "'" + '\n')
                        line = line[f:]
                    else:
                        yaml.write(count_tab * '\t' + line[:f] + '\n')
                        line = line[f:]
                else:
                    if ":" in line or line.isdigit():
                        yaml.write(count_tab * '\t' + "'" + line + "'")
                        line = line[len(line):]
                    else:
                        yaml.write(count_tab * '\t' + line)
                        line = line[len(line):]

    xml.close()
    yaml.close()


XMLtoYAML("data.xml", "data.yaml")
