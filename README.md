# Profanity Detector
This project is a Python program for detecting bad words in a given text. The program includes a class called BadWordDetector, which reads a file of bad words and provides a detect() method that compares each word in a given text to the list of bad words and returns any detected bad words with their closest match and similarity percentage.

The program uses a simple algorithm to calculate the similarity between two words based on the number of common letter pairs in the two words. It is a lightweight and easy-to-understand implementation, making it accessible to developers of all skill levels.

The program can be used as a standalone script or easily integrated into larger applications. It is a useful tool for detecting bad language and inappropriate content in user-generated content.

## Usage Example
```py
from Model import BadWordDetector

detector = BadWordDetector('badwords.txt')
text = 'This is a test string and this repository is amazing like howly shhhhhit. this is really amazing tho like shhiiit'

detected_words = detector.detect(text)
if detected_words:
    for word in detected_words:
        print(f'{word[0]} ({word[1]}, {word[2]*100:.2f}% similarity)')
else:
    print('No bad words detected')
```
