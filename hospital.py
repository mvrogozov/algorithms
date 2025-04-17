import pandas as pd
import xlsxwriter


def get_doctors_stat(file: str):
    df = pd.read_excel(
        file,
        sheet_name=None,
        na_filter=False
    )
    max_length = 0
    result = {}
    for sheetname, sheet_data in df.items():
        indexes = df[sheetname].index
        for index in indexes:
            fio = sheet_data['Doc'][index]
            max_length = max(max_length, len(fio))
            stat = sheet_data['Stats'][index]
            if stat != 1:
                result[fio] = result.setdefault(fio, 0) + 1
    output = 'FIO' + ' ' * (max_length + 2) + 'Stats\n\n'
    print(result)
    ordered_result = dict(sorted(result.items()))
    # for key in sorted(result.keys()):
    #     ordered_result.update({key: result[key]})
    for fio, stat in ordered_result.items():
        output += f'{fio}{" " * (2 * max_length - len(fio))}{stat}\n'
        print(f'OUT-> {output}')
    workbook = xlsxwriter.Workbook('hospital.xlsx')
    worksheet = workbook.add_worksheet('statistic')
    row = col = 0
    # for key in result.keys():
    #     row += 1
    #     worksheet.write(row, col, key)
    for k, v in ordered_result.items():
        worksheet.write(row, col, k)
        worksheet.write(row, col + 1, v)
        row += 1
    worksheet.set_column(0, 0, 50)
    worksheet.set_column(1, 1, 20)
    workbook.close()
    with open('hospital.txt', 'w') as f:
        f.write(output)


filename = 'doc_stat.xlsx'
get_doctors_stat(filename)
