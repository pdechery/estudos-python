import statistics

def quicksort(numbers):

    print(f'given data {numbers}')

    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        
        print(f'pivot {pivot}')
        
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )
        
        print(f'items_less {items_less}')
        print(f'pivot_items {pivot_items}')
        print(f'items_greater {items_greater}')
        
        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )

if __name__ == '__main__':
    
    print(quicksort([10, -3, 21, 6, -8]))