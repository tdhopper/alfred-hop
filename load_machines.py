from workflow import Workflow
import json
import os.path as path


def get_machines():
    with open(path.join(path.expanduser("~"), ".hop.json.db"), "r") as f:
        d = json.load(f)
    return d.iteritems()


if __name__ == u"__main__":
    wf = Workflow()
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    machines = get_machines()
    if query:
        machines = wf.filter(query, machines, key=lambda x: " ".join(x))
    for shortcut, machine in machines:
        if machine.startswith('$server$'):
            machine = machine.split("$")[2]
            wf.add_item("%s - %s" % (shortcut, machine), arg="ssh %s" % machine, valid=True)
        else:
            wf.add_item("%s - %s" % (shortcut, machine), arg="cd %s" % machine, valid=True)
    wf.send_feedback()
