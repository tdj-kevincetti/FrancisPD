#!/usr/bin/env python3
# นายดุลยภาพ จินะแปง
# 620510642
# Lab 13
# Problem 3
# 204111 Sec 003
import string
def word_count(text):
    counts = dict() #สร้างดิกเปล่า
    text = text.lower() #ปรับให้เป็นตัวเล็ก
    words = text.split() #แยกคำจากช่องว่าง
    for word in words:
        word = word.strip(string.punctuation) #ลบอักษรพิเศษตรงขอบ
        if word in counts: #มีคำอยู่แล้ว
            counts[word] += 1 #นับเพิ่ม
        else: #คำใหม่
            counts[word] = 1
    return counts
def main():
    wordz = input()
    print(word_count(wordz))
    print(word_count('the quick brown fox jumps over the lazy dog.'))
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care, he said."))
    print(word_count("I'm your father!!!!"))
    print(word_count("Fuck Call me 555-5555, Marker"))
    print(word_count("Dumb Prayut Chan-O-Cha"))

if __name__ == '__main__':
    main()
    
