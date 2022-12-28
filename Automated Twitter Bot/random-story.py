import pyttsx3
import random

def tell_story():
  stories = [
    "Once upon a time, in a land far, far away, there was a brave knight named Sir Galahad. Sir Galahad was known throughout the kingdom for his bravery and strength, and he was beloved by all who knew him. One day, a terrible dragon terrorized the kingdom, causing destruction and fear wherever it went. Sir Galahad knew that he had to do something to protect the people, so he set out on a quest to defeat the dragon. After a long and difficult journey, Sir Galahad finally found the dragon and engaged it in a fierce battle. Despite the dragon's fearsome fire breath, Sir Galahad was able to vanquish the beast and save the kingdom. The people rejoiced, and Sir Galahad was hailed as a hero. And so, the brave knight lived happily ever after.",
    "There was once a beautiful princess named Cinderella who lived with her cruel stepmother and stepsisters. Despite their mistreatment, Cinderella remained kind and hopeful. One day, the kingdom announced a ball where the prince would choose his bride. Cinderella's stepfamily forbade her from attending, but with the help of her fairy godmother, she was able to go to the ball and dance with the prince. As the night came to an end, Cinderella had to leave before the stroke of midnight, losing one of her glass slippers on the steps of the palace. The prince searched the kingdom for the owner of the glass slipper, and eventually, he found Cinderella and they lived happily ever after.",
    "In a far-off kingdom, there was a kind and wise king who ruled with fairness and justice. One day, a wicked sorcerer cast a spell on the king, turning him into a ferocious beast. The kingdom was thrown into chaos, and the people lived in fear of the beast. But the king's daughter, Belle, was determined to break the curse and save her father. With the help of a magical talking teapot, a clock, and a candelabra, Belle set out on a journey to find a way to reverse the spell. After many trials and tribulations, she finally found a magical rose that held the key to breaking the curse. Belle returned to the kingdom and used the rose to restore the king to his former self. The kingdom rejoiced, and Belle and the king lived happily ever after."
  ]

  engine = pyttsx3.init()
  story = random.choice(stories)
  engine.say(story)
  engine.runAndWait()

tell_story()
