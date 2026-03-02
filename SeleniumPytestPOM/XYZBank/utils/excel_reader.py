import openpyxl
import os

class ExcelReader:
    def __init__(self, relative_path):

        project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..")
        )

        excel_path = os.path.join(project_root, relative_path)

        if not os.path.exists(excel_path):
            raise FileNotFoundError(f"Excel file not found at: {excel_path}")

        self.wb = openpyxl.load_workbook(excel_path)

    def get_data(self, sheet_name):
        sheet = self.wb[sheet_name]
        data = []
        headers = [cell.value for cell in sheet[1]]

        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(dict(zip(headers, row)))

        return data