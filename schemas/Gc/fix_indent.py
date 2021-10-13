import glob
import json

for s in glob.glob('./*/*.schema.json'):
    schema_obj = json.loads(open(s).read())
    #key = list(schema_obj['definitions'])[0]
    #def_obj = schema_obj['definitions'][key]
    #if 'required' in def_obj:
    #    del def_obj['required']
    #schema_obj['definitions'][key] = def_obj
    open(s,'w').write(json.dumps(schema_obj,indent=4))