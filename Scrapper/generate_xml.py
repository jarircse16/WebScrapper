def generate_xml_sitemap(links):
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for link in links:
        xml_content += f'\t<url>\n\t\t<loc>{link.strip()}</loc>\n\t</url>\n'

    xml_content += '</urlset>'
    
    return xml_content

def main():
    errors = []

    try:
        with open('linked.txt', 'r') as file:
            links = file.readlines()
    except FileNotFoundError as e:
        errors.append(f"Error: File 'links.txt' not found: {e}")

    if not links:
        errors.append("Error: No links found in 'links.txt'.")
    else:
        try:
            xml_content = generate_xml_sitemap(links)
        except Exception as e:
            errors.append(f"Error occurred while generating XML sitemap: {e}")
        else:
            try:
                with open('sitemap.xml', 'w') as file:
                    file.write(xml_content)
            except Exception as e:
                errors.append(f"Error occurred while writing to 'sitemap.xml': {e}")

    if errors:
        for error in errors:
            print(error)
    else:
        print("XML sitemap generated successfully.")

if __name__ == "__main__":
    main()
