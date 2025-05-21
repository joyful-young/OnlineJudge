from math import ceil
from collections import defaultdict

"""
출차 내역 없으면 23:59 출차
차량별 누적 주차 시간 계산하여 요금 일괄 정산
기본 요금 + 초과한 시간/단위 시간 * 단위 요금
차량 번호가 작은 자동차부터 청구할 주차 요금을 배열에 담아 반환
"""
def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    total_parking_time = defaultdict(int)
    parking_lot = dict()
    
    # 누적 주차 시간 계산
    for record in records:
        time, car, in_out = record.split()
        if in_out == "IN":
            # 입차
            parking_lot[car] = convert_to_min(time)
        else:
            # 출차
            total_parking_time[car] += convert_to_min(time) - parking_lot[car]
            del parking_lot[car]
    
    exit_time = convert_to_min("23:59")
    for car, entry_time in parking_lot.items():
        total_parking_time[car] += exit_time - entry_time
    
    # 차량별 요금 계산
    parking_fee = [(car, calc_fee(base_time, base_fee, unit_time, unit_fee, parking_time))
                   for car, parking_time in total_parking_time.items()]
    parking_fee.sort(key=lambda x:x[0])
    return [elem[1] for elem in parking_fee]


def convert_to_min(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m


def calc_fee(base_time, base_fee, unit_time, unit_fee, time):
    if time <= base_time:
        return base_fee
    
    return base_fee + ceil((time - base_time) / unit_time) * unit_fee