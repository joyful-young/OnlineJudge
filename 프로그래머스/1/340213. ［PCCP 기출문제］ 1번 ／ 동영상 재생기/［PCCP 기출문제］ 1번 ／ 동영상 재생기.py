def solution(video_len, pos, op_start, op_end, commands):
    v_end, now, op_s, op_e = map(convert_to_sec, [video_len, pos, op_start, op_end])
    if op_s <= now <= op_e:
        now = op_e
    
    for command in commands:
        if command == "prev":
            now = max(0, now - 10)
        else:
            now = min(v_end, now + 10)
            
        if op_s <= now <= op_e:
            now = op_e
    
    m, s = map(str, divmod(now, 60))
    mm = "0" + m if len(m) <= 1 else m
    ss = "0" + s if len(s) <= 1 else s
    return f"{mm}:{ss}"


def convert_to_sec(pos_str):
    m, s = map(int, pos_str.split(":"))
    return m * 60 + s