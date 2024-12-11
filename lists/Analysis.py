# Hemit Patel
# 781159
# ICS3U0-4 
# 10 dec 2024 
# Analysis (numbers)

from collections import Counter

def get_user_input():
    numbers = []
    print("Enter numbers between 1 and 50. Enter 0 to terminate.")
    while True:
        try:
            num = int(input("Enter a number: "))
            if num == 0:
                break
            if 1 <= num <= 50:
                numbers.append(num)
            else:
                print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return numbers

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def calculate_maximum(numbers):
    return max(numbers) if numbers else 0

def calculate_range(numbers):
    return max(numbers) - min(numbers) if numbers else 0

def calculate_median(numbers):
    if not numbers:
        return 0
    count = Counter(numbers)
    most_common = count.most_common(1)
    return most_common[0][0]  # Returns the number that occurs most frequently

def generate_histogram(numbers):
    # Create bins for the histogram (1–5, 6–10, 11–15, ..., 46-50)
    histogram = [0] * 10  # 10 bins, one for each 5-number range
    for num in numbers:
        bin_index = (num - 1) // 5
        histogram[bin_index] += 1
    
    # Print the histogram
    print("\nHistogram (distribution of numbers in 5-number ranges):")
    for i in range(10):
        range_start = i * 5 + 1
        range_end = (i + 1) * 5
        print(f"{range_start}-{range_end}: {'*' * histogram[i]}")

def main():
    numbers = get_user_input()
    
    if not numbers:
        print("No numbers were entered. Exiting.")
        return
    
    avg = calculate_average(numbers)
    max_num = calculate_maximum(numbers)
    range_num = calculate_range(numbers)
    median = calculate_median(numbers)
    
    # Print results
    print("\nAnalysis Results:")
    print(f"Average: {avg:.2f}")
    print(f"Maximum: {max_num}")
    print(f"Range (Maximum - Minimum): {range_num}")
    print(f"Mode (Most Frequent Number): {median}")
    
    # Generate and display the histogram
    generate_histogram(numbers)

# Run the application
if __name__ == "__main__":
    main()
