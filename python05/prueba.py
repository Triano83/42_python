from typing import List, Tuple


class CSVExportPlugin():

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        list_text = []
        for _, text in data:
            list_text.append(text)
        format_text = ",".join(list_text)
        print("CSV Output:")
        print(format_text)


if __name__ == "__main__":
    p = CSVExportPlugin()
    batch = [(0, "Cero"), (1, "Uno")]
    p.process_output(batch)
