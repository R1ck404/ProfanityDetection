from Model import BadWordDetector

detector = BadWordDetector('badwords.txt')
text = 'This is a test string and this repository is amazing like howly shhhhhit. this is really amazing tho like shhiiit'

detected_words = detector.detect(text)
if detected_words:
    for word in detected_words:
        print(f'{word[0]} ({word[1]}, {word[2]*100:.2f}% similarity)')
else:
    print('No bad words detected')
