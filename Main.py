import sys
from PyQt5.QtWidgets import (QApplication, QSizePolicy, QSpacerItem, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QFileDialog, QLabel, QProgressBar)


class FileSelectorUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 메인 레이아웃
        main_layout = QVBoxLayout()

        # 첫 번째 경로 및 버튼 레이아웃
        path1_layout = QHBoxLayout()
        self.file_path_edit1 = QLineEdit(self)
        self.file_path_edit1.setReadOnly(True)
        path1_layout.addWidget(QLabel("엑셀파일 경로"))
        path1_layout.addWidget(self.file_path_edit1)
        self.file_btn1 = QPushButton('...', self)
        self.file_btn1.setFixedSize(40, 25)
        self.file_btn1.clicked.connect(self.showFileDialog1)
        path1_layout.addWidget(self.file_btn1)
        main_layout.addLayout(path1_layout)

        # 두 번째 경로 및 버튼 레이아웃
        path2_layout = QHBoxLayout()
        self.file_path_edit2 = QLineEdit(self)
        self.file_path_edit2.setReadOnly(True)
        path2_layout.addWidget(QLabel("한글파일 경로"))
        path2_layout.addWidget(self.file_path_edit2)
        self.file_btn2 = QPushButton('...', self)
        self.file_btn2.setFixedSize(40, 25)
        self.file_btn2.clicked.connect(self.showFileDialog2)
        path2_layout.addWidget(self.file_btn2)
        main_layout.addLayout(path2_layout)

        # 진행 바
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # 실행 버튼
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.run_button = QPushButton('실행', self)
        self.run_button.setFixedSize(60, 25)  # 버튼의 크기 조절
        button_layout.addWidget(self.run_button)
        main_layout.addLayout(button_layout)

        # 메인 레이아웃 설정
        self.setLayout(main_layout)

        # 윈도우 설정
        self.setWindowTitle('Xslx To hwp Ver 0.0')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def showFileDialog1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "엑셀 파일 선택", "", "All Files (*);;Excel Files (*.xlsx)", options=options)
        if file_path:
            self.file_path_edit1.setText(file_path)

    def showFileDialog2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "한글 파일 선택", "", "All Files (*);;HWP Files (*.hwp)", options=options)
        if file_path:
            self.file_path_edit2.setText(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileSelectorUI()
    sys.exit(app.exec_())
