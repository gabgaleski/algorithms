def study_schedule(permanence_period, target_time):
    n = len(permanence_period)
    count = 0
    if target_time is None:
        return None
    for index in range(n):
        if (
            type(permanence_period[index][0]) != int
            or type(permanence_period[index][1]) != int
        ):
            return None

        if (
            permanence_period[index][0] <= target_time
            and permanence_period[index][1] >= target_time
        ):
            count += 1

    return count
