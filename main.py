import sys
from PyQt6.QtWidgets import QApplication
from ui import AdditionCalculator

def main():
    """애플리케이션을 생성하고 실행합니다."""
    app = QApplication(sys.argv)
    calculator = AdditionCalculator()
    calculator.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
