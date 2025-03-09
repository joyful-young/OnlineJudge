def solution(todo_list, finished):
    return [todo_list[idx] for idx in range(len(todo_list)) if not finished[idx]]