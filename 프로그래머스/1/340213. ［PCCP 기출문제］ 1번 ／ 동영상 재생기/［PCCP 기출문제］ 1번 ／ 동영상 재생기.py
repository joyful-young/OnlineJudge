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
    
    m, s = divmod(now, 60)
    return f"{m:02d}:{s:02d}"


def convert_to_sec(pos_str):
    m, s = map(int, pos_str.split(":"))
    return m * 60 + s