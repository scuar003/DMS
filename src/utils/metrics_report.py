def generate_metrics_report(engagement_data, total_time, frame_count):
    frame_time = total_time / frame_count
    print("\nEngagement Metrics Report:")
    print("----------------------------")
    for stimulus, count in engagement_data.items():
        engagement_time = count * frame_time
        print(f"{stimulus}: {engagement_time:.2f} seconds")
    print(f"\nTotal tracking time: {total_time:.2f} seconds")