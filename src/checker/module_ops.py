class ModuleOps:
    def __init__(self, idx_file, ch_val_file, str_buf_file):
        self.idx_file = idx_file
        self.ch_val_file = ch_val_file
        self.str_buf_file = str_buf_file

    def write_idx(self, value:str):
        self.idx_file.seek(0)
        self.idx_file.write(value)
        self.idx_file.flush()

    def write_ch_val(self, value:str):
        val_str = str(value)
        self.ch_val_file.seek(0)
        self.ch_val_file.write(val_str[0])
        self.ch_val_file.flush()

    def read_idx(self):
        self.idx_file.seek(0)
        return int(self.idx_file.read().strip())

    def read_ch_val(self):
        self.ch_val_file.seek(0)
        ch = self.ch_val_file.read(1).strip()
        return ch

    def read_str_buf(self):
        self.str_buf_file.seek(0)
        return self.str_buf_file.read()
