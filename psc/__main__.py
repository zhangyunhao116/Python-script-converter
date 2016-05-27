# -*- coding:utf-8 -*-
import os
import sys


class PSC:
    def __init__(self, file, version=3):
        # Get path and filename.
        self.path, self.file = os.path.split(file)
        if self.path == '':
            self.path = os.getcwd()
        # Initialization.
        self.content = []
        self.version = version
        self.temp_file = self.file.replace('.py', '') + '._temp'
        # Start.
        self.read_file()
        self.add_module()
        self.modify_permission()

    def read_file(self):
        with open(os.path.join(self.path, self.file), 'r') as f:
            for line in f.readlines():
                if line[-1] == '\n':
                    self.content.append(line[0:-1])
                else:
                    self.content.append(line)

    def save_file(self, filename, mode):
        with open(os.path.join(self.path, filename), mode) as f:
            for item in self.content:
                f.write(str(item) + '\n')

    def add_module(self):
        # Import os and sys.

        import_os_key = True
        import_sys_key = True

        for i in self.content:
            if i.replace(' ', '') == 'importos':
                import_os_key = False
            if i.replace(' ', '') == 'importsys':
                import_sys_key = False

        if import_os_key or import_sys_key:
            for index, item in enumerate(self.content):
                # Ignore comments and import modules.
                if item.find('import') == 0 or item.find('#') == 0:
                    pass
                elif import_os_key:
                    self.content.insert(index, 'import os')
                    import_os_key = False
                elif import_sys_key:
                    self.content.insert(index, 'import sys')
                    import_sys_key = False
                else:
                    break

        # Add header.
        if self.content[0] not in ('#!/usr/bin/env python', '#!/usr/bin/env python3'):
            if self.version == 3:
                self.content.insert(0, '#!/usr/bin/env python3')
            elif self.version == 2:
                self.content.insert(0, '#!/usr/bin/env python')

        # Add path.
        for i in self.content:
            if i.find('import') == 0 or i.find('#') == 0:
                pass
            else:
                list_path = [
                    '# Prevent path error.By PSC.',
                    'psc_path = os.path.dirname(sys.argv[0])',
                    'os.chdir(psc_path)'
                ]

                for j in list_path:
                    self.content.insert(self.content.index(i), j)
                break

        # Save a temp file.
        self.save_file(self.temp_file, mode='w')

    def modify_permission(self):
        # Modify permission.
        name = self.temp_file.replace('._temp', '') + '.command'

        os.rename(os.path.join(self.path, self.temp_file), os.path.join(self.path, name))

        os.system('chmod +x %s' % os.path.join(self.path, name))


def main():
    length = len(sys.argv)
    if length == 1:
        sys.stdout.write('Usage: psc [filename.py] [python-version].(default version == 3)\n')
        sys.stdout.write('[Error]:Please input filename! \n')
        return False
    elif length == 2:
        PSC(sys.argv[1])
    elif length == 3:
        PSC(sys.argv[1], int(sys.argv[2]))
    sys.stdout.write('Success! Powered by ZYunH.\n')
