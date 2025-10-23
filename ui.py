from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QMessageBox,
)

class AdditionCalculator(QWidget):
    """
    두 개의 숫자를 입력받아 덧셈 결과를 보여주는 PyQt 위젯입니다.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """UI를 초기화하고 위젯들을 배치합니다."""
        # 윈도우 설정
        self.setWindowTitle('덧셈 계산기')
        self.setGeometry(300, 300, 300, 200)

        # 위젯 생성
        self.num1_edit = QLineEdit(self)
        self.num1_edit.setPlaceholderText("첫 번째 숫자")

        self.num2_edit = QLineEdit(self)
        self.num2_edit.setPlaceholderText("두 번째 숫자")

        self.add_button = QPushButton('add', self)

        self.result_label = QLabel('결과가 여기에 표시됩니다.', self)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        vbox.addWidget(self.num1_edit)
        vbox.addWidget(self.num2_edit)
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

        # 시그널과 슬롯 연결
        # '더하기' 버튼을 클릭하면 calculate_sum 메서드가 호출됩니다.
        self.add_button.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        """
        입력창의 텍스트를 가져와 덧셈을 수행하고 결과를 레이블에 표시합니다.
        """
        try:
            num1_text = self.num1_edit.text() or '0'
            num2_text = self.num2_edit.text() or '0'
            num1 = float(num1_text)
            num2 = float(num2_text)
            result = num1 + num2
            self.result_label.setText(f'결과: {result}')
        except ValueError:
            QMessageBox.warning(self, '입력 오류', '유효한 숫자를 입력해주세요.')
            self.result_label.setText('결과: 숫자를 입력해주세요.')