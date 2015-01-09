from workflow import Workflow
import json
import os.path as path


def get_machines():
    with open(path.join(path.expanduser("~"), ".hop.json.db"), "r") as f:
        d = json.load(f)
    return [v.split("$")[2] for v in d.values() if v.startswith("$server$")]


if __name__ == u"__main__":
    wf = Workflow()
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    machines = get_machines()
    if query:
        machines = wf.filter(query, machines)
    for machine in machines:
        wf.add_item(machine, arg=machine, valid=True)
    wf.send_feedback()
