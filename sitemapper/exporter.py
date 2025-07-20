def export_to_xml(sitemap_list, filename="sitemap.xml"):
    with open(filename, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap_list:
            f.write("  <url>\n")
            f.write(f"    <loc>{url}</loc>\n")
            f.write("  </url>\n")
        f.write('</urlset>\n')

