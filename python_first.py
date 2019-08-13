{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my first python program\n"
     ]
    }
   ],
   "source": [
    "print(\"my first python program\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this minute seems a little odd\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime \n",
    "\n",
    "odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]\n",
    "\n",
    "right_this_minute= datetime.today().minute\n",
    "\n",
    "if right_this_minute in odds :\n",
    "    print(\"this minute seems a little odd\")\n",
    "else: \n",
    "    print(\"not an odd minute\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(\"1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "from os import getcwd\n",
    "\n",
    "where_am_i = getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'win32'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import sys\n",
    ">>> sys.platform"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(\"2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> 2+5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.7.3 (default, Apr 24 2019, 13:20:13) [MSC v.1915 32 bit (Intel)]\n"
     ]
    }
   ],
   "source": [
    ">>> print(sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\VARUN'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import os\n",
    ">>> os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "environ{'ALLUSERSPROFILE': 'C:\\\\ProgramData',\n",
       "        'APPDATA': 'C:\\\\Users\\\\VARUN\\\\AppData\\\\Roaming',\n",
       "        'COMMONPROGRAMFILES': 'C:\\\\Program Files (x86)\\\\Common Files',\n",
       "        'COMMONPROGRAMFILES(X86)': 'C:\\\\Program Files (x86)\\\\Common Files',\n",
       "        'COMMONPROGRAMW6432': 'C:\\\\Program Files\\\\Common Files',\n",
       "        'COMPUTERNAME': 'DESKTOP-CK20SOL',\n",
       "        'COMSPEC': 'C:\\\\Windows\\\\system32\\\\cmd.exe',\n",
       "        'CONDA_DEFAULT_ENV': 'base',\n",
       "        'CONDA_EXE': 'C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Scripts\\\\conda.exe',\n",
       "        'CONDA_PROMPT_MODIFIER': '(base) ',\n",
       "        'CONDA_PYTHON_EXE': 'C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\python.exe',\n",
       "        'CONDA_ROOT': 'C:\\\\Users\\\\VARUN\\\\Anaconda3',\n",
       "        'CONDA_SHLVL': '1',\n",
       "        'DRIVERDATA': 'C:\\\\Windows\\\\System32\\\\Drivers\\\\DriverData',\n",
       "        'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer',\n",
       "        'FPS_BROWSER_USER_PROFILE_STRING': 'Default',\n",
       "        'HOMEDRIVE': 'C:',\n",
       "        'HOMEPATH': '\\\\Users\\\\VARUN',\n",
       "        'LOCALAPPDATA': 'C:\\\\Users\\\\VARUN\\\\AppData\\\\Local',\n",
       "        'LOGONSERVER': '\\\\\\\\DESKTOP-CK20SOL',\n",
       "        'NUMBER_OF_PROCESSORS': '4',\n",
       "        'ONEDRIVE': 'C:\\\\Users\\\\VARUN\\\\OneDrive',\n",
       "        'OS': 'Windows_NT',\n",
       "        'PATH': 'C:\\\\Users\\\\VARUN\\\\Anaconda3;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\mingw-w64\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\usr\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Scripts;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\condabin;C:\\\\Users\\\\VARUN\\\\Anaconda3;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\mingw-w64\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\usr\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Library\\\\bin;C:\\\\Users\\\\VARUN\\\\Anaconda3\\\\Scripts;C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0;C:\\\\Windows\\\\System32\\\\OpenSSH;C:\\\\Users\\\\VARUN\\\\AppData\\\\Local\\\\Microsoft\\\\WindowsApps;.;C:\\\\Users\\\\VARUN\\\\AppData\\\\Local\\\\Programs\\\\Microsoft VS Code\\\\bin',\n",
       "        'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',\n",
       "        'PROCESSOR_ARCHITECTURE': 'x86',\n",
       "        'PROCESSOR_ARCHITEW6432': 'AMD64',\n",
       "        'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 78 Stepping 3, GenuineIntel',\n",
       "        'PROCESSOR_LEVEL': '6',\n",
       "        'PROCESSOR_REVISION': '4e03',\n",
       "        'PROGRAMDATA': 'C:\\\\ProgramData',\n",
       "        'PROGRAMFILES': 'C:\\\\Program Files (x86)',\n",
       "        'PROGRAMFILES(X86)': 'C:\\\\Program Files (x86)',\n",
       "        'PROGRAMW6432': 'C:\\\\Program Files',\n",
       "        'PROMPT': '(base) $P$G',\n",
       "        'PSMODULEPATH': 'C:\\\\Program Files\\\\WindowsPowerShell\\\\Modules;C:\\\\Windows\\\\system32\\\\WindowsPowerShell\\\\v1.0\\\\Modules',\n",
       "        'PUBLIC': 'C:\\\\Users\\\\Public',\n",
       "        'SESSIONNAME': 'Console',\n",
       "        'SYSTEMDRIVE': 'C:',\n",
       "        'SYSTEMROOT': 'C:\\\\Windows',\n",
       "        'TEMP': 'C:\\\\Users\\\\VARUN\\\\AppData\\\\Local\\\\Temp',\n",
       "        'TMP': 'C:\\\\Users\\\\VARUN\\\\AppData\\\\Local\\\\Temp',\n",
       "        'USERDOMAIN': 'DESKTOP-CK20SOL',\n",
       "        'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-CK20SOL',\n",
       "        'USERNAME': 'VARUN',\n",
       "        'USERPROFILE': 'C:\\\\Users\\\\VARUN',\n",
       "        'WINDIR': 'C:\\\\Windows',\n",
       "        'CONDA_PREFIX': 'C:\\\\Users\\\\VARUN\\\\Anaconda3',\n",
       "        'KERNEL_LAUNCH_TIMEOUT': '40',\n",
       "        'JPY_INTERRUPT_EVENT': '2368',\n",
       "        'IPY_INTERRUPT_EVENT': '2368',\n",
       "        'JPY_PARENT_PID': '2384',\n",
       "        'TERM': 'xterm-color',\n",
       "        'CLICOLOR': '1',\n",
       "        'PAGER': 'cat',\n",
       "        'GIT_PAGER': 'cat',\n",
       "        'MPLBACKEND': 'module://ipykernel.pylab.backend_inline'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import os \n",
    ">>> os.environ"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    ">>> import os\n",
    ">>> os.getenv('HOME')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import datetime\n",
    ">>> datetime.date.today()\n",
    ">>> datetime.date.today().day"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2019-08-13'"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import datetime\n",
    ">>> datetime.date.isoformat(datetime.date.today())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'16 : 51'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import time\n",
    ">>> time.strftime(\"%H : %M\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Tuesday PM'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import time\n",
    ">>> time.strftime(\"%A %p\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This html fragment contains a &lt;script&gt;script&lt;/script&gt; tag.'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import html\n",
    ">>> html.escape(\"This html fragment contains a <script>script</script> tag.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'I ♥ python,s <standard library>.'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    ">>> import html\n",
    ">>> html.unescape(\"I &hearts; python,s &lt;standard library&gt;.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
