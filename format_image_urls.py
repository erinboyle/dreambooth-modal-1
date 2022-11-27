"""
Use this util to format google drive image urls to their download url:
- Highlight all and "copy all urls" from public google drive folder.
- Paste into raw_urls.txt
- Run this file
- Copy resulting urls.txt into pastebin.
"""


raw_filename = "raw_urls.txt"
output_filename = "urls.txt"


def reformat(url):
    # from https://drive.google.com/file/d/1--xmnBgJ_Oe4xZke_g1R4NujkDp3tYJ7/view?usp=sharing
    # to https://drive.google.com/uc?export=download&id=1_v10rZo7IE5WE5nz8-DOEDLMrRip0ATK
    id = url.split("/")[-2]
    return f"https://drive.google.com/uc?export=download&id={id}"


with open(raw_filename, "r") as f:
    lines = f.readlines()

raw_urls = [line.strip() for line in lines]
with open(output_filename, "w") as f:
    for raw_url in raw_urls:
        f.write(reformat(raw_url) + "\n")
