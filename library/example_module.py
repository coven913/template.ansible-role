#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['stableinterface'],
    'supported_by': '<author name>'
}

DOCUMENTATION = '''
---
module: < module name >

short_description: < module description >

options: # specify all available options for the module
    state:
        required: # bool
        default: "< default val >"
        choices: [ "present", "absent" ] # limit input to predefined values
        description:
            - < description >

author:
    - < author name >
'''

EXAMPLES = '''
# provide examples for how to use this module in tasks
'''

RETURN = '''
field:
    description:
        - < field description >
    returned: < describe the conditions under which this field is returned >
    type: < data type of the fields value >
    sample: < provide a sample of the returned field in JSON format >
'''

if __name__ == '__main__':
    main()
