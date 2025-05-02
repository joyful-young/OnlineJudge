def solution(bandage, health, attacks):
    t, x, y = bandage
    time = 0            # 현재 시각
    skill_time = 0      # 붕대 감기 시전 시간
    now_health = health
    for atk_time, damage in attacks:
        # 공격 시간이 될 때까지 붕대 감기
        r_time = atk_time - time - 1    # 붕대 감기가 지속되는 시간
        q, skill_time = divmod(r_time, t)    # 시전 시간이 몇 번 지나가는지
        now_health = min(health, now_health + r_time * x + q * y)
        
        # 몬스터 공격
        now_health -= damage
        if now_health <= 0:
            return -1
        
        skill_time = 0
        time = atk_time
        
    return now_health