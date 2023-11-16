from openpyxl import Workbook
import random

def generate_sales_data():
    # 샘플 데이터를 저장할 새 Excel 워크북 생성
    wb = Workbook()
    ws = wb.active
    ws.append(["전자제품ID", "이름", "가격", "수량"])  # 헤더 행 추가

    # 100개의 샘플 데이터 생성하여 엑셀 시트에 추가
    for _ in range(100):
        product_id = f"PR{random.randint(1000, 9999)}"  # 전자제품 ID 생성
        product_name = f"제품{random.randint(1, 20)}"  # 제품 이름 생성
        price = random.randint(10000, 1000000)  # 제품 가격 생성
        quantity = random.randint(1, 10)  # 판매 수량 생성

        ws.append([product_id, product_name, price, quantity])  # 각 항목을 엑셀 시트에 추가

    # 엑셀 파일로 저장
    wb.save('sales.xlsx')
    print("sales.xlsx 파일이 생성되었습니다.")

# 판매 데이터 생성 함수 실행
generate_sales_data()
