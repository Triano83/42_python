from abc import ABC, abstractmethod
from typing import Protocol, Any, List, Tuple
import typing


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

    @property
    def stats(self) -> Tuple[int, int]:
        return (self._count, len(self._storage))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        return isinstance(data, list) and all(isinstance(x, (int, float))
                                              for x in data)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(str(item))
            self._count += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return isinstance(data, list) and all(isinstance(x, str) for x in data)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._storage.append(item)
            self._count += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_log(d: Any) -> bool:
            return (isinstance(d, dict) and
                    all(isinstance(k, str) and isinstance(v, str)
                        for k, v in d.items()))
        if is_valid_log(data):
            return True
        return isinstance(data, list) and all(is_valid_log(x) for x in data)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            fmt = f"{item.get('log_level')}: {item.get('log_message')}"
            self._storage.append(fmt)
            self._count += 1


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        list_text = [text for _, text in data]
        print("CSV Output:")
        print(",".join(list_text))


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        elementos = [f'"item_{rank}": "{text}"' for rank, text in data]
        print("JSON Output:")
        print("{" + ", ".join(elementos) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: List[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: "
                      f"{element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted_data: List[Tuple[int, str]] = []
            for _ in range(nb):
                try:
                    extracted_data.append(proc.output())
                except IndexError:
                    break
            if extracted_data:
                plugin.process_output(extracted_data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            total, remaining = proc.stats
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    ds.register_processor(NumericProcessor())
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    batch1 = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
          'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    batch2 = [
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
          'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello'
    ]
    print(f"\nSend another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()
