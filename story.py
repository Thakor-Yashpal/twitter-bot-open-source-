import pyttsx3

def tell_story():
  engine = pyttsx3.init()
  engine.say("Once upon a time, in a land far, far away, there was a brave knight named Sir Galahad. Sir Galahad was known throughout the kingdom for his bravery and strength, and he was beloved by all who knew him. One day, a terrible dragon terrorized the kingdom, causing destruction and fear wherever it went. Sir Galahad knew that he had to do something to protect the people, so he set out on a quest to defeat the dragon. After a long and difficult journey, Sir Galahad finally found the dragon and engaged it in a fierce battle. Despite the dragon's fearsome fire breath, Sir Galahad was able to vanquish the beast and save the kingdom. The people rejoiced, and Sir Galahad was hailed as a hero. And so, the brave knight lived happily ever after." )
  engine.runAndWait()

tell_story()
