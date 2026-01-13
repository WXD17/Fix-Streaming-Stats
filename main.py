def calculate_streaming_stats(total_minutes, snack_calories, snacks_eaten):
    hours_watched = total_minutes / 60
    total_snack_calories = snack_calories * snacks_eaten
    average_calories_per_hour = total_snack_calories / hours_watched
    return hours_watched, total_snack_calories, average_calories_per_hour
