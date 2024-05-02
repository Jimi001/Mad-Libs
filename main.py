from gtts import gTTS
import os

# Prompt the user for different words
adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
noun2 = input("Enter another noun: ")
adverb = input("Enter an adverb: ")

# Write a story with blanks (represented by {})
story = f"Today, I went to the zoo. I saw a {adjective} {noun1} {verb} in front of the {noun2}. It was {adverb} funny!"

# Print out the full story
print(story)

# Convert the story to speech
tts = gTTS(story, lang='en')
tts.save('story.mp3')

# Play the generated audio file
os.system("start story.mp3")
