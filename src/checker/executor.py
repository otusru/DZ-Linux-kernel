from module_ops import ModuleOps

class Executor:
    def __init__(self, ops: ModuleOps):
        self.ops = ops

    def idx_exec_test(self, case):
        try:
            self.ops.write_idx(case['write'])
            value = self.ops.read_idx()
            result = str(value) == case['expected']
            status = "PASSED" if result else "FAILED"
            print(f"[idx_test] write: {case['write']}, read: {value}, expected: {case['expected']} -> {status}")
            return result
        except Exception as e:
            print(f"[idx_test] ERROR: {e}")
            return False

    def ch_val_exec_test(self, case):
        try:
            self.ops.write_ch_val(case['write'])
            value = self.ops.read_ch_val()
            result = str(value) == case['expected']
            status = "PASSED" if result else "FAILED"
            print(f"[ch_val_test] write: {case['write']}, read: {value}, expected: {case['expected']} -> {status}")
            return result
        except Exception as e:
            print(f"[ch_val_test] ERROR: {e}")
            return False

    def str_buf_exec_test(self, case):
        try:
            _str = case['write']
            for idx in range(len(_str)):
                self.ops.write_idx(str(idx))
                self.ops.write_ch_val(" ")
            for idx in range(len(_str)):
                self.ops.write_idx(str(idx))
                self.ops.write_ch_val(_str[idx])

            str_buf = self.ops.read_str_buf().strip()
            result = str_buf == case['expected']
            status = "PASSED" if result else "FAILED"
            print(f"[str_buf_test] write: '{_str}', read: '{str_buf}', expected: '{case['expected']}' -> {status}")
            return result
        except Exception as e:
            print(f"[str_buf_test] ERROR: {e}")
            return False
