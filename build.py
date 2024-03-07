import chevron
import datetime
import email.utils
import glob 
import json
import os 

base_url = 'https://soosoo.tech/'
base_dir = './'
data_file = 'data.json'
partials_dir = '_partials'

urls = [];
for source_filename in glob.glob('**/index.mustache', root_dir=base_dir, recursive=True):
    data_file = open('data.json', 'r')
    data = json.load(data_file)
    output_filename = os.path.splitext(source_filename)[0] + '.html';
    output_file = open(output_filename, 'w')
    print(f'convert {source_filename} -> {output_filename}')
    source_file = open(source_filename, 'r')
    output_file.write(chevron.render(source_file, data, partials_path=partials_dir))
    source_file.close()
    output_file.close()
    loc = base_url + output_filename.replace('index.html', '')
    lastmod = os.path.getmtime(source_filename)
    urls.append({ 'loc': loc, 'lastmod': lastmod })

def iso8601(text, render):
  tstamp = float(render(text))
  return datetime.datetime.fromtimestamp(tstamp).isoformat(timespec='seconds') + 'Z'

def rfc822(text, render):
  tstamp = float(render(text))
  return email.utils.format_datetime(datetime.datetime.fromtimestamp(tstamp))

print(f'generate sitemap...')
f1 = open('sitemap.mustache', 'r')
f2 = open('sitemap.xml', 'w');
f2.write(chevron.render(f1, { 'urls': urls, 'datetime': iso8601 }, partials_path=partials_dir))
f1.close()
f2.close()

f1 = open('atom.mustache', 'r')
f2 = open('atom.xml', 'w');
f2.write(chevron.render(f1, { 'urls': urls, 'datetime': iso8601 }, partials_path=partials_dir))
f1.close()
f2.close()

f1 = open('rss.mustache', 'r')
f2 = open('rss.xml', 'w');
f2.write(chevron.render(f1, { 'urls': urls, 'datetime': rfc822 }, partials_path=partials_dir))
f1.close()
f2.close()
