import subprocess
from pastebin_python import PastebinPython
from pastebin_python.pastebin_formats import FORMAT_NONE
from pastebin_python.pastebin_constants import PASTE_PRIVATE, EXPIRE_NEVER

process = subprocess.Popen(["smartctl", "-a", "/dev/sdb"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out1, err1 = process.communicate()

process = subprocess.Popen(["smartctl", "-a", "/dev/sdc"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out2, err2 = process.communicate()

pbin = PastebinPython(api_dev_key="037932354285225f0776a6ac71d04635")
output = out1 + "\n\n" + out2

try:
    print pbin.createAPIUserKey("n1c0la84", "6g0HDKm0")
    print pbin.createPaste(output, "SMART DISKS TEST", FORMAT_NONE, PASTE_PRIVATE, EXPIRE_NEVER)
except Exception as e:
    print e