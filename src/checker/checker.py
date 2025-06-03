import os
import sys

from module_ops import ModuleOps
from tests import Tests

class Checker:
    def __init__(self, module_name):
        self.module_name = module_name
        self.idx_path = f"/sys/module/{module_name}/parameters/idx"
        self.ch_val_path = f"/sys/module/{module_name}/parameters/ch_val"
        self.str_buf_path = f"/sys/module/{module_name}/parameters/str_buf"

        self.idx_file = None
        self.ch_val_file = None
        self.str_buf_file = None

        try:
            self.open_sysfs_files()
            self.ops = ModuleOps(self.idx_file, self.ch_val_file, self.str_buf_file)
            self.tests = Tests(self.ops)
        except Exception as e:
            print(f"Ошибка при инициализации: {e}")
            self.close()
            sys.exit(1)

    def open_sysfs_files(self, mode='r+'):
        self.idx_file = open(self.idx_path, mode)
        self.ch_val_file = open(self.ch_val_path, mode)
        self.str_buf_file = open(self.str_buf_path, 'r')

    def check_idx(self):
        return self.tests.idx_tests()

    def check_ch_val(self):
        return self.tests.ch_val_tests()

    def check_str_buf(self):
        self.str_buf_file.seek(0)
        return self.tests.str_buf_tests()

    def close(self):        
        for f in (self.idx_file, self.ch_val_file, self.str_buf_file):
            if f and not f.closed:
                f.close()
