import re

def clean_script(script):

    # remove hashtags
    script = re.sub(r"#.*", "", script)

    # remove extra symbols
    script = re.sub(r"\[.*?\]", "", script)

    # remove multiple spaces
    script = re.sub(r"\s+", " ", script)

    return script.strip()
