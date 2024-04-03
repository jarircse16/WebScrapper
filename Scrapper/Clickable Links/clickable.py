def generate_xml_sitemap(links):
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for link in links:
        xml_content += f'\t<url>\n\t\t<loc>{link.strip()}</loc>\n\t</url>\n'

    xml_content += '</urlset>'
    
    return xml_content

def main():
    with open('links.txt', 'r') as file:
        links = file.readlines()

    xml_content = generate_xml_sitemap(links)

    # Replace the <loc> tags with clickable links
    for link in links:
        xml_content = xml_content.replace(
            f'<loc>{link.strip()}</loc>',
            f'<loc><a href="{link.strip()}">{link.strip()}</a></loc>'
        )

    with open('sitemap.xml', 'w') as file:
        file.write(xml_content)

if __name__ == "__main__":
    main()
