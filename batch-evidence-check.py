import base64
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
root = Path(__file__).parent
sha = '08954c0366c1dd5aa5bce50a68725498addb9a15'
def run(*args):
    return subprocess.check_output(args, cwd=root)
manifest = json.loads((root/'.worktrees/t_7ebc3588/dashboard/qa/pr3-reviewed/source-manifest.json').read_text())['sha256']
bad = [name for name, digest in manifest.items() if hashlib.sha256(run('git','show',f'{sha}:{name}')).hexdigest() != digest]
print('Committed source manifest:', len(manifest), 'entries;', 'mismatches:', bad)
r = json.loads((root/'.worktrees/t_07a4ef3c-verify/dashboard/qa/layout-corrections/after/results.json').read_text())
print('Saved matrix keys:', list(r))
for key,value in r.items():
    if isinstance(value,list):
        print('Saved matrix',key,'count',len(value))
        if value and isinstance(value[0],dict): print('First item keys', list(value[0]))
pr = json.loads(run('gh','api','repos/hosakb/bachelor-thesis/pulls/3'))
print('Remote PR3',pr['state'],pr['draft'],pr['head']['sha'],pr['base']['ref'])
print('Saved matrix case distribution', dict(Counter(case['viewport'] if isinstance(case['viewport'],str) else case['viewport']['name'] for case in r['cases'])))
print('Saved matrix nonempty defects', sum(bool(case['defects']) for case in r['cases']))
print('Saved matrix nonempty problems', sum(bool(case['problems']) for case in r['cases']))
report=(root/'.worktrees/t_7ebc3588/dashboard/qa/pr3-reviewed/REPORT.txt').read_text()
print('Historical comprehensive-cycle evidence:')
for line in report.splitlines():
    if any(term in line.lower() for term in ['159', 'matrix', 'run1', 'run2', 'run3', 'independent', 'approval']): print(line)
assets = ['dashboard/qa/pr3-reviewed/images/pairs/after/login-mobile.png','dashboard/qa/pr3-reviewed/images/pairs/after/startup-gantt-year-desktop.png','dashboard/qa/pr3-reviewed/images/pairs/after/fund-detail-nav-toggle-mobile.png']
for path in assets:
    remote=json.loads(run('gh','api',f'repos/hosakb/bachelor-thesis/contents/{path}?ref={sha}'))
    data=base64.b64decode(remote['content'])
    print('Remote asset',path,'PNG',data.startswith(b'\x89PNG\r\n\x1a\n'),'matches commit',data==run('git','show',f'{sha}:{path}'))
print('ERP local branch',run('git','branch','--list','*erp*').decode().strip() or 'none')
print('ERP remote branch',run('git','ls-remote','--heads','origin','*erp*').decode().strip() or 'none')
