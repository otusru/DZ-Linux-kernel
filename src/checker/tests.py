from executor import Executor

class Tests:
    def __init__(self, ops):
        # Инициализируем исполнитель тестов
        self.exec = Executor(ops)

    def run_tests(self, name, func, test_cases):
        """Универсальный метод для запуска тестов"""
        print(f"\n--- Запуск тестов {name} ---")
        results = []

        for case in test_cases:
            expect_error = case.get("expect_error", False)
            try:
                result = func(case)
                # Если ожидалась ошибка, а её не произошло — тест провален
                if expect_error:
                    print(f"[{name}] ОШИБКА: ожидалась ошибка, но всё прошло успешно")
                    results.append(False)
                else:
                    results.append(result)
            except Exception as e:
                if expect_error:
                    print(f"[{name}] Ожидаемая ошибка: {e}")
                    results.append(True)
                else:
                    print(f"[{name}] НЕОЖИДАННАЯ ошибка: {e}")
                    results.append(False)

        print(f"\nТесты {name} завершены:", "OK" if all(results) else "FAIL")
        return all(results)

    def idx_tests(self):
        test_cases = [
            {"write": "0", "expected": "0"},
            {"write": "2", "expected": "2"},
            {"write": "A", "expect_error": True},
        ]
        return self.run_tests("idx", self.exec.idx_exec_test, test_cases)

    def ch_val_tests(self):
        test_cases = [
            {"write": "A", "expected": "A"},
            {"write": "123", "expected": "1"},  # ожидаем только первый символ
            {"write": "\n", "expect_error": True},
        ]
        return self.run_tests("ch_val", self.exec.ch_val_exec_test, test_cases)

    def str_buf_tests(self):
        test_cases = [
            {"write": "Hello", "expected": "Hello"},
            {"write": "World!", "expected": "World!"},
            {"write": "Hello, World!", "expected": "Hello, World!"},
        ]
        return self.run_tests("str_buf", self.exec.str_buf_exec_test, test_cases)
