import sys

class ModuleOps:
    def __init__(self, idx_file, ch_val_file, str_buf_file):
        # Сохраняем файловые объекты для параметров модуля
        self.idx_file = idx_file
        self.ch_val_file = ch_val_file
        self.str_buf_file = str_buf_file

    def write_idx(self, value: str):
        """Запись значения в параметр idx"""
        try:
            self.idx_file.seek(0)
            self.idx_file.write(value)
            self.idx_file.flush()
        except Exception as e:
            raise RuntimeError(f"Ошибка записи в idx: {e}")

    def write_ch_val(self, value: str):
        """Запись символа в параметр ch_val"""
        try:
            val_str = str(value)
            if not val_str:
                raise ValueError("Пустая строка не может быть записана в ch_val")
            self.ch_val_file.seek(0)
            self.ch_val_file.write(val_str[0])  # записываем только один символ
            self.ch_val_file.flush()
        except Exception as e:
            raise RuntimeError(f"Ошибка записи в ch_val: {e}")

    def read_idx(self):
        """Чтение значения параметра idx"""
        try:
            self.idx_file.seek(0)
            return int(self.idx_file.read().strip())
        except Exception as e:
            raise RuntimeError(f"Ошибка чтения из idx: {e}")

    def read_ch_val(self):
        """Чтение символа из параметра ch_val"""
        try:
            self.ch_val_file.seek(0)
            ch = self.ch_val_file.read(1).strip()
            return ch
        except Exception as e:
            raise RuntimeError(f"Ошибка чтения из ch_val: {e}")

    def read_str_buf(self):
        """Чтение всей строки из параметра str_buf"""
        try:
            self.str_buf_file.seek(0)
            str_buf = self.str_buf_file.read()
            return str_buf
        except Exception as e:
            raise RuntimeError(f"Ошибка чтения из str_buf: {e}")
