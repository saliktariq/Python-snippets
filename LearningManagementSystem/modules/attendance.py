from datetime import datetime

import openpyxl
from openpyxl.utils import get_column_letter


class Attendance:
    def __init__(self, start_time, end_time, trainer_id, trainer_name, trainees_attended=None, trainees_not_attended=None):
        self.date = datetime.today().strftime('%m-%d-%Y')
        self.start_time = start_time
        self.end_time = end_time
        self.trainer_id = trainer_id
        self.trainer_name = trainer_name
        if trainees_attended is None:
            self.trainees_attended = []
        else:
            self.trainees_attended = trainees_attended
        if trainees_not_attended is None:
            self.trainees_not_attended = []
        else:
            self.trainees_not_attended = trainees_not_attended

    def save_to_excel(self):
        try:
            wb = openpyxl.load_workbook('MasterRecord.xlsx')
        except FileNotFoundError:
            wb = openpyxl.Workbook()
        sheet_name = self.date
        # Check if the sheet already exists
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            row_count = ws.max_row
        # Create a new sheet if it doesn't exist
        else:
            ws = wb.create_sheet(title=sheet_name)
            row_count = 1
            # Write headers to the first row of the sheet
            headers = ['Trainee ID', 'Trainee Name', 'Attendance']
            for col_num, header in enumerate(headers, 1):
                col_letter = get_column_letter(col_num)
                cell = ws['{}{}'.format(col_letter, row_count)]
                cell.value = header
        # Write attendance data to the sheet
        row_count += 1
        for trainee_id, trainee_name in self.trainees_attended:
            ws.cell(row=row_count, column=1, value=trainee_id)
            ws.cell(row=row_count, column=2, value=trainee_name)
            ws.cell(row=row_count, column=3, value='Present')
            row_count += 1
        for trainee_id, trainee_name in self.trainees_not_attended:
            ws.cell(row=row_count, column=1, value=trainee_id)
            ws.cell(row=row_count, column=2, value=trainee_name)
            ws.cell(row=row_count, column=3, value='Absent')
            row_count += 1
        # Write metadata to the sheet
        metadata = {
            'Start Time': self.start_time,
            'End Time': self.end_time,
            'Trainer ID': self.trainer_id,
            'Trainer Name': self.trainer_name,
        }
        for col_num, (key, value) in enumerate(metadata.items(), 1):
            col_letter = get_column_letter(ws.max_column + 1)
            cell = ws['{}{}'.format(col_letter, 1)]
            cell.value = key
            cell = ws['{}{}'.format(col_letter, 2)]
            cell.value = value
        # Save the workbook
        wb.save('MasterRecord.xlsx')