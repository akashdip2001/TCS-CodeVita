```md
# GoodString Problem

## Problem Description
A picnic to a famous museum is being planned in a school for class VI. When they reached the spot, the students started quarreling among themselves in the queue. So the teacher came up with an idea of a "good string."

A **Good String** is provided as input. All letters in this string are good letters. The teacher asked all the students to convert their names into good names using the good string. While converting, they calculate the **distance**, and based on that, the teacher will arrange the students in a queue.

For converting a name into a good name, for each letter `i` in the name, select the nearest letter from the good string. The **distance** is calculated as the difference between the ASCII values of `i` and the selected good letter. If there are two letters equidistant from `i`, select the letter closest to the **previously used** good letter. If `i` is already present in the good string, no need to change it. Initially, the previous good letter is the first letter of the good string. Calculate the total distance for the given name.

Letters from the good string can be reused any number of times.

## Constraints
- \(1 \leq \text{len(good string)} \leq 100\)
- \(1 \leq \text{len(name)} \leq 10^4\)
- The good string consists of lower and upper case alphabets, digits, and symbols.
- The name consists of only spaces, lower, and upper case alphabets.
- Characters are case-sensitive.
- The ASCII values for all characters in the good string and name will be between 32 and 126 (both inclusive).

## Input
- The first line consists of the good string.
- The second line consists of the name of the student.

## Output
- Print the total distance for that name.

## Time Limit
1 second

## Examples

### Example 1:

**Input:**
```
(@HR*i{kcQl
Vyom
```

**Output:**
```
10
```

**Explanation:**
For the name "Vyom":
- ASCII difference between 'V' and nearest good letter 'R' = 4.
- ASCII difference between 'y' and nearest good letter '{' = 2.
- ASCII difference between 'o' and nearest good letter 'l' = 3.
- ASCII difference between 'm' and nearest good letter 'l' = 1.

Total distance = 4 + 2 + 3 + 1 = 10.

### Example 2:

**Input:**
```
6*K4AQf]gpi
Nainika
```

**Output:**
```
33
```

**Explanation:**
For the name "Nainika":
- ASCII difference between 'N' and nearest good letter 'K' = 21.
- ASCII difference between 'a' and nearest good letter ']' = 4.
- ASCII difference between 'n' and nearest good letter 'p' = 2.
- ASCII difference between 'k' and nearest good letter 'i' = 2.
- ASCII difference between 'a' and nearest good letter ']' = 4.

Total distance = 21 + 4 + 2 + 2 + 4 = 33.

---

## Python Code Solution

```python
def find_nearest_good_letter(char, good_string, prev_good_letter):
    # Initialize minimum distance and the closest good letter
    min_distance = float('inf')
    closest_good_letter = None
    
    for good_char in good_string:
        distance = abs(ord(char) - ord(good_char))
        
        # If two letters are equidistant, pick the one closer to the previous good letter
        if distance < min_distance or (distance == min_distance and abs(ord(good_char) - ord(prev_good_letter)) < abs(ord(closest_good_letter) - ord(prev_good_letter))):
            min_distance = distance
            closest_good_letter = good_char
            
    return closest_good_letter, min_distance

def total_distance(good_string, name):
    total_dist = 0
    prev_good_letter = good_string[0]
    
    for char in name:
        if char in good_string:
            prev_good_letter = char  # No need to change, but update the previous good letter
            continue
        closest_good_letter, dist = find_nearest_good_letter(char, good_string, prev_good_letter)
        total_dist += dist
        prev_good_letter = closest_good_letter  # Update previous good letter after every replacement
    
    return total_dist

# Input
good_string = input().strip()
name = input().strip()

# Output
print(total_distance(good_string, name))
```

---

### Explanation:
1. **find_nearest_good_letter**: This helper function finds the nearest good letter to the given character `char`. If two good letters are equidistant, it picks the one closest to the previous good letter.
2. **total_distance**: This function calculates the total distance for converting a student's name to a good name, based on the rules given.
```

