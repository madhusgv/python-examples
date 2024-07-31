import configparser

NSMF_SECURITY_INI_LOC = "C:\GIT\github\madhusgv\python-examples\python-examples\Programs\security.ini"

def validate_security_rules() -> None:
    # validate the integrity of INI file first by simply reading it!
    print("get parser object to read ini file")
    c = configparser.ConfigParser(allow_no_value = True)
    c.optionxform = str
    print("read ini file")
    if not c.read(NSMF_SECURITY_INI_LOC):
        print(f"{NSMF_SECURITY_INI_LOC} is corrupt")
        return
    print("check operation header in ini file")
    if not c.has_section('OPERATION_ALIAS'):
        print(f"OPERATION_ALIAS section not found in {NSMF_SECURITY_INI_LOC}")
        return
    print("check global header in ini file")
    if not c.has_section('GLOBAL'):
        print(f"GLOBAL section not found in {NSMF_SECURITY_INI_LOC}")
        return

    output_dict={s:dict(c.items(s)) for s in c.sections()}
    print(f'output_dict : {output_dict}')
    oa=output_dict['OPERATION_ALIAS']
    print(f'oa : {oa}')

    del output_dict['OPERATION_ALIAS']
    del output_dict['GLOBAL']
    print(f'output_dict after del: {output_dict}')

    for i, (key, value) in enumerate(output_dict.items()):
        print(f'i, key,value  : {i}, {key} , {value}')
        for k, v in output_dict[key].items():
            print(f'i k,v  : {i}, {k} , {v}')
            v1=v.split(",")
            import re
            pattern = re.compile(r'\s*\b(GET|PUT|POST|DELETE)\b|\b(GET|PUT|POST\DELETE)\b\s*')
            res = list(filter(None, [pattern.sub("", s) for s in v1]))
            print(f' res: {res}')
            if res:
                for r in res:
                    if not r in oa:
                        print(f"OPERATION_ALIAS section {r} not found {NSMF_SECURITY_INI_LOC}")
                        return False
    print(f"{NSMF_SECURITY_INI_LOC} validate is successfull.\n")
    return True


def _resource_is_dynamic(resourcename) -> bool:
    return '{' in resourcename

def _match_dynamic_resource(resource, dynamic_expression) -> bool:
    tmp_dynamic_expr_list = dynamic_expression.split('/')
    tmp_resource_list = resource.split('/')

    dynamic_expr_elements = []

    for i in enumerate(tmp_dynamic_expr_list):
        if '{' in i[1]:
            dynamic_expr_elements.append(i[0])

    for i in dynamic_expr_elements:
        tmp_dynamic_expr_list[i] = tmp_resource_list[i]

    tmp_dynamic_expr = '/'.join(tmp_dynamic_expr_list)
    
    return tmp_dynamic_expr == resource

def _match_resource(resourcename, resourcelist) -> Tuple[bool, str]:
    parent_resource = '/'.join(resourcename.split('/')[0:3])

    resource_present = False
    matched_resource = None

    for i in filter(lambda x: x.startswith(parent_resource), resourcelist):
        if _resource_is_dynamic(i):
            resource_present = _match_dynamic_resource(resourcename, i)
        else:
            if resourcename == i:
                resource_present = True

        if resource_present:
            matched_resource = i
            break
    
    return (resource_present, matched_resource)

def _permission_expand(permissions, aliases):
    expanded_permissions = []

    permissions = permissions.split(',')

    def _tmpfunc(x):
        y = x[0].split(',')
        z = x[1].split(',')

        y = [t.strip() for t in y]
        z = [t.strip() for t in z]

        return (y, z)

    aliases = [_tmpfunc(x) for x in aliases]

    for i in permissions:
        for j in aliases:
            if i in j[0]:
                expanded_permissions += j[1]
                break
            elif i in ('PUT', 'GET', 'DELETE', 'POST'):
                expanded_permissions += [i]
                break
            else:
                continue
    
    return list(set(expanded_permissions))


def authorize_request(resource: str, user: str, user_details) -> bool:
    c = configparser.ConfigParser()
    c.optionxform = str
    c.read(NSMF_SECURITY_INI_LOC)

    resources = c.sections()
    resources.remove('OPERATION_ALIAS')
    resources.remove('GLOBAL')

    aliases = c.items('OPERATION_ALIAS')

    user_authorized = False
    resource_present, matched_resource = _match_resource(resource, resources)

    
    if resource_present:
       resource_configuration = c.items(matched_resource)

       for user_entry, _permissions in resource_configuration:
            user_entry_list = [x.strip() for x in user_entry.split(',')]
            permissions = _permission_expand(_permissions, aliases)

            permissions = [x.upper() for x in permissions]

            print(f"user = {user}")
            print(f"user_entry_list = {user_entry_list}")
            print(f"user_details = {user_details.upper()}")
            print(f"permissions = {permissions}")

            if user in user_entry_list and user_details.upper() in permissions:
               user_authorized = True
               break
    return user_authorized


ret = validate_security_rules()
print(ret)

ret = authorize_request()