from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError("No data to output")
        data = self._storage.pop(0)
        rank = self._count - len(self._storage) - 1
        return (rank, data)


class NumericProcessor(DataProcessor):
    """Handles int, float, and lists of numeric types."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and all(isinstance(x, (int, float))
                                          for x in data):
            return True
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._count += 1
        else:
            self._storage.append(str(data))
            self._count += 1


class TextProcessor(DataProcessor):
    """Handles str and lists of strings."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(x, str) for x in data):
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._count += 1
        else:
            self._storage.append(data)
            self._count += 1


class LogProcessor(DataProcessor):
    """Handles dict of string pairs and lists of such dicts."""

    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return (isinstance(d, dict) and
                    all(isinstance(k, str) and isinstance(v, str)
                        for k, v in d.items()))

        if is_valid_log(data):
            return True
        if isinstance(data, list) and all(is_valid_log(x) for x in data):
            return True
        return False

    def ingest(self, data: Union[Dict[str, str],
                                 List[Dict[str, str]]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        def fmt(d: Dict[str, str]) -> str:
            return f"{d.get('log_level', '')}: {d.get('log_message', '')}"

        if isinstance(data, list):
            for item in data:
                self._storage.append(fmt(item))
                self._count += 1
        else:
            self._storage.append(fmt(data))
            self._count += 1


if __name__ == "__main__":
    print("=== Code Nexus Data Processor ===")

    print("\nTesting Numeric Processor.")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")

    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    np.ingest(num_data)
    print("Extracting 3 values...")
    for i in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}:{val}")
    try:
        np.ingest(42)
        np.ingest(43)
        print(f"prueba 1 {np.output()}")
        print(f"prueba 2 {np.output()}")
        np.ingest(42)
        print(f"prueba 3 {np.output()}")
        print(f"prueba 4 {np.output()}")
        print(f"prueba 5 {np.output()}")
        print(f"prueba 6 {np.output()}")
        print(f"prueba 7 {np.output()}")
    except Exception as e:
        print(f"{e}")

    print("\nTestin Text Processor")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    text_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {text_data}")
    tp.ingest(text_data)
    print("Extracting 1 value...")
    rank, val = tp.output()
    print(f"Text value {rank}: {val}")

    print("\nTesting Log Processor.")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_data = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"Processing data: {log_data}")
    lp.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")
