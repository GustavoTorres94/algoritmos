def study_schedule(permanence_period, target_time):
    count = 0

    if target_time is None or not isinstance(target_time, int):
        return None

    for tupla in permanence_period:
        if not all(isinstance(i, int) for i in tupla):
            return None

        if target_time in tupla:
            count += 1
    print(count)
    return count
