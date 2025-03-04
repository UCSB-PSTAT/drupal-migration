import os
import requests
import subprocess
import argparse
from urllib.parse import urlparse

def get_filename_from_url(url):
    """Generate a filename from the URL path, replacing slashes with hyphens."""
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    if not path:
        return "index.md"
    return path.replace('/', '-') + ".md"

def fetch_html(url, output_dir):
    """Fetch HTML content from the given URL and handle non-HTML content."""
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' not in content_type:
            print(f"Non-HTML content detected ({content_type}), saving to {output_dir}/nonhtml/")
            save_non_html_content(url, response.content, content_type, output_dir)
            return None
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_non_html_content(url, content, content_type, output_dir):
    """Save non-HTML content to the nonhtml/ directory."""
    non_html_dir = os.path.join(output_dir, "nonhtml")
    os.makedirs(non_html_dir, exist_ok=True)
    extension = content_type.split('/')[-1]
    filename = get_filename_from_url(url).replace('.md', f'.{extension}')
    file_path = os.path.join(non_html_dir, filename)
    with open(file_path, 'wb') as file:
        file.write(content)
    print(f"Saved non-HTML content: {file_path}")

def convert_html_to_markdown(html):
    """Convert HTML content to Markdown using the html2markdown command-line tool."""
    try:
        process = subprocess.run(['html2markdown'], input=html, text=True, capture_output=True, check=True)
        return process.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error converting HTML to Markdown: {e}")
        return None

def remove_unwanted_section(markdown):
    """Remove predefined unwanted sections from the Markdown output."""
    unwanted_sections = [
        '''[Skip to main content](#main-content)

[University of California, Santa Barbara](http://www.ucsb.edu)

## Search form

Search

[![Department of Statistics and Applied Probability - UC Santa Barbara](https://www.pstat.ucsb.edu/sites/default/themes/at_lsit/images/department/pstat-banner-navy.svg)](/)

# [Department of Statistics and Applied Probability - UC Santa Barbara](/ "Home page")

## Main menu

- [About](/about "About")
- [Undergraduate](/undergrad)
- [Graduate](/graduate)
- [Courses](/courses)
- [Resources](/resources "Resources")
- [People](/people)
- [Alumni](/alumni "Undergraduate Alumni")
- [News and Events](/news)
- [Employment](/about/employment "Employment")
- [Forms](/forms "Forms")
- [Giving](/giving "Giving")''',
        '''## Join Our Listserv

**Department ListServ**

[Subscribe!](https://groups.google.com/u/1/a/pstat.ucsb.edu/g/pstat-undergrad?hl=en)''',
        '''**Department of Statistics and Applied Probability**  
UC Santa Barbara  
Santa Barbara CA 93106-3110

Campus MailCode: 3110  
[Campus Maps](http://www.aw.id.ucsb.edu/maps/)

South Hall 5607A  
Main office hours \[PST]  
Monday through Friday  
9am-12pm and 1-4pm''',
        '''- [About](/about "About")
- [Undergraduate](/undergrad)
- [Graduate](/graduate)
- [Courses](/courses)
- [Resources](/resources "Resources")
- [People](/people)
- [Alumni](/alumni "Undergraduate Alumni")
- [News and Events](/news)
- [Employment](/about/employment "Employment")
- [Forms](/forms "Forms")
- [Giving](/giving "Giving")''',
        '''<!--THE END-->

- [College of Letters and Science](http://www.college.ucsb.edu "College of Letters and Science")
- [UC Santa Barbara](http://www.ucsb.edu "UC Santa Barbara")
- [Accessibility](/accessibility "Accessibility")
- [Appropriate Use](http://www.policy.ucsb.edu/terms_of_use/ "Appropriate Use")
- [Privacy](http://www.policy.ucsb.edu/privacy-notification/ "Privacy")
- [Webmaster](mailto:help@pstat.ucsb.edu "Webmaster")''',
        '''## Support the Department

We invite you to be part of the Department’s success in educating the next generation of leaders. [More info...](/giving)

- ©2025
- The Regents of the University of California.
- All Rights Reserved.
- UC Santa Barbara, Santa Barbara, CA 93106'''
    ]
    
    updated_markdown = markdown
    removed = False
    for section in unwanted_sections:
        if section in updated_markdown:
            updated_markdown = updated_markdown.replace(section, '').strip()
            removed = True
    
    return updated_markdown, removed

def process_urls(input_file, output_dir):
    """Read URLs from a file, fetch and convert HTML to Markdown, and save processed files."""
    os.makedirs(output_dir, exist_ok=True)
    src_dir = os.path.join(output_dir, "src")
    os.makedirs(src_dir, exist_ok=True)
    failed_removals = []
    
    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    
    for url in urls:
        print(f"Processing: {url}")
        html = fetch_html(url, output_dir)
        if html:
            markdown = convert_html_to_markdown(html)
            if markdown:
                updated_markdown, removed = remove_unwanted_section(markdown)
                filename = get_filename_from_url(url)
                
                # Insert filename as first H1 header
                filename_header = f"# {filename.replace('.md', '')}\n\n"
                updated_markdown = filename_header + updated_markdown
                
                file_path = os.path.join(src_dir, filename)
                with open(file_path, 'w') as md_file:
                    md_file.write(updated_markdown)
                print(f"Saved: {file_path}")
                if not removed:
                    failed_removals.append(file_path)
    
    if failed_removals:
        print("Failed to remove unwanted sections in the following files:")
        for file in failed_removals:
            print(f"- {file}")

if __name__ == "__main__":
    """Parse command-line arguments and initiate processing."""
    parser = argparse.ArgumentParser(description="Fetch URLs, convert HTML to Markdown, and save them.")
    parser.add_argument("input_file", help="Path to the file containing URLs")
    parser.add_argument("output_dir", help="Directory to save processed Markdown and non-HTML files")
    args = parser.parse_args()
    
    process_urls(args.input_file, args.output_dir)
