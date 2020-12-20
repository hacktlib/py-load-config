import re


def extract_sam_config_parameter_overrides(parameter_overrides):
    extracted = {}

    parameter_pattern = '(?P<key>[A-Za-z]{1,})=\\\"(?P<val>[^\\\"]*)'

    matches = re.findall(pattern=parameter_pattern, string=parameter_overrides)

    for match in matches:
        extracted[match[0]] = match[1]

    return extracted
