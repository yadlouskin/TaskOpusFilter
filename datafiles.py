from datetime import datetime


class FilePathes:
    en : str = '.data/WikiMatrix.en-ru.en'
    ru : str = '.data/WikiMatrix.en-ru.ru'
    res : str = '.data/result_{:%Y-%m-%d_%H:%M:%S}.ru'


class FilesWrapper:
    def __init__(self, lines_limit : int = -1,
                 path_file_en : str = FilePathes.en,
                 path_file_ru : str = FilePathes.ru,
                 path_file_res : str = FilePathes.res):
        self.lines_limit = lines_limit
        self.path_file_en = path_file_en
        self.path_file_ru = path_file_ru
        self.path_file_res = path_file_res

    def __enter__(self):
        self.file_en = open(self.path_file_en, 'r')
        self.file_ru = open(self.path_file_ru, 'r')
        self.file_res = open(self.path_file_res.format(datetime.now()), 'w')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file_en.close()
        self.file_ru.close()
        self.file_res.close()

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        if 0 < self.lines_limit < self.count:
            raise StopIteration

        self.curr_line_en = next(self.file_en).strip()
        self.curr_line_ru = next(self.file_ru).strip()
        return self.curr_line_en, self.curr_line_ru

    def write_line(self):
        self.file_res.write(self.curr_line_ru)
