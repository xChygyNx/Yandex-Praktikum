from typing import List, Tuple, NamedTuple, Union


class Schedule(NamedTuple):
    lesson_count: int
    time: List[Tuple[float, float]]


def read_lessons(n: int) -> List[Tuple[float, float]]:
    result = []
    for _ in range(n):
        start, end = [float(x) for x in input().split()]
        result.append((start, end))
    result.sort()
    return result


def construct_schedule(lessons: List[Tuple[float, float]]) -> Schedule:
    lesson_count = 0
    time = []
    busy_time_start, busy_time_end = lessons[0][0], lessons[0][1]
    for i in range(1, len(lessons)):
        lesson_start, lesson_end = lessons[i][0], lessons[i][1]
        if lesson_start >= busy_time_end:
            lesson_count += 1
            time.append((busy_time_start, busy_time_end))
            busy_time_start, busy_time_end = lesson_start, lesson_end
        elif lesson_end < busy_time_end:
            busy_time_start, busy_time_end = lesson_start, lesson_end
    lesson_count += 1
    time.append((busy_time_start, busy_time_end))
    return Schedule(lesson_count=lesson_count, time=time)


def int_or_float(num: float) -> Union[int, float]:
    if num % 1 == 0:
        num = int(num)
    return num


if __name__ == '__main__':
    n = int(input())
    lessons = read_lessons(n)
    schedule = construct_schedule(lessons)
    print(schedule.lesson_count)
    line = '\n'.join([' '.join([str(int_or_float(x)) for x in elem]) for elem in schedule.time])
    print(line)